import API
from API.Imports.Paths import *
from API.Imaging.Image import does_img_exist
from API.Debug import DEBUG_MODE, write_debug
from datetime import datetime
from API.Mouse import mouse_move, mouse_click
import random
import pyautogui as pag
import time
import API


def sleep_between(min_seconds, max_seconds, likelihood=100):
    if likelihood == 100:
        r_sleep = random.uniform(min_seconds, max_seconds)
        write_debug(f'🎲 Selecting random time between {min_seconds} & {max_seconds}\n💤 Sleeping for {r_sleep} ms')
        time.sleep(r_sleep)
    else:
        if random.randint(1, 100) < likelihood:
            r_sleep = random.uniform(min_seconds, max_seconds)
            write_debug(f'🎲 Selecting random time between {min_seconds} & {max_seconds}\n💤 Sleeping for {r_sleep} ms')
            time.sleep(r_sleep)
    return


def random_thumbs_up():
    # Randomly give the game a thumbs up in the Exit tab
    return


def print_to_log(text):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    write_debug(f'⛔ Script Stopping @ [{current_time}]: - {text}\n'f'Logging to Script_Stop_Log.txt')

    with open(f'{STOP_LOG_PATH}', 'w') as f:
        f.write(f'{current_time}: {text}')
    return


def random_human_actions(max_downtime_seconds=3.0, likelihood=10, reopen_inventory=True):
    start_time = datetime.now()

    # Generate a random number between 1-10 (or likelihood)
    should_perform_actions = False

    if random.randint(1, likelihood) == likelihood:
        should_perform_actions = True
        write_debug(f"{should_perform_actions} (True?)")
    else:
        write_debug(f'{should_perform_actions} (False?)')

    if should_perform_actions:
        write_debug(f'Performing human actions for max_downtime_seconds: {max_downtime_seconds}')

        while not API.Time.is_time_up(start_time, max_downtime_seconds):
            # Loop around in here while we still have time in max_downtime
            # Sleep for a random interval at the end of each loop to randomly decide how many concurrent actions we do
            #   - If the sleep is longer we'll only do 1-2 actions
            #   - If the sleeps end up being shorter, we might do 3-4 actions
            elapsed_time = datetime.now() - start_time
            write_debug(f'now = {datetime.now()}\nstart_time = {start_time}\nelapsed_time = {elapsed_time}')

            time_remaining = max_downtime_seconds - elapsed_time.total_seconds()
            write_debug(f'time_remaining = {time_remaining}')

            write_debug(f'Random human activity time not up - Doing something and sleeping between 0.1 - {time_remaining} seconds...')

            skill_or_quest_tab = random.randint(1, 10)

            # write_debug(f'skill_or_quest_tab = {skill_or_quest_tab} | if <= 4 (Skill)')

            if skill_or_quest_tab <= 6:
                write_debug(f'Checking Skill Tab...')
                API.Interface.General.check_skill_tab(max_sec=max_downtime_seconds, skill_to_check="random", should_reopen_inventory=reopen_inventory)
            else:
                check_quest_tab(reopen_inventory=reopen_inventory)

            elapsed_time = datetime.now() - start_time
            time_remaining = max_downtime_seconds - elapsed_time.total_seconds()

            if time_remaining < 0:
                write_debug(f'⌛ Time is up!')
                return
            else:
                write_debug(f'⏳ Time not up - sleeping between 0.1 - {time_remaining}')
                sleep_between(0.1, time_remaining)
    else:
        write_debug(f'Not performing human interactions - {should_perform_actions} - Sleeping instead.')
        sleep_between(0.1, max_seconds=max_downtime_seconds)
    return


def shutdown(script_name, reason):
    pwd = os.getcwd()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(
        f'⛔ Script [{script_name}] Stopped @ [{current_time}]: {reason}'
        f'Logging to Script_Stop_Log.txt')
    with open(f'{pwd}\Misc\Stop_Log.txt', 'w') as f:
        f.write(f'{current_time}: {reason}')
    return False


def check_quest_tab(reopen_inventory):
    write_debug(f'🧙Checking Quest tab...')
    API.Interface.General.is_tab_open("quest", should_be_open=True)
    sleep_between(0.6, 1.1)

    # Select a random Quest sub-tab (achievement, quests, combat, favour)
    r_sub_tab = random.randint(0, 3)
    cmb_tab = 1127, 400
    quest_tab = 1204, 401
    achievement_tab = 1282, 401
    favour_tab = 1359, 400
    sub_tab_xys = [cmb_tab, quest_tab, achievement_tab, favour_tab]
    tab_to_sel = sub_tab_xys[r_sub_tab]
    mouse_click(tab_to_sel, max_x_dev=6, max_y_dev=5)
    sleep_between(0.2, 0.4)
    r_num_scrolls = random.randint(1, 3)
    print(f'tab_to_sel: {tab_to_sel}')
    if r_sub_tab == 1 or r_sub_tab == 2:
        quest_list_hover_xy = 1212, 574
        mouse_move(quest_list_hover_xy, 17, 23)
        sleep_between(0.9, 1.2)
        for i in range(1, r_num_scrolls):
            random_scroll = random.randint(-350, 350)
            write_debug(f'Scrolling: {random_scroll}')
            pag.hscroll(random_scroll)
            sleep_between(0.2, 0.5)

    sleep_between(0.6, 2.6)
    if not reopen_inventory:
        API.Interface.General.is_tab_open("quest", should_be_open=False)

    API.Interface.General.is_tab_open("inventory", should_be_open=reopen_inventory)
    return


def check_equipment_tab():

    return
