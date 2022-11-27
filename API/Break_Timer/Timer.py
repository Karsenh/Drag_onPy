import random
import tkinter

break_min = None
break_dev_min = None
interval_min = None
interval_dev_min = None

# Break-Timer Values in Settings Frame


def set_break_timer(time_vars, settings_gui, DEBUG=True):
    global break_min
    global break_dev_min
    global interval_min
    global interval_dev_min

    bt, bdt, it, idt = time_vars
    break_min = int(bt.get())
    break_dev_min = int(bdt.get())
    interval_min = int(it.get())
    interval_dev_min = int(idt.get())

    # If the deviation times are not greater than at least 1, default them to 1
    if not break_dev_min >= 1:
        if DEBUG:
            print(f'Break Deviation Time not >= 1 ... Defaulting to deviation of 1.')
        break_dev_min = 1

    if not interval_dev_min >= 1:
        if DEBUG:
            print(f'Interval Deviation Time not >= 1 ... Defaulting to deviation of 1.')
        interval_dev_min = 1

    # TODO: Add checks to make sure values are even possible based on what they're being used for
    # 1. Check if integer
    # 2. Check if deviation is less than corresponding time
    # 3. If nothing is passed for deviation time, they default to 1

    # Close the Settings GUI window
    settings_gui.destroy()

    if DEBUG:
        print(f'Break schedule fired with values:\nBreak Time: {break_min}\nBreak Time Dev: {break_dev_min}\nInterval Time: {interval_min}\nInterval Time Dev: {interval_dev_min}')
    return


def get_break_times(DEBUG=True):
    global break_min
    global break_dev_min
    global interval_min
    global interval_dev_min

    time_vals = break_min, break_dev_min, interval_min, interval_dev_min

    if DEBUG:
        print(f'BREAK TIME VALS: {break_min} {break_dev_min} {interval_min} {interval_dev_min}')

    return time_vals


