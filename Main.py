import threading
import msvcrt
import sys
import os
import signal

from Database.Connection import check_client_version
from GUI.Imports.GUI_Update_Client import show_update_client_gui
from GUI.Main_GUI import *
from sys import exit
from GUI.Auth_GUI import *
from API.Imaging.Image import *
from API.Setup import get_bluestacks_xy, set_bluestacks_window_size
from pynput import keyboard
# not_exit = True
import keyboard
import os
import signal
import threading


def set_should_cont(value):
    global SHOULD_CONTINUE
    SHOULD_CONTINUE = value
    return


def __main__() -> int:


    try:
        get_bluestacks_xy()
        set_bluestacks_window_size()
        capture_bluestacks()

        if not check_client_version():
            print(f'Exiting Script_Launch...')
            show_update_client_gui()
            return False

        # show_main_gui()
        if show_auth_gui():
            while should_be_running():
                show_main_gui()
                pass

        else:
            print(f'Failed to authenticate.')
    except Exception as e:
        print(f'Exception thrown in Main: {e}')

    return 0


__main__()





