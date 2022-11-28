import tkinter.font
from GUI.Main_GUI import *
from API.Break_Timer.Timer import *
import os
from tkinter import *
from PIL import ImageTk, Image


frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'

sub_gui_row = 3

is_active_gold = False
is_active_skill = False
is_active_pvm_pvp = False


def toggle_active_frame(frame_name, all_frames):
    global is_active_gold
    global is_active_skill
    global is_active_pvm_pvp

    main_frame, gold_frame, skill_frame, pvm_pvp_frame, skill_sub_frames = all_frames

    match frame_name:
        case "gold":
            is_active_gold = not is_active_gold
            if is_active_gold:
                for frame in skill_sub_frames:
                    frame.grid_remove()
                is_active_skill = False
                is_active_pvm_pvp = False
            return_val = is_active_gold

        case "skill":
            # Flip the value based on press
            is_active_skill = not is_active_skill
            # Check what to do based on new val - if skill is now active...
            if is_active_skill:
                for frame in skill_sub_frames:
                    frame.grid_remove()
                is_active_gold = False
                is_active_pvm_pvp = False
            else:
                skill_frame.grid_remove()
            return_val = is_active_skill

        case "pvm pvp":
            is_active_pvm_pvp = not is_active_pvm_pvp
            if is_active_pvm_pvp:
                for frame in skill_sub_frames:
                    frame.grid_remove()
                is_active_gold = False
                is_active_skill = False
            return_val = is_active_pvm_pvp

    return return_val


# RETURN ALL FRAMES
def get_all_frames(root):
    sub_gui_label_font = tkinter.font.Font(family='Helvetica', size=12, weight='normal')

    main_frame = Frame(root, bg=frame_bg_color)
    main_frame.pack()
    main_frame.place(anchor='center', relx=0.5, rely=0.5)

    gold_frame = LabelFrame(main_frame, text="Money making", bg=label_frame_bg_color, font=sub_gui_label_font)
    skill_frame = LabelFrame(main_frame, text="Skill training", bg=label_frame_bg_color, font=sub_gui_label_font)
    pvm_pvp_frame = LabelFrame(main_frame, text="Combat helpers", bg=label_frame_bg_color, font=sub_gui_label_font)

    mining_frame = LabelFrame(main_frame, text="Mining", bg=label_frame_bg_color, font=sub_gui_label_font)
    smithing_frame = LabelFrame(main_frame, text="Smithing", bg=label_frame_bg_color, font=sub_gui_label_font)
    agility_frame = LabelFrame(main_frame, text="Agility", bg=label_frame_bg_color, font=sub_gui_label_font)

    skill_sub_frames = mining_frame, smithing_frame, agility_frame

    # Import All Frames & All Images from GUI Imports
    all_frames = main_frame, gold_frame, skill_frame, pvm_pvp_frame, skill_sub_frames
    return all_frames


# ----
# SHOW FRAME METHODS
# ----

