import API.AntiBan
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click
import pyautogui as pag

should_reset = False
bird_type = "cerulean"


def start_snaring_birds(curr_loop):
    global should_reset

    if curr_loop == 1:
        setup_interface("north", 3, "down")
        API.AntiBan.sleep_between(1.0, 1.1)
        does_img_exist(img_name="inventory_trap", script_name="Bird_Snarer", should_click=True, x_offset=5, y_offset=5)

    for i in range(1, 10):
        check_count = 0
        while not should_reset:
            if not check_snare_for_bird() and not check_for_dead_snare():
                alch()
            check_count += 1
            if check_count > 14:
                if not does_img_exist(img_name="downed_trap", script_name="Bird_Snarer", should_click=True, threshold=0.9):
                    return False
                else:
                    should_reset = True

        reset_tile_xy = 852, 535
        mouse_click(reset_tile_xy)
        API.AntiBan.sleep_between(1.4, 1.5)

        is_tab_open("inventory", True)
        if does_img_exist(img_name="inventory_trap", script_name="Bird_Snarer", should_click=True, x_offset=5,
                          y_offset=5):
            should_reset = False
        else:
            return False

    return True

# Start on the tile you want to place trap

# Place trap from inventory does_img_exist trap
# Wait for image a) dead_ bird or b) dead_trap
# When one is seen


def check_snare_for_bird():
    global should_reset

    # if we find a caught bird...
    if wait_for_img(img_name=f"caught_{bird_type}_bird", script_name="Bird_Snarer", max_wait_sec=2, x_offset=5,
                    y_offset=10, threshold=0.9):
        should_reset = True
        API.AntiBan.sleep_between(1.0, 1.1)
        wait_for_img(img_name=f"caught_{bird_type}_bird", script_name="Bird_Snarer", max_wait_sec=2, x_offset=5,
                     y_offset=10, should_click=True, threshold=0.9)
        if not wait_for_img(img_name="hunter_exp", script_name="Bird_Snarer"):
            # Empty inventory of birds and bones
            is_otd_enabled(should_enable=True)
            API.AntiBan.sleep_between(0.4, 0.6)
            is_tab_open("inventory", True)
            API.AntiBan.sleep_between(0.5, 0.7)
            while does_img_exist(img_name="drop_1", script_name="Bird_Snarer", should_click=True,
                                 threshold=0.9) and \
                    does_img_exist(img_name="drop_2", script_name="Bird_Snarer", should_click=True):
                print(f'Dropping bird shit from inventory...')
            API.AntiBan.sleep_between(0.4, 0.5)
            is_otd_enabled(False)
            check_snare_for_bird()
    return


def check_for_dead_snare():
    global should_reset

    if wait_for_img(img_name=f"dead_trap_{bird_type}", script_name="Bird_Snarer", should_click=True, x_offset=8,
                        y_offset=10, max_wait_sec=2, threshold=0.95):
        should_reset = True
        check_snare_for_bird()
    return


def alch():
    is_tab_open("magic", should_open=True)
    API.AntiBan.sleep_between(0.4, 0.6)
    does_img_exist(img_name="high_alch", script_name="Seers_Rooftops", should_click=True)
    API.AntiBan.sleep_between(0.4, 0.8)
    if not does_img_exist(img_name="magic_long_note", script_name="Seers_Rooftops", x_offset=4, y_offset=4, should_click=True):
        pag.leftClick()
    return
