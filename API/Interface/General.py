import random
from API.Imaging.Image import does_img_exist, does_color_exist, get_color_at_coords, wait_for_img, does_color_exist_in_thresh, does_color_exist_in_sub_image
from API.Mouse import *
from API.Imports.Coords import *
from API.Debug import DEBUG_MODE, write_debug
import API.AntiBan
import pyautogui as pag
import math


compass_xy = 1210, 70
inventory_x, inventory_y = 1447, 403


def relog():
    is_tab_open('logout', True)
    r_value = random.randint(1, 2)
    should_thumb_up = r_value == 2

    if should_thumb_up:
        does_img_exist(img_name='logout_thumbs_up', category='interface', threshold=0.9, should_click=True, click_middle=True)

    does_img_exist(img_name='tap_to_logout', category='interface', threshold=0.9, should_click=True, click_middle=True)

    if not wait_for_img(img_name='login_screen', category='Auth', threshold=0.9, max_wait_sec=15):
        return False

    handle_auth_screens()
    return


def setup_interface(cam_dir="north", cam_distance=3, cam_angle="up"):
    close_chatbox
    turn_compass(direction=cam_dir)
    API.AntiBan.sleep_between(0.5, 0.9)
    zoom_camera(notches=cam_distance)
    API.AntiBan.sleep_between(0.6, 0.9)
    pitch_camera(direction=cam_angle)
    API.AntiBan.sleep_between(0.3, 0.4)
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

    wait_for_img(img_name="mobile_settings_tab", category="Interface", should_click=True)
    API.AntiBan.sleep_between(0.4, 0.6)

    mouse_click(notch_list[index], 0, 0)

    API.AntiBan.sleep_between(0.3, 0.7)

    mouse_click(INVENT_tab_xy)

    return


def drop_inventory(from_spot_num=1, to_spot_num=27, should_random_skip=False, should_close_after=False, should_disable_otd_after=False):
    # Open inventory if not open
    is_tab_open("inventory", should_be_open=True)
    is_otd_enabled(should_enable=True)

    API.AntiBan.sleep_between(1.4, 1.9)

    for i in range(from_spot_num, to_spot_num+1):
        mouse_click(get_xy_for_invent_slot(i))
        if i % 4 == 0:
            API.AntiBan.sleep_between(0.25, 0.55)

    if should_disable_otd_after:
        is_otd_enabled(should_enable=False)

    if should_close_after:
        API.AntiBan.sleep_between(0.8, 1.1)
        is_tab_open("inventory", should_be_open=False)

    return


# --- COLOR MATCHING ---
def is_tab_open(tab="inventory", should_be_open=True):
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
        case "equipment":
            check_tab_xy = EQUIPMENT_tab_xy
        case "combat":
            check_tab_xy = COMBAT_tab_xy
        case "logout":
            check_tab_xy = LOGOUT_tab_xy

    print(f'is_tab_open fired for {tab} = {check_tab_xy}')

    is_open = does_color_exist_in_thresh(check_tab_xy, open_tab_color, 15)

    if not is_open:
        if should_be_open:
            mouse_click(check_tab_xy)
            is_open = True
    else:
        if not should_be_open:
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
            API.AntiBan.sleep_between(0.3, 0.4)
        return True
    else:
        print(f'✖ OTD NOT Enabled')
        if should_enable:
            print(f'Enabling...')
            pag.press('space')
            xy = 48, 340
            mouse_click(xy)
            API.AntiBan.sleep_between(0.3, 0.4)
        return False


def is_run_on(should_click=False):
    run_region_coords = 1190, 230, 1230, 278
    run_on_yellow_color = 205, 167, 1

    if does_color_exist_in_sub_image(run_region_coords, run_on_yellow_color, 'Run_On_Check', count_min=100, color_tolerance=22):
        print(f'🏃‍♂️ON!')
        return True
    else:
        print(f'🏃‍♂️OFF!')
        if should_click:
            run_xy = 1206, 248
            mouse_click(run_xy)
        return does_color_exist_in_sub_image(run_region_coords, run_on_yellow_color, 'Run_On_Check', count_min=100, color_tolerance=22)


