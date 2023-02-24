import random

from API.Interface.General import setup_interface, get_xy_for_invent_slot, is_tab_open
from API.Interface.Bank import is_bank_open, deposit_all, is_withdraw_qty, is_bank_tab_open, close_bank
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Debug import write_debug
from API.Mouse import mouse_click, mouse_long_click
import pyautogui as pag
import API.AntiBan

DHIDE_COLOR = "green"
BANK_TAB_NUM = 1
SCRIPT_NAME = "GE_Dhide_Bodies"
CRAFTING_ATTEMPTS = 0


def start_crafting_dhide_bodies(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop - Main Script Logic Here')
        # If we're crafting (crafting exp drop seen) return True
        if not is_crafting():
            print(f"No crafting exp drop seen for 2 sec. Must not be crafting due to level up or no more mats.")

            if did_level():
                handle_level_dialogue()
                craft_dhide_bodies()
                return True

            open_ge_bank()

            API.AntiBan.sleep_between(0.3, 1.1, likelihood=10)

            deposit_dhide_bodies()

            if not withdraw_leather():
                write_debug(f'We must be out of {DHIDE_COLOR} dragon leather. Exiting...')
                return False

            API.AntiBan.sleep_between(0.4, 0.9)

            close_bank()

            API.AntiBan.sleep_between(0.3, 1.1, likelihood=8)

            return craft_dhide_bodies()

        else:
            print(f"Crafting exp drop seen - we're still crafting. Returning True...")
            return True
    else:
        # First loop - setup script
        print(f'This is the first loop')
        setup_interface("east", 4, "up")
        # Open bank
        if not open_ge_bank():
            return False

        # Deposit all inventory items
        deposit_all()

        # Open Jewelry tab
        is_bank_tab_open(tab_num=BANK_TAB_NUM, should_open=True)

        # Check we're on withdraw qty 1
        is_withdraw_qty(qty="1")

        # Withdraw needle
        does_img_exist(img_name="Banked_needle", script_name=SCRIPT_NAME, should_click=True, x_offset=10)

        # Check we're on withdraw qty All
        is_withdraw_qty("all")

        # Withdraw Thread
        does_img_exist(img_name="Banked_thread", script_name=SCRIPT_NAME, should_click=True)

        # Withdraw Leather Type
        if not withdraw_leather():
            write_debug(f'We must be out of {DHIDE_COLOR} dragon leather. Exiting...')
            return False
        API.AntiBan.sleep_between(0.3, 0.5)

        # Close bank
        close_bank()

        return craft_dhide_bodies()


def open_ge_bank():
    API.AntiBan.sleep_between(0.3, 0.4)
    if not wait_for_img(img_name="ge_bank", script_name=SCRIPT_NAME, threshold=0.9):
        return False

    bank_xy = get_existing_img_xy()
    mouse_long_click(bank_xy)

    if not does_img_exist(img_name='bank_option', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
        if not does_img_exist(img_name='cancel_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
            return False
        mouse_long_click(bank_xy)
        if not does_img_exist(img_name='bank_option', script_name=SCRIPT_NAME, threshold=0.80, should_click=True, click_middle=True):
            write_debug('Failed to find bank option twice - exiting...')
            return False

    # ge_bank_xy = 710, 443
    # mouse_click(ge_bank_xy)
    return is_bank_open()


def is_crafting():
    return wait_for_img(img_name="Crafting", category="Exp_Drops", max_wait_sec=2)


def withdraw_leather():
    is_bank_tab_open(BANK_TAB_NUM, True)
    return does_img_exist(img_name=f"Banked_{DHIDE_COLOR}_leather", script_name=SCRIPT_NAME, should_click=True, img_sel="first", x_offset=40)


def craft_dhide_bodies():
    global CRAFTING_ATTEMPTS

    is_tab_open("inventory", True)
    does_img_exist(img_name="Needle", script_name="GE_Dhide_Bodies", threshold=0.95, should_click=True)
    API.AntiBan.sleep_between(0.1, 0.2)
    # mouse_click(get_random_invent_slot_between(5, 9))
    if not does_img_exist(img_name='inventory_green_leather', script_name=SCRIPT_NAME, threshold=0.88, should_click=True, click_middle=True):
        if not open_ge_bank():
            return False
        withdraw_leather()
        close_bank()
        does_img_exist(img_name="Needle", script_name="GE_Dhide_Bodies", threshold=0.95, should_click=True)
        if not does_img_exist(img_name='inventory_green_leather', script_name=SCRIPT_NAME, threshold=0.88,
                              should_click=True, click_middle=True):
            return False

    API.AntiBan.sleep_between(0.3, 0.4)
    API.AntiBan.sleep_between(0.2, 0.9, 18)
    if not wait_for_img(img_name="Green_body_craft_btn", script_name=SCRIPT_NAME):
        craft_dhide_bodies()
        CRAFTING_ATTEMPTS += 1
        if CRAFTING_ATTEMPTS > 3:
            print(f'Exiting due to Green body craft btn attempts exceeding three.')
            return False
    else:
        CRAFTING_ATTEMPTS = 0
        mouse_click(get_existing_img_xy(), max_x_dev=14, max_y_dev=14)
        API.AntiBan.sleep_between(1.0, 1.1)
    return True


def did_level():
    return does_img_exist(img_name="level_up", category="General")


def handle_level_dialogue():
    pag.press('space')
    API.AntiBan.sleep_between(1.1, 2.3)
    pag.press('space')
    API.AntiBan.sleep_between(0.8, 1.7)
    return


def deposit_dhide_bodies():
    invent_slot_5_xy = get_xy_for_invent_slot(slot_num=5)
    mouse_click(invent_slot_5_xy)
    return


def get_random_invent_slot_between(from_slot_num, to_slot_num):
    r_slot_xy = random.randint(from_slot_num, to_slot_num)
    return get_xy_for_invent_slot(r_slot_xy)
