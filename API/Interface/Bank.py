import random
from API.Imaging.Image import does_color_exist
from API.Imports.Coords import *
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist
from API.AntiBan import print_to_log, sleep_between
import keyboard


def deposit_all(include_equipment=False):
    # If the bank is not open
    mouse_click(BANK_dep_inventory)
    sleep_between(0.5, 0.7)
    if include_equipment:
        mouse_click(BANK_dep_equipment)
    return


def check_if_bank_tab_open(tab_num=0, should_open=True, double_check=True):
    # If the bank tab IS open...
    if does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
        # return true
        return True
    # Else, the bank tab is NOT open...
    else:
        # If it's not open, but we SHOULD open it...
        if should_open:
            # Click that tab xy to open
            mouse_click(BANK_all_tab_xys[tab_num])
            # Check for tab again after clicking (if double check is true)
            if double_check:
                if not does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
                    print(f"Couldn't find expected tab no. {tab_num} despite having tried to click... Exiting")
                    # Print this issue to log file
                    log_text = f"Couldn't find Bank Tab {tab_num} after trying to click it."
                    print_to_log(log_text)
                    exit(-1)
            # Else - It's now open
            return True
        # Still closed because should_open is false
        return False


def close_bank():
    close_method = random.randint(1, 10)

    if close_method > 8:
        bank_close_xy = 1009, 319
        mouse_click(bank_close_xy, max_x_dev=4, max_y_dev=5)
    else:
        keyboard.send('esc')

    return


def is_withdraw_qty(qty="all", should_click=True):
    all_sel_color = 122, 29, 27
    all_sel_xy = 768, 813

    ten_sel_color = 123, 29, 27
    ten_sel_xy = 655, 815

    five_sel_color = 141, 33, 30
    five_sel_xy = 636, 817

    one_sel_color = 138, 33, 30
    one_sel_xy = 594, 816

    match qty:
        case "all":
            color_to_check = all_sel_color
            coords_to_check = all_sel_xy
        case "10":
            color_to_check = ten_sel_color
            coords_to_check = ten_sel_xy
        case "5":
            color_to_check = five_sel_color
            coords_to_check = five_sel_xy
        case "1":
            color_to_check = one_sel_color
            coords_to_check = one_sel_xy

    is_selected = does_color_exist(check_color=color_to_check, xy=coords_to_check)

    if not is_selected and should_click:
        mouse_click(coords_to_check)
        sleep_between(0.7, 0.9)

    return is_selected
