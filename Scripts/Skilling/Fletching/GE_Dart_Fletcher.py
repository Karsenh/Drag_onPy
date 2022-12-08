import random
import API.AntiBan
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist
from API.Interface.General import get_xy_for_invent_slot
from API.Debug import write_debug, log_to_debug


def start_fletching_darts(curr_loop):

    first_slot_xy = get_xy_for_invent_slot(1)
    second_slot_xy = get_xy_for_invent_slot(2)

    if not does_img_exist(img_name="feathers", script_name="GE_Dart_Fletcher", threshold=0.95) \
            or (not does_img_exist(img_name="bronze_dart_tip", script_name="GE_Dart_Fletcher", threshold=0.95) and not does_img_exist(img_name="steel_dart_tip", script_name="GE_Dart_Fletcher", threshold=0.90)):
        msg = "Missing either feathers or dart tips - Exiting..."
        write_debug(msg)
        log_to_debug(msg)
        return False

    for i in range(1, random.randint(13, 27)):
        mouse_click(first_slot_xy)
        mouse_click(second_slot_xy)
        # does_img_exist(img_name="feathers", script_name="GE_Dart_Fletcher", threshold=0.95, should_click=True)
        # does_img_exist(img_name="bronze_dart_tip", script_name="GE_Dart_Fletcher", threshold=0.95, should_click=True)

    return True
