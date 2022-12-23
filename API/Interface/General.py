from API.Imaging.Image import does_img_exist, does_color_exist, get_color_at_coords, wait_for_img
from API.Mouse import *
from API.Imports.Coords import *
from API.Debug import DEBUG_MODE, write_debug
import API.AntiBan
import pyautogui as pag
import math


compass_xy = 1210, 70
inventory_x, inventory_y = 1447, 403


def setup_interface(cam_dir="north", cam_distance=3, cam_angle="up"):
    turn_compass(direction=cam_dir)
    API.AntiBan.sleep_between(0.6, 0.9)
    zoom_camera(notches=cam_distance)
    API.AntiBan.sleep_between(0.6, 0.9)
    pitch_camera(direction=cam_angle)
    return


def turn_compass(direction="south"):
    global compass_xy

    if direction == "north":
        mouse_click(compass_xy)
    else:
        mouse_long_click(compass_xy)
        API.AntiBan.sleep_between(0.3, 1.1)
        if not wait_for_img(img_name=f"compass_{direction}", category="Interface", should_click=True, threshold=0.90):
            return False

    return True


def pitch_camera(direction="up"):
    print(f'Angling camera {direction}')
    center_viewport_xy = 730, 436
    mouse_move(center_viewport_xy, 33, 47)
    API.AntiBan.sleep_between(0.5, 1.1)
    if direction == "up":
        pag.hscroll(200)
    else:
        pag.hscroll(-200)
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

    is_tab_open("settings")

    mouse_click(notch_list[index], 0, 0)

    API.AntiBan.sleep_between(0.3, 0.7)

    mouse_click(INVENT_tab_xy)

    return


def drop_inventory(from_spot_num=1, to_spot_num=27, should_random_skip=False, should_close_after=False, should_disable_otd_after=False):
    # Open inventory if not open
    is_tab_open("inventory", should_open=True)
    is_otd_enabled(should_enable=True)

    API.AntiBan.sleep_between(1.4, 1.9)

    for i in range(from_spot_num, to_spot_num+1):
        mouse_click(get_xy_for_invent_slot(i))
        if i % 4 == 0:
            API.AntiBan.sleep_between(0.3, 0.7)

    if should_disable_otd_after:
        is_otd_enabled(should_enable=False)

    if should_close_after:
        API.AntiBan.sleep_between(0.8, 1.1)
        is_tab_open("inventory", should_open=False)

    return


# --- COLOR MATCHING ---
def is_tab_open(tab="inventory", should_open=True):
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
        case "magic":
            check_tab_xy = MAGIC_tab_xy

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


# One-tap-drop mode on mobile
def is_otd_enabled(should_enable=True):
    enabled_color = 202, 42, 42
    otd_loc = 39, 348
    if does_color_exist(enabled_color, otd_loc):
        print(f'✔ OTD Enabled')
        if not should_enable:
            print(f'Disabling...')
            pag.press('space')
            xy = 48, 340
            mouse_click(xy)
        return True
    else:
        print(f'✖ OTD NOT Enabled')
        if should_enable:
            print(f'Enabling...')
            pag.press('space')
            xy = 48, 340
            mouse_click(xy)
        return False


def is_run_on(should_click=False):
    run_check_xy = 1210, 255
    run_rgb = get_color_at_coords(run_check_xy)
    run_on_color = 236, 218, 103
    run_off_color = 145, 100, 59
    if run_rgb == run_on_color:
        print(f'🥾 ✔ Run is ON with RGB: {run_rgb}')
        return True
    if run_rgb == run_off_color:
        print(f'🥾 ❌ Run is OFF with RGB: {run_rgb}')
        if should_click:
            run_xy = 1206, 248
            mouse_click(run_xy)
        return False
    else:
        print(f'❌ Color: {run_rgb} not detected for 🥾 run energy.')
        return False


def is_run_gt(percent=10):
    off_color = 14, 14, 14

    if percent <= 10:
        xy = 1215, 265
        message = '12 percent.'

    color_at_coords = get_color_at_coords(xy)
    if color_at_coords < off_color:
        print(f'Run energy < {message}')
        return False
    else:
        print(f'Run energy >= {message}')
        return True


