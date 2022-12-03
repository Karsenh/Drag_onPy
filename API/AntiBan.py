from datetime import datetime
from API.Imports.Paths import *
from API.Imaging.Image import does_img_exist
import time
import random
from API.Debug import DEBUG_MODE


def sleep_between(min_seconds, max_seconds):
    global DEBUG_MODE
    r_sleep = random.uniform(min_seconds, max_seconds)
    if DEBUG_MODE:
        print(f'🎲Selecting random time between {min_seconds} & {max_seconds}\n💤 Sleeping for {r_sleep} ms')
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