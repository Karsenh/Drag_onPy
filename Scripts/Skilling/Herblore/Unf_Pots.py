import datetime
import random
from API.AntiBan import shutdown
import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open
from API.Interface.Bank import is_withdraw_qty, close_bank, is_bank_tab_open, deposit_all
from API.Imaging.Image import does_img_exist, get_existing_img_xy, wait_for_img
from API.Mouse import mouse_click, mouse_long_click
from API.Interface.General import get_xy_for_invent_slot
import pyautogui as pag

HERB_TYPE = "snapdragon"
herb_start_time = None

MAKE_FINISHED = True


def start_unf_pots(curr_loop):
    if curr_loop == 1:
        setup_interface("west", 5, "down")
        is_tab_open("inventory", should_be_open=True)

    open_bank()

    if not withdraw_herbs_and_vials(curr_loop):
        return False

    # Close bank
    close_bank()

    API.AntiBan.sleep_between(0.6, 0.7)

    make_unf_pots()

    API.AntiBan.sleep_between(8.0, 11.0)

    return True


def open_bank():
    ge_bank_xy = 771, 469

    # Click to open bank
    mouse_click(ge_bank_xy)
    API.AntiBan.sleep_between(2.5, 2.6)

    return


def withdraw_herbs_and_vials(curr_loop):
    global HERB_TYPE

    deposit_all()
    API.AntiBan.sleep_between(0.5, 0.6)

    if curr_loop != 1:
        print('not first loop')
    #     Withdrawing normally
        if does_img_exist(img_name=HERB_TYPE, script_name="Unf_Pots", should_click=True, x_offset=10, y_offset=7):
            API.AntiBan.sleep_between(0.6, 0.7)
        else:
            return shutdown(script_name="Unf_Pots", reason=f"Couldn't find anymore {HERB_TYPE} to withdraw from bank.")

        if does_img_exist(img_name="water_vial", script_name="Unf_Pots", should_click=True, x_offset=15, y_offset=8, threshold=0.99):
            API.AntiBan.sleep_between(0.8, 0.9)
        else:
            return shutdown(script_name="Unf_Pots", reason=f"Couldn't find anymore vials of water to withdraw from bank.")

    else:
        print('first loop - checking for correct tab')
    #     Check we're on tab 6
        is_bank_tab_open(tab_num=6, should_open=True)
        API.AntiBan.sleep_between(0.6, 0.9)

        withdraw_14(item=HERB_TYPE)

        if does_img_exist(img_name="water_vial", script_name="Unf_Pots", should_click=True, x_offset=15, y_offset=8, threshold=0.99):
            API.AntiBan.sleep_between(0.8, 0.9)

        # withdraw_14(item="water_vial")
    return True


def make_unf_pots():
    global herb_start_time

    if random.randint(1, 5) > 3:
        herb_slot = get_xy_for_invent_slot(13)
        vial_slot = get_xy_for_invent_slot(17)
    else:
        herb_slot = get_xy_for_invent_slot(14)
        vial_slot = get_xy_for_invent_slot(15)

    mouse_click(herb_slot)
    API.AntiBan.sleep_between(0.8, 1.0)
    mouse_click(vial_slot)

    API.AntiBan.sleep_between(1.1, 1.2)

    start_making_xy = 456, 180
    mouse_click(start_making_xy)

    herb_start_time = datetime.datetime.now()

    return


# HELPERS
def withdraw_14(item):
    is_withdraw_qty("x", should_click=True)
    API.AntiBan.sleep_between(0.5, 0.9)

    does_img_exist(img_name=f'{item}', script_name="Unf_Pots")
    herb_xy = get_existing_img_xy()
    mouse_long_click(herb_xy)
    does_img_exist(img_name="withdraw_x", category="Banking", should_click=True, threshold=0.9, x_offset=27, y_offset=5)
    API.AntiBan.sleep_between(1.0, 1.1)

    pag.press('1')
    API.AntiBan.sleep_between(0.4, 0.7)
    pag.press('4')
    API.AntiBan.sleep_between(0.8, 1.1)

    pag.press('enter')

    API.AntiBan.sleep_between(1.7, 1.8)
    return
