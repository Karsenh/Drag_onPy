import random
import pyautogui as pag
import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot
from API.Interface.Bank import is_bank_tab_open, is_withdraw_qty, deposit_all
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Mouse import mouse_click
from API.Skill_Levels import get_skill_level


def start_blowing_glass(curr_loop):

    if not is_still_crafting():
        if not did_level_crafting():
            if curr_loop == 1:
                setup_interface("north", 4, "up")
                is_tab_open("inventory", should_open=True)
                API.AntiBan.sleep_between(0.8, 1.3)

            open_ge_bank(curr_loop)

            blow_glass()

    return True


def open_ge_bank(curr_loop):

    # ge_bank_xy = 679, 440
    # mouse_click(ge_bank_xy)

    wait_for_img(img_name="bank_alt", script_name="GE_Glass_Blower", threshold=0.90, should_click=True, x_offset=39)

    API.AntiBan.sleep_between(3.0, 3.1)

    if curr_loop != 1:
        r_invent_xy = get_xy_for_invent_slot(slot_num=random.randint(2, 5))
        mouse_click(r_invent_xy)
    else:
        deposit_all()

    API.AntiBan.sleep_between(0.6, 0.9)

    is_bank_tab_open(tab_num=2, should_open=True)

    API.AntiBan.sleep_between(0.8, 1.3)

    print(f'withdraw_all not selected? {is_withdraw_qty(qty="all", should_click=True)}')

    API.AntiBan.sleep_between(0.8, 1.3)

    does_img_exist(img_name="pipe", script_name="GE_Glass_Blower", threshold=0.92, should_click=True, x_offset=20, y_offset=15)

    API.AntiBan.sleep_between(0.8, 1.3)

    does_img_exist(img_name="molten_glass", script_name="GE_Glass_Blower", threshold=0.95, should_click=True, x_offset=15, y_offset=13)

    API.AntiBan.sleep_between(0.8, 0.9)

    pag.press('esc')

    API.AntiBan.sleep_between(0.9, 1.8)

    return


def blow_glass():

    # Use pipe on molten glass
    pipe_xy = get_xy_for_invent_slot(1)
    mouse_click(pipe_xy)

    API.AntiBan.sleep_between(0.8, 1.2)

    # Click the molten glass in inventory to use the pipe with it
    does_img_exist(img_name="inventory_molten_glass", script_name="GE_Glass_Blower", threshold=0.85, should_click=True, x_offset=12, y_offset=10)

    API.AntiBan.sleep_between(1.1, 1.3)

    # Check that 'All' Qty is selected for crafting
    if not does_img_exist(img_name="all_qty_selected", category="General", threshold=0.95):
        does_img_exist(img_name="all_qty", category="General", threshold=0.9, should_click=True, x_offset=8, y_offset=7)
        API.AntiBan.sleep_between(2.0, 2.1)

    # Check get crafting level to determine which number to enter
    crafting_lvl = get_skill_level("crafting")

    if 1 < crafting_lvl <= 3:
        pag.press('1')
    if 3 < crafting_lvl <= 11:
        pag.press('2')
    if 11 < crafting_lvl <= 32:
        pag.press('3')
    if 32 < crafting_lvl <= 41:
        pag.press('4')
    if 41 < crafting_lvl <= 45:
        pag.press('5')
    if 45 < crafting_lvl <= 48:
        pag.press('6')
    if crafting_lvl >= 49:
        pag.press('7')

    API.AntiBan.sleep_between(1.0, 1.1)

    return


def is_still_crafting():
    return wait_for_img(img_name="crafting_exp", script_name="GE_Glass_Blower", threshold=0.90, max_wait_sec=3)


def did_level_crafting():
    if does_img_exist("level_up", category="General"):
        pag.press('space')
        API.AntiBan.sleep_between(1.1, 2.3)
        pag.press('space')
        API.AntiBan.sleep_between(0.8, 1.7)

        if does_img_exist(img_name="inventory_molten_glass", script_name="GE_Glass_Blower", threshold=0.85):
            blow_glass()
            return True

    return False
