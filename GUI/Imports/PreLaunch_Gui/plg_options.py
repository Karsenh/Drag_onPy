import tkinter
from tkinter import LabelFrame

frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_plg_options(main_plg_frame, font_styles, script_name):
    break_font, break_btn_font = font_styles

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
