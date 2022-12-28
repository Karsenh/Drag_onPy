import os
import tkinter
from tkinter import Toplevel, LabelFrame, font, Entry, Label, StringVar
from GUI.Imports.PreLaunch_Gui.plg_images import get_plg_gui_images
from PIL import ImageTk, Image

frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_plg(script_name="ardy_knights"):
    break_font = font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = font.Font(family='Helvetica', size=11, weight='bold')

    font_styles = break_font, break_btn_font

    pwd = os.getcwd()
    settings_gui = Toplevel(pady=50, padx=50)
    settings_gui.title('Pre-Launch')
    settings_gui.iconbitmap(f'{pwd}\Icon.ico')
    settings_gui.configure(bg='#969488')

    # Subgui
    show_plg_start_section(settings_gui, font_styles, script_name)

    show_plg_notes_section(settings_gui, font_styles, script_name)

    return


def show_plg_start_section(settings_gui, font_styles, script_name):
    break_m = StringVar(settings_gui)
    break_font, break_btn_font = font_styles

    start_tile_images, start_equipment_images, start_inventory_images = get_plg_gui_images()
    st_ardy_knights = start_tile_images

    start_tile_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Tile\{script_name}.png'))
    start_equip_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Equipment\{script_name}.png'))
    start_invent_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Inventory\{script_name}.png'))

    start_info_frame = LabelFrame(settings_gui, text="Start Setup", bg=frame_bg_color, pady=40, padx=40)

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

    start_info_frame.grid(row=1, column=1)

    return


def show_plg_notes_section(settings_gui, font_styles, script_name):

    info_label_frame = LabelFrame(settings_gui, text="Notes", bg=frame_bg_color, pady=40, padx=40)

    point = '\u2022'
    msg = tkinter.Message(info_label_frame, text=f"Requirements:", background=frame_bg_color, width=400)
    msg.grid(row=1, column=1, columnspan=3)

    msg = tkinter.Message(info_label_frame, text=f"{point} Splasher - Join 'SplashWords' cc to find world.\n{point} Full Rogues outfit", background=frame_bg_color, width=400)
    msg.grid(row=2, column=1, columnspan=3)

    msg = tkinter.Message(info_label_frame, text=f"Known Issues:", background=frame_bg_color, width=400)
    msg.grid(row=3, column=1, columnspan=3)

    msg = tkinter.Message(info_label_frame, text=f"{point} Script will stop when splasher stops\n{point} ", background=frame_bg_color, width=400)
    msg.grid(row=4, column=1, columnspan=3)

    msg = tkinter.Message(info_label_frame, text=f"Run-Time Rating: ⭐⭐⭐ (2-3hrs avg.)", background=frame_bg_color, width=400)
    msg.grid(row=5, column=1, columnspan=6)

    info_label_frame.grid(row=2, column=1)
    return
