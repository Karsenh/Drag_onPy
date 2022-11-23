from API.AntiBan import *
from API.Imaging.Image import *
from API.Mouse import *
import pyautogui as pag
import keyboard
from API.Import_Libs.Coords import *
import math


compass_xy = 1210, 70
inventory_x, inventory_y = 1447, 403


def turn_compass(direction="south", DEBUG=False):
    global compass_xy

    match direction:
        case "north":
            if DEBUG:
                print(f'Turning compass: {direction} - Moving to {compass_xy}')
            xy = 1211, 72
            mouse_click(xy)
            return
        case "east":
            dir_xy = 1200, 172
        case "south":
            dir_xy = 1213, 217
        case "west":
            dir_xy = 1208, 254
        case _:
            print(f'ERROR: Direction {direction} not valid case.')
    if DEBUG:
        print(f'Turning compass: {direction} - Moving to {dir_xy}')
    # Move mouse to compass & click down
    mouse_move(compass_xy)
    pag.mouseDown()
    # Translate the relative coordinates of the direction x, y for dragTo()
    trans_x, trans_y = translate_coords(dir_xy, update_coords=True)
    r_dur = random.uniform(0.5, 0.74)
    pag.dragTo(trans_x, trans_y, duration=r_dur)
    return


def pitch_camera(direction="up"):
    print(f'Angling camera {direction}')
    center_viewport_xy = 730, 436
    mouse_move(center_viewport_xy, 33, 47)
    sleep_between(0.5, 1.1)
    pag.hscroll(200)
    return


def zoom_camera(notches=1):
    # degrees: 1-5 (notches on zoom bar in Runescape mobile settings tab)
    # Check if Settings tab is open (open if not)
    # Check if Settings > mobile tab is selected (select if not)
    notch_y_axis = 560
    notch_1 = 1187, notch_y_axis
    notch_2 = 1227, notch_y_axis
    notch_3 = 1267, notch_y_axis
    notch_4 = 1307, notch_y_axis
    notch_5 = 1344, notch_y_axis

    notch_list = [notch_1, notch_2, notch_3, notch_4, notch_5]
    index = notches - 1

    check_if_tab_open("settings")

    mouse_click(notch_list[index], 0, 0)

    sleep_between(0.3, 0.7)

    mouse_click(INVENT_tab_xy)

    return


def drop_inventory(from_spot_num=1, to_spot_num=27):
    # Open inventory if not open
    check_if_tab_open("inventory", should_open=True)
    check_one_tap_drop_enabled(should_enable=True)

    for i in range(from_spot_num, to_spot_num+1):
        mouse_click(get_xy_for_invent_slot(i))

    return


# --- COLOR MATCHING ---
def check_if_tab_open(tab="inventory", should_open=True):
    open_tab_color = 106, 35, 26

    match tab:
        case "inventory":
            check_tab_xy = INVENT_tab_xy
        case "settings":
            check_tab_xy = SETTINGS_tab_xy
        case "skill":
            check_tab_xy = SKILL_tab_xy
        case "quest":
            check_tab_xy = QUEST_tab_xy

    print(f'Check_tab_xy = {check_tab_xy}')

    is_open = does_color_exist(open_tab_color, check_tab_xy)

    if not is_open:
        if should_open:
            mouse_click(check_tab_xy)
            is_open = True
    else:
        if not should_open:
            mouse_click(check_tab_xy)
            is_open = False

    return is_open


def check_if_bank_tab_open(tab_num=0, should_open=True, double_check=True):
    if does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
        if not should_open:
            mouse_click(BANK_all_tab_xys[tab_num])
            # Check for tab again after clicking (if double check is true)
            if double_check:
                if not does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
                    print(f"Couldn't find expected tab no. {tab_num} despite having tried to click... Exiting")
                    # Print this issue to log file
                    log_text = f"Couldn't find Bank Tab {tab_num} after trying to click it."
                    print_to_log(log_text)
                    exit(-1)
    else:
        if should_open:
            mouse_click(BANK_all_tab_xys[tab_num])
            # Check for tab again after clicking (if double check is true)
            if double_check:
                if not does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
                    print(f"Couldn't find expected tab no. {tab_num} despite having tried to click... Exiting")
                    # Print this issue to log file
                    log_text = f"Couldn't find Bank Tab {tab_num} after trying to click it."
                    print_to_log(log_text)
                    exit(-1)

    return


