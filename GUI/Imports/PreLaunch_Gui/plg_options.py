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

        Global_Script_Options.script_name = script_name
        # Add curr_option field and value (type ScriptOption) to the Global_Script_Options options_arr property

        for option in Global_Script_Options.options_arr:
            if option.name == option_field:
                print(f'Found this option field ({option.name}) - updating value ({new_option_value}) instead of appending this field')
                option.value = new_option_value
                return
            else:
                print(f'Failed to find option.name: {option.name}')

        print(f'Must not have seen any option: {option_field} - Appending with value: {new_option_value} to array')
        curr_option_val = ScriptOption(option_name=option_field, option_value=new_option_value)
        Global_Script_Options.options_arr.append(curr_option_val)

        for option in Global_Script_Options.options_arr:
            print(f'Script = {Global_Script_Options.script_name} Option: {option}')

        return

    script_options_frame = LabelFrame(main_plg_frame, text=f"Additional Options - ({script_name})", bg=frame_bg_color, pady=40, padx=40, width=250)

    # Determines what option buttons to show at the bottom of the Pre-Launch GUI based on the script
    agility_scripts = ["Gnome_Course", "Canifis_Rooftops", "Seers_Rooftops", "Ardy_Rooftops"]

    match script_name:
        case script_name if script_name in agility_scripts:
            script_name = 'Gnome_Course'
            field_name = 'High Alch'

            alch_item = tkinter.StringVar(None, "none")

            option_1 = tkinter.Radiobutton(script_options_frame, variable=alch_item, tristatevalue=1, value="none", text="No Alch", font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, alch_item.get()))
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Radiobutton(script_options_frame, variable=alch_item, tristatevalue=0, value="magic_long_noted", text="Magic Longbow (noted)", font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, alch_item.get()))
            option_1.grid(row=1, column=2)
            option_1 = tkinter.Radiobutton(script_options_frame, variable=alch_item, tristatevalue=0, value="green_dhide_bodies_noted", text="Green Dhide Body (noted)", font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, alch_item.get()))
            option_1.grid(row=1, column=3)

        case "Ardy_Knights":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Dodgy Necklace (Jewelry tab)", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)

        case "Draynor_Shrimp":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Bank Shrimp", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)

        case "Hosidius_Fruit":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Bank Fruit", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)

        case "GE_Bow_Stringer":
            option_1 = tkinter.Radiobutton(script_options_frame, text="Magic Long", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)

        case "GE_Dhide_Bodies":
            option_1 = tkinter.Radiobutton(script_options_frame, text="Green Leather", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)

        case "Tithe_Farmer":
            option_1 = tkinter.Radiobutton(script_options_frame, text="Regular Cans (8)", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Gricollers Can", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=2)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Use Humidfy", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=3)

        case "Blast_Furnace":
            option_1 = tkinter.Radiobutton(script_options_frame, text="Gold Bars", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Runite Bars", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=2)

        case "Poh_Larders":
            script_name = 'Poh_Larders'
            field_name = 'Plank Type'

            plank_type_var = tkinter.StringVar(None, "Wood")
            set_option(script_name, field_name, 'Wood')

            option_1 = tkinter.Radiobutton(script_options_frame, tristatevalue=1, value='Wood', variable=plank_type_var, text="Wood", font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, plank_type_var.get()))
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Radiobutton(script_options_frame, tristatevalue=0, value='Oak', variable=plank_type_var, text="Oak", font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, plank_type_var.get()))
            option_1.grid(row=1, column=2)

        case "Lummy_Chop_And_Fletcher":
            script_name = 'Lummy_Chop_And_Fletcher'
            field_name = 'Fletch Item'

            fletch_item_var = tkinter.StringVar(None, "Arrows")
            set_option(script_name, field_name, 'Arrows')

            option_1 = tkinter.Radiobutton(script_options_frame, text="Arrows Shafts", value='Arrows', variable=fletch_item_var, tristatevalue=1, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, fletch_item_var.get()))
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Javeline Shafts", value='Javelines', variable=fletch_item_var, tristatevalue=0, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, fletch_item_var.get()))
            option_1.grid(row=1, column=2)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Shortbows", value='Shortbows', variable=fletch_item_var, tristatevalue=0, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, fletch_item_var.get()))
            option_1.grid(row=1, column=3)
            option_1 = tkinter.Radiobutton(script_options_frame, text="Longbows", value='Longbows', variable=fletch_item_var, tristatevalue=0, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, fletch_item_var.get()))
            option_1.grid(row=1, column=4)
            option_1 = tkinter.Radiobutton(script_options_frame, text="C'bow Stock", value='Cbow', variable=fletch_item_var, tristatevalue=0, font=break_font, background=frame_bg_color, command=lambda: set_option(script_name, field_name, fletch_item_var.get()))
            option_1.grid(row=2, column=2)

        case "Ardy_Knights":
            option_1 = tkinter.Checkbutton(script_options_frame, text="Wine", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Lobster", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=2)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Monkfish", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=3)
            option_1 = tkinter.Checkbutton(script_options_frame, text="Shark", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=4)

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

    script_options_frame.grid(row=4, column=1)

    return


def get_script_options(field_name):
    for option in Global_Script_Options.options_arr:
        print(f'get_script_options: (field_name: {field_name}) option_name: {option.name} & value: {option.value}')
        if option.name == field_name:
            print(f'Found Item option for field_name {field_name} | option_value: {option.value}')
            return option.value

    return False
