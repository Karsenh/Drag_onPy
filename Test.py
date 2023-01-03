from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
import sys


def on_press(key):
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
    launch_script("GE_Superheat_Gold")

    return


__main__()


