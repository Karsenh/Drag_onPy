import API.AntiBan
from API.Interface.General import setup_interface, is_hp_gt, is_tab_open
from API.Interface.Bank import wait_for_open_bank, is_bank_tab_open, close_bank, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Mouse import mouse_click, mouse_long_click

script_name = "Ardy_Knights"

selected_food = 'monkfish'
food_tab_num = 5
necklace_tab_num = 2
use_dodgy_necklace = True
has_food = False
has_necklace = False
curr_tile = None
pickpocket_count = 0
open_bank_attempts = 0


def start_pickpocketing_ardy_knights(curr_loop):

    if curr_loop == 1:
        setup_interface("east", 4, "down")
        API.AntiBan.sleep_between(0.6, 0.7)
        if not set_curr_tile():
            print(f'Something went wrong trying to set tile on first loop. Exiting...')
            return False
        bank_handler()
        open_coin_bag()
        # Check/set what tile we're on - thieving_tile or bank_tile

    if not set_curr_tile():
        print(f'⛔ Current tile not recognized! Exiting...')
        return False

    thieving_handler()

    bank_handler()

    print(f'🔄 PICKPOCKET COUNT: {pickpocket_count}')

    return True


def set_curr_tile():
    global curr_tile
    attempts = 0

    if does_img_exist(img_name="bank_tile_from_east", script_name=script_name, threshold=0.95):
        curr_tile = "bank_tile"
        print(f'🏦 On bank tile - curr_tile = {curr_tile}')

    elif does_img_exist(img_name="thieving_tile_from_east", script_name=script_name, threshold=0.87):
        curr_tile = "thieving_tile"
        print(f'🦝 On thieving tile - curr_tile = {curr_tile}')

    else:
        if attempts > 1:
            print(f'Failed second attempt. Exiting...')
            return False
        curr_tile = None
        print(f"Couldn't find either tile images (bank nor thieving) - curr_tile = {curr_tile}")
        knight_potential_xy = 772, 418
        mouse_long_click(knight_potential_xy)
        wait_for_img(img_name="pickpocket_knight", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(0.5, 0.6)
        attempts += 1
        print(f'Making another attempt...')
        set_curr_tile()

    return True


# Check if we have food / necklaces
# Bank for what we need and move back to thieving spot
def bank_handler():
    global selected_food
    global has_food
    global use_dodgy_necklace
    global has_necklace

    # Check if we need food
    has_food = does_img_exist(img_name=f"inventory_{selected_food}", script_name=script_name, threshold=0.9)
    print(f'has_food = {has_food}')

    # If we're using necklaces, check if we need necklaces
    if use_dodgy_necklace:
        has_necklace = does_img_exist(img_name='inventory_necklace', script_name=script_name, threshold=0.9)
        print(f'has_necklace = {has_necklace}')

    # We have FOOD
    if has_food:
        if not use_dodgy_necklace:
            return True
        else:
            if has_necklace:
                return True

    # Beyond this point we need food at least...
    open_ardy_bank()

    # Withdraw food
    if not has_food:
        withdraw_food(selected_food)

    # Check if we need necklace and withdraw from appropriate tab
    if use_dodgy_necklace:
        if not has_necklace:
            withdraw_dodgy_necklace()

    # Close bank
    close_bank()

    return


def thieving_handler():
    global selected_food
    global use_dodgy_necklace
    global pickpocket_count
    global curr_tile

    knight_xy_from_bank = 548, 514
    knight_xy_from_thieving = 704, 475

    # Check health
    while not is_hp_gt(50):
        # If less than half - eat food
        does_img_exist(img_name=f"inventory_{selected_food}", script_name=script_name, should_click=True, threshold=0.95)
        API.AntiBan.sleep_between(0.6, 0.7)

    if pickpocket_count % 12 == 1:
        if use_dodgy_necklace:
            # Check if necklace equipped - equip if not
            handle_necklace_equip()

    # Check pickpocket count to determine whether to open inventory coin bag or not
    if pickpocket_count % 8 == 1:
        open_coin_bag()

    if curr_tile == "thieving_tile":
        mouse_click(knight_xy_from_thieving, min_num_clicks=3, max_num_clicks=5)
    elif curr_tile == "bank_tile":
        mouse_long_click(knight_xy_from_bank)
        wait_for_img(img_name="pickpocket_knight", script_name=script_name, should_click=True, y_offset=5, x_offset=10)
        API.AntiBan.sleep_between(0.8, 0.9)
        curr_tile = "thieving_tile"

    # Check curr_tile and click knight_xy accordingly
        # Wait for thieving exp drop to confirm continuation
        # Increase pickpocket count
    if wait_for_img(img_name="thieving_exp", script_name=script_name, max_wait_sec=1):
        pickpocket_count += 1
        thieving_handler()

    return


# --------
# HELPERS
# --------
def open_ardy_bank():
    global open_bank_attempts
    global curr_tile

    wait_for_img(img_name="ardy_bank", script_name="Ardy_Knights", should_click=True, max_clicks=2, threshold=0.95, max_wait_sec=10)

    # if curr_tile == "thieving_tile":
    #     bank_xy = 914, 308
    # elif curr_tile == "bank_tile":
    #     bank_xy = 774, 401
    #
    # mouse_click(bank_xy)

    if not wait_for_open_bank():
        if open_bank_attempts > 3:
            return False
        open_bank_attempts += 1
        open_ardy_bank()
    else:
        open_bank_attempts = 0
        return True


def withdraw_food(food_type):
    global food_tab_num

    is_bank_tab_open(tab_num=food_tab_num, should_open=True)

    is_withdraw_qty(qty='10', should_click=True)

    wait_for_img(img_name=f"bank_{food_type}", script_name=script_name, should_click=True)

    return


def withdraw_dodgy_necklace():
    global necklace_tab_num

    is_bank_tab_open(tab_num=necklace_tab_num, should_open=True)

    wait_for_img(img_name="bank_necklace", script_name=script_name, should_click=True)

    return


def handle_necklace_equip():
    is_tab_open(tab="equipment", should_open=True)
    # API.AntiBan.sleep_between(0.5, 0.6)

    if not does_img_exist(img_name="equipped_necklace", script_name=script_name):
        is_tab_open("inventory", should_open=True)
        wait_for_img(img_name="inventory_necklace", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(0.5, 0.6)
    else:
        is_tab_open("inventory", should_open=True)

    return


def open_coin_bag():
    is_tab_open("inventory", should_open=True)
    API.AntiBan.sleep_between(0.2, 0.3)
    does_img_exist(img_name="inventory_coin_bag", script_name=script_name, should_click=True)
    return
