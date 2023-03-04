import pyautogui

import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_run_on, is_run_gt, is_hp_gt, is_otd_enabled, relog
from API.Imaging.Image import wait_for_img, does_img_exist, does_color_exist_in_sub_image, get_existing_img_xy
from API.Mouse import mouse_click, mouse_long_click
from API.Debug import write_debug

SCRIPT_NAME = 'NMZ'

SKILL_TO_TRAIN = 'str'
USE_DHAROKS = True
CACHED_INVENT_ROCK_CAKE_XY = None
IS_OUTSIDE = False

ABS_QTY = '80'
OVL_QTY = '28'


def set_is_outside(new_val):
    global IS_OUTSIDE
    IS_OUTSIDE = new_val
    print(f'set_is_outside({new_val}) fired')
    return IS_OUTSIDE


def get_is_outside():
    print(f'get_is_outside fired: {IS_OUTSIDE}')
    return IS_OUTSIDE


def start_training_nmz(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')

        if needs_abs():
            print(f'🧪 NEED ABSORPTION POTION')
            if not click_inventory_abs():
                print(f'Out of Absorptions - Checking if we are outside yet...')
                if is_outside_dream():
                    set_is_outside(True)

        if needs_ovl() and not get_is_outside():
            print(f'💪🏼 NEED TO OVERLOAD')
            if not click_inventory_ovl():
                print(f'Out of Overloads - Checking if we are outside yet...')
                if is_outside_dream():
                    set_is_outside(True)

        while needs_rock_cake() and not get_is_outside():
            print(f'🎂 NEED ROCK CAKE - CLICKING INVENTORY CAKE')
            if not click_inventory_cake():
                print(f'FAILED TO FIND INVENTORY ROCK')

        if get_is_outside():
            if is_outside_dream():
                relog()
                setup_interface('north', 3, 'up')
                if not restart_dream():
                    return False
                else:
                    set_is_outside(False)

    else:
        print(f'First loop')
        setup_interface('north', 3, 'up')
        if is_outside_dream():
            if not restart_dream():
                return False

    return True


# -------
# METHODS
# -------
def click_inventory_abs():
    set_is_outside(get_is_outside())

    if not get_is_outside():
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
            API.AntiBan.sleep_between(1.6, 1.7)
    return True


def click_inventory_ovl():
    is_tab_open('inventory', True)
    # Check if we can even click the overload
    if not is_hp_gt(50):
        print(f"🔴 Can't use overload right now - health not above 50%")
        return False

    set_is_outside(get_is_outside())

    if not get_is_outside():
        if not does_img_exist(img_name='inventory_ovl_1', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
            print(f'No inventory overload 1 dose - checking for 2 dose')
            if not does_img_exist(img_name='inventory_ovl_2', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
                print(f'No inventory overload 2 dose - checking for 3 dose')
                if not does_img_exist(img_name='inventory_ovl_3', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
                    print(f'No inventory overload 3 dose - checking for 4 dose')
                    if not does_img_exist(img_name='inventory_ovl_4', script_name=SCRIPT_NAME, threshold=0.98, should_click=True, click_middle=True):
                        print(f'No inventory overload 2 dose - checking for 3 dose')
                        return False
        if needs_abs():
            click_inventory_abs()
            API.AntiBan.sleep_between(2.1, 2.2)
        else:
            API.AntiBan.sleep_between(8.0, 8.1)
    return True


def click_inventory_cake():
    is_tab_open('inventory', True)
    check_rock_cake_xy_set()

    if is_hp_gt(50):
        print(f'Need to overload')
        return False

    elif is_hp_gt(10) and not needs_ovl():
        print(f'Need to guzzle')
        while is_hp_gt(10):
            guzzle_rock_cake()

    print(f'Move to clicking instead of guzzling...')
    set_is_outside(is_outside_dream())

    while needs_rock_cake() and not needs_ovl() and not get_is_outside():
        mouse_click(get_cached_rock_cake_xy())

    return True


def restart_dream():
    # TODO - Check if money in coffer with Onion man dialogue (kind of already does if we dont purchase new dream)

    # 1. Drop remaining absorptions and ovls from inventory
    drop_all_inventory_pots()

    # 2. Purchase another dream from Onion man
    if not purchase_new_dream():
        return False

    # 3. Purchase 88 doses of Absorption & 20 doses of Overload from the chest
    if not restock_doses_from_chest():
        return False

    # 4. Take 20 doses of Overload from the barrel
    withdraw_ovls()

    # 5. Take 88 doses of Absorption from the barrel
    withdraw_abs()

    # 6. Click to enter dream
    if not enter_dream():
        return False

    # 7. Confirm we're in dream and return True if so - else return False
    return True


# -------
# HELPERS
# -------
def is_in_dream():
    return wait_for_img(img_name='inside_dream_flag', script_name=SCRIPT_NAME, threshold=0.9, max_wait_sec=8)


def enter_dream():
    # FROM Absorption potion
    if not does_img_exist(img_name='dream_vial_from_abs', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Failed to find dream_vial_from_abs')
        dream_vial_xy = 1034, 439
    else:
        dream_vial_xy = get_existing_img_xy()

    mouse_long_click(dream_vial_xy)
    if not does_img_exist(img_name='drink_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        print(f'Failed to find drink option on vial from absorptions...')
        if not does_img_exist(img_name='cancel_option', script_name=SCRIPT_NAME, threshold=0.9):
            print(f'Failed to find cancel option on vial long click')
            return False
        if not does_img_exist(img_name='drink_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True,
                              click_middle=True):
            print(f'Failed to find drink option for a second time - exiting...')
            return False

    if not wait_for_img(img_name='click_accept_to_enter', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        print(f'Failed to find Accept button to enter dream')
        return False

    return True


def withdraw_abs():
    # FROM Rewards Chest

    if not does_img_exist(img_name='absorption_barrel_from_overload_barrel', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Failed to find absorption barrel from overload barrel... Hard-coding XY coords')
        absorption_barrel_xy = 664, 356
    else:
        print(f'Found absorption_barrel_from_overload_barrel')
        absorption_barrel_xy = get_existing_img_xy()

    mouse_long_click(absorption_barrel_xy)

    if not sel_take_option():
        print(f'Failed to sel_take_option (abs)...')
        return False

    for num_char in ABS_QTY:
        pyautogui.press(num_char)

    pyautogui.press('enter')

    if not wait_for_img(img_name='inventory_abs_4', script_name=SCRIPT_NAME, threshold=0.9, img_sel='inventory'):
        print(f'Failed to find absorptions in inventory after supposedly withdrawing {ABS_QTY} doses...')
        return False

    print(f'✔ Successfully withdrew {ABS_QTY} doses of absorption potion')
    return


def withdraw_ovls():
    # FROM Rewards Chest

    if not does_img_exist(img_name='overload_barrel_from_rewards_chest', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Failed to find overload barrel from rewards chest... Hard-coding XY coords')
        overload_barrel_xy = 93, 590
    else:
        print(f'Found overload_barrel_from_rewards_chest')
        overload_barrel_xy = get_existing_img_xy()

    mouse_long_click(overload_barrel_xy)

    if not sel_take_option():
        print(f'Failed to sel_take_option...')
        return False

    for num_char in OVL_QTY:
        pyautogui.press(num_char)

    pyautogui.press('enter')

    if not wait_for_img(img_name='inventory_ovl_4', script_name=SCRIPT_NAME, threshold=0.9, img_sel='inventory'):
        print(f'Failed to find overloads in inventory after supposedly withdrawing {OVL_QTY} doses...')
        return False

    print(f'✔ Successfully withdrew {OVL_QTY} doses of overload potion')
    return True


def restock_doses_from_chest():
    if wait_for_img(img_name='rewards_chest', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        print(f'Found rewards chest...')

    else:
        print(f'Failed to find rewards chest to restock potion doses...')
        chest_xy = 820, 167
        mouse_click(chest_xy)

    if not is_reward_chest_open():
        print(f'Failed to see rewards chest open (benefits btn)')
        return False

    if not is_on_benefits_page():
        print(f'Failed to find potions on benefits page')
        return False

    purchase_abs_doses()

    purchase_ovl_doses()

    return True


def purchase_new_dream():
    if does_img_exist(img_name='dom_onion', script_name=SCRIPT_NAME, threshold=0.85):
        print(f'Found Dom!')
        dom_xy = get_existing_img_xy()
        mouse_long_click(dom_xy)
    else:
        print(f'Failed to find Dominic Onion... using raw XY coords')
        dom_xy = 751, 374
        mouse_long_click(dom_xy)

    if not sel_dream_option():
        print(f'Failed to find Dream option...')

    if not sel_previous_dream_option():
        print(f'Failed to find previous dream option in chat dialogue...')

    if not sel_tap_to_cont():
        print(f'Failed to tap to continue (1)')

    if not sel_yes_option():
        print(f'Failed to find Yes option in chat dialogue...')

    if not sel_tap_to_cont():
        print(f'Failed to tap to continue (2)')

    return True


def drop_all_inventory_pots():
    is_tab_open('inventory', True)
    is_otd_enabled(True)

    dose_arr = [1, 2, 3, 4]

    for dose in dose_arr:
        # Overload
        drop_pots_from_invent('ovl', dose)
        # Absorption
        drop_pots_from_invent('abs', dose)

    # TODO: Double check there are no pots in inventory here before returning

    is_otd_enabled(False)
    return


def drop_pots_from_invent(pot_type, dose_num):
    while does_img_exist(img_name=f'inventory_{pot_type}_{dose_num}', script_name=SCRIPT_NAME, threshold=0.96, should_click=True, click_middle=True):
        print(f'Dropping overload 1 dose')
    return


def needs_abs():
    # If the absorption potion icon isn't found at all - we don't have it active
    if not does_img_exist(img_name='abs_active_flag_alt', script_name=SCRIPT_NAME, threshold=0.98):
        print(f'Absorption potion flag not found - Need abs')
        return True

    # Check if it's active but low
    abs_region_check = 113, 250, 188, 290
    abs_color = (255, 129, 129)

    return does_color_exist_in_sub_image(abs_region_check, abs_color, 'is_absorption_active', color_tolerance=40, count_min=20)


def needs_ovl():
    return not does_img_exist(img_name='ovl_active_flag', script_name='NMZ', threshold=0.9)


def needs_rock_cake():
    if is_hp_gt(50):
        print(f'We actually need to overload - not rock cake.')
        return False
    if not does_img_exist(img_name='hp_2', script_name=SCRIPT_NAME):
        if does_img_exist(img_name='hp_3', script_name=SCRIPT_NAME):
            print(f'Hp = 2 or 3 - Use inventory rock cake.')
            return True
        else:
            print(f'Found neither 2 or 3 hp...? - Use cake in case ')
            return True

    return False


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


def is_outside_dream():
    return does_img_exist(img_name='outside_flag', script_name=SCRIPT_NAME, threshold=0.85)


def sel_dream_option():
    return does_img_exist(img_name='dream_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def sel_previous_dream_option():
    return wait_for_img(img_name='previous_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def sel_tap_to_cont():
    return wait_for_img(img_name='tap_to_continue_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def sel_yes_option():
    return wait_for_img(img_name='yes_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def is_reward_chest_open():
    return wait_for_img(img_name='rewards_benefits_btn', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def is_on_benefits_page():
    return does_img_exist(img_name='absorption_benefit', script_name=SCRIPT_NAME, threshold=0.9)


def purchase_abs_doses():
    if not does_img_exist(img_name='absorption_benefit', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Failed to find absorption which is weird because we made it this far and this is a flag...')
        return False

    x, y = get_existing_img_xy()
    abs_benefit_xy = x+10, y+10
    mouse_long_click(abs_benefit_xy)

    sel_buy_x(ABS_QTY)
    return


def purchase_ovl_doses():
    if not does_img_exist(img_name='overload_benefit', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Failed to find overload which is weird because we made it this far and found absorption...')
        return False

    x, y = get_existing_img_xy()
    ovl_benefit = x+10, y+10
    mouse_long_click(ovl_benefit)

    sel_buy_x(OVL_QTY)
    return


def sel_buy_x(qty):
    does_img_exist(img_name='buy_x_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)
    if not wait_for_img(img_name='enter_amount_dialogue', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Failed to see Enter Amount Dialogue - did we click Buy_X_Option correctly?')
        return False

    for num_char in qty:
        pyautogui.press(num_char)

    pyautogui.press('enter')

    return True


def sel_take_option():
    # Select 'take' from potion barrels
    does_img_exist(img_name='take_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)

    if not wait_for_img(img_name='is_in_take_qty_dialogue', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Failed to find TAKE qty dialogue from potion barrels...')
        if not wait_for_img(img_name='cancel_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
            print(f'Failed to find cancel')
            return False

    return True