def is_run_gt(percent=10):
    off_color = 14, 14, 14

    # ToDo finish out all the xy coords for color checks

    if percent <= 9:
        xy = 1215, 265
        message = '12 percent.'
    elif percent >= 10 and percent < 19:
        message = '10-19 % hp'
    elif percent >= 20 and percent < 29:
        message = '20 - 29 % hp'
    elif percent >= 30 and percent < 39:
        message = '30 - 39 %'
    elif percent >= 40 and percent < 49:
        message = '40 - 49 %'
    elif percent >= 50 and percent < 59:
        message = '50 - 59 %'
    elif percent >= 60 and percent < 69:
        message = '60 - 39 %'
    elif percent >= 30 and percent < 69:
        message = '30 - 39 %'
    elif percent >= 70 and percent < 79:
        message = '70 - 79 %'
    elif percent >= 80 and percent < 89:
        message = '80 - 89 %'
    elif percent >= 90 and percent < 99:
        xy = 1188, 122
        message = '80 - 89 %'
    else:
        message = '100% health'

    color_at_coords = get_color_at_coords(xy)
    if color_at_coords < off_color:
        print(f'Run energy < {message}')
        return False
    else:
        print(f'Run energy >= {message}')
        return True


def is_hp_gt(percent=50):
    ninety_percent_xy = 1190, 125
    half_hp_xy = 1175, 138
    ten_percent_xy = 1184, 154

    health_black_color = 19, 19, 19
    health_red_color = 161, 6, 3

    match percent:
        case 90:
            check_xy = ninety_percent_xy
        case 50:
            check_xy = half_hp_xy
        case 10:
            check_xy = ten_percent_xy

    print(f'is_hp_gt(percent={percent}) : {get_color_at_coords(check_xy) > health_black_color}')
    return get_color_at_coords(check_xy) > health_black_color


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


def check_skill_tab(max_sec=2.0, skill_to_check='random', should_reopen_inventory=True):
    # check skill passed in as arg
    start = time.time()
    write_debug(f'Start time: {start}\nOpening Skill tab')
    is_tab_open("skill", should_be_open=True)
    write_debug(f'skill tab: {SKILL_tab_xy}')
    # is_tab_open("skill", should_be_open=True)
    API.AntiBan.sleep_between(0.4, 1.3)

    skills_array = [
        SKILL_XY_ATTACK,
        SKILL_XY_STRENGTH,
        SKILL_XY_DEFENSE,
        SKILL_XY_RANGE,
        SKILL_XY_PRAYER,
        SKILL_XY_MAGIC,
        SKILL_XY_RC,
        SKILL_XY_CON,
        SKILL_XY_HP,
        SKILL_XY_AGILITY,
        SKILL_XY_HERBLORE,
        SKILL_XY_THIEVING,
        SKILL_XY_CRAFTING,
        SKILL_XY_FLETCHING,
        SKILL_XY_SLAYER,
        SKILL_XY_HUNTER,
        SKILL_XY_MINING,
        SKILL_XY_SMITHING,
        SKILL_XY_FISHING,
        SKILL_XY_COOKING,
        SKILL_XY_FIREMAKING,
        SKILL_XY_WOODCUTTING,
        SKILL_XY_FARMING
    ]

    if max_sec >= 2.0:
        diff = max_sec - 1.3
        if skill_to_check.lower() == "random":
            skill_num = random.randint(0, 22)
            skill_to_check = skills_array[skill_num]
            write_debug(f'Skill to check: {skill_to_check}')
        else:
            match skill_to_check.lower():
                case "attack":
                    skill_num = 0
                case "strength":
                    skill_num = 1
                case "defense":
                    skill_num = 2
                case "range":
                    skill_num = 3
                case "prayer":
                    skill_num = 4
                case "magic":
                    skill_num = 5
                case "rc":
                    skill_num = 6
                case "con":
                    skill_num = 7
                case "hp":
                    skill_num = 8
                case "agility":
                    skill_num = 9
                case "herblore":
                    skill_num = 10
                case "thieving":
                    skill_num = 11
                case "crafting":
                    skill_num = 12
                case "slayer":
                    skill_num = 13
                case "hunter":
                    skill_num = 14
                case "mining":
                    skill_num = 15
                case "smithing":
                    skill_num = 16
                case "fishing":
                    skill_num = 17
                case "cooking":
                    skill_num = 18
                case "firemaking":
                    skill_num = 19
                case "woodcutting":
                    skill_num = 20
                case "farming":
                    skill_num = 21

        skill_to_check = skills_array[skill_num]
        write_debug(f'Skill to check: {skill_to_check}')

        mouse_click(skill_to_check)
        if diff < 1:
            API.AntiBan.sleep_between(0.2, 0.3)
        else:
            API.AntiBan.sleep_between(1, diff)

    is_tab_open("inventory", should_be_open=should_reopen_inventory)
    if not should_reopen_inventory:
        is_tab_open("skill", should_be_open=False)

    end = time.time()
    print(f'end: {end}')
    elapsed_time = start - end
    print(f'elapsed time: {elapsed_time}')
    remaining_time = max_sec - elapsed_time
    print(f'remaining time: {remaining_time}')
    # time.sleep(remaining_time)
    return


