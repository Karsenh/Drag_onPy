import pyautogui
import API.AntiBan
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Interface.General import setup_interface, is_tab_open, relog, handle_level_dialogue
from API.Mouse import mouse_move, mouse_click, mouse_long_click
from GUI.Imports.PreLaunch_Gui.Plg_Script_Options import Global_Script_Options

SCRIPT_NAME = 'Gnome_Course'

SHOULD_TELE = False
SHOULD_ALCH = False
USE_COORDS = False
ITEMS_TO_ALCH = ['green_dhide_body_note', 'magic_long_note']
ALCH_ITEM = ITEMS_TO_ALCH[0]
NO_ALCH_SLEEP_TIMES = [1, 1, 1, 1, 1, 1, 1]
MOG_JUMPS = []
JUMPS_TO_LONG_CLICK = [0]
JUMP_NUMS_TO_WAIT = [6]

CURR_JUMP_NUM = 0
NUM_TOTAL_LAPS = 0

CONSEC_TIMES_NO_EXP_SEEN = 0

# JUMP COORDINATES
jump_0 = 172, 530
jump_1 = 730, 630
jump_2 = 743, 470
jump_3 = 979, 465
jump_4 = 900, 487
jump_5 = 765, 202
jump_6 = 753, 300
jump_coords = [jump_0, jump_1, jump_2, jump_3, jump_4, jump_5, jump_6]


