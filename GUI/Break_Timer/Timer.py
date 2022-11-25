import random
import tkinter

break_time = None
break_dev_time = None
interval_time = None
interval_dev_time = None

# Break-Timer Values in Settings Frame


def set_break_timer(time_vars, settings_gui, DEBUG=True):
    global break_time
    global break_dev_time
    global interval_time
    global interval_dev_time

    bt, bdt, it, idt = time_vars
    break_time = bt.get()
    break_dev_time = bdt.get()
    interval_time = it.get()
    interval_dev_time = idt.get()

    # Close the Settings GUI window
    settings_gui.destroy()

    if DEBUG:
        print(f'Break schedule fired with values:\nBreak Time: {break_time}\nBreak Time Dev: {break_dev_time}\nInterval Time: {interval_time}\nInterval Time Dev: {interval_dev_time}')
    return


def get_break_times():
    global break_time
    global break_dev_time
    global interval_time
    global interval_dev_time

    time_vals = break_time, break_dev_time, interval_time, interval_dev_time

    print(f'BREAK TIME VALS: {break_time} {break_dev_time} {interval_time} {interval_dev_time}')

    return time_vals


