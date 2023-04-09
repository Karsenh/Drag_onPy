import random
import pyautogui as pag
import API.Imaging.Image
from API.Imaging.Image import does_color_exist
from API.Imports.Coords import *
from API.Mouse import mouse_click, mouse_move, mouse_long_click
from API.Imaging.Image import does_img_exist
from API.AntiBan import print_to_log, sleep_between
from API.Debug import write_debug
import keyboard

HAS_WITHDRAWN_14 = False


def withdraw_item_from_tab_num(item, qty, tab_num, threshold=0.8):
    global HAS_WITHDRAWN_14
    write_debug(f'Withdrawing {item} from tab_num: {tab_num}')
    scroll_xy = 622, 580

    if not is_bank_open():
        write_debug(f'Bank is not open - returning')
        return False

    is_bank_tab_open(tab_num)

    is_withdraw_qty(qty)

    if qty != 'x' or HAS_WITHDRAWN_14:
        if not does_img_exist(img_name=item, category='Banking\Bank_Items', threshold=threshold, should_click=True, click_middle=True):
            # Scroll and try again before returning false
            write_debug(f'Failed to find bank item: {item} in tab_num: {tab_num}- Scrolling and trying again')
            mouse_move(scroll_xy)
            pag.hscroll(150)
            if not does_img_exist(img_name=item, category='Banking\Bank_Items', threshold=threshold, should_click=True, click_middle=True):
                write_debug(f'Failed to find item: {item} in tab_num: {tab_num} for a second time after scrolling - returning...')
                return False
    else:
        if not does_img_exist(img_name=item, category='Banking\Bank_Items', threshold=threshold):
            write_debug(f'Failed to find bank item: {item} in tab_num: {tab_num}- Scrolling and trying again')
            mouse_move(scroll_xy)
            pag.hscroll(150)
            if not does_img_exist(img_name=item, category='Banking\Bank_Items', threshold=threshold):
                write_debug(f'Failed to find item: {item} in tab_num: {tab_num} for a second time after scrolling - returning...')
                return False

        bank_item_xy = API.Imaging.Image.get_existing_img_xy()
        mouse_long_click(bank_item_xy)
        does_img_exist(img_name="withdraw_x", category="Banking", should_click=True, threshold=0.9, click_middle=True)
        API.AntiBan.sleep_between(1.0, 1.1)

        pag.press('1')
        API.AntiBan.sleep_between(0.4, 0.7)
        pag.press('4')
        API.AntiBan.sleep_between(0.8, 1.1)

        pag.press('enter')

        API.AntiBan.sleep_between(1.7, 1.8)

        HAS_WITHDRAWN_14 = True

    return True


def open_ge_bank():
    # Opens GE bank from diagonal tile (SE) while facing EAST zoomed all the way in
    # if not does_img_exist(img_name="GE_SE_6_Zoom_Bank", category="Banking", threshold=0.98):
    #     write_debug(f'Failed to find GE bank (facing East with 5x zoom?)')
    #     return False
    ge_bank_xy = 798, 583
    # ge_bank_xy = API.Imaging.Image.get_existing_img_xy()
    API.Mouse.mouse_long_click(ge_bank_xy)
    if not does_img_exist(img_name='bank_grand', category='Banking', threshold=0.9, should_click=True, click_middle=True):
        write_debug('❌ Failed to find bank grand exchange long-click option after long clicking')
        if not does_img_exist(img_name='cancel', category='General', threshold=0.9, should_click=True, click_middle=True):
            write_debug('⛔ Failed to find cancel option as well - exiting...')
            return False
        if not does_img_exist(img_name='bank_grand', category='Banking', threshold=0.85, should_click=True, click_middle=True):
            write_debug('⛔ Failed to find the bank grand exchange long-click option for a second time - exiting...')
            return False

    write_debug('✔ Clicked Bank Grand Exchange long-click option - checking if bank is open...')
    bank_open = is_bank_open()
    if not bank_open:
        write_debug(f'Something went wrong while opening the GE bank')
    return bank_open


def deposit_all(include_equipment=False):
    # If the bank is not open
    mouse_click(BANK_dep_inventory)
    sleep_between(0.5, 0.7)
    if include_equipment:
        mouse_click(BANK_dep_equipment)
    return


def is_bank_tab_open(tab_num=0, should_open=True, double_check=True):
    # If the bank tab IS open...
    if does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
        # return true
        return True
    # Else, the bank tab is NOT open...
    else:
        # If it's not open, but we SHOULD open it...
        if should_open:
            # Click that tab xy to open
            mouse_click(BANK_all_tab_xys[tab_num])
            # Check for tab again after clicking (if double check is true)
            if double_check:
                if not does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
                    print(f"Couldn't find expected tab no. {tab_num} despite having tried to click... Exiting")
                    # Print this issue to log file
                    log_text = f"Couldn't find Bank Tab {tab_num} after trying to click it."
                    print_to_log(log_text)
                    exit(-1)
            # Else - It's now open
            return True
        # Still closed because should_open is false
        return False


def close_bank():
    close_method = random.randint(1, 10)

    if close_method > 8:
        bank_close_xy = 1009, 319
        mouse_click(bank_close_xy, max_x_dev=4, max_y_dev=5)
    else:
        keyboard.send('esc')

    sleep_between(0.9, 1.1)
    return


def is_withdraw_qty(qty="all", should_click=True):
    all_sel_color = 122, 29, 27
    all_sel_xy = 768, 813

    x_sel_color = 138, 33, 30
    x_sel_xy = 720, 816

    ten_sel_color = 123, 29, 27
    ten_sel_xy = 655, 815

    five_sel_color = 141, 33, 30
    five_sel_xy = 636, 817

    one_sel_color = 138, 33, 30
    one_sel_xy = 594, 816

    match qty:
        case "all":
            color_to_check = all_sel_color
            coords_to_check = all_sel_xy
        case "x":
            color_to_check = x_sel_color
            coords_to_check = x_sel_xy
        case "10":
            color_to_check = ten_sel_color
            coords_to_check = ten_sel_xy
        case "5":
            color_to_check = five_sel_color
            coords_to_check = five_sel_xy
        case "1":
            color_to_check = one_sel_color
            coords_to_check = one_sel_xy

    is_selected = does_color_exist(check_color=color_to_check, xy=coords_to_check)

    if not is_selected and should_click:
        mouse_click(coords_to_check)
        sleep_between(0.3, 0.4)

    return is_selected


def is_bank_open(max_wait_sec=8):
    return API.Imaging.Image.wait_for_img(img_name="bank_is_open", category="Banking", max_wait_sec=max_wait_sec)

