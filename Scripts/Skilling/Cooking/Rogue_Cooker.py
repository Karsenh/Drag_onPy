import random
import keyboard
import pyautogui as pag
from datetime import datetime
import API.AntiBan
from API.Mouse import mouse_click, mouse_drag, mouse_long_click
from API.Interface.General import setup_interface, get_xy_for_invent_slot, relog
from API.Interface.Bank import is_bank_tab_open, deposit_all, close_bank, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Debug import write_debug
from API.Time import get_curr_runtime, reset_curr_runtime
from GUI.Imports.PreLaunch_Gui.Plg_Script_Options import Global_Script_Options

BANK_TAB = 1
FOOD_TO_COOK = None
has_cooking_gauntlets = True
START_COOK_TIME = None


def start_rogue_cooking(curr_loop):
    global START_COOK_TIME

    if curr_loop != 1:
        write_debug(f'Checking if cooking...')

        curr_rt = get_curr_runtime()

        if curr_rt.total_seconds() > 19800:
            relog()
            setup_interface("south", 5, "up")
            reset_curr_runtime()

        if not open_rogue_bank():
            return False

        deposit_all()

        withdraw_food_to_cook()

        close_bank()

        cook_food()
    else:
        # This is the first loop
        set_food_to_cook()
        setup_interface("south", 5, "up")
        API.AntiBan.sleep_between(0.7, 0.8)
        if not open_rogue_bank():
            return False
        # check_for_gauntlets()
        deposit_all()
        withdraw_food_to_cook()
        close_bank()
        cook_food()
        # API.AntiBan.sleep_between(1.5, 1.8)

    return True


def set_food_to_cook():
    global FOOD_TO_COOK

    for option in Global_Script_Options.options_arr:
        if option.name == 'Food Type':
            print(f'Found Food Type option - Setting to: {option.value}')
            FOOD_TO_COOK = option.value

    return


def open_rogue_bank():
    # API.AntiBan.sleep_between(2.0, 2.1)
    bank_sel_xy = 950, 450
    mouse_long_click(bank_sel_xy)
    API.AntiBan.sleep_between(0.1, 0.8)
    if not wait_for_img(img_name="bank_emerald", script_name="Rogue_Cooker", should_click=True, x_offset=10, y_offset=5,
                 threshold=0.90, max_wait_sec=5):
        return False
    # Wait for bank to be open, then proceed otherwise something went wrong
    if not wait_for_img(img_name="bank_is_open", script_name="Rogue_Cooker", threshold=0.95):
        return False
    is_withdraw_qty('all', should_click=True)
    API.AntiBan.sleep_between(0.5, 0.6)
    if not is_bank_tab_open(tab_num=BANK_TAB, should_open=True, double_check=True):
        return False
    return True


def withdraw_food_to_cook():
    # food_withdraw_slot = 905, 443
    does_img_exist(img_name=f"banked_raw_{FOOD_TO_COOK}", script_name="Rogue_Cooker", threshold=0.92, should_click=True, click_middle=True)
    API.AntiBan.sleep_between(0.6, 0.7)

    return


def cook_food():
    global START_COOK_TIME
    fire_xy = 775, 667

    mouse_click(fire_xy, max_x_dev=15, max_y_dev=13)

    # API.AntiBan.sleep_between(1.75, 1.8)
    if not wait_for_img(img_name="cook_dialogue", script_name="Rogue_Cooker"):
        return False

    if not does_img_exist(img_name="all_qty_selected", category="General", threshold=0.95):
        does_img_exist(img_name="all_qty", category="General", threshold=0.9, should_click=True, x_offset=8, y_offset=7)
        API.AntiBan.sleep_between(2.0, 2.1)

    pag.press("space")

    API.AntiBan.sleep_between(1.1, 1.6)

    if START_COOK_TIME is None:
        START_COOK_TIME = datetime.now()

    curr_time = datetime.now()
    time_diff = curr_time - START_COOK_TIME
    time_diff_seconds = time_diff.total_seconds()
    print(f'Time difference: {time_diff_seconds}')
    max_wait_seconds = random.randint(60, 65)
    wait_sec = max_wait_seconds - time_diff_seconds
    if wait_sec > 1:
        if wait_for_img(img_name='level_up', category='General', max_wait_sec=wait_sec):
            cook_food()

    START_COOK_TIME = None
    return True


def is_cooking():
    return wait_for_img(img_name="cooking_exp", script_name="Rogue_Cooker", threshold=0.90, max_wait_sec=6)


def check_for_level_dialogue():
    if does_img_exist(img_name="level_up", category="General"):
        API.AntiBan.sleep_between(2.0, 2.1)
        return True
    return False


def check_for_gauntlets():
    is_bank_tab_open(tab_num=BANK_TAB, should_open=True)

    # Withdraw gauntlets if found in bank
    if does_img_exist(img_name="cooking_gauntlets", script_name="Rogue_Cooker", threshold=0.99, should_click=True):
        API.AntiBan.sleep_between(0.6, 0.7)

        # Equip cooking gauntlets in inventory
        invent_gauntlets_xy = get_xy_for_invent_slot(1)
        mouse_long_click(invent_gauntlets_xy)
        does_img_exist(img_name="Wear", category="General", threshold=0.95, should_click=True, y_offset=15, x_offset=5)
        API.AntiBan.sleep_between(0.4, 0.5)

    return
