from datetime import datetime
import random
from API.Interface.General import setup_interface, get_xy_for_invent_slot, is_tab_open
from API.Interface.Bank import is_withdraw_qty, close_bank, is_bank_tab_open, deposit_all, open_ge_bank, \
    withdraw_item_from_tab_num
from API.Interface.Bank import is_bank_open, deposit_all, is_withdraw_qty, is_bank_tab_open, close_bank
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Debug import write_debug
from API.Mouse import mouse_click, mouse_long_click
import pyautogui as pag
import API.AntiBan
from API.Time import is_time_up

SCRIPT_NAME = 'GE_Dhide_Bodies'
BANK_TAB_NUM = 1
CRAFTING_ATTEMPTS = 0
START_TIME = None


def start_crafting_dhide_bodies(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')
        if not craft_dhide_bodies():
            return False

        if not bank_dhide_bodies():
            return False
    else:
        print(f'First loop')
        setup_interface("east", 5, "up")
        if not open_ge_bank():
            return False
        deposit_all()
        withdraw_needle_and_thread()
        withdraw_dragon_leather()
        close_bank()

    return True


##########
# METHODS
##########
def craft_dhide_bodies():
    global CRAFTING_ATTEMPTS
    global START_TIME

    is_tab_open('inventory')

    mouse_click(get_xy_for_invent_slot(1))

    if not does_img_exist(img_name='inventory_green_leather', script_name=SCRIPT_NAME, img_sel='first', threshold=0.85, should_click=True, click_middle=True):
        open_ge_bank()
        if not withdraw_dragon_leather():
            return False
        close_bank()
        craft_dhide_bodies()

    if not wait_for_img(img_name="Green_body_craft_btn", script_name=SCRIPT_NAME):
        craft_dhide_bodies()
        CRAFTING_ATTEMPTS += 1
        if CRAFTING_ATTEMPTS > 3:
            print(f'Exiting due to Green body craft btn attempts exceeding three.')
            return False
    else:
        if START_TIME is None:
            START_TIME = datetime.now()
        CRAFTING_ATTEMPTS = 0
        mouse_click(get_existing_img_xy(), max_x_dev=14, max_y_dev=14)
        API.AntiBan.sleep_between(1.0, 1.1)

    curr_time = datetime.now()
    time_diff = curr_time - START_TIME
    time_diff_seconds = time_diff.total_seconds()
    print(f'Time difference: {time_diff_seconds}')
    max_wait_seconds = random.randint(14, 16)
    wait_sec = max_wait_seconds - time_diff_seconds
    if wait_sec > 1:
        sleep_while_checking_for_level(wait_sec)

    START_TIME = None
    return True


def sleep_while_checking_for_level(wait_time):
    if wait_for_img(img_name="level_up", category="General", max_wait_sec=wait_time):
        handle_level_dialogue()
        craft_dhide_bodies()

    return True


def bank_dhide_bodies():
    if not open_ge_bank():
        return False

    deposit_dhide_bodies()

    if not withdraw_dragon_leather():
        return False

    close_bank()
    return True


##########
# HELPERS
##########
def withdraw_dragon_leather():
    withdraw_item_from_tab_num(item='green_d_leather', qty='all', tab_num=BANK_TAB_NUM)
    return wait_for_img(img_name='inventory_green_leather', script_name=SCRIPT_NAME, threshold=0.85, img_sel='inventory', max_wait_sec=8)


def withdraw_needle_and_thread():
    withdraw_item_from_tab_num(item='needle', qty='1', tab_num=BANK_TAB_NUM)
    withdraw_item_from_tab_num(item='thread', qty='all', tab_num=BANK_TAB_NUM)
    return


def deposit_dhide_bodies():
    mouse_click(get_xy_for_invent_slot(random.randint(3, 10)))
    return True


def handle_level_dialogue():
    pag.press('space')
    API.AntiBan.sleep_between(1.1, 2.3)
    pag.press('space')
    API.AntiBan.sleep_between(0.8, 1.7)
    return