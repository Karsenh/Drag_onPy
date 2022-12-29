import API.AntiBan
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist
from API.Mouse import mouse_click
import pyautogui as pag
from API.Debug import write_debug

script_name = "Double_Trap_Ceruleans"

should_reset_traps = False
bird_type = "cerulean"

monitor_tile_from_trap_1 = 810, 740
monitor_tile_from_trap_2 = 811, 424

trap_tile_1 = 849, 404
trap_tile_2 = 846, 749

needs_reset_1 = False
needs_reset_2 = False

# 92 on dt
caught_threshold = 0.91
caught_threshold_from_drop = 0.94
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
        is_otd_enabled(should_enable=False)
        set_initial_traps()

    i = 0
    while not should_reset_traps:
        i += 1
        write_debug(f'👀 While not should_reset_traps executed {i} time(s) - Checking traps...')
        if check_should_reset_traps():
            write_debug(f'✔ should_reset_traps flipped to TRUE')
            should_reset_traps = True

        else:
            write_debug(f"🧿 should_reset_traps = False. Dropping bird shit...")
            drop_bird_shit()
            # high_alch()

    # Reset traps that need it
    handle_trap_state()
    should_reset_traps = False
    i = 0
    print(f'🧿 Traps handled. should_reset_traps = False again - Exiting main...')

    return True


# ----------------
# INTERNAL METHODS:
# ----------------
def set_initial_traps():
    global monitor_tile_from_trap_2
    trap_2_from_1_xy = 869, 798

    does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True, x_offset=5, y_offset=5)

    if wait_for_img(img_name="trap_1_set", script_name=script_name):
        mouse_click(trap_2_from_1_xy)
        API.AntiBan.sleep_between(2.0, 2.1)
        does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True, x_offset=5, y_offset=5)

        if wait_for_img(img_name="trap_2_set", script_name=script_name):
            API.AntiBan.sleep_between(0.7, 0.8)
            mouse_click(monitor_tile_from_trap_2)

    return


def check_should_reset_traps():
    global last_reset_trap_num

    if last_reset_trap_num == 2:
        write_debug(f"Last trap was 2 - Checking 1 first...")
        if check_trap_num(1):
            write_debug(f"✔ Check_trap_num(1) returned true - skipping other checks to handle")
            return True
        if check_trap_num(2):
            write_debug(f"🧿 Trap 2 needs reset - double checking Trap 1...")
            check_trap_num(1)
    else:
        if check_trap_num(2):
            write_debug(f"✔ Check_trap_num(2) returned true - skipping other checks to handle")
            return True
        if check_trap_num(1):
            write_debug(f"🧿 Trap 1 needs reset - double checking Trap 2...")
            check_trap_num(2)

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
        print(f'🧿 Both traps need to be reset')
        if reset_trap_num(1):
            # Since both traps need replacing, click trap 2 from here
            if reset_trap_two_from_one():
                # Move back to monitor tile and begin checking trap status'
                move_back_to_monitor(from_tile=2)
                needs_reset_1 = False
                needs_reset_2 = False
                last_reset_trap_num = 2
            else:
                print(f'reset_trap_from_one in handle_trap_state() is fucked.')
        else:
            write_debug(f"⛔ Couldn't reset trap one & therefore didn't try two...")

    else:
        # Check individually
        if needs_reset_1:
            print(f'Only trap ONE needs resetting')
            reset_trap_num(1)
            # Move back to monitor tile
            # mouse_click(monitor_tile_from_trap_1)
            move_back_to_monitor(from_tile=1)

            needs_reset_1 = False
            last_reset_trap_num = 1

        if needs_reset_2:
            print(f'Only trap TWO needs resetting')
            reset_trap_num(2)
            # mouse_click(monitor_tile_from_trap_2)
            move_back_to_monitor(from_tile=2)

            needs_reset_2 = False
            last_reset_trap_num = 2

    # API.AntiBan.sleep_between(2.0, 2.1)

    return True


