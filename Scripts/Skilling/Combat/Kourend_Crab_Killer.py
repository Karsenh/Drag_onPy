import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_run_on, is_run_gt
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click

SCRIPT_NAME = "Kourend_Crab_Killer"

# Attack, Strength, Defense
ATTACK_STYLE = "Defense"
# 1 = NW tip (4 crabs)
CRAB_SPOT = 1


def start_killing_kourend_crabs(curr_loop):
    global ATTACK_STYLE
    if curr_loop != 1:
        if not is_fighting_crab(wait=6):
            print(f'Not fighting crabs - Resetting aggro')
            reset_aggro()

    else:
        setup_interface("east", 2, "up")
        set_attack_style(ATTACK_STYLE)
    return True


def reset_aggro():
    reset_xy = 1355, 73
    move_back_xy = 1327, 275

    if does_img_exist(img_name="Reset_Spot", script_name=SCRIPT_NAME, threshold=0.9):
        run_sleep = handle_run()
        mouse_click(reset_xy)
        print(f'RUN SLEEP TIME: {run_sleep}')
        API.AntiBan.sleep_between(run_sleep, run_sleep+1)

    if does_img_exist(img_name="Training_Spot", script_name=SCRIPT_NAME, threshold=0.9):
        run_sleep2 = handle_run()
        mouse_click(move_back_xy)
        print(f'RUN SLEEP_2 TIME: {run_sleep2}')
        API.AntiBan.sleep_between(run_sleep2, run_sleep2+1)

    return True


def is_fighting_crab(wait):
    return wait_for_img(img_name="Hp", category="Exp_Drops", threshold=0.9, max_wait_sec=wait)


def set_attack_style(style):
    is_tab_open(tab="combat", should_be_open=True)

    if wait_for_img(img_name="Combat_tab", category="Interface", threshold=0.85):
        match style:
            case "Attack":
                does_img_exist(img_name="Combat_Chop", category="Interface", threshold=0.9, should_click=True, click_middle=True)
                return True
            case "Defense":
                does_img_exist(img_name="Combat_Block", category="Interface", threshold=0.9, should_click=True, click_middle=True)
                return True

    return False


def handle_run():
    if is_run_gt(percent=9):
        if is_run_on():
            # API.AntiBan.sleep_between(16.0, 16.1)
            return 16
        else:
            if is_run_gt(percent=90):
                is_run_on(True)
    else:
        if does_img_exist(img_name="Inventory_Stamina_4", script_name="Kourend_Crab_Killer", threshold=0.94,
                          should_click=True, click_middle=True) and is_run_on(True):
            # API.AntiBan.sleep_between(16.0, 16.1)
            return 16
        else:
            if does_img_exist(img_name="Inventory_Stamina_3", script_name="Kourend_Crab_Killer", threshold=0.94,
                              should_click=True, click_middle=True) and is_run_on(True):
                # API.AntiBan.sleep_between(16.0, 16.1)
                return 16
            else:
                if does_img_exist(img_name="Inventory_Stamina_2", script_name="Kourend_Crab_Killer", threshold=0.94, should_click=True, click_middle=True) and is_run_on(True):
                    # API.AntiBan.sleep_between(16.0, 16.1)
                    return 16
                elif does_img_exist(img_name="Inventory_Stamina_1", script_name="Kourend_Crab_Killer", threshold=0.94, should_click=True, click_middle=True) and is_run_on(True):
                    # API.AntiBan.sleep_between(16.0, 16.1)
                    return 16
                else:
                    # API.AntiBan.sleep_between(28.0, 28.1)
                    return 28


# -------
# HELPERS
# -------
