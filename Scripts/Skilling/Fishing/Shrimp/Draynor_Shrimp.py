import random
from API.Mouse import mouse_click
from API.Interface.General import setup_interface, is_inventory_full, is_tab_open, get_xy_for_invent_slot
from API.Interface.Bank import check_if_bank_tab_open, deposit_all
from API.Imaging.Image import does_img_exist, wait_for_img
from API.AntiBan import print_to_log
import API.AntiBan


def fish_draynor_shrimp(curr_loop):

    if curr_loop == 1:
        setup_interface(cam_dir="east", cam_distance=3, cam_angle="up")

        is_tab_open("inventory", should_open=False)

        if not bank():
            return False

        check_if_bank_tab_open(tab_num=5, should_open=True)

        API.AntiBan.sleep_between(0.4, 1.2)

        deposit_all(include_equipment=True)

        API.AntiBan.sleep_between(0.6, 1.4)

        if not withdraw_banked_net():
            print(f'Need small fishing net!')
            print_to_log('Need small fishing net!')
            return False

        API.AntiBan.sleep_between(0.6, 1.6)

        if not move_to_fishing_spot():
            print_to_log("Can't see fishing spot image")
            return False

        API.AntiBan.sleep_between(10.3, 14.5)

    if not is_fishing():
        click_fishing_spot()
        API.AntiBan.sleep_between(2.1, 4.7)
        if is_inventory_full(should_drop=False):
            print(f'Entering is_inventory_full true block')
            if not bank():
                return False
            # r_invent_slot = random.randint(2, 28)
            # deposit_shrimp = get_xy_for_invent_slot(r_invent_slot)
            # mouse_click(deposit_shrimp)
            deposit_all()
            API.AntiBan.sleep_between(0.8, 1.4)
            if not withdraw_banked_net():
                return False
            API.AntiBan.sleep_between(0.7, 1.2)
            if not move_to_fishing_spot():
                return False
            API.AntiBan.sleep_between(10.3, 12.4)
            if not is_fishing():
                click_fishing_spot()
                API.AntiBan.sleep_between(1.6, 4.7)
    else:
        API.AntiBan.sleep_between(1.3, 3.7)

    return True


def bank():
    if not move_to_bank():
        return False

    API.AntiBan.sleep_between(10.0, 13.1)

    if not open_bank():
        return False

    API.AntiBan.sleep_between(1.3, 2.3)
    return True


def move_to_bank():
    return does_img_exist(img_name="bank_spot", script_name="Draynor_Shrimp", x_offset=5, y_offset=5, should_click=True)


def open_bank():
    return does_img_exist(img_name="bank_booth", script_name="Draynor_Shrimp", threshold=0.95, should_click=True)


def is_net_in_inventory():
    return does_img_exist(img_name="no_small_net", script_name="Draynor_Shrimp")


def withdraw_banked_net():
    return does_img_exist(img_name="small_net", script_name="Draynor_Shrimp", threshold=0.99, should_click=True)


def move_to_fishing_spot():
    return does_img_exist(img_name="fishing_spot", script_name="Draynor_Shrimp", threshold=0.95, should_click=True, x_offset=0, y_offset=0)


def is_fishing():
    return wait_for_img(img_name="is_fishing", script_name="Draynor_Shrimp", category_name="Scripts", max_wait_sec=5, threshold=0.60)


def click_fishing_spot():
    return does_img_exist(img_name="shrimp_spot", script_name="Draynor_Shrimp", threshold=0.65, should_click=True)


