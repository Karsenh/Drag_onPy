import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click

SCRIPT_NAME = "Kourend_Crab_Killer"

# Attack, Strength, Defense
ATTACK_STYLE = "Defense"
# 1 = NW tip (4 crabs)
CRAB_SPOT = 1


def start_killing_kourend_crabs(curr_loop):
    if curr_loop != 1:
        if not is_fighting_crab():
            print(f'Not fighting crabs - Resetting aggro')
            reset_aggro()

    else:
        setup_interface("east", 2, "up")

    return True


def reset_aggro():
    reset_xy = 1355, 73
    move_back_xy = 1327, 275

    if does_img_exist(img_name="Reset_Spot", script_name=SCRIPT_NAME, threshold=0.9):
        mouse_click(reset_xy)
        API.AntiBan.sleep_between(16.0, 16.1)

    if does_img_exist(img_name="Training_Spot", script_name=SCRIPT_NAME, threshold=0.9):
        mouse_click(move_back_xy)
        API.AntiBan.sleep_between(16.0, 16.1)

    return True


def is_fighting_crab():
    return wait_for_img(img_name="Hp", category="Exp_Drops", threshold=0.9, max_wait_sec=6)


def set_attack_style():
    is_tab_open(tab="combat", should_be_open=True)

    if wait_for_img(img_name="Combat_tab", category="Interface", threshold=0.85):
        match ATTACK_STYLE:
            case "Attack":
                does_img_exist(img_name="Combat_Chop", category="Interface", threshold=0.9, should_click=True, click_middle=True)



    return


# -------
# HELPERS
# -------
