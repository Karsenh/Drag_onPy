import pyautogui

import API.AntiBan
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Interface.General import setup_interface, is_tab_open, relog
from API.Mouse import mouse_move, mouse_click, mouse_long_click

SCRIPT_NAME = 'Seers_Rooftops'

SHOULD_TELE = False
SHOULD_ALCH = False
USE_COORDS = True
ITEMS_TO_ALCH = ['green_dhide_body_note', 'magic_long_note']
ALCH_ITEM = ITEMS_TO_ALCH[0]

CURR_JUMP_NUM = 0

CONSEC_TIMES_NO_EXP_SEEN = 0

jump_0 = 513, 410
jump_1 = 660, 592
jump_2 = 756, 570
jump_3 = 495, 536
jump_4 = 780, 505
jump_coords = [jump_0, jump_1, jump_2, jump_3, jump_4]


def start_seers_rooftops(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')

        if not click_to_start_course():
            return False

        if SHOULD_ALCH:
            if not wait_then_alch(-1):
                print(f'❌ Failed to wait_then_alch()')
        else:
            if not wait_for_agility_exp():
                print(f'❌ Failed to find agility exp - did we fall?')

        while CURR_JUMP_NUM < 5:
            print(f'🔢 Handle_curr_jump: {CURR_JUMP_NUM} 🔢')
            if not handle_curr_jump(CURR_JUMP_NUM):
                return False
            print(f'✨✨ CURR_JUMP_NUM now: {CURR_JUMP_NUM} ✨✨')

        move_back_to_start(curr_loop)

    else:
        print(f'First loop')
        # setup_interface("north", 1, "up")

    return True


##########
# METHODS
##########
def click_to_start_course():
    if not does_img_exist(img_name='v2_start_course', script_name='Seers_Rooftops', threshold=0.8, should_click=True, click_middle=True):
        if not wait_for_img(img_name='v2_restart_course_from_flowers', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True, max_wait_sec=15):
            print(f'⛔ Failed to find either course start images (2)')
            return False
    return True


def wait_then_alch(curr_jump_num):
    if not prepare_alch():
        print(f'❌ Prepare_alch failed in wait_then_alch either opening tab or finding high-alch spell img')
        return False

    if not wait_for_agility_exp():
        cast_alch()
        print(f'❌ Failed to find exp drop - assuming after 15 seconds we got it and continuing')
        handle_fall(curr_jump_num)
    else:
        cast_alch()

    return True


def handle_curr_jump(curr_jump_num):
    # Jumps with mark of grace spawn
    mog_jumps = [0, 1, 2, 4]
    alt_mog_jumps = [1]

    print(f'CONSEC_TIME_NO_EXP_SEEN: {CONSEC_TIMES_NO_EXP_SEEN} (> 4?)')
    if CONSEC_TIMES_NO_EXP_SEEN > 4:
        return False

    if CURR_JUMP_NUM == 2 or CURR_JUMP_NUM == 3:
        print(f'Waiting a second longer...')
        API.AntiBan.sleep_between(0.6, 0.7)

    # IF THIS JUMP HAS MOG SPAWN
    if curr_jump_num in mog_jumps:

        if found_and_retrieved_mog(curr_jump_num):
            API.AntiBan.sleep_between(5, 6)
            if not click_curr_jump(f'jump_{curr_jump_num}_from_mog', from_mog=True):
                print(f'Failed to find jump_{curr_jump_num}_from_mog')

                match CURR_JUMP_NUM:
                    case 1:
                        jump_from_mog_xy = 777, 567
                        mouse_click(jump_from_mog_xy)

                    case _:
                        print(f'Failed to find recovery xy')
                        return False

        # Current jump has mog spawn but didn't have primary mog
        else:
            # If current jump has alternative spawn, check that too
            if curr_jump_num in alt_mog_jumps:
                print(f'Checking for alternative mog spawn...')

                # Found alt mog
                if found_and_retrieved_mog(curr_jump_num, is_alt_mog=True):
                    print(f'Found Alternative Mog on jump: {curr_jump_num}')
                    API.AntiBan.sleep_between(5, 6)
                    if not click_curr_jump(f'jump_{curr_jump_num}_from_mog_alt', from_mog=True):
                        print(f'Failed to find jump_{curr_jump_num}_from_mog')
                        return False
                # Else Didn't find alt mog
                else:
                    if USE_COORDS:
                        print(f'Using coords: (curr jump {curr_jump_num}) - {jump_coords[curr_jump_num]}')
                        mouse_click(jump_coords[curr_jump_num])
                    else:
                        if not click_curr_jump(f'jump_{curr_jump_num}'):
                            print(f'Failed to find jump_{curr_jump_num}')
                            return False

            # Current jump does NOT have alt mog spawn
            else:
                if USE_COORDS:
                    print(f'Using coords: (curr jump {curr_jump_num}) - {jump_coords[curr_jump_num]}')
                    mouse_click(jump_coords[curr_jump_num])
                else:
                    if not click_curr_jump(f'jump_{curr_jump_num}'):
                        print(f'Failed to find jump_{curr_jump_num}')
                        return False

    # current jump does NOT have mog spawn
    # CLICK JUMP
    else:
        if USE_COORDS:
            print(f'Using coords: (curr jump {curr_jump_num}) - {jump_coords[curr_jump_num]}')
            mouse_click(jump_coords[curr_jump_num])
        else:
            if not click_curr_jump(f'jump_{curr_jump_num}'):
                print(f'Failed to find jump_{curr_jump_num}')
                return False

    API.AntiBan.sleep_between(0.3, 0.4)

    # ALCH AFTER JUMP
    if SHOULD_ALCH:
        if not wait_then_alch(curr_jump_num):
            print(f'❌ Failed to wait_then_alch()')
        inc_curr_jump_num()

    else:
        if not wait_for_agility_exp():
            print(f'❌ Failed to find exp drop - assuming after 15 seconds we got it and continuing')
            handle_fall(curr_jump_num)
        else:
            inc_curr_jump_num()

    return True


def handle_fall(curr_jump_num):
    fall_on_jumps = [0, 1]

    if curr_jump_num not in fall_on_jumps:
        return

    if did_fall_on(jump_num=curr_jump_num):
        print(f'Detected fall on jump_num: {curr_jump_num} - resetting')
        handle_fall_on(curr_jump_num)
    return


def move_back_to_start(curr_loop):
    global CURR_JUMP_NUM
    CURR_JUMP_NUM = 0

    if curr_loop % 300 == 0:
        relog()
        setup_interface("north", 1, "up")

    print('click move_back image')
    if not wait_for_img(img_name="move_back_alt", script_name="Seers_Rooftops", threshold=0.9, should_click=True,
                        x_offset=25,
                        y_offset=25, max_wait_sec=10):
        if does_img_exist(img_name='at_course_end_flag', script_name='Seers_Rooftops', threshold=0.9):
            flower_tile_xy = 1135, 285
            mouse_long_click(flower_tile_xy)
            return does_img_exist(img_name='walk_here_option', script_name='Seers_Rooftops', threshold=0.85,
                                  should_click=True, click_middle=True)
    return True


# ######
# HELPERS
# ######
def prepare_alch():
    global SHOULD_ALCH

    is_tab_open(tab='magic', should_be_open=True)

    if not does_img_exist(img_name='high_alch', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        print(f'❌ Failed to find high alchemy spell for some reason - out of runes or not in magic tab?')
        return False

    if not wait_for_img(img_name=ALCH_ITEM, script_name=SCRIPT_NAME, threshold=0.88):
        print(f'❌ Failed to find ALCH_ITEM: {ALCH_ITEM}')
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
        mouse_long_click(jump_coords[CURR_JUMP_NUM])
        if not does_img_exist(img_name='jump_option', script_name=SCRIPT_NAME, should_click=True, click_middle=True):
            print(f'f Manually Left Clicking (PAG)')
            pyautogui.leftClick()
            inc_num_times_no_exp_seen()
            inc_curr_jump_num()
            return False
    else:
        reset_num_times_no_exp_seen()
    return True


def found_and_retrieved_mog(curr_jump_num, is_alt_mog=False):
    if not is_alt_mog:
        return does_img_exist(img_name=f'mog_on_{curr_jump_num}', script_name=SCRIPT_NAME, threshold=0.80, should_click=True, click_middle=True)
    else:
        return does_img_exist(img_name=f'mog_on_{curr_jump_num}_alt', script_name=SCRIPT_NAME, threshold=0.80, should_click=True, click_middle=True)


def click_curr_jump(curr_jump_name, from_mog=False):
    should_click_middle = not from_mog
    return does_img_exist(img_name=curr_jump_name, script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=should_click_middle)


def inc_curr_jump_num():
    global CURR_JUMP_NUM

    CURR_JUMP_NUM += 1
    return


def inc_num_times_no_exp_seen():
    global CONSEC_TIMES_NO_EXP_SEEN
    CONSEC_TIMES_NO_EXP_SEEN += 1
    return


def reset_num_times_no_exp_seen():
    global CONSEC_TIMES_NO_EXP_SEEN

    CONSEC_TIMES_NO_EXP_SEEN = 0
    return


def did_fall_on(jump_num):
    print(f'Checking for fall on jump_num: {jump_num}')
    return does_img_exist(img_name=f'fall_on_{jump_num}', script_name=SCRIPT_NAME, threshold=0.86)


def handle_fall_on(curr_jump_num):
    # Fall will only happen on curr_jump_num 0 (west jump) and 1 (south jump)
    match curr_jump_num:
        case 0:
            print(f'Setting recovery_xy coords to case 0')
            recover_xy = 1176, 586
        case 1:
            print(f'Setting recovery_xy coords to case 1')
            recover_xy = 1204, 338
        case _:
            print(f'Fell on unexpected curr_jump_num: {curr_jump_num}')
            return False

    mouse_click(recover_xy)
    return True