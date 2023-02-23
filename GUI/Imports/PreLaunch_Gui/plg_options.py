import tkinter
from tkinter import LabelFrame

from GUI.Imports.PreLaunch_Gui.Plg_Script_Options import Global_Script_Options, ScriptOption
from GUI.Imports.Skill_Level_Input.Skill_Level_Input import get_skill_level

frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_plg_options(main_plg_frame, font_styles, script_name):
    break_font, break_btn_font = font_styles

    def set_option(script_name, option_field, new_option_value):
        print(f'script_name = {script_name}')
        print(f'options_field = {option_field}')
        print(f'options_value = {new_option_value}')
        print(f'plg_script_options = {Global_Script_Options}')
        # plg_script_options

        # TODO - Using script_name, find the corresponding plg_script_options obj and set the option_string

        Global_Script_Options.SCRIPT_NAME = script_name
        # Add curr_option field and value (type ScriptOption) to the Global_Script_Options options_arr property

        for option in Global_Script_Options.options_arr:
            if option.name == option_field:
                print(f'Found this option field ({option.name}) - updating value ({new_option_value}) instead of appending this field')
                return
            else:
                print(f'Failed to find option.name: {option.name}')

        print(f'Must not have seen any option: {option_field} - Appending with value: {new_option_value} to array')
        curr_option_val = ScriptOption(option_name=option_field, option_value=new_option_value)
        Global_Script_Options.options_arr.append(curr_option_val)

        for option in Global_Script_Options.options_arr:
            print(f'Script = {Global_Script_Options.SCRIPT_NAME} Option: {option}')

        return

    script_options_frame = LabelFrame(main_plg_frame, text=f"Additional Options - ({script_name})", bg=frame_bg_color, pady=40, padx=40, width=250)

    # Determines what option buttons to show at the bottom of the Pre-Launch GUI based on the script
    match script_name:
        case "Ardy_Knights":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Dodgy Necklace (Jewelry tab)", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
        case "Cwars_Teak":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Bank Logs", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Use Ring of Dueling", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=2)
        case "Cwars_Lavas":
            option_1 = tkinter.Radiobutton(script_options_frame, text="Small Pouch", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Medium Pouch", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=2)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Large Pouch", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=3)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Giant Pouch", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=4)
        case "Poh_Larder":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Wood", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Oak", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=2)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Level-based", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=3)
        case "Poh_Table":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Wood", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
        case "Rogue_Cooker":
            script_name = 'Rogue_Cooker'
            field_name = 'Food Type'
            cooking_lvl = get_skill_level(skill_name='cooking')
            print(f'Fetched cooking level: {cooking_lvl}')

            if cooking_lvl < 40:
                # rogue_cooker_var = tkinter.IntVar()
                print(f'Setting default food type to: shrimp')
                rogue_cooker_var = tkinter.StringVar(None, "Shrimp")
                set_option(script_name, field_name, 'Shrimp')

            elif 40 >= cooking_lvl < 62:
                # rogue_cooker_var = tkinter.IntVar()
                print(f'Setting default food type to: lobs')
                rogue_cooker_var = tkinter.StringVar(None, "Lobster")
                set_option(script_name, field_name, 'Lobster')

            elif 62 >= cooking_lvl < 80:
                # rogue_cooker_var = tkinter.IntVar()
                print(f'Setting default food type to: monks')
                rogue_cooker_var = tkinter.StringVar(None, "Monkfish")
                set_option(script_name, field_name, 'Monkfish')

            else:
                # rogue_cooker_var = tkinter.IntVar()
                print(f'Setting default food type to: sharks')
                rogue_cooker_var = tkinter.StringVar(None, "Shark")
                set_option(script_name, field_name, 'Shark')

            option_1 = tkinter.Radiobutton(script_options_frame, text="Shrimp", value='Shrimp', variable=rogue_cooker_var, tristatevalue=0, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, rogue_cooker_var.get()))
            option_1.grid(row=1, column=1, columnspan=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Lobster", value='Lobster', variable=rogue_cooker_var, tristatevalue=0, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, rogue_cooker_var.get()))
            option_1.grid(row=1, column=2, columnspan=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Monkfish", value='Monkfish', variable=rogue_cooker_var, tristatevalue=0, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, rogue_cooker_var.get()))
            option_1.grid(row=1, column=3, columnspan=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Shark", value='Shark', variable=rogue_cooker_var, tristatevalue=1, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, rogue_cooker_var.get()))
            option_1.grid(row=1, column=4, columnspan=1)
        case "Kourend_Crab_Killer":
            option_1 = tkinter.Radiobutton(script_options_frame, text="Attack", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Strength", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=2)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Defense", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=3)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Range", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=4)

            option_1 = tkinter.Checkbutton(script_options_frame, text="Super Attack", font=break_font, background=frame_bg_color)
            option_1.grid(row=2, column=1, pady=10, padx=10, columnspan=2)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Super Strength", font=break_font, background=frame_bg_color)
            option_1.grid(row=2, column=3, pady=10, padx=10, columnspan=2)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Range Potion", font=break_font, background=frame_bg_color)
            option_1.grid(row=2, column=5, pady=10, padx=10, columnspan=2)

    script_options_frame.grid(row=4, column=1)

    return
