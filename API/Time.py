from datetime import datetime
from API.Debug import write_debug

START_TIME = None


def is_time_up(start_time, max_downtime_sec):
    curr_time = datetime.now()
    time_diff = curr_time - start_time

    # write_debug(f'⏲ Time diff: {time_diff} | Time diff seconds: {time_diff.total_seconds()} | is > {max_downtime_sec} ?')
    if time_diff.total_seconds() > max_downtime_sec:
        # write_debug(f'Time is up!')
        return True
    # write_debug(f'Time is not up yet...')
    return False


def start_script_timer():
    # Sets START_TIME global
    global START_TIME
    START_TIME = datetime.now()
    return


def get_curr_runtime():
    # Returns the difference in time from now to the time we started
    curr_time = datetime.now()

    curr_runtime = curr_time - START_TIME
    write_debug(f'CURRENT RUN-TIME: {curr_runtime}')
    return curr_runtime
