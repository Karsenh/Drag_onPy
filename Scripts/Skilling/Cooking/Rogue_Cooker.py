import random
import keyboard
import pyautogui as pag
import API.AntiBan
from API.Mouse import mouse_click, mouse_drag
from API.Interface.General import setup_interface, get_xy_for_invent_slot
from API.Interface.Bank import check_if_bank_tab_open, deposit_all, close_bank, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Debug import write_debug


def start_rogue_cooking(curr_loop):
    if curr_loop == 1:
        setup_interface("south", 5, "up")

    write_debug(f'Checking if cooking...')
    if not is_cooking():

        write_debug(f'Not cooking. Checking for level dialogue...')

        if check_for_level_dialogue():
            write_debug(f'Level dialogue found. Continuing to cook...')
            cook_food()

        else:
            write_debug(f'No level dialogue found. Opening bank to get food...')

            open_rogue_bank()

            API.AntiBan.sleep_between(1.2, 1.7)

            deposit_all()

            withdraw_food_to_cook()

            cook_food()

    return True


def open_rogue_bank():
    API.AntiBan.sleep_between(2.0, 2.1)
    rogue_bank_xy = 978, 441
    bank_sel_xy = 979, 549
    mouse_drag(rogue_bank_xy, bank_sel_xy)
    API.AntiBan.sleep_between(1.2, 1.3)
    if not check_if_bank_tab_open(tab_num=5, should_open=True, double_check=True):
        return False
    print(f'WITHDRAW QTY ALL: {is_withdraw_qty(qty="all", should_click=True)}')
    return


def withdraw_food_to_cook():
    food_withdraw_slot = 905, 443
    mouse_click(food_withdraw_slot)
    API.AntiBan.sleep_between(0.7, 1.5)
    close_bank()
    API.AntiBan.sleep_between(0.9, 1.4)
    return


def cook_food():
    fire_xy = 775, 667

    mouse_click(fire_xy, max_x_dev=15, max_y_dev=13)

    API.AntiBan.sleep_between(1.75, 2.2)

    if not does_img_exist(img_name="all_qty_selected", category="General", threshold=0.95):
        does_img_exist(img_name="all_qty", category="General", threshold=0.9, should_click=True, x_offset=8, y_offset=7)
        API.AntiBan.sleep_between(2.0, 2.1)

    pag.press("space")

    API.AntiBan.sleep_between(1.1, 1.6)

    return True


def is_cooking():
    return wait_for_img(img_name="cooking_exp", script_name="Rogue_Cooker", threshold=0.90, max_wait_sec=6)


def check_for_level_dialogue():
    if does_img_exist(img_name="level_up", category="General"):
        print(f'Level-up detected. Spacing through...')
        cook_food()
        API.AntiBan.sleep_between(2.0, 2.1)
        return True
    return False