def is_on_dc_screen(should_cont=True):
    if wait_for_img(img_name="disconnected_screen", category="Auth", threshold=0.85, max_wait_sec=15) and should_cont:
        xy = 755, 555
        mouse_click(xy)
        return True

    return False


def is_on_login_screen(should_cont=True):
    if wait_for_img(img_name="login_screen", category="Auth", threshold=0.85, max_wait_sec=15) and should_cont:
        xy = 753, 471
        mouse_click(xy, 67, 23)
        return True

    return False


def is_on_welcome_screen(should_cont=True):
    if wait_for_img(img_name="welcome_screen", category="Auth", threshold=0.85, max_wait_sec=15, ) and should_cont:
        xy = 755, 593
        mouse_click(xy, 54, 34)
        return True

    return False


def handle_auth_screens():

    if does_img_exist(img_name="disconnected_screen", category="Auth", threshold=0.85):
        if is_on_dc_screen():
            if is_on_login_screen():
                if is_on_welcome_screen():
                    API.AntiBan.sleep_between(1.0, 1.1)
                    print(f'1 Relogged and returning True from Handle_Auth_Screen()')
                    return True

    elif does_img_exist(img_name="login_screen", category="Auth", threshold=0.85):
        if is_on_login_screen():
            if is_on_welcome_screen():
                API.AntiBan.sleep_between(1.0, 1.1)
                print(f'2 Relogged and returning True from Handle_Auth_Screen()')
                return True

    elif does_img_exist(img_name="welcome_screen", category="Auth", threshold=0.85):
        if is_on_welcome_screen():
            API.AntiBan.sleep_between(1.0, 1.1)
            print(f'3 Relogged and returning True from Handle_Auth_Screen()')
            return True

    else:
        print(f'Returning False from Handle_Auth_Screens')
        return False


def toggle_public_chat(state="on"):
    public_chat_xy = 291, 59
    mouse_long_click(public_chat_xy)

    match state:
        case "off":
            does_img_exist(img_name='show_none', category='Interface', threshold=0.9, should_click=True, click_middle=True)
        case "on":
            does_img_exist(img_name='show_standard', category='Interface', threshold=0.9, should_click=True, click_middle=True)
    return


def close_chatbox():
    all_xy = 83, 51
    game_xy = 190, 53

    mouse_click(all_xy)
    API.AntiBan.sleep_between(0.4, 0.9)

    mouse_click(game_xy)
    API.AntiBan.sleep_between(0.6, 0.7)

    mouse_click(game_xy)
    return


def handle_level_dialogue():
    if does_img_exist(img_name="level_up", category="General"):
        pag.press('space')
        API.AntiBan.sleep_between(1.1, 2.3)
        pag.press('space')
    return
