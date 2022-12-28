import os
import json
import tkinter
from tkinter import Toplevel, LabelFrame, font, Entry, Label, StringVar, Tk, Button
from GUI.Imports.PreLaunch_Gui.plg_images import get_plg_gui_images
from PIL import ImageTk, Image
from GUI.Imports.PreLaunch_Gui.plg_notes import get_plg_notes
from GUI.Imports.Script_Launch import launch_script


frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_plg(script_name):

    auth_top_height = 1050
    auth_top_width = 750

    break_font = font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = font.Font(family='Helvetica', size=11, weight='bold', underline=True)

    font_styles = break_font, break_btn_font

    pwd = os.getcwd()
    plg_gui = Toplevel(pady=50, padx=50)
    plg_gui.title('Pre-Launch')
    plg_gui.iconbitmap(f'{pwd}\Icon.ico')
    plg_gui.configure(bg='#969488')
    plg_gui.protocol("WM_DELETE_WINDOW", plg_gui.destroy)
    plg_gui.geometry(f"{auth_top_width}x{auth_top_height}")

    main_plg_frame = LabelFrame(plg_gui, text="Pre-Launch", bg=frame_bg_color, pady=40, padx=40)
    main_plg_frame.place(anchor='center', relx=0.5, rely=.5)

    # Subgui
    show_plg_start_section(main_plg_frame, font_styles, script_name)
    show_plg_notes_section(main_plg_frame, font_styles, script_name)
    show_plg_options(main_plg_frame, font_styles, script_name)

    # SCRIPT START BUTTON
    start_image = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\start_btn.png'))
    start_btn = Button(main_plg_frame, text="Defence", image=start_image, bg="#3e3529", activebackground=btn_active_bg_color, command=lambda: launch_script(script_name))
    start_btn.photo = start_image
    start_btn.grid(row=5, column=1, pady=(30, 0))

    return


def show_plg_start_section(main_plg_frame, font_styles, script_name):
    break_font, break_btn_font = font_styles

    start_tile_images, start_equipment_images, start_inventory_images = get_plg_gui_images()
    st_ardy_knights = start_tile_images

    start_tile_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Tile\{script_name}.png'))
    start_equip_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Equipment\{script_name}.png'))
    start_invent_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Inventory\{script_name}.png'))

    start_info_frame = LabelFrame(main_plg_frame, text="Start Setup", bg=frame_bg_color, pady=40, padx=40)

    # Start_Tile
    start_tile_img_label = Label(start_info_frame, image=start_tile_img, background=frame_bg_color)
    start_tile_img_label.photo = start_tile_img
    start_tile_img_label.grid(row=1, column=1)

    # Start_Equipment
    start_equip_img_label = Label(start_info_frame, image=start_equip_img, background=frame_bg_color)
    start_equip_img_label.photo = start_equip_img
    start_equip_img_label.grid(row=1, column=2)

    # Start_Inventory
    start_invent_img_label = Label(start_info_frame, image=start_invent_img, background=frame_bg_color)
    start_invent_img_label.photo = start_invent_img
    start_invent_img_label.grid(row=1, column=3)

    start_info_frame.grid(row=2, column=1)

    return


def show_plg_notes_section(main_plg_frame, font_styles, script_name):
    break_font, break_btn_font = font_styles

    notes_label_frame = LabelFrame(main_plg_frame, text="Notes", bg=frame_bg_color, pady=40, padx=40, width=250)

    plg_notes = get_plg_notes()

    for note in plg_notes:
        if note.name == script_name:
            curr_script_notes = note

    requirements_txt = curr_script_notes.requirements
    issues_txt = curr_script_notes.known_issues
    rating_txt = curr_script_notes.rtr

    msg = tkinter.Message(notes_label_frame, text=f"Requirements:", anchor='w', background=frame_bg_color, width=400, font=break_btn_font)
    msg.grid(row=1, column=1, columnspan=3)
    msg = tkinter.Message(notes_label_frame, text=requirements_txt, background=frame_bg_color, width=400, font=break_font)
    msg.grid(row=2, column=1, columnspan=3, pady=(10, 25))

    msg = tkinter.Message(notes_label_frame, text=f"Known Issues:", background=frame_bg_color, width=400, font=break_btn_font)
    msg.grid(row=3, column=1, columnspan=3)
    msg = tkinter.Message(notes_label_frame, text=issues_txt, background=frame_bg_color, width=400, font=break_font)
    msg.grid(row=4, column=1, columnspan=3, pady=(10, 25))

    msg = tkinter.Message(notes_label_frame, text=f"Run-Time Rating:", background=frame_bg_color, width=400, font=break_btn_font)
    msg.grid(row=5, column=1, columnspan=6)
    msg = tkinter.Message(notes_label_frame, text=rating_txt, background=frame_bg_color, width=400, font=break_font)
    msg.grid(row=6, column=1, columnspan=6)

    notes_label_frame.grid(row=3, column=1, pady=(20, 20))
    return


def show_plg_options(main_plg_frame, font_styles, script_name):
    break_font, break_btn_font = font_styles

    adtl_options_frame = LabelFrame(main_plg_frame, text="Additional Options", bg=frame_bg_color, pady=40, padx=40, width=250)

    option_1 = tkinter.Checkbutton(adtl_options_frame, text="Option 1 test", font=break_font, background=frame_bg_color)
    option_1.grid(row=1, column=1)

    adtl_options_frame.grid(row=4, column=1)

    return

