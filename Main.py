import threading
import msvcrt
import sys
from GUI.Main_GUI import *
from sys import exit
from GUI.Auth_GUI import *
from API.Imaging.Image import *
from API.Setup import get_bluestacks_xy, set_bluestacks_window_size
from pynput import keyboard
# not_exit = True


def set_should_cont(value):
    global SHOULD_CONTINUE
    SHOULD_CONTINUE = value
    return


def terminate_script(key):
    if str(key) == TERMINATION_KEY:
        print(f'⛔ Script Terminated by User - Main')
        set_should_cont(False)
        sys.exit(-99)


def on_press(key):
    if key == keyboard.Key.end:
        # Send signal to main thread to terminate
        threading.main_thread().stop()
        return False


listener_thread = keyboard.Listener(on_press=on_press)
listener_thread.start()
# def input_thread():
#     while True:
#         if msvcrt.kbhit():
#             # Read one character of keyboard input
#             key = msvcrt.getch()
#
#             # Check if 'End' key was pressed
#             if key == b'\x1b':  # b'\x1b' is the 'End' key
#                 # Send signal to main thread to terminate
#                 threading.main_thread().stop()
#                 break
#
#
# # Start the input thread
# input_thread = threading.Thread(target=input_thread)


def __main__() -> int:

    try:
        get_bluestacks_xy()
        set_bluestacks_window_size()
        capture_bluestacks()

        # show_main_gui()
        if show_auth_gui():
            while should_be_running():
                show_main_gui()

        else:
            print(f'Failed to authenticate.')
    except:
        print(f'Exception thrown in Main')

    return 0


__main__()






