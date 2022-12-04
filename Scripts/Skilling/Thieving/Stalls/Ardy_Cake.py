from API.Interface.General import setup_interface, is_otd_enabled, is_inventory_full
from API.Imaging.Image import does_img_exist
from API.AntiBan import wait_for_img, sleep_between
from API.Mouse import mouse_click


def steal_ardy_cake(curr_loop):
    if curr_loop == 1:
        setup_interface("east", 3, "up")
        is_otd_enabled(should_enable=True)

    is_inventory_full(should_cont=True, should_drop=True, start_slot=1, end_slot=28)

    if check_for_ready_stall():
        click_cake_stall()
        sleep_between(1.1, 1.5)

    is_inventory_full(should_cont=True, should_drop=True, start_slot=1, end_slot=28)

    return True


def check_for_ready_stall():
    return does_img_exist(img_name="stall_is_ready", script_name="Ardy_Cake", category="Scripts", threshold=0.9, should_click=False)


def click_cake_stall():
    stall_xy = 760, 525
    mouse_click(stall_xy, max_num_clicks=2)
    return
