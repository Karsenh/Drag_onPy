import pyautogui

import API.AntiBan
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy, does_color_exist
from API.Imports.Paths import BS_SCREEN_PATH
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled, drop_inventory
from API.Mouse import mouse_click, mouse_move

SCRIPT_NAME = 'Desert_Granite_Miner'
CURR_TILE = 1

rock_1_xy = 1063, 166
rock_2_xy = 930, 650
rock_3_xy = 933, 677
rock_4_xy = 627, 720

ORE_COORDS = [rock_1_xy, rock_2_xy, rock_3_xy, rock_4_xy]
SLEEP_TIMES = [.2, .3, .2, .2]
CACHED_HARR_XY = None
CACHED_TAR_XY = None

SHOULD_CONTINUE_MINING = True

NUM_TIMES_EXP_NOT_SEEN = 0

USE_SPEC = True


def start_mining_granite(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        start_mining(curr_loop)
        i = 1
        while SHOULD_CONTINUE_MINING:
            print(f'Mine Next Rock Loop iteration: {i}')
            if not mine_next_rock(i):
                return False
            i += 1

        drop_granite()

        if need_water_refill():
            print(f'is_last_drop: TRUE')
            if not humidify_waterskins():
                if not humidify_waterskins():
                    print(f'Failed to humidify twice')
                    return False

        if is_dpick_spec_ready():
            use_spec()

    else:
        print(f'First loop')
        setup_interface('south', 5, 'up')
        if is_dpick_spec_ready():
            use_spec()
    return True


def start_mining(curr_loop):
    # Click herb
    sel_invent_harralander()

    # Click tar
    use_harralander_with_tar()

    # Click ore nearby
    if curr_loop != 2:
        next_ore_xy = ORE_COORDS[CURR_TILE-1]
        increment_curr_tile()
    else:
        next_ore_xy = 775, 726

    mouse_click(next_ore_xy)

    return True


def mine_next_rock(curr_iteration):
    global CURR_TILE
    global NUM_TIMES_EXP_NOT_SEEN
    global SHOULD_CONTINUE_MINING

    # Click herb
    if not sel_invent_harralander():
        return False

    # Hover over tar
    hover_tar_with_harralander_sel()

    # Wait for mining xp drop
    if not saw_mining_exp():
        print(f'❌ Failed to see mining exp - clicking tar then next ore...')
        SHOULD_CONTINUE_MINING = not does_img_exist(img_name='too_full', script_name=SCRIPT_NAME)
        if not SHOULD_CONTINUE_MINING:
            return True
    else:
        print(f'✔ Saw next mining exp')

    # Click tar (hovered)
    pyautogui.leftClick()

    # Click next ore
    ore_xy = ORE_COORDS[CURR_TILE - 1]
    print(f'Clicking coordinates - {ore_xy}')
    mouse_click(ore_xy)

    increment_curr_tile()

    # Do checks
    # (humidify)

    API.AntiBan.sleep_between(0.8, 0.8)

    return True


# HELPERS
def increment_curr_tile():
    global CURR_TILE

    CURR_TILE += 1
    print(f'Inc curr_tile (now): {CURR_TILE}')

    if CURR_TILE == 5:
        print(f'Resetting curr tile to 1')
        CURR_TILE = 1
    return


def need_water_refill():
    return does_img_exist(img_name='last_drop_of_water', script_name=SCRIPT_NAME, threshold=0.9)


def humidify_waterskins():
    is_tab_open('magic')
    does_img_exist(img_name='lunar_humidify_spell', category='Spells', threshold=0.8, should_click=True, click_middle=True)
    return wait_for_img(img_name='Magic', category='Exp_Drops', threshold=0.75)


def drop_granite():
    global SHOULD_CONTINUE_MINING
    is_otd_enabled(True)
    drop_inventory(from_spot_num=3, to_spot_num=16, should_disable_otd_after=True)
    SHOULD_CONTINUE_MINING = True
    return


def saw_mining_exp():
    return wait_for_img(img_name='Mining', category='Exp_Drops', max_wait_sec=4)


def is_time_to_humidify():
    # Check if 36 minutes has elapsed
    return


def sel_invent_harralander():
    global CACHED_HARR_XY

    is_tab_open('inventory')

    if CACHED_HARR_XY:
        mouse_click(CACHED_HARR_XY)
    else:
        if not does_img_exist(img_name='clean_harralander', script_name=SCRIPT_NAME, threshold=0.8, should_click=True, click_middle=True):
            print(f'⛔ Failed to find Clean Harralander in inventory to click')
            return False
        x, y, = get_existing_img_xy()
        adj_xy = x+6, y+6
        CACHED_HARR_XY = adj_xy

    return True


def use_harralander_with_tar():
    global CACHED_TAR_XY

    is_tab_open('inventory')

    if CACHED_TAR_XY:
        mouse_click(CACHED_TAR_XY)
    else:
        if not does_img_exist(img_name='tar', script_name=SCRIPT_NAME, threshold=0.8, should_click=True, click_middle=True):
            print(f'⛔ Failed to find Tar in inventory to use Harralander with')
            return False
        x, y, = get_existing_img_xy()
        adj_xy = x+6, y+6
        CACHED_TAR_XY = adj_xy
    return True


def is_dpick_spec_ready():
    col_xy = 1244, 273
    spec_col = 29, 143, 171
    return does_color_exist(spec_col, col_xy, BS_SCREEN_PATH)


def use_spec():
    spec_xy = 1244, 290
    mouse_click(spec_xy)
    return


def hover_tar_with_harralander_sel():
    global CACHED_TAR_XY

    is_tab_open('inventory')

    if CACHED_TAR_XY:
        # mouse_click(CACHED_TAR_XY)
        mouse_move(CACHED_TAR_XY)
    else:
        if not does_img_exist(img_name='tar', script_name=SCRIPT_NAME):
            print(f'⛔ Failed to find Tar in inventory to use Harralander with')
            return False
        x, y, = get_existing_img_xy()
        adj_xy = x+6, y+6
        CACHED_TAR_XY = adj_xy
        mouse_move(CACHED_TAR_XY)
    return True


def click_next_ore():
    return
