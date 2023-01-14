import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot
from API.Interface.Bank import open_ge_bank, is_bank_tab_open, is_withdraw_qty, close_bank, deposit_all
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Mouse import mouse_click, mouse_long_click
from API.Debug import write_debug
import pyautogui as pag
import numpy as np

SCRIPT_NAME = "GE_Sulpher_Fertalizer"
HERB_BANK_TAB_NUM = 6


def start_making_fertalizer(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        bank_for_mats(curr_loop)
        process_buckets()
        # Look for farming exp drops
        # If not - enter here and rebank for more shit
    else:
        print(f'First loop')
        # setup_interface('east', 5, 'up')
        # Get shit out of bank
        # Start processing
        # Return true
    return True


def process_buckets():
    is_tab_open("inventory", True)

    salt_slots_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    compost_slots_arr = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

    np.random.shuffle(salt_slots_arr)

    while does_img_exist(img_name="Inventory_Salt", script_name=SCRIPT_NAME, threshold=0.9):
        while len(salt_slots_arr) >= 1:
            mouse_click(get_xy_for_invent_slot(salt_slots_arr[0]))
            salt_slots_arr.pop(0)
            mouse_click(get_xy_for_invent_slot(compost_slots_arr[0]))
            compost_slots_arr.pop(0)

    return


def bank_for_mats(curr_loop):
    if not open_ge_bank():
        # Try again just in case
        if not open_ge_bank():
            return False

    is_bank_tab_open(tab_num=HERB_BANK_TAB_NUM, should_open=True)

    deposit_all()

    API.AntiBan.sleep_between(0.3, 0.4)

    if curr_loop == 1:
        # Set withdraw to x
        is_withdraw_qty("x", True)
        # Right click salt peter and withdraw 14
        if not withdraw_initial_salt():
            write_debug(f'Something went wrong while withdrawing initial salts')
            return False
    else:
        # Withdraw salt normally
        if not withdraw_salt():
            write_debug(f'Something went wrong while withdrawing salt normally')
            return False

        if not withdraw_compost():
            write_debug(f'Something went wrong while withdrawing compost')
            return False

        API.AntiBan.sleep_between(0.2, 0.8)

    close_bank()

    API.AntiBan.sleep_between(0.4, 0.5)
    return True


# HELPERS
def withdraw_initial_salt():
    if does_img_exist(img_name="Banked_Salt", script_name=SCRIPT_NAME, threshold=0.9):
        write_debug(f'Found salt - Long clicking to withdraw')
        x, y = get_existing_img_xy()
        adj_salt_xy = x + 15, y + 15
        mouse_long_click(adj_salt_xy)
        if wait_for_img(img_name="withdraw_x", category="Banking", threshold=0.9, should_click=True, click_middle=True):
            if wait_for_img(img_name="Enter_Amount", category="Interface", threshold=0.9):
                pag.press('1')
                pag.press('4')
                API.AntiBan.sleep_between(0.2, 0.4)
                pag.press('enter')
                return True
    return False


def withdraw_salt():
    return wait_for_img(img_name="Banked_Salt", script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def withdraw_compost():
    return wait_for_img(img_name="Banked_Compost", script_name="GE_Sulpher_Fertalizer", threshold=0.96, should_click=True, click_middle=True)


def is_processing():
    return wait_for_img(img_name="Farming", category="Exp_Drops", threshold=0.9)