import API.AntiBan
from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from GUI.Imports.Script_Launch import launch_script
from Scripts.Skilling.Farming.Tithe_Farmer import resupply_seeds
from Scripts.Skilling.Runecrafting.Cwars_Lavas import set_equipped_items, set_inventory_items, fill_pouches, \
    withdraw_ess, empty_pouches, teleport_to_duel_arena, craft_lavas, move_to_ruins, move_to_altar, cast_imbue, \
    teleport_to_cwars
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

    # show_main_gui()

    launch_script("Tithe_Farmer")

    # wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.9, should_click=True, y_offset=2)


    # wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.97, should_click=True,
    #              click_middle=True)
    # wait_for_img(img_name="Start_Tile", script_name="Tithe_Farmer", threshold=0.95, should_click=True)
    # resupply_seeds()

    # fill_empty_cans()

    # wait_for_img(img_name="Inventory_Rod", script_name="Cwars_Lavas", threshold=0.92, img_sel="inventory")

    return


__main__()







