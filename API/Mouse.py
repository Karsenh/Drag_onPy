import random

import API.AntiBan
from API.Setup import *
import pyautogui as pag


#  Moves mouse to specified X, Y and clicks
def mouse_click(xy, max_x_dev=2, max_y_dev=2, click_direction="left", max_num_clicks=1, min_num_clicks=1, max_int_delay=0.3):
    trans_x, trans_y = translate_coords(xy)

    if max_x_dev < 13:
        move_x = trans_x
    else:
        organic_x = random.randint(5, max_x_dev)
        move_x = trans_x + organic_x

    if max_y_dev < 13:
        move_y = trans_y
    else:
        organic_y = random.randint(5, max_y_dev)
        move_y = trans_y + organic_y

    # API.AntiBan.sleep_between(0.2, 0.3)

    if max_num_clicks == 1:
        print(f'Clicking {click_direction} once @ x: {move_x} | y: {move_y}')
        pag.click(button=click_direction, x=move_x, y=move_y)

    elif max_num_clicks > 1:
        num_clicks = random.randint(min_num_clicks, max_num_clicks)
        print(f'Clicking {click_direction} once @ x: {move_x} | y: {move_y}')
        for x in range(num_clicks):
            r_sleep = random.uniform(0.1, max_int_delay)
            pag.click(button=click_direction, x=move_x, y=move_y)
            time.sleep(r_sleep)

    return


def mouse_drag(from_xy, to_xy, drag_delay=True):
    # Move mouse to compass & click down
    if not drag_delay:
        trans_x, trans_y = translate_coords(to_xy, update_coords=True)
    mouse_move(from_xy)
    pag.mouseDown()
    # Do this translation after mouse_down and use the processing time to pause for mousedown delay
    if drag_delay:
        trans_x, trans_y = translate_coords(to_xy, update_coords=True)
    # Translate the relative coordinates of the direction x, y for dragTo()
    r_dur = random.uniform(0.47, 0.53)
    pag.dragTo(trans_x, trans_y, duration=r_dur)
    return


def mouse_move(xy, max_x_dev=0, max_y_dev=0):
    # Get top-left coords of BlueStacks window to offset x, y coords provided to be relative to BlueStacks window
    move_x, move_y = translate_coords(xy, update_coords=False)

    # If deviation args passed - generate random number between 5 and max deviation to offset x, y mouse location organically
    if max_x_dev > 5:
        organic_x = random.randint(5, max_x_dev)
        move_x += organic_x
    if max_y_dev > 5:
        organic_y = random.randint(5, max_y_dev)
        move_y += organic_y

    pag.moveTo(move_x, move_y)
    return


def mouse_long_click(xy):
    move_x, move_y = translate_coords(xy, update_coords=False)

    pag.mouseDown(move_x, move_y)
    API.AntiBan.sleep_between(0.7, 0.8)
    pag.mouseUp()
    return


