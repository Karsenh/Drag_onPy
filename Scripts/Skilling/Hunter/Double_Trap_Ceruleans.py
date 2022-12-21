import API.AntiBan
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click
import pyautogui as pag

script_name = "Double_Trap_Ceruleans"

should_reset_traps = False
bird_type = "cerulean"

monitor_tile_from_trap_1 = 703, 608
monitor_tile_from_trap_2 = 685, 419

trap_tile_1 = 775, 367
trap_tile_2 = 779, 665

needs_reset_1 = False
needs_reset_2 = False

# 92 on dt
caught_threshold = 0.92
# 91 on dt
down_threshold = 0.94
reset_threshold = 0.90

last_reset_trap_num = 0


def start_trapping_birds(curr_loop):
    global should_reset_traps

    if curr_loop == 1:
        setup_interface("north", 5, "up")
        API.AntiBan.sleep_between(1.0, 1.1)
        is_tab_open("inventory", should_open=True)
        set_initial_traps()

    while not should_reset_traps:
        if check_should_reset_traps():
            print(f'✅ should_reset_traps flipped to TRUE')
            should_reset_traps = True
        else:
            high_alch()

    # Reset traps that need it
    handle_trap_state()
    should_reset_traps = False
    print(f'Traps handled and should_reset_traps set back to false.')

    return True


def set_initial_traps():
    global monitor_tile_from_trap_2
    trap_2_from_1_xy = 869, 798

    does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True, x_offset=5, y_offset=5)

    if wait_for_img(img_name="trap_1_set", script_name=script_name):
        mouse_click(trap_2_from_1_xy)
        API.AntiBan.sleep_between(2.0, 2.1)
        does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True, x_offset=5, y_offset=5)

        if wait_for_img(img_name="trap_2_set", script_name=script_name):
            mouse_click(monitor_tile_from_trap_2)

    return


def check_should_reset_traps():
    global last_reset_trap_num

    if last_reset_trap_num == 2:
        check_trap_num(1)
        check_trap_num(2)
    else:
        check_trap_num(2)
        check_trap_num(1)

    if needs_reset_1 or needs_reset_2:
        print(f'✅ Check_should_reset returning True\nneeds_reset_1 = {needs_reset_1}\nneeds_reset_2 = {needs_reset_2}')
        return True
    else:
        print(f'⛔ Check_should_reset returning False\nneeds_reset_1 = {needs_reset_1}\nneeds_reset_2 = {needs_reset_2}')
        return False


def handle_trap_state():
    global needs_reset_1
    global needs_reset_2

    global monitor_tile_from_trap_1
    global monitor_tile_from_trap_2

    global trap_tile_1
    global trap_tile_2

    global last_reset_trap_num

    if needs_reset_1 and needs_reset_2:
        # Both traps need resetting - go from one directly to the other - then back to monitor tile from second
        print(f'Both traps need to be reset')
        if reset_trap_num(1):
            # Since both traps need replacing, click trap 2 from here
            reset_trap_two_from_one()
            # Move back to monitor tile and begin checking trap status'
            mouse_click(monitor_tile_from_trap_2)
            needs_reset_1 = False
            needs_reset_2 = False
            last_reset_trap_num = 2

    else:
        # Check individually
        if needs_reset_1:
            print(f'Only trap ONE needs resetting')
            reset_trap_num(1)
            # Move back to monitor tile
            mouse_click(monitor_tile_from_trap_1)
            if not wait_for_img(img_name="monitor_tile_signal_from_1", script_name="Double_Trap_Ceruleans", threshold=0.90, max_wait_sec=3):
                mouse_click(monitor_tile_from_trap_1)
            needs_reset_1 = False
            last_reset_trap_num = 1

        if needs_reset_2:
            print(f'Only trap TWO needs resetting')
            reset_trap_num(2)
            mouse_click(monitor_tile_from_trap_2)
            if not wait_for_img(img_name="monitor_tile_signal_from_2", script_name="Double_Trap_Ceruleans", threshold=0.90, max_wait_sec=3):
                mouse_click(monitor_tile_from_trap_2)
            needs_reset_2 = False
            last_reset_trap_num = 2

    API.AntiBan.sleep_between(2.0, 2.1)

    return True


