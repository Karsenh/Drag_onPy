import random
import pyautogui as pag
import API.AntiBan
from API.Imaging.OCR.Skill_Levels import ocr_skill_levels
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Interface.General import setup_interface, is_otd_enabled, get_xy_for_invent_slot, drop_inventory, is_tab_open
from API.Mouse import mouse_click
from API.Imaging.OCR.Skill_Levels import get_skill_level

curr_tree_num = 1


def start_chop_fletching(curr_loop):
    global curr_tree_num
    print(f'Curr_loop: {curr_loop}')

    if curr_loop == 1:
        ocr_skill_levels()
        setup_interface("west", 2, "up")
        is_otd_enabled(should_enable=False)
        API.AntiBan.sleep_between(1.1, 2.3)

    chop_and_wait_for_exp()

    curr_tree_num += 1

    if curr_tree_num > 11:
        handle_level_dialogue()
        fletch_logs()
        curr_tree_num = 1

    return True


def chop_and_wait_for_exp():
    if wait_for_img(img_to_search=f"t{curr_tree_num}", script_name="Lummy_Chop_Fletch", img_threshold=0.9, max_wait_sec=4):
        does_img_exist(img_name=f"t{curr_tree_num}", script_name="Lummy_Chop_Fletch", should_click=True, x_offset=23, y_offset=20, threshold=0.9)

    if not wait_for_img(img_to_search="wc_exp", script_name="Lummy_Chop_Fletch", max_wait_sec=6, img_threshold=0.88):
        print(f"Havent't chopped the logs yet?")
        API.AntiBan.sleep_between(0.6, 1.2)

    API.AntiBan.sleep_between(1.6, 1.7)
    return


def fletch_logs(should_drop_recursive=True):
    should_drop_fletched_items = True
    slot_1_xy = get_xy_for_invent_slot(slot_num=1)

    is_tab_open("inventory", should_open=True)

    mouse_click(slot_1_xy)
    API.AntiBan.sleep_between(0.7, 1.1)

    # if random.randint(1, 5) > 3:
    #     log_xy = get_xy_for_invent_slot(slot_num=5)
    # else:
    #     log_xy = get_xy_for_invent_slot(slot_num=6)

    # mouse_click(log_xy)
    does_img_exist(img_name="inventory_log", script_name="Lummy_Chop_Fletch", threshold=0.9, should_click=True, x_offset=12, y_offset=11)

    API.AntiBan.sleep_between(1.2, 1.6)

    lvl_val = get_skill_level("fletching")
    if lvl_val == "n/a":
        lvl_val = 1
    else:
        lvl_val = int(lvl_val)

    curr_fletch_lvl = lvl_val

    if curr_fletch_lvl <= 4:
        pag.press("1")
        should_drop_fletched_items = False
    if 4 < curr_fletch_lvl <= 9:
        pag.press("3")
    elif curr_fletch_lvl > 9:
        pag.press("4")

    while wait_for_img(img_to_search="fletching_exp", script_name="Lummy_Chop_Fletch", max_wait_sec=3, img_threshold=0.8):
        print(f'Still fletching...')
        API.AntiBan.sleep_between(1.1, 1.6)

    handle_level_dialogue()

    if should_drop_recursive:
        if should_drop_fletched_items:
            drop_inventory(from_spot_num=4, to_spot_num=14, should_close_after=True, should_disable_otd_after=True)

    API.AntiBan.sleep_between(0.9, 1.3)
    return


def handle_level_dialogue():
    if does_img_exist("level_up", category="General"):
        pag.press('space')
        API.AntiBan.sleep_between(1.1, 2.3)
        pag.press('space')
        API.AntiBan.sleep_between(0.8, 1.7)

        if does_img_exist(img_name="inventory_log", script_name="Lummy_Chop_Fletch", threshold=0.85):
            fletch_logs(False)
    return
