import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_run_on, is_run_gt, is_hp_gt
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click
from API.Debug import write_debug

SCRIPT_NAME = "Kourend_Crab_Killer"

# Attack, Strength, Defense
ATTACK_STYLE = "Defense"
# 1 = NW tip (4 crabs)
CURR_SPOT = 1

SUPPORTED_FOOD_ARR = ["Monkfish"]


def start_killing_kourend_crabs(curr_loop):
    global ATTACK_STYLE
    global CURR_SPOT

    if curr_loop != 1:

        check_health()

        if not is_fighting_crab(wait=8):
            print(f'Not fighting crabs - Resetting aggro')
            handle_run()
            if not reset_spot_1():
                return False
            API.AntiBan.sleep_between(3.0, 3.1)

    else:
        setup_interface("west", 1, "up")
        set_attack_style(ATTACK_STYLE)
        # set_curr_spot()
    return True


def check_health():
    if not is_hp_gt(percent=9):
        eat_foot()
    return


def reset_spot_1():
    RESET_IMG_THRESH = 0.96

    if not does_img_exist(img_name=f"Reset_Spot_1_Agg_A", script_name="Kourend_Crab_Killer",
                          threshold=RESET_IMG_THRESH, should_click=True, x_offset=30, y_offset=28):
        manual_xy = 1324, 296
        mouse_click(manual_xy)

    # Arrow image before heading back
    if not wait_for_img(img_name=f"Reset_Spot_1_Agg_B", script_name="Kourend_Crab_Killer",
                        threshold=0.95, should_click=True, max_wait_sec=10):
        manual_xy = 1367, 270
        mouse_click(manual_xy)

    API.AntiBan.sleep_between(4.5, 4.6)

    if not wait_for_img(img_name=f"Reset_Spot_1_Agg_Back_A", script_name="Kourend_Crab_Killer",
                        threshold=RESET_IMG_THRESH, should_click=True, x_offset=40, max_wait_sec=10):
        manual_xy = 1367, 270
        mouse_click(manual_xy)

    API.AntiBan.sleep_between(6.5, 6.6)

    return wait_for_img(img_name="At_Spot_1", script_name="Kourend_Crab_Killer",
                 threshold=0.95, should_click=True, x_offset=55, y_offset=0, max_wait_sec=15)


def set_curr_spot():
    global CURR_SPOT

    if does_img_exist(img_name="At_Spot_1", script_name=SCRIPT_NAME, threshold=0.9):
        print(f'✅ AT SPOT ONE')
        CURR_SPOT = 1
    elif does_img_exist(img_name="At_Spot_2", script_name=SCRIPT_NAME, threshold=0.9):
        print(f'✅ AT SPOT TWO')
        CURR_SPOT = 2
    else:
        print(f'Couldnt find either spot images - set to none!')
        CURR_SPOT = None
    return


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


# -------
# HELPERS
# -------
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


def eat_foot():
    use_food = None

    is_tab_open('inventory', True)

    for curr_food in SUPPORTED_FOOD_ARR:
        if does_img_exist(img_name=f"Inventory_{curr_food}", script_name="Kourend_Crab_Killer", threshold=0.9):
            use_food = curr_food

    return does_img_exist(img_name=f"Inventory_{use_food}", script_name="Kourend_Crab_Killer", should_click=True, click_middle=True, threshold=0.9)