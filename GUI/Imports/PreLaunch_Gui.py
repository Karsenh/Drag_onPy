import os
from tkinter import Toplevel, LabelFrame, font, Entry, Label, StringVar

frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_pre_launch_gui():
    break_font = font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = font.Font(family='Helvetica', size=11, weight='bold')

    pwd = os.getcwd()
    settings_gui = Toplevel(pady=50, padx=50)
    settings_gui.title('Pre-Launch')
    settings_gui.iconbitmap(f'{pwd}\Icon.ico')
    settings_gui.configure(bg='#969488')

    break_m = StringVar(settings_gui)

    bt_frame_1 = LabelFrame(settings_gui, text="⏱ Break Schedule", bg=frame_bg_color, pady=40, padx=40)

    e_min_label_prefix = Label(bt_frame_1, text="Every", background=frame_bg_color, font=break_font)
    e_min = Entry(bt_frame_1, textvariable=break_m, background=label_frame_bg_color, font=break_btn_font)

    e_min_label_prefix.grid(row=1, column=1)
    e_min.grid(row=1, column=2, columnspan=1, padx=20, pady=10)

    bt_frame_1.grid(row=1, column=1)

    return