# ---------
# HELPERS
# ---------
def reset_trap_num(trap_num=1):
    # If we're in here - one or both flags are True
    global trap_tile_1
    global trap_tile_2

    match trap_num:
        case 1:
            trap_tile_xy = trap_tile_1
        case 2:
            trap_tile_xy = trap_tile_2

    is_tab_open("inventory", True)

    # Check for CAUGHT trap separately - might need to empty invent
    if wait_for_img(img_name=f"trap_{trap_num}_caught", script_name=script_name, threshold=caught_threshold):
        API.AntiBan.sleep_between(0.4, 0.5)
        # Click caught bird trap to dismantle...
        wait_for_img(img_name=f"trap_{trap_num}_caught", script_name=script_name, threshold=caught_threshold, y_offset=6, x_offset=4, should_click=True)

        # Wait for hunter exp (trap harvest)...
        if wait_for_img(img_name="hunter_exp", script_name=script_name):
            # Clicking the tile we want to set trap ONE on
            mouse_click(trap_tile_xy)
            API.AntiBan.sleep_between(1.2, 1.3)
            # Clicking a trap to set
            does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
            # API.AntiBan.sleep_between(5.0, 5.1)
            return True

        # Trap not harvested - most likely full inventory
        else:
            # Drop bird shit to make inventory space & try to set the trap again from current tile
            drop_bird_shit()
            # Click trap reset tile to try picking up trap again after making inventory space
            does_img_exist(img_name=f"trap_{trap_num}_from_drop_invent", script_name="Double_Trap_Ceruleans", threshold=caught_threshold_from_drop, should_click=True, y_offset=5)
            API.AntiBan.sleep_between(2.0, 2.1)
            # Move to trap reset tile
            mouse_click(trap_tile_xy)
            API.AntiBan.sleep_between(2.1, 2.3)
            # Clicking a trap to set
            does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
            # API.AntiBan.sleep_between(5.0, 5.1)
            return True

    # Check for DOWN - no need to empty inventory here
    elif does_img_exist(img_name=f"trap_{trap_num}_down", script_name=script_name, threshold=down_threshold, should_click=True, x_offset=9, y_offset=6):
        API.AntiBan.sleep_between(3.0, 3.1)
        # After picking up the downed trap - move to the tile to reset another
        mouse_click(trap_tile_xy)
        API.AntiBan.sleep_between(1.2, 1.3)
        # Clicking a trap to set
        does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(5.0, 5.1)
        return True

    # Check for trap PICKUP and click a single time - we'll move directly to the trap tile
    elif does_img_exist(img_name=f"trap_{trap_num}_pickup", script_name=script_name, threshold=reset_threshold, should_click=True):
        API.AntiBan.sleep_between(3.0, 3.1)
        does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(5.0, 5.1)
        return True

    print(f"⛔ Didn't find trap_{trap_num}_caught / down / reset. Returning False")
    return False


def reset_trap_two_from_one():
    print(f'🧿 Reset_trap_two_from_one fired...')
    if wait_for_img(img_name=f"trap_2_caught_from_1", script_name=script_name, threshold=0.90, should_click=True, max_wait_sec=2):
        print(f'✔ Trap_2_Caught_from_1 found!')
        # API.AntiBan.sleep_between(5.0, 5.1)
        # Click the tile we want to set trap TWO on
        if wait_for_img(img_name="hunter_exp", script_name=script_name, max_wait_sec=8):
            # Clicking the tile we want to set trap ONE on
            mouse_click(trap_tile_2)
            API.AntiBan.sleep_between(2.0, 2.1)
            # Set new trap TWO
            does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
            API.AntiBan.sleep_between(5.0, 5.1)
        else:
            drop_bird_shit()
            mouse_click(trap_tile_2)
            API.AntiBan.sleep_between(3.0, 3.1)
            # Set new trap TWO
            does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
            API.AntiBan.sleep_between(5.0, 5.1)
        return True
    elif wait_for_img(img_name=f"trap_2_down_from_1", script_name=script_name, threshold=0.9, should_click=True, x_offset=5, y_offset=4, max_wait_sec=2):
        print(f'✔ Trap two seen needing RESET from trap 2 down. Clicking...')
        API.AntiBan.sleep_between(5.0, 5.1)
        # Click the tile we want to set trap TWO on
        mouse_click(trap_tile_2)
        API.AntiBan.sleep_between(2.0, 2.1)
        # Set new trap TWO
        does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(5.0, 5.1)
        return True
    elif does_img_exist(img_name=f"trap_2_pickup_from_1", script_name=script_name, threshold=0.9, should_click=True):
        print(f'✔ Trap two seen needing PICKUP from trap 1 reset. Clicking...')
        API.AntiBan.sleep_between(4.0, 4.1)
        does_img_exist(img_name="inventory_trap", script_name=script_name, should_click=True)
        API.AntiBan.sleep_between(5.0, 5.1)
        return True

    print(f'⛔ Reset_Trap_Two_From_One didnt find any trap on 2 despite both flags being True')
    return False


