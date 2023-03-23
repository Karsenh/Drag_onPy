import random

import API.AntiBan
from API.Mouse import mouse_click, mouse_move, mouse_long_click
from API.Interface.General import setup_interface, is_tab_open, relog
from API.Imaging.Image import wait_for_img, get_existing_img_xy, does_img_exist
import pyautogui as pag

CURR_JUMP_NUM = 1
ALCH_ITEM = "green_dhide_body_note"
SHOULD_ALCH = False

# OPTIONS
# Teleport to Seers
# Alch / what to alch (magic long, green d'hide body, etc.)


def start_seers_rooftops(curr_loop):
    global CURR_JUMP_NUM

    if curr_loop == 1:
        begin_course()
        alch_on_agility_drop()

    for i in range(1, 8):
        if not handle_next_jump(curr_loop):
            print(f'Something went wrong in handle_next_jump()')
            return False
        CURR_JUMP_NUM += 1
        print(f'Incrementing curr_jump_num +1 (now {CURR_JUMP_NUM})')
        # if random.randint(1, 10) < 9:
        if SHOULD_ALCH:
            alch_on_agility_drop()
        else:
            if not wait_for_img(img_name="agility_exp", script_name="Seers_Rooftops", max_wait_sec=15):
                CURR_JUMP_NUM -= 1
                print(f'Didnt see exp drop - trying previous jump again on next loop...')

    return True


def begin_course():
    setup_interface("north", 1, "up")
    is_tab_open("magic", should_be_open=True)
    wait_for_img(img_name='course_start', script_name='Seers_Rooftops', should_click=True, threshold=0.95, x_offset=-20, y_offset=75)
    return


def alch_on_agility_drop():
    global CURR_JUMP_NUM
    global SHOULD_ALCH

    API.AntiBan.sleep_between(0.2, 0.8)

    if not wait_for_img(img_name='high_alch', script_name='Seers_Rooftops', threshold=0.8, should_click=True):
        # 2. If not found - check if Magic tab is open and search for high-alch again, clicking if found.
        if is_tab_open("magic", should_be_open=True):
            if not wait_for_img(img_name='high_alch', script_name='Seers_Rooftops', threshold=0.9, should_click=True):
                print(f"Couldn't find alchemy spell despite magic tab being open")
                # return False
            else:
                # We've clicked the high-alch spell - click the magic long
                if wait_for_img(img_name=ALCH_ITEM, script_name="Seers_Rooftops", x_offset=4, y_offset=4, threshold=0.95):
                    print(f'Hovering mouse over magic long while we wait for agility jump...')
                    mouse_move(get_existing_img_xy())
                else:
                    print(f'Found and alched magic_long_note')
        else:
            print(f"Couldn't open magic tab")
            # return False
    else:
        # 3. Hover mouse over magic_long_note with High-alch selected, waiting for agility exp before left clicking
        if wait_for_img(img_name=ALCH_ITEM, script_name="Seers_Rooftops", x_offset=4, y_offset=4, threshold=0.95):
            print(f'Hovering mouse over magic long while we wait for agility jump...')
            mouse_move(get_existing_img_xy())
        else:
            print(f'No more {ALCH_ITEM}s in inventory. Stopping Alching')
            SHOULD_ALCH = False
            return

    if CURR_JUMP_NUM != 7:
        if wait_for_img(img_name="Agility", category='Exp_Drops', max_wait_sec=15):
            print(f'Saw agility exp - clicking to alch magic long...')
            pag.leftClick()
        else:
            print(f'Did not see Agility Exp drop - clicking to alch anyways to close inventory interface...')
            pag.leftClick()
            API.AntiBan.sleep_between(0.4, 0.8)
    else:
        API.AntiBan.sleep_between(3.0, 3.1)
    return


