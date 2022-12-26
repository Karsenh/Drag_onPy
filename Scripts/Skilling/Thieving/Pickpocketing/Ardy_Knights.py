import API.AntiBan
from API.Interface.General import setup_interface, is_hp_gt, is_tab_open
from API.Interface.Bank import wait_for_open_bank, is_bank_tab_open, close_bank, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img

selected_food = 'monkfish'
food_tab_num = 5
necklace_tab_num = 2
use_dodgy_necklace = True
has_food = False
has_necklace = False
curr_tile = None
pickpocket_count = 0


def start_pickpocketing_ardy_knights(curr_loop):
    global has_food
    global has_necklace

    if curr_loop == 1:
        setup_interface("west", 4, "up")
        # Check/set what tile we're on - thieving_tile or bank_tile
        set_curr_tile()

        bank_handler()

        thieving_handler()



            # Open bank and withdraw food


        # Check if we have food in inventory
            # If no invent food - click to open bank based on what tile we're on
                #
                # Check if we're in food tab - open if not
                # Check if withdraw 10 is selected - select if not
                # Withdraw the bank_<selected_food> (click twice for 20)
            # If we have invent food - continue

        # Move to thieving tile based on the tile we're currently on

    # Check curr_health_gt(percent=10)
        # If gt 10% - Thieve
        # If lt 10% - Click inventory food
            # If no inventory food - open bank from curr_tile
            # Check if fish tab open - open if not
            #

    # Thieve()
        # Check if coinpouch == 28
        # If == 28 - Click coinpouch to open
        # Else click ardy_knight_pickpocket_xy

    # open_bank_from_curr_tile()
        #
    return True


def set_curr_tile():
    global curr_tile

    if does_img_exist(img_name="bank_tile", script_name="Ardy_Knights"):
        curr_tile = "bank_tile"
        print(f'On bank tile - curr_tile = {curr_tile}')
    elif does_img_exist(img_name="thieving_tile", script_name="Ardy_Knights"):
        curr_tile = "thieving_tile"
        print(f'On thieving tile - curr_tile = {curr_tile}')
    else:
        curr_tile = None
        print(f"Couldn't find either tile images (bank nor thieving) - curr_tile = {curr_tile}")

    return curr_tile


# Check if we have food / necklaces
# Bank for what we need and move back to thieving spot
def bank_handler():
    global selected_food
    global has_food
    global use_dodgy_necklace
    global has_necklace

    # Check if we need food
    has_food = does_img_exist(img_name=f"inventory_{selected_food}", script_name="Ardy_Knights")
    print(f'has_food = {has_food}')

    # If we're using necklaces, check if we need necklaces
    if use_dodgy_necklace:
        has_necklace = does_img_exist(img_name='inventory_necklace', script_name="Ardy_Knights", threshold=0.9)
        print(f'has_necklace = {has_necklace}')

    # We have FOOD
    if has_food:
        if not use_dodgy_necklace:
            return True
        else:
            if has_necklace:
                return True
            else:
                print(f'Food but no necklace')

    # Beyond this point we need food at least...
    open_ardy_bank()

    # Withdraw food
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
    knight_xy_from_bank = 12, 12
    knight_xy_from_thieving = 113, 133

    # Check health
    while not is_hp_gt(50):
        # If less than half - eat food
        does_img_exist(img_name=f"inventory_{selected_food}", script_name="Ardy_Knights", should_click=True)
        API.AntiBan.sleep_between(0.6, 0.7)

    # Check if necklace equipped
        # If not - click in inventory

    # Check pickpocket count to determine whether to open inventory coin bag or not

    # Check curr_tile and click knight_xy accordingly
        # Wait for thieving exp drop to confirm continuation
        # Increase pickpocket count


    return


# --------
# HELPERS
# --------
def open_ardy_bank():
    does_img_exist(img_name="ardy_bank", script_name="Ardy_Knights", should_click=True, threshold=0.9)
    if not wait_for_open_bank():
        return False
    return


def withdraw_food(food_type):
    global food_tab_num

    is_bank_tab_open(tab_num=food_tab_num, should_open=True)

    is_withdraw_qty(qty='10', should_click=True)

    wait_for_img(img_name=f"bank_{food_type}", script_name="Ardy_Knights")

    return


def withdraw_dodgy_necklace():
    global necklace_tab_num

    is_bank_tab_open(tab_num=necklace_tab_num, should_open=True)

    wait_for_img(img_name="bank_necklace", script_name="Ardy_Knights", should_click=True)

    return


def is_necklace_equipped():
    is_tab_open(tab="equipment", )