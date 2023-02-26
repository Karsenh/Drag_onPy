import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_run_on, is_run_gt, is_hp_gt
from API.Imaging.Image import wait_for_img, does_img_exist, does_color_exist_in_sub_image, get_existing_img_xy
from API.Mouse import mouse_click, mouse_long_click
from API.Debug import write_debug

SCRIPT_NAME = 'NMZ'

SKILL_TO_TRAIN = 'str'
USE_DHAROKS = True
CACHED_INVENT_ROCK_CAKE_XY = None

# TODO:
# 1. Add guzzle on rock cake if above 10 percent
# 2. Add check for


def start_training_nmz(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')

        if needs_abs():
            print(f'🧪 NEED ABSORPTION POTION')
            if not click_inventory_abs():
                print(f'Exiting script - out of absorptions')
                return False

        if needs_ovl():
            print(f'💪🏼 NEED TO OVERLOAD')
            click_inventory_ovl()

        while needs_rock_cake():
            print(f'🎂 NEED ROCK CAKE - CLICKING INVENTORY CAKE')
            if not click_inventory_cake():
                print(f'FAILED TO FIND INVENTORY ROCK')

    else:
        print(f'First loop')
        setup_interface('north', 3, 'up')
    return True


# -------
# METHODS
# -------
def click_inventory_abs():
    is_tab_open('inventory', True)
    if not does_img_exist(img_name='inventory_abs_4', script_name=SCRIPT_NAME, threshold=0.94, should_click=True, click_middle=True):
        print(f'No inventory absorption pots (4) found')
        if not does_img_exist(img_name='inventory_abs_3', script_name=SCRIPT_NAME, threshold=0.94, should_click=True, click_middle=True):
            print(f'No inventory absorption pots (3) found')
            if not does_img_exist(img_name='inventory_abs_2', script_name=SCRIPT_NAME, threshold=0.94, should_click=True, click_middle=True):
                print(f'No inventory absorption pots (2) found')
                if not does_img_exist(img_name='inventory_abs_1', script_name=SCRIPT_NAME, threshold=0.94,
                                      should_click=True, click_middle=True):
                    print(f'No inventory absorption pots (1) found')
                    return False
    inventory_abs_4_pot = get_existing_img_xy()
    for i in range(5):
        mouse_click(inventory_abs_4_pot)
        API.AntiBan.sleep_between(2.6, 2.7)
    return True


def click_inventory_ovl():
    is_tab_open('inventory', True)
    if not does_img_exist(img_name='inventory_ovl_1', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
        print(f'No inventory overload 1 dose - checking for 2 dose')
        if not does_img_exist(img_name='inventory_ovl_2', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
            print(f'No inventory overload 2 dose - checking for 3 dose')
            if not does_img_exist(img_name='inventory_ovl_3', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
                print(f'No inventory overload 3 dose - checking for 4 dose')
                if not does_img_exist(img_name='inventory_ovl_4', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
                    print(f'No inventory overload 2 dose - checking for 3 dose')
                    return False
    API.AntiBan.sleep_between(8.0, 8.1)
    return True


def click_inventory_cake():
    is_tab_open('inventory', True)
    if is_hp_gt(50):
        print(f'Need to overload')
        return False
    elif is_hp_gt(10):
        print(f'Need to guzzle')
        guzzle_rock_cake()
    else:
        print(f'Need to click')
        check_rock_cake_xy_set()

        while needs_rock_cake():
            mouse_click(get_cached_rock_cake_xy())

    return True


def needs_abs():
    abs_region_check = 113, 250, 188, 290
    abs_color = (255, 129, 129)
    return does_color_exist_in_sub_image(abs_region_check, abs_color, 'is_absorption_active', color_tolerance=30, count_min=50)


def needs_ovl():
    return not does_img_exist(img_name='ovl_active_flag', script_name='NMZ', threshold=0.9)


def needs_rock_cake():
    if is_hp_gt(50):
        print(f'We actually need to overload - not rock cake.')
        return False
    if not does_img_exist(img_name='hp_2', script_name=SCRIPT_NAME):
        if does_img_exist(img_name='hp_3', script_name=SCRIPT_NAME):
            print(f'Hp = 2 - Use inventory rock cake.')
            return True
        else:
            print(f'Found neither 2 or 3 hp...? - Use cake in case ')
            return True

    return False


# -------
# HELPERS
# -------
def set_cached_rock_cake_xy(new_xy):
    global CACHED_INVENT_ROCK_CAKE_XY
    CACHED_INVENT_ROCK_CAKE_XY = new_xy
    return


def get_cached_rock_cake_xy():
    return CACHED_INVENT_ROCK_CAKE_XY


def guzzle_rock_cake():
    check_rock_cake_xy_set()

    mouse_long_click(get_cached_rock_cake_xy())
    select_guzzle_option()
    return True


def select_guzzle_option():
    if not does_img_exist(img_name='guzzle_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        does_img_exist(img_name='cancel_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)

        if get_cached_rock_cake_xy() is None:
            if not does_img_exist(img_name='inventory_rock_cake', script_name=SCRIPT_NAME, threshold=0.9):
                print(f'Failed to find inventory rock cake within select_guzzle_option...')
                return False
            set_cached_rock_cake_xy(get_existing_img_xy())

        mouse_long_click(get_cached_rock_cake_xy())

        if not does_img_exist(img_name='guzzle_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True,
                              click_middle=True):
            print(f'Failed to find guzzle option twice.')
            return False
    return True


def check_rock_cake_xy_set():
    if get_cached_rock_cake_xy() is None:
        if not does_img_exist(img_name='inventory_rock_cake', script_name=SCRIPT_NAME, threshold=0.9):
            print(f'Failed to find inventory rock cake...')
            return False
        set_cached_rock_cake_xy(get_existing_img_xy())
    return