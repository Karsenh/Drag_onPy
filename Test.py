import API.AntiBan
from GUI.Main_GUI import show_main_gui
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from GUI.Imports.Script_Launch import launch_script
from GUI.Imports.Skill_Level_Input.Skill_Level_Input import get_skill_level, update_skill_level

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

    launch_script("Black_Lizards")




    # capture_img_region(90, 475, 280, 543, "test")
    #
    # yellow_coords = 761, 376
    # get_color_at_coords(yellow_coords)
    # mouse_move(yellow_coords)

    # test_region = 377, 362, 443, 420
    # yellow_color = 160, 132, 8
    # green_color = 29, 163, 51
    # if does_color_exist_in_sub_image(test_region, yellow_color, 'Trap_Color'):
    #     print(f'Found 🟡')
    # else:
    #     print(f'No Yellow Found')
    # if does_color_exist_in_sub_image(test_region, green_color, 'Trap_Color'):
    #     print(f'Found 🟢')
    # else:
    #     print(f'No Green Found')

    # wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.9, should_click=True, y_offset=2)


    # wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.97, should_click=True,
    #              click_middle=True)
    # wait_for_img(img_name="Start_Tile", script_name="Tithe_Farmer", threshold=0.95, should_click=True)
    # resupply_seeds()

    # fill_empty_cans()

    # wait_for_img(img_name="Inventory_Rod", script_name="Cwars_Lavas", threshold=0.92, img_sel="inventory")

    return


__main__()







