import datetime
import random

import API.AntiBan
from API.Interface.General import setup_interface, toggle_public_chat, is_tab_open, get_xy_for_invent_slot
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Imports.Coords import INVENT_slot_1
from API.Mouse import mouse_click, mouse_drag, mouse_move, mouse_long_click
import pyautogui as pag

SCRIPT_NAME = 'Gilded_Altar_v2'
CACHED_ALTAR_XY = None
SEL_WORKLESS_ATTEMPTS = 0


def start_worshipping_bones(curr_loop):
    if curr_loop != 1:
        print(f'This is not the first loop')
        if not unnote_bones():
            return False

        if not move_to_house(curr_loop):
            return False

        if not worship_bones():
            return False

        if not move_back_to_phials():
            return False

    else:
        print(f'This is the first loop')
        setup_interface('north', 2, 'up')
        toggle_public_chat("off")
        is_tab_open('inventory', True)

    return True


# MAIN METHODS
def unnote_bones():
    if not sel_invent_dbones():
        return False

    if not use_bones_with_phials():
        return False

    if not sel_exchange_all():
        if not does_img_exist(img_name='too_full', script_name=SCRIPT_NAME, threshold=0.8):
            return False

    # if not wait_for_img(img_name='exchange_success', script_name=SCRIPT_NAME, threshold=0.8):
    #     print(f'Failed to find exchange successful - are we full already?')

    does_img_exist(img_name='tap_to_cont', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)

    return True


def move_to_house(curr_loop):
    global CACHED_ALTAR_XY

    # Long click house ad box from Phials
    if not long_click_house_box():
        return False

    # Select Visit Last every time except for the first loop
    if curr_loop != 2:
        if not sel_visit_last():
            return False
    # Select to view the list and then enter workless' house the first loop
    else:
        if not sel_view_list():
            return False
        if not sel_workless_ad():
            return False

    if not wait_for_img(img_name='gilded_altar', script_name=SCRIPT_NAME, threshold=0.9, max_wait_sec=10):
        return False

    x, y = get_existing_img_xy()
    CACHED_ALTAR_XY = x, y+18
    # Inside house here
    return True


def worship_bones():
    r_invent_xy = get_xy_for_invent_slot(slot_num=random.randint(3, 8))
    mouse_long_click(r_invent_xy)

    if not wait_for_img(img_name='use_dbone', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        print(f'Failed to find Use option on dbone long click')
        return False

    if not use_bones_with_altar():
        print(f'Failed to find altar to use bone on')
        return False

    API.AntiBan.sleep_between(3.0, 3.1)

    while is_worshipping():
        print('Saw Prayer Exp - Still Worshipping')

    return True


def move_back_to_phials():
    if not click_portal_to_leave():
        return False

    if not is_outside_portal():
        return False

    click_back_to_phials()
    return True


# HELPERS
def sel_invent_dbones():
    return does_img_exist(img_name='noted_inventory_dbones', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def use_bones_with_phials():
    num_phials_imgs = 6
    attempts = 0
    max_attempts = 6

    while attempts < max_attempts:
        for i in range(1, num_phials_imgs+1):
            if does_img_exist(img_name=f'phials_{i}', script_name=SCRIPT_NAME, threshold=0.80):
                x, y = get_existing_img_xy()
                phials_xy = x+3, y+6
                mouse_long_click(phials_xy)

                if not wait_for_img(img_name='use_bones_with_phials', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
                    if not wait_for_img(img_name='use_bones_with_phials_highlighted', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
                        if not wait_for_img(img_name='cancel', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
                            return False
                    else:
                        return True
                else:
                    return True
        attempts += 1

    print(f'Failed to find Phials to use noted bones with.')
    return False


def sel_exchange_all():
    return wait_for_img(img_name='exchange_all', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True, max_wait_sec=4)


def long_click_house_box():
    attempts = 0
    max_attempts = 10

    while attempts <= max_attempts:
        for i in range(1, 3):
            if does_img_exist(img_name=f'house_box_{i}', script_name=SCRIPT_NAME, threshold=0.7):
                x, y = get_existing_img_xy()
                loc_xy = x + 6, y + 6
                mouse_long_click(loc_xy)
                return True
        attempts += 1

    print(f'Failed to find house box images')
    return False


def sel_visit_last():
    if not wait_for_img(img_name='visit_last_house', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        if not wait_for_img(img_name='visit_last_house_2', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
            return False
    return True


def sel_view_list():
    return wait_for_img(img_name='view_house', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def sel_workless_ad():
    global SEL_WORKLESS_ATTEMPTS

    if not wait_for_img(img_name='workless_ad', script_name=SCRIPT_NAME, threshold=0.95, max_wait_sec=8):
        if SEL_WORKLESS_ATTEMPTS > 4:
            print(f'Exceeded attempts in finding Workless ad')
            return False
        scroll_xy = 640, 564
        mouse_move(scroll_xy)
        API.AntiBan.sleep_between(0.8, 1.1)
        pag.hscroll(-55)
        API.AntiBan.sleep_between(1.0, 1.1)
        SEL_WORKLESS_ATTEMPTS += 1
        sel_workless_ad()

    x, y = get_existing_img_xy()
    workless_arrow_xy = x+700, y+10
    mouse_click(workless_arrow_xy)
    return True


def use_bones_with_altar():
    global CACHED_ALTAR_XY

    if CACHED_ALTAR_XY:
        print(f'CACHED_ALTAR_XY Exists: {CACHED_ALTAR_XY}')
        mouse_click(CACHED_ALTAR_XY)
    else:
        print(f'CACHED_ALTAR_XY DOES NOT Exist - Setting to ')
        if not wait_for_img(img_name='gilded_altar', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True, max_wait_sec=10):
            print(f'Failed to find Gilded Altar image')
            return False

        CACHED_ALTAR_XY = get_existing_img_xy()
    return True


def is_worshipping():
    if not wait_for_img(img_name='Prayer', category='Exp_Drops', threshold=0.9, max_wait_sec=4):
        # Check if we gained a level
        if does_img_exist(img_name="level_up", category="General"):
            if not does_img_exist(img_name='inventory_dbone', script_name=SCRIPT_NAME, threshold=0.85):
                return False
            dbone_xy = get_existing_img_xy()
            mouse_long_click(dbone_xy)
            wait_for_img(img_name='use_dbone', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)
            return wait_for_img(img_name='gilded_altar_from_altar', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)

    return False


def click_portal_to_leave():
    return does_img_exist(img_name='portal_out', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)


def click_back_to_phials():
    phials_house_xy = 1326, 214
    mouse_click(phials_house_xy)

    API.AntiBan.sleep_between(5.0, 5.1)
    return


def is_outside_portal():
    return wait_for_img(img_name='is_outside_portal', script_name=SCRIPT_NAME, threshold=0.9, max_wait_sec=10)