# HELPERS
def handle_next_jump(curr_loop):
    global CURR_JUMP_NUM

    jumps_with_mog = [1, 2, 3, 5]
    jumps_with_alt_mog = [2]

    API.Interface.General.handle_level_dialogue()

    # If we're still on the course (jumps 1-5)
    if CURR_JUMP_NUM < 6:
        print(f'🦘 CURR JUMP {CURR_JUMP_NUM}')
        # Check if the current jump rooftop has a mark of grace spawn we need to check...
        if CURR_JUMP_NUM == 4:
            print(f'Manually jumping this one...')
            jump_xy = 496, 535
            mouse_click(jump_xy, min_num_clicks=2, max_num_clicks=2, max_int_delay=0.2)
            return True

        if CURR_JUMP_NUM in jumps_with_mog:
            print("This roof has a Mark of Grace spawn that we're checking...")
            if CURR_JUMP_NUM == 3:
                API.AntiBan.sleep_between(.6, .7)

            if does_img_exist(img_name=f"mog_on_{CURR_JUMP_NUM}", script_name="Seers_Rooftops", threshold=0.9, should_click=True, x_offset=5, y_offset=5):
                print(f'Found a Mark of Grace and clicked it... Looking for jump_{CURR_JUMP_NUM}_from_mog')
                API.AntiBan.sleep_between(0.6, 0.7)

                y_offset = 0
                if CURR_JUMP_NUM == 3:
                    y_offset = 10

                if not wait_for_img(img_name=f"jump_{CURR_JUMP_NUM}_from_mog", script_name="Seers_Rooftops", x_offset=12, y_offset=y_offset, should_click=True):
                    return False

            # Check if an alt mog is present...
            elif CURR_JUMP_NUM in jumps_with_alt_mog and\
                    does_img_exist(img_name=f"mog_on_{CURR_JUMP_NUM}_alt", script_name="Seers_Rooftops", threshold=0.9, should_click=True, x_offset=5, y_offset=5):
                print(f'Found a ALT Mark of Grace and clicked it... Looking for jump_{CURR_JUMP_NUM}_from_mog')

                # Move to next jump from alt mog
                if not wait_for_img(img_name=f"jump_{CURR_JUMP_NUM}_from_mog_alt", script_name="Seers_Rooftops", should_click=True):
                    print(f"⛔ Couldn't find jump_from_mog_alt for some reason...")
                    return False

            else:
                if not wait_for_img(img_name=f"jump_{CURR_JUMP_NUM}", script_name="Seers_Rooftops", threshold=0.80, should_click=True, x_offset=10, y_offset=14):
                    if CURR_JUMP_NUM == 1:
                        if not wait_for_img(img_name=f"jump_{CURR_JUMP_NUM}", script_name="Seers_Rooftops",
                                            threshold=0.70, should_click=True, x_offset=10, y_offset=14):
                            return False
                    else:
                        if not wait_for_img(img_name=f"jump_{CURR_JUMP_NUM - 1}", script_name="Seers_Rooftops", threshold=0.80,
                                            should_click=True, x_offset=10, y_offset=10):
                            if wait_for_img(img_name=f"fall_on_{CURR_JUMP_NUM}", script_name="Seers_Rooftops"):
                                print(f'We seem to have fallen looking for jump_num: {CURR_JUMP_NUM} - but we can get up...')
                                if CURR_JUMP_NUM == 2:
                                    recover_xy = 1176, 586
                                if CURR_JUMP_NUM == 3:
                                    recover_xy = 1204, 338
                                # Reset the jump number since we're back to the start
                                CURR_JUMP_NUM = 0
                                mouse_click(recover_xy)
                            else:
                                return False
        else:
            if not wait_for_img(img_name=f"jump_{CURR_JUMP_NUM}", script_name="Seers_Rooftops", threshold=0.80, should_click=True, x_offset=10, y_offset=14):
                print(f"Couldn't find curr_jump_num ({CURR_JUMP_NUM} - Looking for previous jump before looking for fall")
                if not wait_for_img(img_name=f"jump_{CURR_JUMP_NUM - 1}", script_name="Seers_Rooftops", threshold=0.8, should_click=True, x_offset=10, y_offset=10, max_wait_sec=3):
                    if wait_for_img(img_name=f"fall_on_{CURR_JUMP_NUM}", script_name="Seers_Rooftops"):
                        print(f'We seem to have fallen looking for jump_num: {CURR_JUMP_NUM} - but we can get up...')
                        if CURR_JUMP_NUM == 2:
                            recover_xy = 1176, 586
                        if CURR_JUMP_NUM == 3:
                            recover_xy = 1204, 338
                        # Reset the jump number since we're back to the start
                        CURR_JUMP_NUM = 0
                        mouse_click(recover_xy)
                    else:
                        return False

    elif CURR_JUMP_NUM == 6:
        if curr_loop % 300 == 0:
            relog()
            setup_interface("north", 1, "up")

        print('click move_back image')
        if not wait_for_img(img_name="move_back_alt", script_name="Seers_Rooftops", threshold=0.9, should_click=True, x_offset=25,
                 y_offset=25, max_wait_sec=10):
            if does_img_exist(img_name='at_course_end_flag', script_name='Seers_Rooftops', threshold=0.9):
                flower_tile_xy = 1116, 278
                mouse_long_click(flower_tile_xy)
                return does_img_exist(img_name='walk_here_option', script_name='Seers_Rooftops', threshold=0.85, should_click=True, click_middle=True)

    else:
        # else jump_num == 7 | reset it back to 1 (0 + 1) after restarting course
        print('click restart_course image')
        pag.leftClick()
        API.AntiBan.sleep_between(2.0, 2.1)
        if not wait_for_img(img_name="restart_course", script_name="Seers_Rooftops", threshold=0.86, should_click=True, max_wait_sec=15, max_clicks=2, click_middle=True):
            return False
        print(f'Setting curr_jump_num ({CURR_JUMP_NUM}) = 0 ')
        CURR_JUMP_NUM = 0

    return True
