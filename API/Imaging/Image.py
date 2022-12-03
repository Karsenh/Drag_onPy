import os
from PIL import Image, ImageGrab
import numpy as np
import cv2
from API.Setup import get_bluestacks_region
import pyautogui
from API.Imports.Paths import *
from API.Mouse import mouse_click
from API.Debug import DEBUG_MODE


img_check_xy = 0, 0


def capture_bluestacks():
    x1, y1, x2, y2 = get_bluestacks_region()
    if DEBUG_MODE:
        print(f'🐛 x1: {x1}, y1: {y1}')
        print(f'🐛 x2: {x2}, y2: {y2}')

    # w, h = get_bluestacks_window_size()
    pyautogui.screenshot(imageFilename=fr'{BS_SCREEN_PATH}', region=(x1, y1, x2-x1, y2-y1))
    if DEBUG_MODE:
        print(f'📸 Captured & Saved Live (BlueStacks) Img: {BS_SCREEN_PATH}')
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
        if DEBUG_MODE:
            print(f'✔ Check Color rgb: {r,g,b} FOUND @ {xy}')
        return True
    else:
        if DEBUG_MODE:
            print(f'✖ Check Color rgb: {r,g,b} NOT Found @ {xy}')
        return False


def get_color_at_coords(xy):
    x, y = xy
    capture_bluestacks()
    image = Image.open(f'{BS_SCREEN_PATH}')
    picture = image.load()
    if DEBUG_MODE:
        print(f'RGB Color @ {x}, {y} = {picture[x, y]}')
    return picture[x, y]


def does_img_exist(img_name, script_name=None, category='Scripts', threshold=0.8, should_click=False, x_offset=8, y_offset=8):
    global img_check_xy
    capture_bluestacks()
    img_rgb = cv2.imread(BS_SCREEN_PATH)

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Read the template (disconnected)
    if script_name is not None:  # If it's a script name
        print(f'Checking if {img_name}.png exists in {SCRIPTS_SCREEN_PATH}\{script_name}\{img_name}.png ... ')
        template_img_path = f'{SCRIPTS_SCREEN_PATH}\{script_name}\{img_name}.png'

    else:  # If no script name - get Category
        print(f'Checking if {img_name}.png exists in Comparators\{category}...')
        template_img_path = f'{ROOT_COMPARATORS_PATH}\{category}\{img_name}.png'

    template = cv2.imread(template_img_path, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # if DEBUG_MODE:
    #     print(f'Res: {res}')

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)

    if len(loc[0]) == 0 and len(loc[1]) == 0:
        if DEBUG_MODE:
            print(f'✖ {img_name}.png NOT found within game window.\n {loc[0]} {loc[1]}')
        return False
    else:
        if DEBUG_MODE:
            print(f'✔ {img_name}.png found:\n loc[0] = {loc[0]}\nloc[1] = {loc[1]}')
        #     Save the 'deepest' find of img's xy coords
        img_check_xy = loc[1][len(loc[1])-1], loc[0][len(loc[0])-1]
        if should_click:
            img_x, img_y = img_check_xy
            adj_x = img_x + x_offset
            adj_y = img_y + y_offset
            adj_xy = adj_x, adj_y
            mouse_click(adj_xy)
        print(f'{img_check_xy} saved to img_check_xy global')
        return True


def get_existing_img_xy():
    return img_check_xy


def find_color_xy(img_path, search_color):
    pim = Image.open(img_path).convert('RGB')
    im = np.array(pim)

    y, x = np.where(np.all(im == search_color, axis=2))
    print(f'Found X: {x} & Y: {y}')
    return x, y
