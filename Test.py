from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from GUI.Imports.Script_Launch import launch_script
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

    launch_script("Cwars_Teak")


    # Spec available color = (30, 144, 172) @ 1242, 273
    # NO spec color = (18, 18, 18)



    # does_img_exist(img_name="Drop_Lizard", script_name="Desert_Lizards", threshold=0.9, should_click=True)
    # setup_interface("west", 3, "up")



    return


__main__()


