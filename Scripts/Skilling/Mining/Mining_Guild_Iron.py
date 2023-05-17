import keyboard

import API.AntiBan
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy, does_color_exist, \
    does_color_exist_in_thresh
from API.Imports.Paths import BS_SCREEN_PATH
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled, drop_inventory, relog
from API.Mouse import mouse_click, mouse_long_click
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

ROCK_CLICK_INTERVAL = 0.85


def start_mining_guild_iron(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        while not inventory_full():
            mine_iron()

        curr_rt = get_curr_runtime()

        if curr_rt.total_seconds() > 19800:
            relog()
            setup_interface("south", 5, "up")
            reset_curr_runtime()

        if not deposit_inventory():
            print(f'⛔ Deposite inventory failed for some reason - likely found iron in inventory after attempting to deposit - Exiting...')
            return False

        if not move_back_to_ore():
            return False

        if is_dpick_spec_ready():
            use_spec()



    else:
        print(f'First loop')
        setup_interface('south', 3, 'up')
        if is_dpick_spec_ready():
            use_spec()
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