def check_trap_num(trap_num):

    write_debug(f'🧿 Check_trap_num {trap_num} fired.')

    if does_img_exist(img_name=f"trap_{trap_num}_caught", script_name=script_name, threshold=caught_threshold):
        set_needs_reset(trap_num)
        write_debug(f"✔ Found CAUGHT for trap: {trap_num} - Needs reset = True")
        return True

    elif does_img_exist(img_name=f"trap_{trap_num}_down", script_name=script_name, threshold=down_threshold):
        set_needs_reset(trap_num)
        write_debug(f"✔ Found DOWN for trap: {trap_num} - Needs reset = True")
        return True

    elif does_img_exist(img_name=f"trap_{trap_num}_pickup", script_name=script_name, threshold=reset_threshold):
        set_needs_reset(trap_num)
        write_debug(f"✔ Found PICKUP for trap: {trap_num} - Needs reset = True")
        return True

    return False


def drop_bird_shit():


    is_tab_open("inventory", True)
    API.AntiBan.sleep_between(0.5, 0.7)

    if does_img_exist(img_name="drop_1", script_name="Bird_Catcher", threshold=0.9) or does_img_exist(img_name="drop_2", script_name="Bird_Catcher"):
        is_otd_enabled(should_enable=True)
        API.AntiBan.sleep_between(0.4, 0.6)

    while does_img_exist(img_name="drop_1", script_name="Bird_Catcher", should_click=True,
                         threshold=0.9) or \
            does_img_exist(img_name="drop_2", script_name="Bird_Catcher", should_click=True):
        print(f'Dropping bird shit from inventory...')

    API.AntiBan.sleep_between(0.4, 0.5)
    is_otd_enabled(False)
    API.AntiBan.sleep_between(0.4, 0.5)
    return


def set_needs_reset(trap_num):
    global needs_reset_1
    global needs_reset_2

    if trap_num == 1:
        needs_reset_1 = True
    else:
        needs_reset_2 = True
    return


def move_back_to_monitor(from_tile):
    if from_tile == 1:
        monitor_tile_xy = monitor_tile_from_trap_1
    else:
        monitor_tile_xy = monitor_tile_from_trap_2

    if wait_for_img(img_name=f"trap_{from_tile}_set", script_name=script_name):
        API.AntiBan.sleep_between(0.7, 0.8)
        mouse_click(monitor_tile_xy)
        if not wait_for_img(img_name=f"monitor_tile_signal_from_{from_tile}", script_name="Double_Trap_Ceruleans", threshold=0.85,
                            max_wait_sec=6):
            write_debug(f"❌ Couldn't find monitor_tile_signal_from_{from_tile} after trying to click there - clicking tile again.")
            mouse_click(monitor_tile_xy)
        else:
            write_debug(f"🧿 We're back on Monitor tile from trap {from_tile}")

    else:
        write_debug(f"⛔ move_back_to_monitor couldn't find trap_{from_tile}_set image. Why?")
        mouse_click(monitor_tile_xy)
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
