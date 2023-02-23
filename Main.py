from GUI.Main_GUI import *
from sys import exit
from GUI.Auth_GUI import *
from API.Imaging.Image import *
from API.Setup import get_bluestacks_xy, set_bluestacks_window_size
# not_exit = True


def terminate_script(key):
    if str(key) == TERMINATION_KEY:
        print(f'⛔ Script Terminated by User - Main')
        set_should_cont(False)
        sys.exit(-99)


def __main__() -> int:
    listener = keyboard.Listener(
        on_press=lambda event: terminate_script(event))
    listener.start()

    get_bluestacks_xy()
    set_bluestacks_window_size()
    capture_bluestacks()

    # show_main_gui()
    if show_auth_gui():
        while should_be_running():
            show_main_gui()

    else:
        print(f'Failed to authenticate.')

    return 0


__main__()






