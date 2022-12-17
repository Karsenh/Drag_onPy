import random
import API.AntiBan
from API.Imaging.Image import wait_for_img
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist
from API.Interface.General import get_xy_for_invent_slot, setup_interface, is_otd_enabled, is_tab_open
from API.Debug import write_debug, log_to_debug


def start_fletching_darts(curr_loop):

    if not curr_loop == 1:
        first_slot_xy = get_xy_for_invent_slot(1)
        second_slot_xy = get_xy_for_invent_slot(2)

        mouse_click(first_slot_xy)
        mouse_click(second_slot_xy)

        if not wait_for_img(img_name="Fletching_exp", script_name="GE_Dart_Fletcher", max_wait_sec=5, threshold=0.8):
            return False

        for i in range(1, random.randint(13, 27)):
            mouse_click(first_slot_xy)
            mouse_click(second_slot_xy)
    else:
        setup_interface("north", 4, "down")
        API.AntiBan.sleep_between(0.6, 0.9)
        is_otd_enabled(False)
        API.AntiBan.sleep_between(0.6, 0.9)
        is_tab_open("inventory", should_open=True)

    return True
