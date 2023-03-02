import pyautogui

import API.AntiBan
from GUI.Main_GUI import show_main_gui
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from GUI.Imports.Script_Launch import launch_script
from GUI.Imports.Skill_Level_Input.Skill_Level_Input import get_skill_level, update_skill_level
from API.Interface.Bank import is_bank_tab_open
from Scripts.Skilling.Combat.NMZ import drop_pots_from_invent, purchase_new_dream, restock_doses_from_chest, \
    withdraw_ovls, withdraw_abs
from Scripts.Skilling.Mining.Motherlode_Miner import claim_ore

import sys
from pynput import keyboard


def terminate_app(key):
    try:
        print(f'Key {key} pressed')

        if str(key) == "Key.end":
            write_debug("☠ Script Terminated by User")
            sys.exit(-1)
    except AttributeError:
        print(f'special key {key} pressed')


def __main__():

    listener = keyboard.Listener(
        on_press=terminate_app)
    listener.start()

    get_bluestacks_xy()
    set_bluestacks_window_size()
    capture_bluestacks()
    clear_debug_log()

    # launch_script("NMZ")

    # is_tab_open('logout', True)
    # does_img_exist(img_name='logout_thumbs_up', category='interface', threshold=0.9, should_click=True,
    #                click_middle=True)
    #
    # does_img_exist(img_name='tap_to_logout', category='interface', threshold=0.9, should_click=True, click_middle=True)

    relog()

    qty = '88'

    # restock_doses_from_chest()

    # withdraw_ovls()

    # withdraw_abs()


    # purchase_new_dream()


    # does_img_exist(img_name='inventory_ovl_1', script_name='NMZ', threshold=0.94, should_click=True,
    #                click_middle=True)

    # color_check = 142, 261
    # get_color_at_coords(color_check)



    # does_img_exist(img_name='ovl_active_flag', script_name='NMZ', threshold=0.92)

    return


__main__()







