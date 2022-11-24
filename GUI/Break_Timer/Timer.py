import tkinter

break_time = None
break_dev_time = None
interval_time = None
interval_dev_time = None

# Break-Timer Values in Settings Frame


def set_break_timer(time_vars, settings_gui):
    bt, bdt, it, idt = time_vars
    break_time = bt.get()
    break_dev_time = bdt.get()
    interval_time = it.get()
    interval_dev_time = idt.get()

    settings_gui.destroy()

    print(f'Break schedule fired with values:\n{break_time}\n{break_dev_time}\n{interval_time}\n{interval_dev_time}')
    return


def get_break_vals():
    global break_time
    global break_dev_time
    global interval_time
    global interval_dev_time

    return break_time, break_dev_time, interval_time, interval_dev_time