def start_gnome_course(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        handle_next_jump()

    else:
        print(f'First loop')
        set_script_options()
        setup_interface('north', 2, 'up')

    return True


#########
# METHODS
#########
def handle_next_jump():
    global SHOULD_ALCH

    print(f'CONSEC_TIME_NO_EXP_SEEN: {CONSEC_TIMES_NO_EXP_SEEN} (> 4?)')
    if CONSEC_TIMES_NO_EXP_SEEN > 4:
        return False

    handle_level_dialogue()

    # Check for Mog
    if CURR_JUMP_NUM in MOG_JUMPS:
        print(f'Checking for MoG on: {CURR_JUMP_NUM}')
        if does_img_exist(img_name=f'mog_on_{CURR_JUMP_NUM}', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
            API.AntiBan.sleep_between(3.0, 3.5)
            if not does_img_exist(img_name=f'jump_{CURR_JUMP_NUM}_from_mog', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
                print(f'❌ Failed to find jump_{CURR_JUMP_NUM}_from_mog - using xy coords...')
                match (CURR_JUMP_NUM):
                    case 3:
                        jump_xy_from_mog = 666, 456
                    case _:
                        print(f'❌ Failed to set jump_xy from mog')
                mouse_click(jump_xy_from_mog)
        else:
            print(f'Clicking jump {CURR_JUMP_NUM} @ {jump_coords[CURR_JUMP_NUM]}')
            mouse_click(jump_coords[CURR_JUMP_NUM])
    else:
        # Click curr jump
        print(f'Clicking jump {CURR_JUMP_NUM} @ {jump_coords[CURR_JUMP_NUM]}')
        if CURR_JUMP_NUM in JUMPS_TO_LONG_CLICK:
            mouse_long_click(jump_coords[CURR_JUMP_NUM])
            if not does_img_exist(img_name='walk_across_option', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
                print(f'⛔ Failed to find walk_across_option on jump_num: {CURR_JUMP_NUM}')
                return False
        else:
            mouse_click(jump_coords[CURR_JUMP_NUM])

    if SHOULD_ALCH:
        if not handle_wait_and_alch():
            print(f'⛔ Something went wrong handle_wait_and_alch...')
            SHOULD_ALCH = False
            is_tab_open('inventory')
        # else:
        inc_curr_jump_num()
    else:
        if not handle_wait():
            print(f'⛔ Something went wrong handle_wait...')
        else:
            inc_curr_jump_num()

    if CURR_JUMP_NUM == len(jump_coords):
        reset_curr_jump()
        inc_num_total_laps()
        print(f'TOTAL NUM LAPS: {NUM_TOTAL_LAPS}')
        if NUM_TOTAL_LAPS % 240 == 0:
            relog()

    return True


def handle_wait_and_alch():
    if not prepare_alch():
        print(f'❌ handle_wait_and_alch - failed to prepare_alch')
        return False

    if not wait_for_agility_exp():
        print(f'❌ handle_wait_and_alch - failed to find agility exp')
        if not handle_exp_not_seen():
            print(f'⛔ Failed to handle_exp_not_seen')
            return False
        # if not handle_fall():
        #     print(f'❌ handle_wait_and_alch - failed to handle fall as well - are we on next jump or prev?')
        #     return False
    else:
        cast_alch()

    return True


def handle_wait():
    sleep_time_sec = NO_ALCH_SLEEP_TIMES[CURR_JUMP_NUM]
    API.AntiBan.sleep_between(sleep_time_sec, sleep_time_sec+0.1)
    # if CURR_JUMP_NUM in JUMP_NUMS_TO_WAIT:
    #     API.AntiBan.sleep_between(1.0, 1.3)

    if not wait_for_agility_exp():
        print(f'❌ handle_wait - failed to find agility exp')
        if not handle_exp_not_seen():
            print(f'⛔ Failed to handle_exp_not_seen')
            return False
        # if not handle_fall():
        #     print(f'❌handle_wait - failed to handle fall - are we on prev or next jump?')
        #     return False
    return True


def handle_fall():
    print(f'Did we fall?')
    # 1395 276
    # 1355, 268
    match CURR_JUMP_NUM:
        case 1:
            recov_1 = 1355, 268
            recovery_xys = [recov_1]
        case 3:
            print(f'⛔⛔ Add recov xy data for this fall!')
            recov_1 = 1392, 270
            recov_2 = 1388, 210
            recovery_xys = [recov_1, recov_2]

    for coords in recovery_xys:
        mouse_click(coords)
        API.AntiBan.sleep_between(6.0, 6.1)

    reset_curr_jump()
    return


def handle_exp_not_seen():
    if SHOULD_ALCH:
        # Clear Alch
        pyautogui.leftClick()

    # Are we on next jump?
    if is_on_jump('next'):
        return True

    # Are we on same jump?
    if is_on_jump('curr'):
        return True

    # Did we fall?
    if did_fall():
        if handle_fall():
            return True

    return False


#########
# HELPERS
#########
def did_fall():
    return does_img_exist(img_name=f'fall_on_{CURR_JUMP_NUM}', script_name=SCRIPT_NAME, threshold=0.85)


def is_on_jump(jump_name='curr'):
    if jump_name == 'curr':
        jump_coord_idx = CURR_JUMP_NUM
    else:
        jump_coord_idx = CURR_JUMP_NUM+1

    mouse_long_click(jump_coords[jump_coord_idx])

    if not does_img_exist(img_name='walk_across_options', script_name=SCRIPT_NAME, should_click=True, click_middle=True):
        if not does_img_exist(img_name='walk_on_option', script_name=SCRIPT_NAME, threshold=0.92, should_click=True, click_middle=True):
            if not does_img_exist(img_name='balance_across_option', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
                print(f'Failed to find Jump, Walk, and Balance options on {jump_name} jump')
                pyautogui.leftClick()
                return False
    return True


def prepare_alch():
    global SHOULD_ALCH

    is_tab_open(tab='magic', should_be_open=True)

    if not wait_for_img(img_name='high_alch', script_name='Seers_Rooftops', threshold=0.9, max_wait_sec=5, should_click=True, click_middle=True):
        print(f'❌ Failed to find high alchemy spell for some reason - out of runes or not in magic tab?')
        is_tab_open(tab='magic', should_be_open=True)
        if not wait_for_img(img_name='high_alch', script_name='Seers_Rooftops', threshold=0.9, max_wait_sec=5,
                            should_click=True, click_middle=True):
            return False

    if not wait_for_img(img_name=ALCH_ITEM, script_name='Seers_Rooftops', threshold=0.88):
        print(f'❌ Failed to find ALCH_ITEM: {ALCH_ITEM}')
        pyautogui.leftClick()
        SHOULD_ALCH = False
    else:
        alch_item_coords = get_existing_img_xy()
        mouse_move(alch_item_coords)

    return True


def cast_alch():
    pyautogui.leftClick()
    API.AntiBan.sleep_between(0.8, 1.3)
    return


def wait_for_agility_exp():
    if not wait_for_img(img_name='Agility', category='Exp_Drops', max_wait_sec=15):
        inc_num_times_no_exp_seen()
        return False
    else:
        reset_num_times_no_exp_seen()
        return True


def inc_curr_jump_num():
    global CURR_JUMP_NUM
    print(f'Curr_jump_num was just: {CURR_JUMP_NUM}')
    CURR_JUMP_NUM += 1
    print(f'Curr_jump_num is NOW: {CURR_JUMP_NUM}')
    return


def reset_curr_jump():
    global CURR_JUMP_NUM
    print(f'RESETTING CURR JUMP NUM')
    CURR_JUMP_NUM = 0
    return


def inc_num_times_no_exp_seen():
    global CONSEC_TIMES_NO_EXP_SEEN
    CONSEC_TIMES_NO_EXP_SEEN += 1
    return


def reset_num_times_no_exp_seen():
    global CONSEC_TIMES_NO_EXP_SEEN

    CONSEC_TIMES_NO_EXP_SEEN = 0
    return


def inc_num_total_laps():
    global NUM_TOTAL_LAPS
    NUM_TOTAL_LAPS += 1
    return


def set_script_options():
    global SHOULD_ALCH
    global ALCH_ITEM

    for option in Global_Script_Options.options_arr:
        if option.name == 'High Alch':
            print(f'Found Food Type option - Setting to: {option.value}')
            SHOULD_ALCH = True
            match option.value:
                case "none":
                    print(f'Not Alching')
                    ALCH_ITEM = None
                    SHOULD_ALCH = False
                case "magic_long_noted":
                    print(f'Alching Magic Long notes')
                    ALCH_ITEM = ITEMS_TO_ALCH[1]
                case "green_dhide_bodies":
                    print(f'Alching Green Dhide Bodies notes')
                    ALCH_ITEM = ITEMS_TO_ALCH[0]
                case _:
                    print(f'Default case hit')

            SHOULD_ALCH = option.value

    return