def show_settings_frame():
    break_font = tkinter.font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = tkinter.font.Font(family='Helvetica', size=11, weight='bold')

    pwd = os.getcwd()
    settings_gui = Toplevel(pady=50, padx=50)
    settings_gui.title('Settings')
    settings_gui.iconbitmap(f'{pwd}\Assets\Images\Icon.ico')
    settings_gui.configure(bg='#969488')

    break_m = tkinter.StringVar(settings_gui)
    break_dev_m = tkinter.StringVar(settings_gui)
    interval_m = tkinter.StringVar(settings_gui)
    interval_dev_m = tkinter.StringVar(settings_gui)

    time_vars = break_m, break_dev_m, interval_m, interval_dev_m

    # Every 'a' minutes             (int_minutes)
    # Give or take 'b' minutes      (int_dev_minutes)
    # Break for 'c' minutes         (break_minutes)
    # Give or take 'd' minutes      (break_dev_minutes)

    test_img_1 = ImageTk.PhotoImage(Image.open(f'{pwd}\Assets\Images\GUI_Images\Gold\Cballs.png'))
    test_img_2 = ImageTk.PhotoImage(Image.open(f'{pwd}\Assets\Images\GUI_Images\Gold\Cballs.png'))

    bt_frame_1 = LabelFrame(settings_gui, text="⏱ Break Schedule", bg=frame_bg_color, pady=40, padx=40)

    e_min_label_prefix = Label(bt_frame_1, text="Every", background=frame_bg_color, font=break_font)
    e_min = Entry(bt_frame_1, textvariable=break_m, background=label_frame_bg_color, font=break_btn_font)
    e_min_label_suffix = Label(bt_frame_1, text="minutes,", background=frame_bg_color, font=break_font)

    e_min_label_prefix2 = Label(bt_frame_1, text="give or take", background=frame_bg_color, font=break_font)
    e_min2 = Entry(bt_frame_1, textvariable=break_dev_m, background=label_frame_bg_color, font=break_btn_font)
    e_min_label_suffix2 = Label(bt_frame_1, text="minutes,", background=frame_bg_color, font=break_font)

    e_min_label_prefix3 = Label(bt_frame_1, text="Break for", background=frame_bg_color, font=break_font)
    e_min3 = Entry(bt_frame_1, textvariable=interval_m, background=label_frame_bg_color, font=break_btn_font)
    e_min_label_suffix3 = Label(bt_frame_1, text="minutes,", background=frame_bg_color, font=break_font)

    e_min_label_prefix4 = Label(bt_frame_1, text="give or take", background=frame_bg_color, font=break_font)
    e_min4 = Entry(bt_frame_1, textvariable=interval_dev_m, background=label_frame_bg_color, font=break_btn_font)
    e_min_label_suffix4 = Label(bt_frame_1, text="minutes,", background=frame_bg_color, font=break_font)

    e_min_label_prefix.grid(row=1, column=1)
    e_min.grid(row=1, column=2, columnspan=1, padx=20, pady=10)
    e_min_label_suffix.grid(row=1, column=3, padx=10, pady=15)

    e_min_label_prefix2.grid(row=2, column=1)
    e_min2.grid(row=2, column=2, columnspan=1, padx=20, pady=10)
    e_min_label_suffix2.grid(row=2, column=3, padx=10, pady=15)

    e_min_label_prefix3.grid(row=3, column=1)
    e_min3.grid(row=3, column=2, columnspan=1, padx=20, pady=10)
    e_min_label_suffix3.grid(row=3, column=3, padx=10, pady=15)

    e_min_label_prefix4.grid(row=4, column=1)
    e_min4.grid(row=4, column=2, columnspan=1, padx=20, pady=10)
    e_min_label_suffix4.grid(row=4, column=3, padx=10, pady=15)

    test_btn = Button(bt_frame_1, fg='white', padx=10, pady=5, text="Set Schedule", font=break_btn_font, bg=btn_bg_color, activebackground=btn_active_bg_color, command=lambda: set_break_timer(time_vars, settings_gui))
    test_btn.grid(row=5, column=1, pady=20, padx=20, columnspan=3)

    bt_frame_1.grid(row=1, column=1)
    # hwd_frame_2 = LabelFrame(settings_gui, text="HWID", bg=frame_bg_color, height=250, width=450)
    # hwd_frame_2.grid(row=2, column=1)

    return


def show_gold_frame(all_frames, gold_gui_btns, toggle_active_frame, gui_btns):

    gold_btn, skill_btn, pvm_pvp_btn = gui_btns
    is_active = toggle_active_frame("gold", all_frames)
    # print(f'Entering 💰 Gold Frame with is_active: {not is_active} which is now: {is_active}')
    gold_btn.configure(bg=btn_active_bg_color)
    skill_btn.configure(bg=btn_bg_color)
    pvm_pvp_btn.configure(bg=btn_bg_color)

    cball_btn = gold_gui_btns
    main_frame, gold_frame, skill_frame, pvm_pvp_frame, skill_sub_frame = all_frames

    skill_frame.grid_remove()
    pvm_pvp_frame.grid_remove()

    gold_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    cball_btn.grid(row=1, column=1, padx=50, pady=35)

    # If is_active is false here, it was true when we clicked, therefore exit
    if not is_active:
        gold_frame.grid_remove()
        gold_btn.configure(bg=btn_bg_color)

    return


