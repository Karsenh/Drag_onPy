import tkinter
import os
from tkinter import Toplevel, LabelFrame, Label, Entry, Button
from GUI.Imports.GUI_Frames import frame_bg_color, label_frame_bg_color, btn_bg_color, btn_active_bg_color
from osrs_api import Hiscores
from API.Debug import write_debug

initial_get = True


def show_skill_input_frame(skill_level_input_frame, t_active_frame, all_frames, username_arg=""):
    global initial_get

    break_font = tkinter.font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = tkinter.font.Font(family='Helvetica', size=11, weight='bold')

    is_active = t_active_frame("skill", all_frames)

    skill_level_input_frame.grid(row=3, column=1, columnspan=4, pady=20)

    user_search_sub_frame = LabelFrame(skill_level_input_frame, text="Load Levels by User", bg=label_frame_bg_color, font=break_font)
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
    elif username_arg == "" and not initial_get:
        username_var.set(username_from_file)
    else:
        username_var.set(username_arg)

    # username_label = Label(user_search_sub_frame, text="Search Username", background=frame_bg_color, font=break_font)
    username_input = Entry(user_search_sub_frame, textvariable=username_var, background=label_frame_bg_color, font=break_btn_font)

    if username_from_file and initial_get:
        print(f'Found username ({username_from_file}) in {assets_path}\Levels.txt')
        user_hiscores = fetch_hiscores_for_user(username_from_file)
        initial_get = False
    elif username_arg == "" and not initial_get:
        print(f'Fetching HiScores for user from file (not intial and no arg passed): {username_arg}')
        user_hiscores = fetch_hiscores_for_user(username_from_file)
    else:
        print(f'Fetching HiScores for user_arg: {username_arg}')
        user_hiscores = fetch_hiscores_for_user(username_arg)

    # username_label.grid(row=1, column=1)
    username_input.grid(row=1, column=1, padx=20, pady=10)

    username_lookup_btn = Button(user_search_sub_frame, fg="white", font=break_btn_font, text="Search User", bg=btn_bg_color, activebackground=btn_active_bg_color, command=lambda: show_skill_input_frame(skill_level_input_frame, t_active_frame, all_frames, username_arg=username_input.get()))

    username_lookup_btn.grid(row=2, column=1, columnspan=3, pady=10)

    # SKILL LEVEL INPUTS
    skill_level_input_sub_frame = LabelFrame(skill_level_input_frame, text="Input Levels", bg=label_frame_bg_color, font=break_font)
    skill_level_input_sub_frame.grid(row=2, padx=(10, 10), pady=20)

    add_new_skill_input("attack", skill_level_input_sub_frame, user_hiscores, row=3, start_col=1)
    add_new_skill_input("hitpoints", skill_level_input_sub_frame, user_hiscores, row=3, start_col=3)
    add_new_skill_input("mining", skill_level_input_sub_frame, user_hiscores, row=3, start_col=5)

    add_new_skill_input("strength", skill_level_input_sub_frame, user_hiscores, row=4, start_col=1)
    add_new_skill_input("agility", skill_level_input_sub_frame, user_hiscores, row=4, start_col=3)
    add_new_skill_input("smithing", skill_level_input_sub_frame, user_hiscores, row=4, start_col=5)

    add_new_skill_input("defence", skill_level_input_sub_frame, user_hiscores, row=5, start_col=1)
    add_new_skill_input("herblore", skill_level_input_sub_frame, user_hiscores, row=5, start_col=3)
    add_new_skill_input("fishing", skill_level_input_sub_frame, user_hiscores, row=5, start_col=5)

    add_new_skill_input("ranged", skill_level_input_sub_frame, user_hiscores, row=6, start_col=1)
    add_new_skill_input("thieving", skill_level_input_sub_frame, user_hiscores, row=6, start_col=3)
    add_new_skill_input("cooking", skill_level_input_sub_frame, user_hiscores, row=6, start_col=5)

    add_new_skill_input("prayer", skill_level_input_sub_frame, user_hiscores, row=7, start_col=1)
    add_new_skill_input("crafting", skill_level_input_sub_frame, user_hiscores, row=7, start_col=3)
    add_new_skill_input("firemaking", skill_level_input_sub_frame, user_hiscores, row=7, start_col=5)

    add_new_skill_input("magic", skill_level_input_sub_frame, user_hiscores, row=8, start_col=1)
    add_new_skill_input("fletching", skill_level_input_sub_frame, user_hiscores, row=8, start_col=3)
    add_new_skill_input("woodcutting", skill_level_input_sub_frame, user_hiscores, row=8, start_col=5)

    add_new_skill_input("runecrafting", skill_level_input_sub_frame, user_hiscores, row=9, start_col=1)
    add_new_skill_input("slayer", skill_level_input_sub_frame, user_hiscores, row=9, start_col=3)
    add_new_skill_input("farming", skill_level_input_sub_frame, user_hiscores, row=9, start_col=5)

    add_new_skill_input("construction", skill_level_input_sub_frame, user_hiscores, row=10, start_col=1)
    add_new_skill_input("hunter", skill_level_input_sub_frame, user_hiscores, row=10, start_col=3)

    save_levels_btn = Button(skill_level_input_sub_frame, state='disabled', font=break_btn_font, text="Update Levels", bg=btn_bg_color, activebackground=btn_active_bg_color, command=lambda: save_hs_to_file(username_var.get(), user_hiscores))
    save_levels_btn.grid(row=11, column=1, columnspan=6, pady="20")

    return


