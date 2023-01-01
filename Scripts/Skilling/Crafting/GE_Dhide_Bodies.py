import random

from API.Interface.General import setup_interface, get_xy_for_invent_slot, is_tab_open
from API.Interface.Bank import is_bank_open, deposit_all, is_withdraw_qty, is_bank_tab_open, close_bank
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Debug import write_debug
from API.Mouse import mouse_click
import pyautogui as pag
import API.AntiBan

dragon_leather_color = "green"
jewelry_tab_num = 2
script_name = "GE_Dhide_Bodies"


def start_crafting_dhide_bodies(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop - Main Script Logic Here')
        # If we're crafting (crafting exp drop seen) return True
        if not is_crafting():
            print(f"No crafting exp drop seen for six sec. Must not be crafting due to level up or no more mats.")

            if did_level():
                handle_level_dialogue()
                craft_dhide_bodies()
                return True

            open_ge_bank()

            API.AntiBan.sleep_between(0.3, 1.1, likelihood=50)

            deposit_dhide_bodies()

            if not withdraw_leather():
                write_debug(f'We must be out of {dragon_leather_color} dragon leather. Exiting...')
                return False

            API.AntiBan.sleep_between(0.4, 0.9)

            close_bank()

            API.AntiBan.sleep_between(0.3, 1.1, likelihood=50)

            return craft_dhide_bodies()

        else:
            print(f"Crafting exp drop seen - we're still crafting. Returning True...")
            return True
    else:
        # First loop - setup script
        print(f'This is the first loop')
        setup_interface("north", 4, "up")
        # Open bank
        if not open_ge_bank():
            return False

        # Deposit all inventory items
        deposit_all()

        # Open Jewelry tab
        is_bank_tab_open(tab_num=jewelry_tab_num, should_open=True)

        # Check we're on withdraw qty 1
        is_withdraw_qty(qty="1")

        # Withdraw needle
        does_img_exist(img_name="Banked_needle", script_name=script_name, should_click=True, x_offset=10)

        # Check we're on withdraw qty All
        is_withdraw_qty("all")

        # Withdraw Thread
        does_img_exist(img_name="Banked_thread", script_name=script_name, should_click=True)

        # Withdraw Leather Type
        if not withdraw_leather():
            write_debug(f'We must be out of {dragon_leather_color} dragon leather. Exiting...')
            return False

        # Close bank
        close_bank()

        return craft_dhide_bodies()


def open_ge_bank():
    wait_for_img(img_name="Ge_bank", script_name=script_name, threshold=0.85, should_click=True, x_offset=20)
    if is_bank_open():
        return True
    else:
        return False


def is_crafting():
    is_tab_open("inventory", True)
    return does_img_exist(img_name=f"Inventory_{dragon_leather_color}_leather", script_name="GE_Dhide_Bodies", threshold=0.8)


def withdraw_leather():
    global dragon_leather_color
    return does_img_exist(img_name=f"Banked_{dragon_leather_color}_leather", script_name=script_name, should_click=True, img_sel="first", x_offset=40)


def craft_dhide_bodies():
    is_tab_open("inventory", True)
    does_img_exist(img_name="Needle", script_name="GE_Dhide_Bodies", threshold=0.7, should_click=True)
    API.AntiBan.sleep_between(0.2, 0.7, 35)
    mouse_click(get_random_invent_slot_between(5, 9))
    API.AntiBan.sleep_between(0.2, 0.9, 35)
    if not wait_for_img(img_name="Green_body_craft_btn", script_name=script_name, should_click=True):
        return False
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
