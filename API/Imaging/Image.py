import os
import random

import API.AntiBan
from API.Time import is_time_up
from PIL import Image, ImageGrab
import numpy as np
import cv2
from API.Setup import get_bluestacks_region
from API.Imports.Paths import *
from API.Mouse import mouse_click
from API.Debug import write_debug
from datetime import datetime
import pyautogui as pag


LATEST_IMG_XY = 0, 0


def capture_img_region(window_x, window_y, window_x2, window_y2, image_name):
    x1, y1, _, _ = get_bluestacks_region()

    run_x1 = x1 + window_x
    run_y1 = y1 + window_y
    run_x2 = window_x2 - window_x
    run_y2 = window_y2 - window_y
    img_path = fr'{CUSTOM_IMG_PATH}\{image_name}.png'

    pag.screenshot(imageFilename=img_path, region=(run_x1, run_y1, run_x2, run_y2))
    return


def capture_bluestacks():
    x1, y1, x2, y2 = get_bluestacks_region()

    # write_debug(f'🐛 x1: {x1}, y1: {y1}\n🐛 x2: {x2}, y2: {y2}')

    # w, h = get_bluestacks_window_size()
    pag.screenshot(imageFilename=fr'{BS_SCREEN_PATH}', region=(x1, y1, x2-x1, y2-y1))
    # write_debug(f'📸 Captured & Saved Live (BlueStacks) Img: {BS_SCREEN_PATH}')
    return


def does_color_exist(check_color, xy):
    # Take screenshot of BlueStacks window only
    capture_bluestacks()
    # Opens the screenshot taken
    image = Image.open(f'{BS_SCREEN_PATH}')
    # Load the image into memory
    picture = image.load()
    # Pull x, y from region arg
    x, y = xy
    # Pull RGB from check_color arg
    r, g, b = check_color
    # Get the RGB from the region to compare
    cr, cg, cb = picture[x, y]

    # Compare passed RGB values with comparative RGB values
    if r == cr and g == cg and b == cb:

        write_debug(f'✔ Check Color rgb: {r,g,b} FOUND @ {xy}')
        return True
    else:
        write_debug(f'✖ Check Color rgb: {r,g,b} NOT Found @ {xy}')
        return False


def get_color_at_coords(xy):
    x, y = xy
    capture_bluestacks()
    image = Image.open(f'{BS_SCREEN_PATH}')
    picture = image.load()
    write_debug(f'RGB Color @ {x}, {y} = {picture[x, y]}')
    return picture[x, y]


def does_img_exist(img_name, script_name=None, category='Scripts', threshold=0.8, should_click=False, x_offset=8, y_offset=8, min_clicks=1, max_clicks=1, img_sel="last", click_middle=False):
    global LATEST_IMG_XY
    capture_bluestacks()
    img_rgb = cv2.imread(BS_SCREEN_PATH)

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Read the template (disconnected)
    if script_name is not None:  # If it's a script name
        write_debug(f'Checking for {img_name}.png in {SCRIPTS_SCREEN_PATH}\{script_name}\{img_name}.png ... ')
        template_img_path = f'{SCRIPTS_SCREEN_PATH}\{script_name}\{img_name}.png'

    else:  # If no script name - get Category
        write_debug(f'Checking for {img_name}.png in Comparators\{category}...')
        template_img_path = f'{ROOT_COMPARATORS_PATH}\{category}\{img_name}.png'

    template = cv2.imread(template_img_path, 0)

    print(f'🔴 template shape: {template.shape}')
    temp_height, temp_width = template.shape
    temp_middle_height = temp_height / 2
    temp_middle_width = temp_width / 2

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)

    if len(loc[0]) == 0 and len(loc[1]) == 0:
        # write_debug(f'✖ {img_name}.png NOT found within game window.\n {loc[0]} {loc[1]}')
        return False
    else:
        write_debug(f'✔ {img_name}.png found:\n loc[0] = {loc[0]}\nloc[1] = {loc[1]}')
        if img_sel == "first":
            # Save the first img find xy coords
            LATEST_IMG_XY = loc[1][0], loc[0][0]
        elif img_sel == "random":
            r_x = random.randint(0, len(loc[1])-1)
            r_y = random.randint(0, len(loc[0])-1)
            print(f'Random img returning')
            LATEST_IMG_XY = loc[1][r_x], loc[0][r_y]
        else:
            # Save the 'deepest' find of img's xy coords
            LATEST_IMG_XY = loc[1][len(loc[1]) - 1], loc[0][len(loc[0]) - 1]

        if should_click:
            if click_middle:
                print(f'Clicking calculated middle of template image.')
                img_x, img_y = LATEST_IMG_XY
                adj_x = img_x + temp_middle_width
                adj_y = img_y + temp_middle_height
                adj_xy = adj_x, adj_y
                mouse_click(adj_xy, min_num_clicks=min_clicks, max_num_clicks=max_clicks)
            else:
                img_x, img_y = LATEST_IMG_XY
                adj_x = img_x + x_offset
                adj_y = img_y + y_offset
                adj_xy = adj_x, adj_y
                mouse_click(adj_xy, min_num_clicks=min_clicks, max_num_clicks=max_clicks)
        write_debug(f'{LATEST_IMG_XY} saved to img_check_xy global')
        return True


# Search for a particular img on screen for a set amount of time
#       Returns True if the image is found within the amount of time
#       Returns False if the image is not found after trying for specified amount of time
def wait_for_img(img_name, script_name=None, category="Scripts",
                 max_wait_sec=5, threshold=0.8,
                 should_click=False, x_offset=0, y_offset=0,
                 min_clicks=1, max_clicks=1,
                 img_sel="last", click_middle="False"):
    start_time = datetime.now()
    write_debug(f'⏲ Wait_For_Img Start Time: {start_time}')

    while not is_time_up(start_time, max_wait_sec):
        img_found = does_img_exist(img_name, script_name=script_name, category=category,
                                   threshold=threshold, should_click=should_click,
                                   x_offset=x_offset, y_offset=y_offset,
                                   min_clicks=min_clicks, max_clicks=max_clicks,
                                   img_sel=img_sel, click_middle=click_middle)
        if img_found:
            # does_img_exist(img_name, script_name=script_name, category=category, threshold=threshold, should_click=should_click, x_offset=x_offset, y_offset=y_offset)
            return True
        # else:
            # write_debug(f'Still checking for image...')
            # if max_wait_sec > 60:
            #     API.AntiBan.random_human_actions(max_downtime_seconds=6, likelihood=5, reopen_inventory=False)
    return False


def get_existing_img_xy():
    return LATEST_IMG_XY


def find_color_xy(img_path, search_color):
    pim = Image.open(img_path).convert('RGB')
    im = np.array(pim)

    y, x = np.where(np.all(im == search_color, axis=2))
    write_debug(f'Found X: {x} & Y: {y}')
    return x, y
