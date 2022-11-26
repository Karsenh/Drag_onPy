from GUI.Break_Timer.Timer import *
from datetime import datetime, timedelta
import time
from API.Interface import handle_auth_screens


script_start_time = None


def check_break_timer(callback_fn=None):
    if is_break_timer_set():
        if should_break():
            go_on_break()
            handle_auth_screens()
            if callback_fn is None:
                return
            else:
                callback_fn()
    return


# Boolean check if a break-schedule has been set in GUI
def is_break_timer_set():
    break_vals = get_break_times()
    break_time, _, _, _ = break_vals
    if break_time is None:
        return False
    else:
        return True
    return


# Checks the interval times to see if we need to use the break times
def should_break(DEBUG=True):
    global script_start_time
    break_vals = get_break_times()
    _, _, interval_t, interval_dev_t = break_vals

    # If this is the first loop - set the start time of the script to now
    if not script_start_time:
        start_time = datetime.now()
        print(f'1️First loop - 🕑 Script_Start_Time (setting): {start_time}')
        script_start_time = start_time

    # Calculate how long has elapsed since start
    # print(f'Script start time: {script_start_time}')
    # curr_time = datetime.now()
    # print(f'Curr time: {curr_time}')
    # elapsed_time = curr_time - script_start_time
    # print(f'Elapsed Time (min): {elapsed_time.total_seconds() / 60}')

    rand_interval_dev = random.randint(1, interval_dev_t)
    should_be_negative = random.randint(1, 10)
    if should_be_negative > 5:
        rand_interval_dev * -1

    actual_interval_minutes = interval_t + rand_interval_dev

    break_at = script_start_time + timedelta(minutes=actual_interval_minutes)

    now = datetime.now()

    if DEBUG:
        print(f'🕒 Script start time: {script_start_time}\n⏱ actual_interval_minutes: {actual_interval_minutes} minutes\n🕓 break_at: {break_at}\n🕖 now: {now}')
    # Check if the elapsed time is greater than or equal to the break interval time (how often we should take a break)
    if now > break_at:
        # If we should take a break, return true
        print(f'⌛ We should go on break now.')
        return True

    # Else, return false
    return False


# Uses the break times based on the interval times warranting it
def go_on_break(DEBUG=True):
    global script_start_time
    #     Sleep for however long the break_time is
    break_vals = get_break_times()
    break_t, break_dev_t, _, _ = break_vals

    rand_break_dev = random.randint(1, break_dev_t)
    should_be_negative = random.randint(1, 10)
    if should_be_negative > 5:
        rand_break_dev * -1

    actual_break_minutes = break_t + rand_break_dev
    actual_break_seconds = actual_break_minutes * 60

    if DEBUG:
        print(f'💤 🛌🏼 Going on break - Sleeping for {actual_break_minutes} minutes ({actual_break_seconds} seconds) with values:\nRand_break_dev: {rand_break_dev}\nbreak_t: {break_t}')
    time.sleep(actual_break_seconds)

    # Reset script start time after finished breaking to get out of break loop and start fresh
    script_start_time = datetime.now()

    return
