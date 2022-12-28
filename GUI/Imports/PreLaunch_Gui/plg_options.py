import tkinter
from tkinter import LabelFrame

frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_plg_options(main_plg_frame, font_styles, script_name):
    break_font, break_btn_font = font_styles

    adtl_options_frame = LabelFrame(main_plg_frame, text=f"Additional Options - ({script_name})", bg=frame_bg_color, pady=40, padx=40, width=250)

    # Determines what option buttons to show at the bottom of the Pre-Launch GUI based on the script
    match script_name:
        case "Ardy_Knights":
            option_1 = tkinter.Checkbutton(adtl_options_frame, text="Dodgy Necklace (Jewelry tab)", font=break_font, background=frame_bg_color)
            option_1.grid(row=1, column=1)

    adtl_options_frame.grid(row=4, column=1)

    return