# --- IMAGE MATCHING ---
def is_inventory_full(should_cont=True, should_drop=False, start_slot=1, end_slot=27, should_close_after=False):
    does_exist = does_img_exist("inventory_full", category="General"), does_img_exist("inventory_full_fish", category="General")

    write_debug(f'is_inventory_full does_exist: {does_exist}')

    if any(does_exist):
        if should_cont:
            pag.press('space')
            r_sleep = random.uniform(1.0, 1.2)
            time.sleep(r_sleep)
        if should_drop:
            drop_inventory(start_slot, end_slot, should_close_after)
        return True

    else:
        return False


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
    write_debug(f'Start time: {start}\nOpening Skill tab')
    is_tab_open("skill", should_open=True)
    write_debug(f'skill tab: {SKILL_tab_xy}')
    is_tab_open("skill", should_open=True)
    API.AntiBan.sleep_between(0.4, 1.3)
    if max_sec >= 2.0:
        diff = max_sec - 1.3
        print(f'smithing skill {SKILL_smithing}')
        if skill_to_check == "random":
            skill_to_check = random.randint(1, 5)
            match skill_to_check:
                case 1:
                    skill_to_check_xy = SKILL_smithing
                    write_debug(f'{skill_to_check_xy}')
                case 2:
                    skill_to_check_xy = SKILL_fishing
                    write_debug(f'{skill_to_check_xy}')
                case 3:
                    skill_to_check_xy = SKILL_agility
                    write_debug(f'{skill_to_check_xy}')
                case 4:
                    skill_to_check_xy = SKILL_attack
                    write_debug(f'{skill_to_check_xy}')
                case 5:
                    skill_to_check_xy = SKILL_defence
                    write_debug(f'{skill_to_check_xy}')
                case 6:
                    skill_to_check_xy = SKILL_strength
                    write_debug(f'{skill_to_check_xy}')
        else:
            match skill_to_check:
                case "smithing":
                    skill_to_check_xy = SKILL_smithing
                case "fishing":
                    skill_to_check_xy = SKILL_fishing
        mouse_click(skill_to_check_xy)
        API.AntiBan.sleep_between(1, diff)

    is_tab_open("inventory", should_open=True)
    end = time.time()
    print(f'end: {end}')
    elapsed_time = start - end
    print(f'elapsed time: {elapsed_time}')
    remaining_time = max_sec - elapsed_time
    print(f'remaining time: {remaining_time}')
    time.sleep(remaining_time)
    return


def is_on_dc_screen(should_cont=True):
    if wait_for_img(img_name="disconnected_screen", category="Auth", threshold=0.85) and should_cont:
        xy = 755, 555
        mouse_click(xy)
        return True

    return False


def is_on_login_screen(should_cont=True):
    if wait_for_img(img_name="login_screen", category="Auth", threshold=0.85) and should_cont:
        xy = 753, 471
        mouse_click(xy, 67, 23)
        return True

    return False


def is_on_welcome_screen(should_cont=True):
    if wait_for_img(img_name="welcome_screen", category="Auth", threshold=0.85) and should_cont:
        xy = 755, 593
        mouse_click(xy, 54, 34)
        return True

    return False


def handle_auth_screens():

    if does_img_exist(img_name="disconnected_screen", category="Auth", threshold=0.85):
        if is_on_dc_screen():
            if is_on_login_screen():
                if is_on_welcome_screen():
                    return True

    elif does_img_exist(img_name="login_screen", category="Auth", threshold=0.85):
        if is_on_login_screen():
            if is_on_welcome_screen():
                return True

    elif does_img_exist(img_name="welcome_screen", category="Auth", threshold=0.85):
        if is_on_welcome_screen():
            return True

    else:
        return False


def toggle_public_chat(state="on"):
    public_chat_xy = 291, 59
    match state:
        case "off":
            sel_state_xy = 283, 285
        case "on":
            sel_state_xy = 293, 201
    mouse_drag(from_xy=public_chat_xy, to_xy=sel_state_xy)
    return
