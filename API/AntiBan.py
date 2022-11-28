from datetime import datetime
from API.Imports.Paths import *
import time
import random


def sleep_between(min_seconds, max_seconds, DEBUG=True):
    r_sleep = random.uniform(min_seconds, max_seconds)
    if DEBUG:
        print(f'💤 Sleeping for {r_sleep} ms')
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

