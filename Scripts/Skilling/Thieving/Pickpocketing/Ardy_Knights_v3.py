import random

import pyautogui

import API.AntiBan
from API.Interface.General import setup_interface, is_hp_gt, is_tab_open
from API.Interface.Bank import is_bank_open, is_bank_tab_open, close_bank, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Mouse import mouse_click, mouse_long_click
from API.AntiBan import write_debug

SCRIPT_NAME = 'Ardy_Knights'

FOOD_TYPE = 'monkfish'
IS_USING_NECKLACE = True
CURR_TILE = None
BANK_TAB_NUM = 1
NEEDS_FOODS = False
NEEDS_NECKLACES = False


def start_pickpocketing_knight(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')

        if get_needs_food() or get_needs_necklaces() or curr_loop == 2:
            # if not has_inventory_food():
            #     print(f'🦈❌NEED FOOD')
            #     needs_food = True
            # else:
            #     print(f'🦈✔ HAVE FOOD')
            #
            # if IS_USING_NECKLACE and not has_inventory_necklace():
            #     print(f'📿❌NEED NECKLACE')
            #     needs_necklace = True
            # else:
            #     print(f'📿✔ HAVE NECKLACE')
            #
            # if needs_food or needs_necklace:
            #     print(f'💰🏧 OPENING BANK\nneeds_food: {needs_food}\nneeds_necklace: {needs_necklace}')
            open_bank()

            if get_needs_food():
                print(f'🎒🦈WITHDRAWING FOOD')
                withdraw_food()
            if get_needs_necklaces():
                print(f'🎒📿WITHDRAWING FOOD')
                withdraw_necklaces()

            close_bank()

        if curr_loop == 2 or curr_loop % 6 == 0:
            print(f'📿 CHECKING FOR EQUIPPED NECKLACE')
            if not has_equipped_necklace():
                if not equip_new_necklace():
                    print(f'NO NECKLACE EQUIPPED OR IN INVENTORY')
                    set_needs_necklaces(True)
                    return False

        pickpocket_knight()

    else:
        print(f'First loop')
        setup_interface('west', 4, 'down')

    return True


def pickpocket_knight():
    set_curr_tile()

    if get_curr_tile() == 3:
        # We're clicking the knigth from the bank first
        click_knight_from_bank()

    set_curr_tile()

    if get_curr_tile() != 1 and get_curr_tile() != 2:
        print(f'⛔ Unexpected curr_tile: {get_curr_tile()}')
        return False

    num_pickpockets = 0
    open_coin_pouch()

    while (num_pickpockets < 5 and not needs_to_eat()) or (saw_thieving_exp() and not needs_to_eat()):
        print(f'num_pickpockets = {num_pickpockets}')
        knight_xy_from_1_and_2 = 785, 530
        mouse_click(knight_xy_from_1_and_2, min_num_clicks=4, max_num_clicks=6)
        num_pickpockets += 1
        if num_pickpockets % 15 == 0:
            open_coin_pouch()

    return


def needs_to_eat():
    if not is_hp_gt(50):
        print(f'💔 HP LESS THAN 50 - ATTEMPING TO EAT 🦈')
        while not is_hp_gt(90) and has_inventory_food():
            eat_food()
            API.AntiBan.sleep_between(0.3, 0.4)

        if not has_inventory_food():
            print(f'⛔ 🦈 NO INVENTORY FOOD FOUND - SETTING NEEDS FOOD TRUE')
            set_needs_food(True)
            return True

    return False


def eat_food():
    is_tab_open('inventory', True)
    return does_img_exist(img_name=f'inventory_{FOOD_TYPE}', script_name=SCRIPT_NAME, threshold=0.94, should_click=True, click_middle=True)


def open_coin_pouch():
    is_tab_open('inventory', True)
    return does_img_exist(img_name='inventory_coin_pouch', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def click_knight_from_bank():
    knight_from_bank_xy = 914, 482

    mouse_long_click(knight_from_bank_xy)
    if not does_img_exist(img_name='pickpocket_knight_option', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
        mouse_click(knight_from_bank_xy)

    if not saw_thieving_exp():
        print(f'⛔ Failed to find XP drop after clicking knight from bank')
    else:
        API.AntiBan.sleep_between(0.6, 0.7)

    return


def saw_thieving_exp():
    return wait_for_img(img_name='Thieving', category='Exp_Drops', threshold=0.8, max_wait_sec=2)


def equip_new_necklace():
    is_tab_open('inventory', True)
    return does_img_exist(img_name='inventory_dodgy_necklace', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def has_inventory_food():
    print(f'CHECKING FOR INVENTORY FOOD 🦈')
    is_tab_open('inventory', True)
    return does_img_exist(img_name=f'inventory_{FOOD_TYPE}', script_name=SCRIPT_NAME, threshold=0.9)


def has_inventory_necklace():
    print(f'CHECKING FOR INVENTORY NECKLACES 📿')
    is_tab_open('inventory', True)
    return does_img_exist(img_name=f'inventory_dodgy_necklace', script_name=SCRIPT_NAME, threshold=0.9)


def has_equipped_necklace():
    print(f'CHECKING FOR EQUIPPED NECKLACE 👨🏼📿')
    is_tab_open('equipment', True)
    return does_img_exist(img_name='equipped_dodgy_necklace', script_name=SCRIPT_NAME, threshold=0.9)


def open_bank():
    set_curr_tile()

    print(f'OPENING BANK FROM CURR_TILE: {CURR_TILE}')

    if get_curr_tile() == 1:
        bank_xy = 375, 475
    elif get_curr_tile() == 2:
        bank_xy = 405, 370
    elif get_curr_tile() == 3:
        bank_xy = 610, 355

    mouse_click(bank_xy)

    return is_bank_open(max_wait_sec=15)


def set_curr_tile():
    global CURR_TILE
    print(f'SETTING CURR TILE')

    if does_img_exist(img_name='tile_1', script_name=SCRIPT_NAME, threshold=0.9):
        CURR_TILE = 1
    elif does_img_exist(img_name='tile_2', script_name=SCRIPT_NAME, threshold=0.9):
        CURR_TILE = 2
    elif does_img_exist(img_name='bank_tile', script_name=SCRIPT_NAME, threshold=0.9):
        CURR_TILE = 3
    else:
        print(f'⛔ FAILED TO SET CURR TILE')
        return False

    print(f'✏ SET CURR TILE: {CURR_TILE}')
    return True


def get_curr_tile():
    print(f'🖐🏼 GET CURR TILE: {CURR_TILE}')
    return CURR_TILE


def withdraw_food():
    print(f'WITHDRAWING FOOD')
    is_bank_tab_open(tab_num=BANK_TAB_NUM, should_open=True)
    is_withdraw_qty('10', True)
    return does_img_exist(img_name=f'banked_{FOOD_TYPE}', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def withdraw_necklaces():
    print(f'WITHDRAWING NECKLACES')
    is_bank_tab_open(tab_num=BANK_TAB_NUM, should_open=True)
    is_withdraw_qty('10', True)
    return does_img_exist(img_name=f'banked_dodgy_necklace', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def set_needs_food(new_val):
    global NEEDS_FOODS
    NEEDS_FOODS = new_val
    return


def get_needs_food():
    return NEEDS_FOODS


def set_needs_necklaces(new_val):
    global NEEDS_NECKLACES
    NEEDS_NECKLACES = new_val
    return


def get_needs_necklaces():
    return NEEDS_NECKLACES
# PSEUDO CODE:
# 1. Check if we have inventory necklaces
# 2. Check if we have inventory food
# 3. Check our current tile