# ---------
# HELPERS
# ---------
def reset_trap_num(trap_num=1):
    global trap_tile_1
    global trap_tile_2

    match trap_num:
        case 1:
            trap_tile_xy = trap_tile_1
        case 2:
            trap_tile_xy = trap_tile_2

    is_tab_open("inventory", True)

    # Check for caught trap separately - might need to empty invent
    if wait_for_img(img_name=f"trap_{trap_num}_caught", script_name=script_name, threshold=caught_threshold, y_offset=4, x_offset=4):
        API.AntiBan.sleep_between(0.3, 0.6)
        wait_for_img(img_name=f"trap_{trap_num}_caught", script_name=script_name, threshold=caught_threshold, y_offset=4, x_offset=4, should_click=True)
        if wait_for_img(img_name="hunter_exp", script_name=script_name):
            # Clicking the tile we want to set trap ONE on
            mouse_click(trap_tile_xy)
            API.AntiBan.sleep_between(1.2, 1.3)
            # Clicking a trap to set
            wait_for_img(img_name="inventory_trap", script_name=script_name, should_click=True)
            API.AntiBan.sleep_between(5.0, 5.1)
            return True

        else:
            # Drop bird shit to make inventory space & try to set the trap again from current tile
            is_otd_enabled(should_enable=True)
            API.AntiBan.sleep_between(0.4, 0.6)
            is_tab_open("inventory", True)
            API.AntiBan.sleep_between(0.5, 0.7)
            while does_img_exist(img_name="drop_1", script_name="Bird_Catcher", should_click=True,
                                 threshold=0.9) and \
                    does_img_exist(img_name="drop_2", script_name="Bird_Catcher", should_click=True):
                print(f'Dropping bird shit from inventory...')
            API.AntiBan.sleep_between(0.4, 0.5)
            is_otd_enabled(False)
            API.AntiBan.sleep_between(0.4, 0.5)
            wait_for_img(img_name=f"trap_{trap_num}_from_drop_invent", script_name="Double_Trap_Ceruleans", threshold=caught_threshold, should_click=True)
            # Click track reset tile to try picking up trap again after making inventory space
            API.AntiBan.sleep_between(2.0, 2.1)
            # Move to trap reset tile
            mouse_click(trap_tile_xy)
            API.AntiBan.sleep_between(2.1, 2.3)
            # Clicking a trap to set
            does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
            API.AntiBan.sleep_between(5.0, 5.1)
            return True
    # Check for down / pickup separate from caught - no need to empty inventory here
    elif wait_for_img(img_name=f"trap_{trap_num}_down", script_name=script_name, threshold=down_threshold, should_click=True, x_offset=9, y_offset=8):
        API.AntiBan.sleep_between(3.0, 3.1)
        # Clicking the tile we want to set trap ONE on
        mouse_click(trap_tile_xy)
        API.AntiBan.sleep_between(1.2, 1.3)
        # Clicking a trap to set
        wait_for_img(img_name="inventory_trap", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(5.0, 5.1)
        return True
    elif wait_for_img(img_name=f"trap_{trap_num}_pickup", script_name=script_name, threshold=reset_threshold, should_click=True):
        wait_for_img(img_name="inventory_trap", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(5.0, 5.1)

    print(f"Didn't find trap_{trap_num}_caught / down / reset. Returning False")
    return False


def reset_trap_two_from_one():
    if does_img_exist(img_name=f"trap_2_caught_from_1", script_name=script_name, threshold=0.9, should_click=True) or \
            does_img_exist(img_name=f"trap_2_down_from_1", script_name=script_name, threshold=0.9, should_click=True, x_offset=5, y_offset=4) or \
            does_img_exist(img_name=f"trap_2_pickup_from_1", script_name=script_name, threshold=0.9, should_click=True):
        print(f'Trap two seen needing reset from trap 1 reset. Clicking...')
        API.AntiBan.sleep_between(5.0, 5.1)
        # Click the tile we owant to set trap TWO on
        mouse_click(trap_tile_2)
        API.AntiBan.sleep_between(3.0, 3.1)
        # Set new trap TWO
        does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(5.0, 5.1)
        return True
    return False


def check_trap_num(trap_num):

    if wait_for_img(img_name=f"trap_{trap_num}_caught", script_name=script_name, threshold=caught_threshold, max_wait_sec=3):
        set_needs_reset(trap_num)

    elif wait_for_img(img_name=f"trap_{trap_num}_down", script_name=script_name, threshold=down_threshold, max_wait_sec=2):
        set_needs_reset(trap_num)

    elif wait_for_img(img_name=f"trap_{trap_num}_pickup", script_name=script_name, threshold=reset_threshold, max_wait_sec=2):
        set_needs_reset(trap_num)

    return


def set_needs_reset(trap_num):
    global needs_reset_1
    global needs_reset_2

    if trap_num == 1:
        needs_reset_1 = True
    else:
        needs_reset_2 = True
    return


def high_alch():
    is_tab_open("magic", should_open=True)
    API.AntiBan.sleep_between(0.3, 0.5)
    does_img_exist(img_name="high_alch", script_name="Seers_Rooftops", should_click=True)
    API.AntiBan.sleep_between(0.4, 0.8)
    if not does_img_exist(img_name="magic_long_note", script_name="Seers_Rooftops", x_offset=4, y_offset=4, should_click=True):
        pag.leftClick()
    API.AntiBan.sleep_between(0.4, 0.83)
    return
