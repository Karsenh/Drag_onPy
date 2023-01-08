import random

import numpy.random

import API.AntiBan
from API.Mouse import mouse_click, mouse_long_click
from API.Interface.Bank import is_bank_open, is_bank_tab_open, close_bank, deposit_all, is_withdraw_qty
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy

SCRIPT_NAME = "GE_Superheat_Gold"

MAGIC_TAB_NUM = 1
SMITHING_TAB_NUM = 4
NEEDS_STAFF = True
NEEDS_GAUNTLETS = True

USE_GAUNTLETS = True

# SCRIPT NOTES:
# This script requires a mystic fire staff / fire staff - can't use other's like mist and smoke etc. slotted in MAGIC/RC tab
# This script requires nature runes slotted in MAGIC/RC tab or inventory

# OPTIONS:
# Use Goldsmithing Gauntlets (requries slot in SMITHING bank tab)


def start_superheating_gold(curr_loop):

    if curr_loop != 1:
        print(f'doing main loop shit')

        if not open_ge_bank():
            return False

        deposit_gold_bars()

        if not withdraw_gold_ore():
            return False

        close_bank()

        superheat_gold_ore()

    else:
        print(f'This is the first loop')
        setup_interface("east", 4, "up")

        check_equipment()

        if not open_ge_bank():
            return False

        deposit_all()

        if NEEDS_STAFF:
            withdraw_staff()

        if NEEDS_GAUNTLETS:
            if USE_GAUNTLETS:
                withdraw_gauntlets()

        withdraw_nats()

        withdraw_gold_ore()

        API.AntiBan.sleep_between(0.2, 0.3)

        close_bank()

        superheat_gold_ore()

    return True


def open_ge_bank():

    # ge_bank_xy = 710, 443
    # mouse_click(ge_bank_xy, min_num_clicks=2)
    wait_for_img(img_name="Ge_Bank", script_name="GE_Superheat_Gold", should_click=True, threshold=0.95, x_offset=10, min_clicks=2, max_clicks=3)

    if is_bank_open():
        return True
    else:
        return False


def check_equipment():
    global NEEDS_STAFF
    global NEEDS_GAUNTLETS

    is_tab_open("equipment", should_be_open=True)

    if does_img_exist(img_name="Equipped_Fire_Staff", script_name=SCRIPT_NAME):
        NEEDS_STAFF = False

    if does_img_exist(img_name="Equipped_Gauntlets", script_name=SCRIPT_NAME):
        NEEDS_GAUNTLETS = False

    return


def withdraw_staff():
    global MAGIC_TAB_NUM

    is_bank_tab_open(tab_num=MAGIC_TAB_NUM, should_open=True)
    is_withdraw_qty("1", should_click=True)

    does_img_exist(img_name="Banked_fire_staff", script_name=SCRIPT_NAME, should_click=True, x_offset=30)
    API.AntiBan.sleep_between(0.9, 1.1)

    mouse_long_click(get_xy_for_invent_slot(1))
    wait_for_img(img_name="Wield", category="General", should_click=True)
    API.AntiBan.sleep_between(0.1, 0.2)

    deposit_all()
    return


def withdraw_nats():
    global MAGIC_TAB_NUM

    is_bank_tab_open(tab_num=MAGIC_TAB_NUM, should_open=True)

    is_withdraw_qty("all", should_click=True)

    does_img_exist(img_name="Banked_Nats", script_name=SCRIPT_NAME, should_click=True, x_offset=30, threshold=0.98)
    return


def withdraw_gauntlets():
    global SMITHING_TAB_NUM

    is_bank_tab_open(tab_num=SMITHING_TAB_NUM, should_open=True)

    does_img_exist(img_name="Banked_Goldsmith_Gauntlets", script_name=SCRIPT_NAME, should_click=True)
    API.AntiBan.sleep_between(0.9, 1.2)

    mouse_long_click(get_xy_for_invent_slot(1))
    wait_for_img(img_name="Wear", category="General", should_click=True)
    API.AntiBan.sleep_between(0.1, 0.2)

    deposit_all()
    return


def withdraw_gold_ore():
    global SMITHING_TAB_NUM

    is_bank_tab_open(tab_num=SMITHING_TAB_NUM, should_open=True)
    is_withdraw_qty(qty="all", should_click=True)

    return does_img_exist(img_name="Banked_Gold_Ore", script_name="GE_Superheat_Gold", x_offset=30, should_click=True, threshold=0.95)


def deposit_gold_bars():
    is_withdraw_qty("all", should_click=True)

    r_invent_slot_num = random.randint(2, 27)

    mouse_click(get_xy_for_invent_slot(r_invent_slot_num))
    return


def superheat_gold_ore():
    should_continue = True

    # while should_continue:

    img_sels = ["first", "last"]
    is_tab_open("magic", should_be_open=True)
    gold_ore_slots = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    # Shuffle inventory slots of gold for random selection order
    numpy.random.shuffle(gold_ore_slots)

    print(f'RANDOM SHUFFLE ARR = {gold_ore_slots}')
    # API.AntiBan.sleep_between(5.0, 5.1)

    curr_gold_slot = 2
    curr_slot_idx = 0

    while gold_ore_slots:
        if not wait_for_img(img_name="Superheat_Spell", script_name=SCRIPT_NAME, should_click=True, x_offset=6, y_offset=6):
            is_tab_open("magic", True)
            if not wait_for_img(img_name="Superheat_Spell", script_name=SCRIPT_NAME, should_click=True, x_offset=6, y_offset=6):
                return False

        r_slot = random.randint(0, len(gold_ore_slots) - 1)
        API.AntiBan.sleep_between(0.1, 0.6, likelihood=32)
        print(f'gold_ore_slots[curr_slot]: {gold_ore_slots[r_slot]}\nr_slot: {r_slot}')

        curr_invent_xy = get_xy_for_invent_slot(gold_ore_slots[r_slot])
        gold_ore_slots.remove(curr_gold_slot)
        mouse_click(curr_invent_xy)
        curr_gold_slot += 1

        API.AntiBan.sleep_between(0.8, 0.9)

    return
