from API.Interface.General import setup_interface, does_img_exist, is_otd_enabled, is_tab_open, is_inventory_full
from API.AntiBan import sleep_between, wait_for_img


fishing_attempts = 0


def fish_barb_trout(curr_loop):
    global fishing_attempts

    if curr_loop == 1:
        setup_interface("west", 2, "up")
        is_otd_enabled(should_enable=True)
        sleep_between(0.8, 2.3)
        is_tab_open(tab="inventory", should_open=False)
        sleep_between(1.1, 2.1)

    if not is_fishing_trout():
        if not click_trout_spot():
            fishing_attempts += 1
            print(f"Couldn't find trout spot to click (a) - attempts: {fishing_attempts}")
            if fishing_attempts > 5:
                return False
        sleep_between(4.3, 6.7)

    if is_inventory_full(should_drop=True, start_slot=1, end_slot=26):
        is_tab_open("inventory", False)
        if not click_trout_spot():
            fishing_attempts += 1
            print(f"Couldn't find trout spot to click (b) - attempts: {fishing_attempts}")
        sleep_between(4.1, 5.3)

    return True


def is_fishing_trout(DEBUG=True):
    return wait_for_img(img_to_search="is_fishing_trout", script_name="Barb_Trout", category_name="Scripts", max_wait_sec=5, img_threshold=0.60)


def click_trout_spot():
    return does_img_exist(img_name="trout_spot", script_name="Barb_Trout", category="Scripts", threshold=0.8, should_click=True, x_offset=20, y_offset=45)