def add_new_skill_input(skill_name, skill_level_input_sub_frame, user_hiscores, row, start_col):
    break_font = tkinter.font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = tkinter.font.Font(family='Helvetica', size=11, weight='bold')

    mining_level_var = tkinter.StringVar(skill_level_input_sub_frame)
    mining_level_var.set(user_hiscores.skills[f'{skill_name}'].level)
    mining_label = Label(skill_level_input_sub_frame, text=f"{skill_name.capitalize()}:", background=frame_bg_color, font=break_font)
    mining_input = Entry(skill_level_input_sub_frame, textvariable=mining_level_var, background=label_frame_bg_color, font=break_btn_font, width=3)
    mining_label.grid(row=row, column=start_col, pady=(15, 0), sticky='W')
    mining_input.grid(row=row, column=start_col+1, padx=(5, 15), pady=(15, 0))
    return


def fetch_hiscores_for_user(username):
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

    save_hs_to_file(username, user_hiscores)

    return user_hiscores


def save_hs_to_file(username, hiScores):
    assets_path = f"{os.getcwd()}\Assets"

    with open(f'{assets_path}\Levels.txt', 'w') as file:
        file.write(f"{username}\n")
        file.write(str(hiScores))
    return


def get_skill_level(skill_name="agility", should_update_file=False):
    levels_txt_file_path = f'{os.getcwd()}\Assets\Levels.txt'

    if should_update_file:
        with open(levels_txt_file_path, 'r') as file:
            username = file.readline().replace("\n", "")
        # Fetch hiscores and update file
        hi_scores = fetch_hiscores_for_user(username)
        save_hs_to_file(username, hi_scores)
        write_debug(f'✔Updated Skill levels file for {username}')

    search_skill = f'={skill_name}'
    search_line = ""
    with open(levels_txt_file_path, "r") as file:
        file_lines = file.readlines()
        for line in file_lines:
            if search_skill in line:
                print(f'Line contains skill_name: {line}')
                search_line = line
            # print(f'line: {line}')

    if search_line:
        trimmed_level = search_line.split('level=')[1].split(',')[0]
        print(f'trimmed_level = {trimmed_level}')
        return int(trimmed_level)

    else:
        return None


def update_skill_level(skill, specific_level=None, increment=True):
    if not increment:
        if not specific_level:
            write_debug(f'Need to specify a level to update if not incrementing by 1.')
            return False
        else:
            print(f'Updating skill: {skill} in file to specific_level: {specific_level}')
    else:
        # Increment the skill arg by one
        write_debug(f'Incrementing skill: {skill} in file to {get_skill_level(skill)+1}')

    return True
