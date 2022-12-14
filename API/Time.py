from datetime import datetime
from API.Debug import write_debug


def is_time_up(start_time, max_downtime_sec):
    curr_time = datetime.now()
    time_diff = curr_time - start_time

    write_debug(f'⏲ Time diff: {time_diff} | Time diff seconds: {time_diff.total_seconds()} | is > {max_downtime_sec} ?')
    if time_diff.total_seconds() > max_downtime_sec:
        write_debug(f'Time is up!')
        return True
    else:
        write_debug(f'Time is not up yet...')
        return False