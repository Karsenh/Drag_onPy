import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_run_on, is_run_gt
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click

SCRIPT_NAME = "Kourend_Crab_Killer"

# Attack, Strength, Defense
ATTACK_STYLE = "Defense"
# 1 = NW tip (4 crabs)
CRAB_SPOT = 1

CURR_SPOT = 1


def start_killing_kourend_crabs(curr_loop):
    global ATTACK_STYLE
    if curr_loop != 1:
        if not is_fighting_crab(wait=8):
            print(f'Not fighting crabs - Resetting aggro')
            reset_aggro()

    else:
        setup_interface("east", 1, "up")
        set_attack_style(ATTACK_STYLE)
        set_curr_spot()
    return True


def reset_aggro():
    global CURR_SPOT

    handle_run()

    if CURR_SPOT == 1:
        print(f'case 1')
        return move_to_spot(2)
    else:
        print(f'case 2')
        return move_to_spot(1)


def set_curr_spot():
    global CURR_SPOT

    if does_img_exist(img_name="At_Spot_1", script_name=SCRIPT_NAME, threshold=0.9):
        print(f'AT SPOT ONE')
        CURR_SPOT = 1
    elif does_img_exist(img_name="At_Spot_2", script_name=SCRIPT_NAME, threshold=0.9):
        print(f'AT SPOT TWO')
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

def move_to_spot(spot_num):
    global CURR_SPOT

    if does_img_exist(img_name=f"Move_To_Spot_{spot_num}_A", script_name="Kourend_Crab_Killer", threshold=0.9,
                      should_click=True, click_middle=True):
        API.AntiBan.sleep_between(4.0, 4.1)
        if wait_for_img(img_name=f"Move_To_Spot_{spot_num}_B", script_name="Kourend_Crab_Killer", threshold=0.9,
                          should_click=True, click_middle=True, max_wait_sec=10):
            API.AntiBan.sleep_between(5.0, 5.1)
            CURR_SPOT = spot_num
            return True
        else:
            # Cant find second move to spot image moving back to original spots
            does_img_exist(img_name=f"Cancel_Move_To_{spot_num}")

    else:
        # First move to spot img not found - we're likely not on right tile - recenter
        if CURR_SPOT == 2:
            if does_img_exist(img_name=f"Reposition_Spot_2", script_name=SCRIPT_NAME, should_click=True, threshold=0.9, x_offset=-35, y_offset=40):
                return True
            else:
                return False
        elif CURR_SPOT == 1:
            if does_img_exist(img_name=f"Reposition_Spot_1", script_name=SCRIPT_NAME, threshold=0.9, should_click=True):
                return True
            else:
                return False

        return False