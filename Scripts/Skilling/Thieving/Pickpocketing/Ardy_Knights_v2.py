import random

import API.AntiBan
from API.Interface.General import setup_interface, is_hp_gt, is_tab_open
from API.Interface.Bank import is_bank_open, is_bank_tab_open, close_bank, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Mouse import mouse_click, mouse_long_click
from API.AntiBan import write_debug

USE_NECKLACE = True
NECKLACE_TAB_NUM = 1
FOOD_TAB_NUM = 1
FOOD_TYPE = 'monkfish'
CURR_TILE = 1

SCRIPT_NAME = 'Ardy_Knights'


class CoordinatesFromTile:
    def __init__(self, knight_xy, bank_xy):
        self.knight_xy = knight_xy
        self.bank_xy = bank_xy


# Thieving Tile
knight_from_1 = 724, 483
bank_from_1 = 842, 270
TILE_1 = CoordinatesFromTile(knight_from_1, bank_from_1)

# Bank Tile
knight_from_2 = 576, 437
bank_from_2 = 825, 256
TILE_2 = CoordinatesFromTile(knight_from_2, bank_from_2)


def start_pickpocketing_knight(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        if not update_curr_tile():
            return False

        # Check if we have food in inventory
        needs_food = not has_inventory_food()
        write_debug(f'needs_food: {needs_food}')

        # Check the dodgy necklace
        needs_necklace = False

        should_check_necklace = curr_loop == 2 or curr_loop % 9 == 0

        if USE_NECKLACE and should_check_necklace:
            has_equipped_necklace = get_is_necklace_equipped()
            has_inventory_necklace = get_is_necklace_in_inventory()

            if not has_equipped_necklace and not has_inventory_necklace:
                needs_necklace = True

            elif not has_equipped_necklace:
                equip_necklace_from_invent()

        write_debug(f'needs_necklace: {needs_necklace}')

        # Bank based on food / necklace values
        should_bank = False

        if needs_food:
            should_bank = True

        if USE_NECKLACE and needs_necklace:
            should_bank = True

        write_debug(f'should_bank = {should_bank}')

        if should_bank:
            if not open_bank():
                return False
            else:
                update_curr_tile()

            if USE_NECKLACE and needs_necklace:
                withdraw_dodgy_necklace()

            if needs_food:
                withdraw_food()

            close_bank()

        # Otherwise, pickpocket ardy knight
        while not is_hp_gt(50):
            if not eat_food():
                return True

        r_max_num_pickpockets = random.randint(8, 11)

        should_cont_pickpocketing = True

        open_coin_pouch()

        while should_cont_pickpocketing:
            print(f'⏬ TILE: {CURR_TILE}')
            # pickpocket_knight()
            knight_from_1_xy = 701, 457
            mouse_click(knight_from_1_xy, min_num_clicks=1, max_num_clicks=3)
            should_cont_pickpocketing = saw_thieving_exp()

    else:
        print(f'First loop')
        setup_interface('east', 4, 'down')

    return True


# METHODS
def update_curr_tile():
    global CURR_TILE

    if is_on_tile_1():
        set_tile_val(1)
    elif is_on_tile_2():
        set_tile_val(2)
    else:
        write_debug('⛔ Failed to find a curr tile!')
        return False

    write_debug(f'CURR_TILE Set: {CURR_TILE}')
    return True


def open_bank():
    long_click_bank_from_curr_tile()
    sel_bank_option()
    return is_bank_open(max_wait_sec=5)


def withdraw_dodgy_necklace():
    is_bank_tab_open(tab_num=NECKLACE_TAB_NUM, should_open=True)
    is_withdraw_qty(qty='10', should_click=True)
    return does_img_exist(img_name='banked_dodgy_necklace', script_name=SCRIPT_NAME, should_click=True, click_middle=True)


def withdraw_food():
    is_bank_tab_open(tab_num=NECKLACE_TAB_NUM, should_open=True)
    is_withdraw_qty(qty='10', should_click=True)
    return does_img_exist(img_name=f'banked_{FOOD_TYPE}', script_name=SCRIPT_NAME, should_click=True, click_middle=True)


def equip_necklace_from_invent():
    is_tab_open('inventory', True)
    return does_img_exist(img_name='inventory_dodgy_necklace', script_name=SCRIPT_NAME, should_click=True, click_middle=True, threshold=0.9)


def move_to_tile_1():
    long_click_knight_from_curr_tile()
    return does_img_exist(img_name='pickpocket_knight_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def pickpocket_knight():
    long_click_knight_from_curr_tile()
    return does_img_exist(img_name='pickpocket_knight_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def eat_food():
    is_tab_open('inventory', True)
    return does_img_exist(img_name=f'inventory_{FOOD_TYPE}', script_name=SCRIPT_NAME, threshold=0.94, should_click=True, click_middle=True)


def open_coin_pouch():
    is_tab_open('inventory', True)
    return does_img_exist(img_name='inventory_coin_pouch', script_name=SCRIPT_NAME, should_click=True, click_middle=True)


# HELPERS
def is_on_tile_1():
    write_debug(f'Checking if on tile 1')
    return wait_for_img(img_name='tile_1_flag', script_name=SCRIPT_NAME, threshold=0.85, max_wait_sec=3)


def is_on_tile_2():
    write_debug(f'Checking if on tile 2')
    if wait_for_img(img_name='tile_2_flag', script_name=SCRIPT_NAME, threshold=0.85, max_wait_sec=3) or is_bank_open(3):
        write_debug(f'Bank is open or tile 2 flag found')
        return True
    else:
        return False


def set_tile_val(new_tile_val):
    global CURR_TILE
    write_debug(f'Upating CURR_TILE: from: {CURR_TILE} to {new_tile_val}')
    CURR_TILE = new_tile_val
    return


def has_inventory_food():
    write_debug(f'Checking for inventory food: {FOOD_TYPE}')
    is_tab_open('inventory', True)
    return does_img_exist(img_name=f'inventory_{FOOD_TYPE}', script_name=SCRIPT_NAME, threshold=0.94)


def get_is_necklace_equipped():
    write_debug(f'Checking for equipped Dodgy Necklace')
    is_tab_open('equipment', True)
    return does_img_exist(img_name=f'equipped_dodgy_necklace', script_name=SCRIPT_NAME, threshold=0.85)


def sel_bank_option():
    return wait_for_img(img_name='bank_option', script_name=SCRIPT_NAME, threshold=0.96, should_click=True, click_middle=True)


def get_is_necklace_in_inventory():
    is_tab_open('inventory', True)
    return does_img_exist(img_name='inventory_dodgy_necklace', script_name=SCRIPT_NAME)


def long_click_bank_from_curr_tile():
    if CURR_TILE == 1:
        mouse_long_click(TILE_1.bank_xy)
    elif CURR_TILE == 2:
        mouse_long_click(TILE_2.bank_xy)
    else:
        write_debug(f'Failed to long_click_bank_from bad CURR_TILE: {CURR_TILE}')
        return False
    return True


def long_click_knight_from_curr_tile():
    if CURR_TILE == 1:
        mouse_long_click(TILE_1.knight_xy)
    elif CURR_TILE == 2:
        mouse_long_click(TILE_2.knight_xy)
    else:
        write_debug(f'Failed to long_click_knight_from bad CURR_TILE: {CURR_TILE}')
        return False
    return True


def saw_thieving_exp():
    return wait_for_img(img_name='Thieving', category='Exp_Drops', max_wait_sec=2)