def show_skill_frame(all_frames, skill_gui_btns, toggle_active_frame, gui_btns):
    gold_btn, skill_btn, pvm_pvp_btn = gui_btns
    skill_btn_y_pad = 3
    skill_btn_x_pad = 5

    is_active = toggle_active_frame("skill", all_frames)
    # print(f'📊 Skill Frame with is_active: {not is_active} which is now: {is_active}')
    gold_btn.configure(bg=btn_bg_color)
    skill_btn.configure(bg=btn_active_bg_color)
    pvm_pvp_btn.configure(bg=btn_bg_color)

    attack_btn, hp_btn, mining_btn, strength_btn, agility_btn, smithing_btn = skill_gui_btns
    main_frame, gold_frame, skill_frame, pvm_pvp_frame, skill_sub_frame = all_frames

    gold_frame.grid_remove()
    pvm_pvp_frame.grid_remove()

    skill_frame.grid(row=sub_gui_row, column=1, columnspan=3, pady=50)

    # Top row
    attack_btn.grid(row=1, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    hp_btn.grid(row=1, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    mining_btn.grid(row=1, column=3, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    # Second row
    strength_btn.grid(row=2, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    agility_btn.grid(row=2, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    smithing_btn.grid(row=2, column=3, pady=skill_btn_y_pad, padx=skill_btn_x_pad)

    # If is_active is false here, it was true when we clicked, therefore exit
    if not is_active:
        skill_frame.grid_remove()
        skill_btn.configure(bg=btn_bg_color)

    return


def show_pvm_pvp_frame(all_frames, pvm_pvp_btns, toggle_active_frame, gui_btns):
    gold_btn, skill_btn, pvm_pvp_btn = gui_btns

    is_active = toggle_active_frame("pvm pvp", all_frames)
    # print(f'Entering ☠ PvM/PvP Frame with is_active: {not is_active} which is now: {is_active}')
    gold_btn.configure(bg=btn_bg_color)
    skill_btn.configure(bg=btn_bg_color)
    pvm_pvp_btn.configure(bg=btn_active_bg_color)

    ags_gmaul_btn = pvm_pvp_btns
    main_frame, gold_frame, skill_frame, pvm_pvp_frame, skill_sub_frame = all_frames

    gold_frame.grid_remove()
    skill_frame.grid_remove()

    pvm_pvp_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    ags_gmaul_btn.grid(row=1, column=1, pady=35, padx=50)

    # If is_active is false here, it was true when we clicked, therefore exit
    if not is_active:
        pvm_pvp_frame.grid_remove()
        pvm_pvp_btn.configure(bg=btn_bg_color)

    return


# ---
# SKILL FRAME - SUB-FRAMES
# ---
def show_mining_frame(all_frames, toggle_active_frame, iron_pisc_btn):
    # Close skill_frame
    _, _, _, _, skill_sub_frames = all_frames
    mining_frame, _, _ = skill_sub_frames

    is_active = toggle_active_frame("skill", all_frames)
    print(f'show_mining_frame - skill_frame - is_active: {is_active}')

    mining_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    mining_path = 'Assets\Images\GUI_Images\Stats\Mining'
    iron_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{mining_path}\iron_ore.png'))

    iron_img_label = Label(mining_frame, image=iron_img, height=100, width=100, bg=label_frame_bg_color)
    iron_img_label.image = iron_img

    # Load button with ore
    iron_img_label.grid(row=1, column=1)
    iron_pisc_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=30)

    return


def show_smithing_frame(all_frames, toggle_active_frame, edge_gold_btn):
    _, _, _, _, skill_sub_frames = all_frames
    _, smithing_frame, _ = skill_sub_frames

    is_active = toggle_active_frame("skill", all_frames)
    print(f'show_smithing_frame - skill_frame - is_active: {is_active}')

    smithing_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    smithing_path = 'Assets\Images\GUI_Images\Stats\Smithing'
    gold_bar_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{smithing_path}\gold_bar.png'))

    gold_img_label = Label(smithing_frame, image=gold_bar_img, height=100, width=100, bg=label_frame_bg_color)
    gold_img_label.image = gold_bar_img

    # Load button with ore
    gold_img_label.grid(row=1, column=1)
    edge_gold_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=30)

    return


def show_agility_frame(all_frames, toggle_active_frame, gnome_course_btn):
    _, _, _, _, skill_sub_frames = all_frames
    _, _, agility_frame = skill_sub_frames

    is_active = toggle_active_frame("skill", all_frames)
    print(f'show_agility_frame - skill_frame - is_active: {is_active}')

    agility_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    agility_path = 'Assets\Images\GUI_Images\Stats\Agility'
    gnome_course_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{agility_path}\Gnome_Course.png'))

    gold_img_label = Label(agility_frame, image=gnome_course_img, height=100, width=100, bg=label_frame_bg_color)
    gnome_course_img.image = gnome_course_img

    # Load button with ore
    gold_img_label.grid(row=1, column=1)
    gnome_course_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=30)
    return
