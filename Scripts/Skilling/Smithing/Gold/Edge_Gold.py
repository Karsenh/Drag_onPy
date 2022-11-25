import random
from GUI.Break_Timer.Timer import *
from API.Interface import *

exit_prog = False
first_loop = True

def smith_gold_edge():
    global exit_prog
    global first_loop

    exit_prog = False
    check_for_gauntlets = True
    keyboard.add_hotkey('esc', lambda: quit_script())

    # normalize interface
    # Start in front of NW bank booth in Edge bank
    if first_loop:
        setup()

        # 1. Opens bank booth
        if not is_furnace_start():
            start_open_bank()

        # 2. Deposits All inventory & equipment
        deposit_all(include_equipment=True)

        # 3. Checks if we're on mining tab - clicks mining tab if not
        check_if_bank_tab_open(4, True)

        # 4. Checks for goldsmithing gauntlets - withdraws & equips if found
        if check_for_gauntlets:
            equip_gauntlets_if_banked()

        # 5. Checks if we're on 'All' withdraw qty
        check_withdraw_qty_all()

        first_loop = False

    # 6. Checks if we have ore - exits if not
    # while

    if not first_loop:
        deposit_all()

    # 7. Withdraws ore
    withdraw_gold_if_banked()

    # 8. Click furnace
    move_to_furnace()

    # 9. Click / 6 / Space (after first selection) to select gold bar
    select_gold_bar()

    get_break_times()

    # 10. Sleep for ~84 seconds
    check_for_level()

    bank_from_furnace()

    # 11. Repeat from step 6

    # sleep_between(1.1, 1.2)
    return


def setup():
    check_one_tap_drop_enabled(should_enable=False)
    turn_compass("north")
    zoom_camera(1)
    pitch_camera("up")
    sleep_between(1.1, 1.6)
    return


def is_furnace_start():
    furnace_loc_check = 1459, 194
    furnace_loc_color = 55, 86, 73
    if does_color_exist(furnace_loc_color, furnace_loc_check):
        bank_from_furnace()
        return True
    return False


def start_open_bank():
    start_bank_xy = 743, 483
    mouse_click(start_bank_xy, 11, 12)
    time.sleep(1.4)
    return


def deposit_all(include_equipment=False):
    mouse_click(BANK_dep_inventory)
    sleep_between(0.5, 0.7)
    if include_equipment:
        mouse_click(BANK_dep_equipment)
    return


def equip_gauntlets_if_banked():
    sleep_between(0.8, 1.2)
    if does_img_exist("goldsmith_gauntlets", script_name="Edge_Gold", threshold=0.99):
        xy = get_existing_img_xy()
        x, y = xy
        new_xy = x+30, y+20
        mouse_click(new_xy)
        sleep_between(0.9, 1.3)
        to_xy = 1173, 763
        mouse_drag(INVENT_slot_1, to_xy)
    return


def check_withdraw_qty_all():
    qty_all_color = 119, 28, 26
    if not does_color_exist(qty_all_color, BANK_qty_all):
        mouse_click(BANK_qty_all)
    return


def withdraw_gold_if_banked():
    print(f'Withdrawing gold ore if comparator image is found')
    if not does_img_exist("gold_ore", script_name="Edge_Gold", threshold=0.95):
        print_to_log("No gold ore found in bank.")
        exit(-1)
    else:
        print(f'🥇 Clicking gold ore at: {get_existing_img_xy()}')
        mouse_click(get_existing_img_xy())
        sleep_between(0.7, 1)
        rand_long_wait = random.randint(1,10)
        if rand_long_wait >= 9:
            sleep_between(3.0, 9.0)

    return


def move_to_furnace():
    furnace_xy = 1090, 340
    mouse_click(furnace_xy, 3, 3, max_num_clicks=2)
    sleep_between(6.0, 6.4)
    # TODO Check if we're actually at the furnace when we get here
    return


def select_gold_bar():
    gold_bar_xy = 548, 180
    mouse_click(gold_bar_xy)
    return


def check_for_level():
    # Loop 17 times (total of ~85 seconds)
    start = time.time()

    for x in range(35):
        print(f'START LOOP TIME = {start}')
        # Sleep ~5 sec
        sleep_or_move = random.randint(1, 20)
        if sleep_or_move <= 19:
            print(f'Sleeping between 1.9 - 2.3')
            sleep_between(1.9, 2.3)
        else:
            skill_or_quest_tab = random.randint(1, 10)
            if skill_or_quest_tab <= 7:
                print(f'check between 1.9 - 2.3')
                check_skill_tab(max_sec=2.0, skill_to_check="smithing")
            else:
                print(f'🧙‍Opening quest tab')
                check_if_tab_open("quest", should_open=True)
                sleep_between(0.5, 0.9)
                quest_list_hover_xy = 1212, 574
                mouse_move(quest_list_hover_xy, 21, 19)
                sleep_between(0.3, 1.2)
                random_scroll = random.randint(-389, 400)
                print(f'{random_scroll}')
                pag.hscroll(random_scroll)
                sleep_between(0.5, 1.6)
                check_if_tab_open("inventory", should_open=True)
        # Check if we leveled up
        if does_img_exist("level_up", category="General"):
            # If so, click the furnace again to start making bars
            furnace_xy = 782, 449
            mouse_click(furnace_xy, 3, 3, max_num_clicks=2)
            sleep_between(1.1, 1.4)
            select_gold_bar()
        end = time.time()
        print(f'END LOOP TIME = {end}')

    return


def bank_from_furnace():
    bank_booth_xy = 334, 622
    mouse_click(bank_booth_xy, 3, 4)
    sleep_between(5.9, 6.2)
    return


def quit_script():
    global exit_prog
    exit_prog = True
    return
