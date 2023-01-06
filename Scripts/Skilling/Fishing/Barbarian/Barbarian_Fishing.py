from API.Interface.General import setup_interface, is_otd_enabled, is_inventory_full, is_tab_open
from API.Imaging.Image import does_img_exist
from API.Imaging.OCR.Total_Exp import wait_for_exp_change
import API.AntiBan
import pyautogui as pag
from API.Debug import write_debug


click_fish_attempts = 0


def barbarian_fishing(curr_loop):
    global click_fish_attempts

    if curr_loop == 1:
        setup_interface("east", 2, "up")
        is_otd_enabled(True)
        is_tab_open("inventory", should_be_open=False)
        click_barbarian_fish()

    is_tab_open("inventory", should_be_open=False)

    if is_inventory_full(should_cont=True, should_drop=True, start_slot=1, end_slot=26, should_close_after=True):
        if not any(click_barbarian_fish()):
            click_fish_attempts += 1
            if click_fish_attempts > 10:
                return False

    # If level up dialogue - clear and re-click fish
    if not is_barbarian_fishing():
        if not any(click_barbarian_fish()):
            click_fish_attempts += 1
            if click_fish_attempts > 10:
                return False
        API.AntiBan.sleep_between(1.1, 2.3)

    if is_inventory_full(should_cont=True, should_drop=True, start_slot=1, end_slot=26, should_close_after=True):
        if not any(click_barbarian_fish()):
            click_fish_attempts += 1
            if click_fish_attempts > 10:
                return False

    return True


def click_barbarian_fish():
    is_leaping_trout = does_img_exist("leaping_trout", script_name="Barbarian_Fishing", category="Scripts", threshold=0.8, should_click=True, x_offset=15, y_offset=50)
    is_leaping_salmon = does_img_exist("leaping_salmon", script_name="Barbarian_Fishing", category="Scripts", threshold=0.8, should_click=True, x_offset=15, y_offset=50)
    is_leaping_sturgeon = does_img_exist("leaping_sturgeon", script_name="Barbarian_Fishing", category="Scripts", threshold=0.8, should_click=True, x_offset=15, y_offset=50)
    all_fish = is_leaping_salmon, is_leaping_trout, is_leaping_sturgeon
    return all_fish


def is_barbarian_fishing():
    return API.Imaging.Image.wait_for_img(img_name="exp_change", script_name="Barbarian_Fishing", threshold=0.8, max_wait_sec=8)
    # return wait_for_exp_change(max_wait_sec=8)


def handle_level_dialogue():
    if does_img_exist("level_up", category="General"):
        pag.press('space')
        API.AntiBan.sleep_between(1.1, 2.3)
        pag.press('space')
        API.AntiBan.sleep_between(0.8, 1.7)
    return
