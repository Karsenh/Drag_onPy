import tkinter.font
from GUI.Main_GUI import *
from API.Break_Timer.Timer import *
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from API.Debug import *


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

    defence_frame = LabelFrame(main_frame, text="Defence", bg=label_frame_bg_color, font=sub_gui_label_font)
    herblore_frame = LabelFrame(main_frame, text="Herblore", bg=label_frame_bg_color, font=sub_gui_label_font)
    fishing_frame = LabelFrame(main_frame, text="Fishing", bg=label_frame_bg_color, font=sub_gui_label_font)

    ranged_frame = LabelFrame(main_frame, text="Ranged", bg=label_frame_bg_color, font=sub_gui_label_font)
    thieving_frame = LabelFrame(main_frame, text="Thieving", bg=label_frame_bg_color, font=sub_gui_label_font)
    cooking_frame = LabelFrame(main_frame, text="Cooking", bg=label_frame_bg_color, font=sub_gui_label_font)

    prayer_frame = LabelFrame(main_frame, text="Prayer", bg=label_frame_bg_color, font=sub_gui_label_font)
    crafting_frame = LabelFrame(main_frame, text="Crafting", bg=label_frame_bg_color, font=sub_gui_label_font)
    firemaking_frame = LabelFrame(main_frame, text="Firemaking", bg=label_frame_bg_color, font=sub_gui_label_font)

    magic_frame = LabelFrame(main_frame, text="Magic", bg=label_frame_bg_color, font=sub_gui_label_font)
    fletching_frame = LabelFrame(main_frame, text="Fletching", bg=label_frame_bg_color, font=sub_gui_label_font)
    woodcutting_frame = LabelFrame(main_frame, text="Woodcutting", bg=label_frame_bg_color, font=sub_gui_label_font)

    runecrafting_frame = LabelFrame(main_frame, text="Runecrafting", bg=label_frame_bg_color, font=sub_gui_label_font)
    slayer_frame = LabelFrame(main_frame, text="Slayer", bg=label_frame_bg_color, font=sub_gui_label_font)
    farming_frame = LabelFrame(main_frame, text="Farming", bg=label_frame_bg_color, font=sub_gui_label_font)

    construction_frame = LabelFrame(main_frame, text="Construction", bg=label_frame_bg_color, font=sub_gui_label_font)
    hunter_frame = LabelFrame(main_frame, text="Hunter", bg=label_frame_bg_color, font=sub_gui_label_font)

    skill_sub_frames = mining_frame, smithing_frame, agility_frame, \
                       defence_frame, herblore_frame, fishing_frame, \
                       ranged_frame, thieving_frame, cooking_frame, \
                       prayer_frame, crafting_frame, firemaking_frame, \
                       magic_frame, fletching_frame, woodcutting_frame, \
                       runecrafting_frame, slayer_frame, farming_frame, \
                       construction_frame, hunter_frame

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

    # Break Timer Frame
    bt_frame_1.grid(row=1, column=1)

    # DEBUG MODE
    # sep = tkinter.ttk.Separator(settings_gui, orient="horizontal")
    # sep.grid(row=6, column=1, columnspan=4)

    db_frame_2 = LabelFrame(settings_gui, text="🐛 Debugging", bg=frame_bg_color, pady=40, padx=40)

    # Debug checkbox variable
    is_debug = tkinter.IntVar()

    is_debug_cb = tkinter.Checkbutton(db_frame_2, text='Enable DEBUG', bg=frame_bg_color, variable=is_debug, offvalue=False, onvalue=True, command=lambda: set_is_debug(is_debug))
    is_debug_cb.grid(row=1, column=1)

    # Debug Frame
    db_frame_2.grid(row=2, column=1)


    return


def show_gold_frame(all_frames, gold_gui_btns, t_active_frame, gui_btns):

    gold_btn, skill_btn, pvm_pvp_btn = gui_btns
    is_active = t_active_frame("gold", all_frames)
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


