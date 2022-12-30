import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled
from API.AntiBan import write_debug
from API.Mouse import mouse_click, mouse_move, mouse_long_click
from API.Interface.Bank import is_bank_tab_open, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist, get_existing_img_xy
from API.Imports.Coords import BANK_qty_all
from API.Imports.Coords import *
import pyautogui as pag


logs_to_use = "yew"


def burn_logs_at_ge(curr_loop):
    if curr_loop == 1:

        setup_interface("east", 3, "up")
        API.AntiBan.sleep_between(0.3, 1.3)

        is_otd_enabled(False)
        API.AntiBan.sleep_between(0.3, 1.3)

        is_tab_open("inventory", should_open=True)
        API.AntiBan.sleep_between(1.0, 1.5)

        if not click_to_open_bank():
            print(f'Something went wrong opening the bank')
            return False
        API.AntiBan.sleep_between(1.1, 1.8)

        # Check if on tab 3
        is_bank_tab_open(tab_num=3, should_open=True)

        # Check if withdraw qty all
        is_withdraw_qty("all")

        # Check if tinderbox withdrawn
        does_img_exist(img_name="banked_tinderbox", script_name="GE_Log_Burner", category="Scripts", threshold=0.98, should_click=True, y_offset=30, x_offset=20)

    else:
        # Just open bank
        write_debug(f'Not first loop')
        if not click_to_open_bank():
            print(f'Something went wrong opening the bank')
            return False


    # Withdraw logs
    click_to_withdraw_logs()

    # Click path & wait
    first_move_xy = 1341, 53
    odd_move_xy = 1349, 50
    even_move_xy = 1333, 49

    first_start_xy = 1342, 116
    odd_start_xy = 1342, 115
    even_start_xy = 1340, 122

    if curr_loop == 1:
        curr_move_xy = first_move_xy
        curr_start_xy = first_start_xy
    elif curr_loop % 2 == 0:
        curr_move_xy = even_move_xy
        curr_start_xy = even_start_xy
    else:
        curr_move_xy = odd_move_xy
        curr_start_xy = odd_start_xy

    move_away_from_bank(curr_move_xy)
    # Click start spot
    move_to_start(curr_start_xy)
    if not burn_logs():
        return False
    return True


def move_away_from_bank(move_xy):
    mouse_click(move_xy, max_x_dev=0, max_y_dev=0)
    API.AntiBan.sleep_between(8.4, 8.5)
    return


def move_to_start(move_xy):
    start_spot_xy = move_xy
    mouse_click(start_spot_xy, max_x_dev=0, max_y_dev=1)
    API.AntiBan.sleep_between(3.0, 3.6)
    return


def burn_logs():
    i = 0

    if not does_img_exist(img_name=f"inventory_{logs_to_use}_log", script_name="GE_Log_Burner", category="Scripts", threshold=0.85, should_click=False):
        return False

    while does_img_exist(img_name=f"inventory_{logs_to_use}_log", script_name="GE_Log_Burner", category="Scripts", threshold=0.85, should_click=False):
        i += 1

        write_debug(f'BURN LOGS - {i}/28')

        does_img_exist(img_name="inventory_tinderbox", script_name="GE_Log_Burner", category="Scripts", threshold=.95, should_click=True, y_offset=6, x_offset=6)
        API.AntiBan.sleep_between(0.1, 0.2)

        if i > 1:
            does_img_exist(img_name=f"inventory_{logs_to_use}_log", script_name="GE_Log_Burner", category="Scripts", threshold=0.85, should_click=False)
            next_log_xy = get_existing_img_xy()
            mouse_move(next_log_xy, max_x_dev=15, max_y_dev=15)

            if wait_for_img(img_name="log_burned", script_name="GE_Log_Burner", category="Scripts", max_wait_sec=3):
                pag.click(button="left")
            else:
                write_debug(f'Exp drop not seen! Clicking anyways because we saw a log here.')
                pag.leftClick()
        else:
            does_img_exist(img_name=f"inventory_{logs_to_use}_log", script_name="GE_Log_Burner", category="Scripts", threshold=0.85, should_click=True, x_offset=15, y_offset=15)

    # wait_for_img(img_name="log_burned", script_name="GE_Log_Burner", category="Scripts", max_wait_sec=6)
    return True


def click_to_open_bank():
    wait_for_img(img_name="bank_alt", script_name="GE_Log_Burner", threshold=0.95, y_offset=-6, should_click=True)

    if wait_for_img(img_name="bank_is_open", category="Banking"):
        return True
    elif wait_for_img(img_name="banker_dialogue", script_name="GE_Log_Burner", threshold=0.85):
        print(f"Couldn't find bank open - long clicking bank_alt")
        does_img_exist(img_name="bank_alt", script_name="GE_Log_Burner", threshold=0.95)
        long_click_xy = get_existing_img_xy()
        mouse_long_click(long_click_xy)
        wait_for_img(img_name="open_bank_selection", script_name="GE_Log_Burner", threshold=0.9, should_click=True)
        if wait_for_img(img_name="bank_is_open", category="Banking"):
            return True
        else:
            print(f'Tried to long press open bank but still couldnt seem to open bank - returning false...')
            return False

    print(f"Couldn't find bank anything to open bank - Exiting...")
    return False


def click_to_withdraw_logs():
    wait_for_img(img_name=f"banked_{logs_to_use}_log", script_name="GE_Log_Burner", threshold=0.95, should_click=True,
                   x_offset=22, y_offset=15)
    API.AntiBan.sleep_between(0.5, 0.6)
    return
