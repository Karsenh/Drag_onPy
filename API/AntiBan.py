from datetime import datetime
from API.Imports.Paths import *
from API.Imaging.Image import does_img_exist
import time
import random
from API.Debug import DEBUG_MODE, write_debug


def sleep_between(min_seconds, max_seconds):
    r_sleep = random.uniform(min_seconds, max_seconds)
    write_debug(f'🎲Selecting random time between {min_seconds} & {max_seconds}\n💤 Sleeping for {r_sleep} ms')
    time.sleep(r_sleep)
    return


def random_thumbs_up():
    # Randomly give the game a thumbs up in the Exit tab
    return


def print_to_log(text):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(
        f'⛔ Script Stopping @ [{current_time}]: - {text}\n'
        f'Logging to Script_Stop_Log.txt')

    with open(f'{STOP_LOG_PATH}', 'w') as f:
        f.write(f'{current_time}: {text}')
    return


# Search for a particular img on screen for a set amount of time
#       Returns True if the image is found within the amount of time
#       Returns False if the image is not found after trying for specified amount of time
def wait_for_img(img_to_search, script_name=None, category_name="Scripts", max_wait_sec=5, img_threshold=0.8):
    start_time = datetime.now()
    if DEBUG_MODE:
        print(f'⏲ Wait_For_Img Start Time: {start_time}')

    while not is_time_up(start_time, max_wait_sec):
        img_found = does_img_exist(img_to_search, script_name=script_name, category=category_name, threshold=img_threshold)
        if img_found:
            return True
        else:
            print(f'Still checking for image...')

    return


def is_time_up(start_time, max_wait_sec):
    curr_time = datetime.now()
    time_diff = curr_time - start_time

    if DEBUG_MODE:
        print(f'⏲ Time diff: {time_diff} | Time diff seconds: {time_diff.total_seconds()} | is > {max_wait_sec} ?')
    if time_diff.total_seconds() > max_wait_sec:
        print(f'Time is up!')
        return True
    else:
        print(f'Time is not up yet.')
        return False


def random_human_actions(max_downtime_seconds=3.0):
    start_time = datetime.now()

    # Generate a random number between 1-10
    should_perform_actions = False
    if random.randint(1, 10) < 10:
        should_perform_actions = True
        write_debug(f"{should_perform_actions} (True?)")
    else:
        write_debug(f'{should_perform_actions} (False?)')

    if should_perform_actions:
        write_debug(f'Performing human actions for max_downtime_seconds: {max_downtime_seconds}')

        while not is_time_up(start_time, max_downtime_seconds):
            # Loop around in here while we still have time in max_downtime
            # Sleep for a random interval at the end of each loop to randomly decide how many concurrent actions we do
            #   - If the sleep is longer we'll only do 1-2 actions
            #   - If the sleeps end up being shorter, we might do 3-4 actions
            elapsed_time = datetime.now() - start_time
            write_debug(f'now = {datetime.now()}\nstart_time = {start_time}\nelapsed_time = {elapsed_time}')

            time_remaining = max_downtime_seconds - elapsed_time.total_seconds()
            write_debug(f'time_remaining = {time_remaining}')

            write_debug(f'Random human activity time not up - Doing something and sleeping between 0.1 - {time_remaining} seconds...')



            sleep_between(0.1, time_remaining)

    return


