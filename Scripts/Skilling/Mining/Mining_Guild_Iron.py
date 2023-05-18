import keyboard
import pyautogui

import API.AntiBan
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy, does_color_exist, \
    does_color_exist_in_thresh
from API.Imports.Paths import BS_SCREEN_PATH
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled, drop_inventory, relog, \
    get_xy_for_invent_slot
from API.Mouse import mouse_click, mouse_long_click, mouse_move
from API.Time import get_curr_runtime, reset_curr_runtime

SCRIPT_NAME = 'Mining_Guild_Iron'

r1_xy = 765, 524
r2_xy = 832, 479
r3_xy = 756, 388
rock_xy = [r1_xy, r2_xy, r3_xy]

r1_col = [66, 41, 31]
r2_col = [60, 38, 30]
r3_col = [66, 41, 31]
rock_colors = [r1_col, r2_col, r3_col]

CURR_ROCK = 0

ROCK_CLICK_INTERVAL = 0.75

POWER_MINE = True

PM_ITERATION = 0


def start_mining_guild_iron(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')

        if not POWER_MINE:
            while not inventory_full():
                mine_iron()

            curr_rt = get_curr_runtime()

            if curr_rt.total_seconds() > 19800:
                relog()
                setup_interface("south", 3, "up")
                reset_curr_runtime()

            if not deposit_inventory():
                print(f'⛔ Deposite inventory failed for some reason - likely found iron in inventory after attempting to deposit - Exiting...')
                return False

            if not move_back_to_ore():
                return False

            if is_dpick_spec_ready():
                use_spec()
        else:
            print('Power mining...')
            power_mine()
    else:
        print(f'First loop')
        # setup_interface('south', 3, 'up')
        if is_dpick_spec_ready():
            use_spec()
    return True


def power_mine():
    global CURR_ROCK
    global PM_ITERATION

    safe_mode = False

    # turn on otd
    is_otd_enabled(True)

    # open inventory
    is_tab_open('inventory')
    mouse_click(rock_xy[CURR_ROCK])
    CURR_ROCK += 1
    API.AntiBan.sleep_between(1.9, 1.9)

    # click rock
    while get_curr_runtime().total_seconds() < 19800 and not inventory_full():
        print(f'CURR ROCK: {CURR_ROCK}')
        mouse_click(rock_xy[CURR_ROCK])
        if PM_ITERATION % 2 == 0:
            drop_slot_num = 1
        else:
            drop_slot_num = 2

        mouse_move(get_xy_for_invent_slot(drop_slot_num))

        if CURR_ROCK == 1 or CURR_ROCK == 2:
            API.AntiBan.sleep_between(1.2, 1.2)
        else:
            API.AntiBan.sleep_between(1.4, 1.4)
        if safe_mode:
            wait_for_img(img_name='Mining', category='Exp_Drops', max_wait_sec=2)

        pyautogui.leftClick()

        PM_ITERATION += 1
        CURR_ROCK += 1
        if CURR_ROCK == 3:
            CURR_ROCK = 0

    if inventory_full():
        drop_inventory(from_spot_num=1, to_spot_num=27)

    return True


def mine_iron():
    global CURR_ROCK

    if does_color_exist_in_thresh(color_xy=rock_xy[CURR_ROCK], check_color=rock_colors[CURR_ROCK], threshold=15):
        print(f'Found iron color @ curr_rock: {CURR_ROCK}')
        mouse_click(rock_xy[CURR_ROCK], min_num_clicks=1, max_num_clicks=2)
        # wait_for_img(img_name='Mining', category='Exp_Drops', threshold=0.75, max_wait_sec=2)
        API.AntiBan.sleep_between(ROCK_CLICK_INTERVAL, ROCK_CLICK_INTERVAL)
        CURR_ROCK += 1

    if CURR_ROCK == 3:
        CURR_ROCK = 0

    return True


def inventory_full():
    return does_img_exist(img_name='too_full', script_name='Desert_Granite_Miner')


def deposit_inventory():
    print(f'Inventory seems to be full - depositing...')
    bank_deposit_xy = 1385, 342

    mouse_click(bank_deposit_xy)

    if not wait_for_img(img_name='deposit_inventory_btn', category='Banking', should_click=True, click_middle=True, max_wait_sec=15):
        print(f'Failed to find deposit inventory button in deposit box interface - exiting...')
        return False

    keyboard.send('esc')
    return True

    # API.AntiBan.sleep_between(1.0, 1.1)
    #
    # return not does_img_exist(img_name='inventory_iron_ore', script_name=SCRIPT_NAME, img_sel='inventory')


def move_back_to_ore():
    print(f'Moving back to ore spot...')
    ore_spot_xy = 248, 549

    mouse_long_click(ore_spot_xy)

    if not does_img_exist(img_name='walk_here_dark', category='Interface', threshold=0.75, should_click=True, click_middle=True):
        print(f'❌ Failed to find walk_here_dark option - clicking manually...')
        mouse_click(ore_spot_xy)

    API.AntiBan.sleep_between(4.5, 4.6)

    return True


def is_dpick_spec_ready():
    col_xy = 1244, 273
    spec_col = 29, 143, 171
    return does_color_exist(spec_col, col_xy, BS_SCREEN_PATH)


def use_spec():
    spec_xy = 1244, 290
    mouse_click(spec_xy)
    return