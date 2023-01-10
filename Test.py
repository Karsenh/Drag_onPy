from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from GUI.Imports.Script_Launch import launch_script
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

    launch_script("Cwars_Lavas")


    # does_img_exist(img_name="Inventory_Medium_Pouch_Degraded", script_name="Cwars_Lavas", threshold=0.90, should_click=True)

    # wait_for_img(img_name="Inventory_Rod", script_name="Cwars_Lavas", threshold=0.95, img_sel="first", should_click=True)


    # does_img_exist(img_name="Banked_Steam_Staff", script_name="Cwars_Lavas", threshold=0.995, should_click=True,
    #                click_middle=True)

    # does_img_exist(img_name="Banked_Tiara", script_name="Cwars_Lavas", should_click=True, click_middle=True,
    #                threshold=0.96)
    # does_img_exist(img_name="Minimap_Ruins", script_name="Cwars_Lavas", should_click=True, y_offset=4, threshold=0.95)

    # move_to_ruins()
    # move_to_altar()
    # cast_imbue()
    # craft_lavas()
    # empty_pouches()
    # craft_lavas()
    # teleport_to_cwars()



    # set_equipped_items()
    # set_inventory_items()
    # withdraw_ess()
    # fill_pouches()
    # teleport_to_duel_arena()
    # craft_lavas()



    return


__main__()