def show_skill_frame(all_frames, skill_gui_btns, t_active_frame, gui_btns):
    gold_btn, skill_btn, pvm_pvp_btn = gui_btns
    skill_btn_y_pad = 3
    skill_btn_x_pad = 5

    is_active = t_active_frame("skill", all_frames)
    # print(f'📊 Skill Frame with is_active: {not is_active} which is now: {is_active}')
    gold_btn.configure(bg=btn_bg_color)
    skill_btn.configure(bg=btn_active_bg_color)
    pvm_pvp_btn.configure(bg=btn_bg_color)

    attack_btn, hp_btn, mining_btn, \
    strength_btn, agility_btn, smithing_btn, \
    defence_btn, herblore_btn, fishing_btn, \
    ranged_btn, thieving_btn, cooking_btn, \
    prayer_btn, crafting_btn, firemaking_btn, \
    magic_btn, fletching_btn, woodcutting_btn, \
    runecrafting_btn, slayer_btn, farming_btn, \
    construction_btn, hunter_btn = skill_gui_btns

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
    # Third row
    defence_btn.grid(row=3, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    herblore_btn.grid(row=3, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    fishing_btn.grid(row=3, column=3, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    # Fourth row
    ranged_btn.grid(row=4, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    thieving_btn.grid(row=4, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    cooking_btn.grid(row=4, column=3, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    # Fifth row
    prayer_btn.grid(row=5, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    crafting_btn.grid(row=5, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    firemaking_btn.grid(row=5, column=3, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    # Sixth row
    magic_btn.grid(row=6, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    fletching_btn.grid(row=6, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    woodcutting_btn.grid(row=6, column=3, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    # Seventh row
    runecrafting_btn.grid(row=7, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    slayer_btn.grid(row=7, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    farming_btn.grid(row=7, column=3, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    # Eighth row
    construction_btn.grid(row=8, column=1, pady=skill_btn_y_pad, padx=skill_btn_x_pad)
    hunter_btn.grid(row=8, column=2, pady=skill_btn_y_pad, padx=skill_btn_x_pad)

    # If is_active is false here, it was true when we clicked, therefore exit
    if not is_active:
        skill_frame.grid_remove()
        skill_btn.configure(bg=btn_bg_color)

    return


def show_pvm_pvp_frame(all_frames, pvm_pvp_btns, t_active_frame, gui_btns):
    gold_btn, skill_btn, pvm_pvp_btn = gui_btns

    is_active = t_active_frame("pvm pvp", all_frames)
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
def show_mining_frame(all_frames, t_active_frame, mining_frame, mining_sub_btns):
    # Close skill_frame
    _, _, _, _, skill_sub_frames = all_frames
    # mining_frame, _, _, _, _, _, _, _, _ = skill_sub_frames
    iron_pisc_btn = mining_sub_btns

    is_active = t_active_frame("skill", all_frames)
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


def show_smithing_frame(all_frames, t_active_frame, smithing_frame, smithing_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames
    # _, smithing_frame, _, _, _, _, _, _, _ = skill_sub_frames
    edge_gold_btn = smithing_sub_btns

    is_active = t_active_frame("skill", all_frames)
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


def show_agility_frame(all_frames, t_active_frame, agility_frame, agility_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames
    # _, _, agility_frame, _, _, _, _, _, _ = skill_sub_frames
    gnome_course_btn = agility_sub_btns

    is_active = t_active_frame("skill", all_frames)
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


def show_defence_frame(all_frames, t_active_frame, defence_frame, defence_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames
    # _, _, _, defence_frame, _, _, _, _, _ = skill_sub_frames

    is_active = t_active_frame("skill", all_frames)
    print(f'show_defence_frame - skill_frame - is_active: {is_active}')

    defence_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    defence_img_path = 'Assets\Images\GUI_Images\Stats\Defence'
    gnome_course_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{defence_img_path}\Gnome_Course.png'))

    gold_img_label = Label(defence_frame, image=gnome_course_img, height=100, width=100, bg=label_frame_bg_color)
    gnome_course_img.image = gnome_course_img

    # Load button with ore
    gold_img_label.grid(row=1, column=1)
    # gnome_course_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=30)
    return


def show_herblore_frame(all_frames, t_active_frame, herblore_frame, herblore_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames
    # _, _, _, _, herblore_frame, _, _, _, _ = skill_sub_frames

    is_active = t_active_frame("skill", all_frames)
    print(f'show_herblore_frame - skill_frame - is_active: {is_active}')

    herblore_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    herblore_img_path = 'Assets\Images\GUI_Images\Stats\Herblore'
    gnome_course_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{herblore_img_path}\Gnome_Course.png'))

    gold_img_label = Label(herblore_frame, image=gnome_course_img, height=100, width=100, bg=label_frame_bg_color)
    gnome_course_img.image = gnome_course_img

    # Load button with ore
    gold_img_label.grid(row=1, column=1)
    # gnome_course_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=30)
    return


def show_fishing_frame(all_frames, t_active_frame, fishing_frame, fishing_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames
    # _, _, _, _, _, fishing_frame, _, _, _ = skill_sub_frames

    draynor_shrimp_btn, barb_trout_btn, barb_fishing_btn = fishing_sub_btns

    is_active = t_active_frame("skill", all_frames)
    print(f'show_fishing_frame - skill_frame - is_active: {is_active}')

    fishing_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    fishing_img_path = 'Assets\Images\GUI_Images\Stats\Fishing'

    draynor_man_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{fishing_img_path}\Shrimp.png'))

    draynor_man_label = Label(fishing_frame, image=draynor_man_img, height=100, width=100, bg=label_frame_bg_color)
    draynor_man_img.image = draynor_man_img

    ardy_cake_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{fishing_img_path}\Trout.png'))

    barb_trout_label = Label(fishing_frame, image=ardy_cake_img, height=100, width=100, bg=label_frame_bg_color)
    ardy_cake_img.image = ardy_cake_img

    barb_fishing_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{fishing_img_path}\leaping_sturgeon.png'))

    barb_fishing_label = Label(fishing_frame, image=barb_fishing_img, height=100, width=100, bg=label_frame_bg_color)
    barb_fishing_img.image = barb_fishing_img

    draynor_man_label.grid(row=1, column=1, padx=35)
    draynor_shrimp_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=25)

    barb_trout_label.grid(row=2, column=1, padx=35)
    barb_trout_btn.grid(row=2, column=2, columnspan=2, pady=20, padx=25)

    barb_fishing_label.grid(row=3, column=1, padx=35)
    barb_fishing_btn.grid(row=3, column=2, columnspan=2, pady=20, padx=25)

    return


def show_ranged_frame():

    return


def show_cooking_frame(all_frames, t_active_frame, cooking_frame, cooking_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames
    rogue_cooker_btn = cooking_sub_btns

    is_active = t_active_frame("skill", all_frames)
    print(f'show_cooking_frame - skill_frame - is_active: {is_active}')

    cooking_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    cooking_img_path = 'Assets\Images\GUI_Images\Stats\Cooking'

    # Draynor Man
    fire_gif = Image.open(f'{os.getcwd()}\{cooking_img_path}\Fire.png')
    rogue_cooker_map_image = ImageTk.PhotoImage(fire_gif)

    rogue_cooker_label = Label(cooking_frame, image=rogue_cooker_map_image, height=100, width=100, bg=label_frame_bg_color)
    rogue_cooker_map_image.image = rogue_cooker_map_image

    rogue_cooker_label.grid(row=1, column=1, padx=35)
    rogue_cooker_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=25)

    return


def show_thieving_frame(all_frames, t_active_frame, thieving_frame, thieving_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames

    draynor_man_btn, ardy_cake_btn = thieving_sub_btns

    is_active = t_active_frame("skill", all_frames)
    print(f'show_fishing_frame - skill_frame - is_active: {is_active}')

    thieving_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    thieving_img_path = 'Assets\Images\GUI_Images\Stats\Thieving'

    # Draynor Man
    draynor_man_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{thieving_img_path}\draynor_man.png'))

    draynor_man_label = Label(thieving_frame, image=draynor_man_img, height=100, width=100, bg=label_frame_bg_color)
    draynor_man_img.image = draynor_man_img

    # Ardy Cake
    ardy_cake_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{thieving_img_path}\Cake.png'))

    barb_trout_label = Label(thieving_frame, image=ardy_cake_img, height=100, width=100, bg=label_frame_bg_color)
    ardy_cake_img.image = ardy_cake_img


    draynor_man_label.grid(row=1, column=1, padx=35)
    draynor_man_btn.grid(row=1, column=2, columnspan=2, pady=20, padx=25)

    barb_trout_label.grid(row=2, column=1, padx=35)
    ardy_cake_btn.grid(row=2, column=2, columnspan=2, pady=20, padx=25)

    return


def show_firemaking_frame(all_frames, t_active_frame, firemaking_frame, firemaking_sub_btns):
    _, _, _, _, skill_sub_frames = all_frames
    ge_log_burner = firemaking_sub_btns

    is_active = t_active_frame("skill", all_frames)
    print(f'show_firemaking_frame - skill_frame - is_active: {is_active}')

    firemaking_frame.grid(row=sub_gui_row, column=1, columnspan=5, pady=50)

    firemaking_img_path = 'Assets\Images\GUI_Images\Stats\Firemaking'
    tinderbox_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{firemaking_img_path}\Tinderbox.png'))

    tinderbox_img_label = Label(firemaking_frame, image=tinderbox_img, height=100, width=100, bg=label_frame_bg_color)
    tinderbox_img_label.image = tinderbox_img

    # Load button with ore
    tinderbox_img_label.grid(row=1, column=1)
    ge_log_burner.grid(row=1, column=2, columnspan=2, pady=20, padx=30)
    return
