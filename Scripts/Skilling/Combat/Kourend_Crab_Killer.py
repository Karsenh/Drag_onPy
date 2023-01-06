import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click

script_name = "Kourend_Crab_Killer"

clicked_crabs = 0
should_reset_aggro = False
found_path_1 = False
found_path_2 = False
crab_search_attempts = 0


def start_killing_kourend_crabs(curr_loop):
    global clicked_crabs
    global found_path_1
    global found_path_2
    global should_reset_aggro
    global crab_search_attempts

    if curr_loop == 1:
        setup_interface("west", 1, "up")

    # If we're not getting hp_exp for six seconds:
        # Click other crabs to aggro

    is_tab_open("inventory", should_be_open=False)

    # Else - we're fighting crabs
    if not wait_for_img(img_name="hp_exp", script_name=script_name, max_wait_sec=6, threshold=0.90):
        print(f"❌ Not fighting Crab. Have we tried clicking crabs before? click_crabs = {clicked_crabs} & crab_search_attempts = {crab_search_attempts}")

        if clicked_crabs > 2 or crab_search_attempts > 2:
            print(f'🔙 We need to reset aggro!')
            reset_aggro()

        # Find a crab to click
        for i in range(0, 24):
            if does_img_exist(img_name=f"crab_{i}", script_name=script_name, threshold=0.85, should_click=True):
                API.AntiBan.sleep_between(5.7, 5.8)
                clicked_crabs += 1
                print(f'🖱 Found a crab and clicked it - clicked_crabs now = {clicked_crabs}')
                if clicked_crabs > 1:
                    print(f"🖱 Found and clicked at least 2 crabs - We should be in combat, returning... clicked_crabs = {clicked_crabs}")
                    return True

        if clicked_crabs == 0:
            crab_search_attempts += 1
            print(f"❌ We didn't find any crabs to click out of all images - crab_search_attempts increased: {crab_search_attempts}")
    else:
        print(f"⚔ We're in combat - clicked_crabs reset to 0")
        clicked_crabs = 0
        crab_search_attempts = 0

    return True


def reset_aggro():
    if not handle_reaggro_for_path("a"):
        if not handle_reaggro_for_path("b"):
            return False

    return True


# -------
# HELPERS
# -------
def handle_reaggro_for_path(path_letter="a"):
    should_move_back = False

    if does_img_exist(img_name=f"aggro_path_{path_letter}_0", script_name="Kourend_Crab_Killer", threshold=0.98, should_click=True):
        API.AntiBan.sleep_between(7.0, 7.1)

    if does_img_exist(img_name=f"aggro_path_{path_letter}_1", script_name="Kourend_Crab_Killer", threshold=0.98, should_click=True):
        API.AntiBan.sleep_between(7.0, 7.1)

    if does_img_exist(img_name=f"aggro_path_{path_letter}_2", script_name="Kourend_Crab_Killer", threshold=0.98, should_click=True):
        should_move_back = True
        API.AntiBan.sleep_between(7.0, 7.1)

    if should_move_back:
        if path_letter == "a":
            move_back_from_a()
        else:
            move_back_from_b()
        return True

    return False


def move_back_from_b():
    back_1_xy = 1303, 265
    mouse_click(back_1_xy)
    API.AntiBan.sleep_between(6.0, 6.1)
    back_2_xy = 1281, 259
    mouse_click(back_2_xy)
    API.AntiBan.sleep_between(5.0, 5.1)
    return


def move_back_from_a():
    back_1_xy = 1381, 287
    mouse_click(back_1_xy)
    API.AntiBan.sleep_between(6.0, 6.1)

    back_2_xy = 1388, 261
    mouse_click(back_2_xy)
    API.AntiBan.sleep_between(6.0, 6.1)
    return