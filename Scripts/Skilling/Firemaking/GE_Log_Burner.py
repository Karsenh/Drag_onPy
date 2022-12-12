import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open
from API.AntiBan import write_debug
from API.Mouse import mouse_click, mouse_move
from API.Interface.Bank import check_if_bank_tab_open
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist, get_existing_img_xy
from API.Imports.Coords import BANK_qty_all
from API.Imports.Coords import *
import pyautogui as pag


logs_to_use = "yew"


def burn_logs_at_ge(curr_loop):
    if curr_loop == 1:

        setup_interface("east", 3, "up")

        API.AntiBan.sleep_between(0.3, 1.3)

        is_tab_open("inventory", should_open=True)

        API.AntiBan.sleep_between(1.0, 1.5)

        click_to_open_bank()

        API.AntiBan.sleep_between(1.1, 1.8)

        # Check if on tab 3
        check_if_bank_tab_open(tab_num=3, should_open=True)

        # Check if withdraw qty all
        check_withdraw_qty_all()

        # Check if tinderbox withdrawn
        does_img_exist(img_name="banked_tinderbox", script_name="GE_Log_Burner", category="Scripts", threshold=0.98, should_click=True, y_offset=30, x_offset=20)

    else:
        # Just open bank
        write_debug(f'Not first loop')
        click_to_open_bank()


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

    burn_logs()
    # Burn logs
    #       - Click tinderbox @ inventory x
    #       - Click log to burn @ inventory slot [i]

    #   {LOOP 26 times}
    #       - Click tinderbox
    #       - Move mouse to next log to burn @ inventory slot [i+1]
    #       - Wait for log burned

    #       - Click log to burn @ inventory slot [i+1]

    return True


def check_withdraw_qty_all():
    qty_all_color = 119, 28, 26
    if not does_color_exist(qty_all_color, BANK_qty_all):
        mouse_click(BANK_qty_all)
    return


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
    while does_img_exist(img_name=f"inventory_{logs_to_use}_log", script_name="GE_Log_Burner", category="Scripts", threshold=0.85, should_click=False):
        i += 1
        write_debug(f'BURN LOGS - {i}/28')
        does_img_exist(img_name="inventory_tinderbox", script_name="GE_Log_Burner", category="Scripts", threshold=.95, should_click=True, y_offset=6, x_offset=6)
        API.AntiBan.sleep_between(0.3, 0.7)

        if i > 1:
            does_img_exist(img_name=f"inventory_{logs_to_use}_log", script_name="GE_Log_Burner", category="Scripts", threshold=0.85, should_click=False)
            next_log_xy = get_existing_img_xy()
            mouse_move(next_log_xy, max_x_dev=15, max_y_dev=15)

            if wait_for_img(img_name="log_burned", script_name="GE_Log_Burner", category_name="Scripts", max_wait_sec=6):
                pag.click(button="left")
            else:
                write_debug(f'Exp drop not seen!')
                pag.leftClick()
        else:
            does_img_exist(img_name=f"inventory_{logs_to_use}_log", script_name="GE_Log_Burner", category="Scripts", threshold=0.85, should_click=True, x_offset=15, y_offset=15)

    wait_for_img(img_name="log_burned", script_name="GE_Log_Burner", category_name="Scripts", max_wait_sec=6)
    return


def click_to_open_bank():
    bank_open_xy = 774, 481
    mouse_click(bank_open_xy, max_x_dev=0, max_y_dev=0)
    API.AntiBan.sleep_between(1.1, 1.5)
    return


def click_to_withdraw_logs():
    does_img_exist(img_name=f"banked_{logs_to_use}_log", script_name="GE_Log_Burner", threshold=0.96, should_click=True,
                   x_offset=22, y_offset=15)
    return