def check_one_tap_drop_enabled(should_enable=True):
    enabled_color = 202, 42, 42
    otd_loc = 39, 348
    if does_color_exist(enabled_color, otd_loc):
        print(f'✔ OTD Enabled')
        if not should_enable:
            print(f'Disabling...')
            keyboard.press('space')
            xy = 48, 340
            mouse_click(xy)
        return True
    else:
        print(f'✖ OTD NOT Enabled')
        if should_enable:
            print(f'Enabling...')
            keyboard.press('space')
            xy = 48, 340
            mouse_click(xy)
        return False


# --- IMAGE MATCHING ---
def is_on_dc_screen(should_cont=True):
    img_found = does_img_exist("disconnected", category="Auth")

    if img_found and should_cont:
        xy = 755, 555
        mouse_click(xy)
        sleep_between(3.0, 3.1)

    return img_found


def is_on_login_screen(should_cont=True):
    img_found = does_img_exist("login_screen", category="Auth")

    if img_found and should_cont:
        xy = 753, 471
        mouse_click(xy, 67, 23)
        sleep_between(7.0, 7.1)

    return img_found


def is_on_welcome_screen(should_cont=True):
    img_found = does_img_exist("welcome_screen", category="Auth")

    if img_found and should_cont:
        xy = 755, 593
        mouse_click(xy, 54, 34)
        sleep_between(1.0, 1.3)

    return img_found


def is_inventory_full(should_cont=True, should_drop=True, start_slot=1, end_slot=27):
    does_exist = does_img_exist("inventory_full", category="General")

    if does_exist and should_cont:
        pyautogui.press('space')
        r_sleep = random.uniform(1.0, 1.2)
        time.sleep(r_sleep)
        if should_drop:
            drop_inventory(start_slot, end_slot)

    return does_exist


def is_on_right_tile(obj_xys, obj_colors):
    checks = []
    curr_index = 0

    for obj in obj_xys:
        check = does_color_exist(obj_colors[curr_index], obj)
        checks.append(check)
        curr_index += 1

    if not all(checks):
        print(f'⛔ At least one check failed for correct tile.')
        i = 0
        for check in checks:
            i += 1
            if not check:
                print(f'Check_{i}: ❌')
            else:
                print(f'Check_{i}: ✔')
        return False
    else:
        print(f'✅ Still on correct tile.')
        i = 0
        for check in checks:
            i += 1
            if not check:
                print(f'Check_{i}: ❌')
            else:
                print(f'Check_{i}: ✔')
        return True


def get_xy_for_invent_slot(slot_num):
    # find out the
    col = slot_num % 4   # total number of cols
    if col == 0:
        col = 4
    row = math.ceil(slot_num / 4) # total number of rows

    print(f'Slot [{slot_num}] Col = {col} & Row = {row}')

    if col == 1:
        x_offset = 0
    else:
        x_offset = INVENT_slot_x_step * (col - 1)
    if row == 1:
        y_offset = 0
    else:
        y_offset = INVENT_slot_y_step * (row - 1)

    slot_1_x, slot_1_y = INVENT_slot_1

    return slot_1_x + x_offset, slot_1_y + y_offset


def check_skill_tab(max_sec=2.0, skill_to_check='random'):
    # check skill passed in as arg
    start = time.time()
    print(f'start: {start}')
    check_if_tab_open("skill", should_open=True)
    print(f'skill tab: {SKILL_tab_xy}')
    # check_if_tab_open("skill", should_open=True)
    sleep_between(0.4, 1.3)
    if max_sec >= 2.0:
        diff = max_sec - 1.3
        print(f'smithing skill {SKILL_smithing}')
        match skill_to_check:
            case "smithing":
                skill_to_check_xy = SKILL_smithing
        mouse_click(skill_to_check_xy)
        sleep_between(1, diff)
    # check_skills(max_sec)

    check_if_tab_open("inventory", should_open=True)
    end = time.time()
    print(f'end: {end}')
    elapsed_time = start - end
    print(f'elapsed time: {elapsed_time}')
    remaining_time = max_sec - elapsed_time
    print(f'remaining time: {remaining_time}')
    time.sleep(remaining_time)
    return
