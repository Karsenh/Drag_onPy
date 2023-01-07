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

    launch_script("Red_Lizards")

    # CAUGHT - testing
    # wait_for_img(img_name="Reset_Trap_1_Caught_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)
    underneath_xy = 743, 462


    # ✅ 1 from 1
    # (✔✔CAUGHT)
    # wait_for_img(img_name="Trap_1_Caught_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_1_Caught_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔DOWN)
    # wait_for_img(img_name="Trap_1_Down_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_1_Down", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # ✅ 1 from 2
    # (✔✔✔CAUGHT)
    # wait_for_img(img_name="Trap_1_Caught_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_1_Caught_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔DOWN)
    # wait_for_img(img_name="Trap_1_Down_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_1_Down", script_name="Red_Lizards", threshold=0.8, should_click=True)

    # ✅ 1 from 3
    # (✔✔✔CAUGHT)
    # wait_for_img(img_name="Trap_1_Caught_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_1_Caught_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔DOWN)
    # wait_for_img(img_name="Trap_1_Down_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_1_Down", script_name="Red_Lizards", threshold=0.85, should_click=True)

    # -----2-----

    # ✅ 2 from 1
    # (✔✔CAUGHT)
    # wait_for_img(img_name="Trap_2_Caught_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_2_Caught_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔DOWN)
    # wait_for_img(img_name="Trap_2_Down_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(2.0, 2.1)
    # wait_for_img(img_name="Reset_Trap_2_Down", script_name="Red_Lizards", threshold=0.85, should_click=True)

    # ✅ 2 from 2
    # (✔✔CAUGHT)
    # wait_for_img(img_name="Trap_2_Caught_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_2_Caught_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔DOWN)
    # wait_for_img(img_name="Trap_2_Down_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_2_Down", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # ✅ 2 from 3
    # (✔✔✔CAUGHT)
    # wait_for_img(img_name="Trap_2_Caught_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_2_Caught_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔DOWN)
    # wait_for_img(img_name="Trap_2_Down_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_2_Down", script_name="Red_Lizards", threshold=0.85, should_click=True)

    # -----3-----

    # ✅ 3 from 1
    # (✔✔CAUGHT)
    # wait_for_img(img_name="Trap_3_Caught_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_3_Caught_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔✔DOWN)
    # wait_for_img(img_name="Trap_3_Down_From_1", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(2.0, 2.1)
    # mouse_click(underneath_xy)
    # wait_for_img(img_name="Reset_Trap_3_Down", script_name="Red_Lizards", threshold=0.85, should_click=True)

    # ✅ 3 from 2
    # (✔✔CAUGHT)
    # wait_for_img(img_name="Trap_3_Caught_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_3_Caught_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔✔DOWN)
    # wait_for_img(img_name="Trap_3_Down_From_2", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(2.0, 2.1)
    # mouse_click(underneath_xy)
    # wait_for_img(img_name="Reset_Trap_3_Down", script_name="Red_Lizards", threshold=0.85, should_click=True)

    # ✅ 3 from 3
    # (✔✔✔CAUGHT)
    # wait_for_img(img_name="Trap_3_Caught_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_3_Caught_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)

    # (✔✔✔DOWN)
    # wait_for_img(img_name="Trap_3_Down_From_3", script_name="Red_Lizards", threshold=0.95, should_click=True)
    # sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Reset_Trap_3_Down", script_name="Red_Lizards", threshold=0.95, should_click=True)

    return


__main__()


