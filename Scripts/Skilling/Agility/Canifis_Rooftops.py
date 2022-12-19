import API.AntiBan
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Interface.General import setup_interface, is_tab_open
from API.Mouse import mouse_click
import pyautogui as pag


def start_canifis_rooftops(curr_loop):
    if curr_loop != 1:
        click_first_tree()
        click_second_jump()
        click_third_jump()
        click_fourth_jump()
        click_fifth_jump()
        click_sixth_jump()
        click_seventh_jump()
        click_last_jump()
    else:
        setup_interface("north", 2, "up")
        API.AntiBan.sleep_between(0.4, 0.6)
        is_tab_open("inventory", False)
    return True


def click_first_tree():
    handle_level_dialogue()
    wait_for_img(img_name="o1_alt", script_name="Canifis_Rooftops", threshold=0.85, should_click=True, max_wait_sec=15, y_offset=16, x_offset=4)
    return


def click_second_jump():
    if wait_for_img(img_name="mog_4", script_name="Canifis_Rooftops", threshold=0.9, should_click=True, max_wait_sec=8,
                    x_offset=5, y_offset=15):
        API.AntiBan.sleep_between(0.8, 1.1)
        return wait_for_img(img_name='o2_from_mog', script_name="Canifis_Rooftops", threshold=0.9, should_click=True,
                            x_offset=20, y_offset=22, max_wait_sec=10)
    else:
        if not wait_for_img(img_name='o2', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, max_wait_sec=15, x_offset=6):
            if not wait_for_img(img_name='o2_from_broken', script_name="Canifis_Rooftops", threshold=0.95, should_click=True,
                         max_wait_sec=5):
                handle_level_dialogue()
    return


def click_third_jump():
    if wait_for_img(img_name="mog_on_2", script_name="Canifis_Rooftops", threshold=0.92, should_click=True, max_wait_sec=6, x_offset=4, y_offset=8):
        return wait_for_img(img_name='o3_from_mog', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=38, y_offset=25, max_wait_sec=10)
    else:
        if not wait_for_img(img_name='o3_alt', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=35, y_offset=45, max_wait_sec=10):
            handle_level_dialogue()
    return


def click_fourth_jump():
    if wait_for_img(img_name="mog_on_3", script_name="Canifis_Rooftops", threshold=0.9, max_wait_sec=6, x_offset=24, y_offset=4, should_click=True):
        API.AntiBan.sleep_between(1.0, 1.1)
        return wait_for_img(img_name='o4_from_mog', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=20, y_offset=22, max_wait_sec=10)
    if not wait_for_img(img_name='o4', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=25, y_offset=22, max_wait_sec=10):
        if wait_for_img(img_name='o4_fall', script_name="Canifis_Rooftops", threshold=0.9):
            # Return to the start of the course (recover from o3 fall)
            back_to_start_xy = 1445, 230
            mouse_click(back_to_start_xy)
            wait_for_img(img_name="o4_restart", script_name="Canifis_Rooftops", threshold=0.80, should_click=True, y_offset=4, max_wait_sec=10)
            API.AntiBan.sleep_between(2.5, 2.6)
            click_second_jump()
            click_third_jump()
        else:
            handle_level_dialogue()
    return


def click_fifth_jump():
    if wait_for_img(img_name="mog_on_5", script_name="Canifis_Rooftops", threshold=0.92, should_click=True, max_wait_sec=8, x_offset=14, y_offset=12):
        return wait_for_img(img_name='o5_from_mog', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=20, y_offset=22, max_wait_sec=10)
    if not wait_for_img(img_name='o5', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=15, y_offset=12, max_wait_sec=10):
        if wait_for_img(img_name='o4_fall', script_name="Canifis_Rooftops", threshold=0.9):
            # Return to the start of the course (recover from o3 fall)
            back_to_start_xy = 1445, 230
            mouse_click(back_to_start_xy)
            API.AntiBan.sleep_between(2.8, 3.1)
            wait_for_img(img_name="o4_restart", script_name="Canifis_Rooftops", threshold=0.75, should_click=True, y_offset=4, max_wait_sec=8)
            click_second_jump()
            click_third_jump()
            click_fourth_jump()
            click_fifth_jump()
    return


def click_sixth_jump():
    if wait_for_img(img_name="mog_3", script_name="Canifis_Rooftops", should_click=True, max_wait_sec=6):
        return wait_for_img(img_name='o6_from_mog', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=20, y_offset=22, max_wait_sec=10)
    else:
        if not wait_for_img(img_name='o6', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, max_wait_sec=10):
            handle_level_dialogue()
    return


def click_seventh_jump():
    is_tab_open("inventory", False)
    if not wait_for_img(img_name='o7', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, max_wait_sec=10):
        if wait_for_img(img_name='o7_broken_alt', script_name="Canifis_Rooftops", threshold=0.9, should_click=True,
                     max_wait_sec=6, x_offset=205, y_offset=-160):
            wait_for_img(img_name='o7_from_broken', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, max_wait_sec=10)
        else:
            handle_level_dialogue()
    return


def click_last_jump():
    if not wait_for_img(img_name='o8', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=15, y_offset=12, max_wait_sec=15):
        if not wait_for_img(img_name='o8_restart', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, x_offset=15, y_offset=12, max_wait_sec=10):
            handle_level_dialogue()
    return


def handle_level_dialogue():
    if does_img_exist(img_name="level_up", category="General"):
        pag.press('space')
        API.AntiBan.sleep_between(1.1, 2.3)
        pag.press('space')
        API.AntiBan.sleep_between(0.8, 1.7)

    return