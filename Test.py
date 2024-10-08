import sys
import API.AntiBan
from API.Actions.Teleporting import teleport_with_crafting_cape, teleport_with_spellbook
from Database.Connection import check_client_version
from GUI.Main_GUI import show_main_gui
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from GUI.Imports.Script_Launch import launch_script
from GUI.Imports.Skill_Level_Input.Skill_Level_Input import get_skill_level, update_skill_level
from API.Interface.Bank import is_bank_tab_open, open_ge_bank, withdraw_item_from_tab_num
from Scripts.Skilling.Combat.NMZ import drop_pots_from_invent, purchase_new_dream, restock_doses_from_chest, \
    withdraw_ovls, withdraw_abs
from Scripts.Skilling.Mining.Motherlode_Miner import claim_ore
from pynput import keyboard

from Scripts.Skilling.Runecrafting.Cwars_Lavas_v2 import empty_small_pouch, empty_medium_pouch, empty_large_pouch, \
    empty_giant_pouch
from Scripts.Skilling.Runecrafting.Moonclan_Astrals import start_crafting_astrals


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

    launch_script("Cwars_Lavas")

    # SCRIPT_NAME = 'Moonclan_Astrals'
    # wait_for_img(img_name='move_2', script_name=SCRIPT_NAME, should_click=True, click_middle=True, max_wait_sec=15,
    #              threshold=0.95)



    # empty_small_pouch()
    # empty_medium_pouch()
    # empty_large_pouch()
    # empty_giant_pouch()

    # does_img_exist(img_name='move_2', script_name='Moonclan_Astrals', threshold=0.96, should_click=True, click_middle=True)
    # does_img_exist(img_name='last_drop_of_water', script_name='Desert_Granite_Miner', threshold=0.85)

    # r1_xy = 764, 511
    # r2_xy = 832, 479
    # r3_xy = 756, 388
    # r1_col = [66, 41, 31]
    # r2_col = [60, 38, 30]
    # r2_col = [66, 41, 31]
    # print(f'color: ${get_color_at_coords(r1_xy)}')


    # does_img_exist(img_name='available_patch', script_name='Tithe_Farmer', threshold=0.85)
    # launch_script("Gnome_Course")

    # check_client_version()
    # does_img_exist(img_name='jump_4', script_name='Ardy_Rooftops', threshold=0.9, should_click=True, click_middle=True)


    # does_img_exist(img_name='tile_1_flag', script_name='Ardy_Knights', threshold=0.9)
    # is_tab_open('logout', True)
    # does_img_exist(img_name='logout_thumbs_up', category='interface', threshold=0.9, should_click=True,
    #                click_middle=True)
    #
    # does_img_exist(img_name='tap_to_logout', category='interface', threshold=0.9, should_click=True, click_middle=True)

    # relog()

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







