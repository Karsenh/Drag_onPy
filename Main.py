from GUI.Main_GUI import *
from GUI.Auth_GUI import *
from API.Imaging.Image import *
from API.Setup import get_bluestacks_xy, set_bluestacks_window_size
# not_exit = True


def __main__() -> int:
    # while not_exit:
    get_bluestacks_xy()
    set_bluestacks_window_size()
    capture_bluestacks()

    show_main_gui()
    # show_auth_gui()

    return 0


__main__()


def exit_dragonpy():
    print(f'User exited application.')
    exit(-1)
    return






