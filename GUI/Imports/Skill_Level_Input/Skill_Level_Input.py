import tkinter
import os
from tkinter import Toplevel, LabelFrame, Label, Entry, Button
from GUI.Imports.GUI_Frames import frame_bg_color, label_frame_bg_color, btn_bg_color, btn_active_bg_color
from osrs_api import Hiscores

initial_get = True


def show_skill_input_frame(skill_level_input_frame, t_active_frame, all_frames, username_arg=""):
    global initial_get

    break_font = tkinter.font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = tkinter.font.Font(family='Helvetica', size=11, weight='bold')

    is_active = t_active_frame("skill", all_frames)

    skill_level_input_frame.grid(row=3, column=1, columnspan=5, pady=50)

    user_search_sub_frame = LabelFrame(skill_level_input_frame, text="Lookup Level by User", bg=label_frame_bg_color, font=break_font)
    user_search_sub_frame.grid(row=1, pady=(20, 5))

    print(f'Show_Skill_Input_Frame Fired')
    assets_path = f"{os.getcwd()}\Assets"

    username_from_file = ""

    if username_arg == "":
        with open(f"{assets_path}\Levels.txt") as file:
            username_from_file = file.readline()
            username_from_file = username_from_file.replace("\n", "")

    username_var = tkinter.StringVar(user_search_sub_frame)

    if initial_get:
        username_var.set(username_from_file)
    else:
        username_var.set(username_arg)

    # username_label = Label(user_search_sub_frame, text="Search Username", background=frame_bg_color, font=break_font)
    username_input = Entry(user_search_sub_frame, textvariable=username_var, background=label_frame_bg_color, font=break_btn_font)

    if username_from_file and initial_get:
        print(f'Found username ({username_from_file}) in {assets_path}\Levels.txt')
        user_hiscores = get_hiscores_for_user(username_from_file, user_search_sub_frame, t_active_frame, all_frames)
        initial_get = False
    elif username_arg == "" and not initial_get:
        print(f'Fetching HiScores for user from file (not intial and no arg passed): {username_arg}')
        user_hiscores = get_hiscores_for_user(username_from_file, user_search_sub_frame, t_active_frame, all_frames)
    else:
        print(f'Fetching HiScores for user_arg: {username_arg}')
        user_hiscores = get_hiscores_for_user(username_arg, user_search_sub_frame, t_active_frame, all_frames)

    # username_label.grid(row=1, column=1)
    username_input.grid(row=1, column=1, padx=20, pady=10)

    username_lookup_btn = Button(user_search_sub_frame, font=break_btn_font, text="Search User", bg=btn_bg_color, activebackground=btn_active_bg_color, command=lambda: show_skill_input_frame(skill_level_input_frame, t_active_frame, all_frames, username_arg=username_input.get()))

    username_lookup_btn.grid(row=2, column=1, columnspan=3, pady=10)

    # SKILL LEVEL INPUTS
    skill_level_input_sub_frame = LabelFrame(skill_level_input_frame, text="Levels", bg=label_frame_bg_color, font=break_font, padx=40, pady=20)
    skill_level_input_sub_frame.grid(row=2)

    attack_level_var = tkinter.StringVar(skill_level_input_frame)
    attack_level_var.set(user_hiscores.skills['attack'].level)
    attack_label = Label(skill_level_input_sub_frame, text="Attack:", background=frame_bg_color, font=break_font)
    attack_input = Entry(skill_level_input_sub_frame, textvariable=attack_level_var, background=label_frame_bg_color, font=break_btn_font, width=3)
    attack_label.grid(row=3, column=1, padx=0)
    attack_input.grid(row=3, column=2, pady=0, padx=(5, 15))

    hp_level_var = tkinter.StringVar(skill_level_input_sub_frame)
    hp_level_var.set(user_hiscores.skills['hitpoints'].level)
    hp_label = Label(skill_level_input_sub_frame, text="Hitpoints:", background=frame_bg_color, font=break_font)
    hp_input = Entry(skill_level_input_sub_frame, textvariable=hp_level_var, background=label_frame_bg_color, font=break_btn_font, width=3)
    hp_label.grid(row=3, column=3)
    hp_input.grid(row=3, column=4, padx=(5, 15))

    mining_level_var = tkinter.StringVar(skill_level_input_sub_frame)
    mining_level_var.set(user_hiscores.skills['mining'].level)
    mining_label = Label(skill_level_input_sub_frame, text="Mining:", background=frame_bg_color, font=break_font)
    mining_input = Entry(skill_level_input_sub_frame, textvariable=mining_level_var, background=label_frame_bg_color, font=break_btn_font, width=3)
    mining_label.grid(row=3, column=5)
    mining_input.grid(row=3, column=6, padx=(5, 15))

    return


def get_hiscores_for_user(username, skill_level_input_frame, t_active_frame, all_frames):
    global initial_get

    # raw_username = username.get()
    if type(username) == tkinter.StringVar:
        print(f'StringVar detected. Using get() to extract...')
        username = username.get()

    print(f'username = {username}')

    cleaned_username = username.replace(' ', '_').lower()

    print(f'Fetching HiScores for user: {cleaned_username}')

    user_hiscores = Hiscores(cleaned_username)

    print(f'hiscores for: {cleaned_username} = \n{user_hiscores}')
    print(f"Attack = {user_hiscores.skills['attack'].level}")
    print(f"Agility = {user_hiscores.skills['agility'].level}")

    assets_path = f"{os.getcwd()}\Assets"

    with open(f'{assets_path}\Levels.txt', 'w') as file:
        file.write(f"{cleaned_username}\n")
        file.write(str(user_hiscores))

    return user_hiscores

