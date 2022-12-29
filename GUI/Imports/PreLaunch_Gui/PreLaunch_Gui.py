import os
from tkinter import Toplevel, LabelFrame, font, Entry, Label, StringVar, Tk, Button
from GUI.Imports.PreLaunch_Gui.plg_images import get_plg_gui_images
from PIL import ImageTk, Image
from GUI.Imports.Script_Launch import launch_script
from GUI.Imports.PreLaunch_Gui.plg_options import show_plg_options
import win32gui


frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_plg(script_name):

    auth_top_height = 1035
    auth_top_width = 650

    break_font = font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = font.Font(family='Helvetica', size=11, weight='bold', underline=True)

    font_styles = break_font, break_btn_font

    plg_hwid = win32gui.FindWindow(None, 'Script Pre-Launch')
    if plg_hwid:
        print(f'Already have Pre-launch window open: {plg_hwid}')
        win32gui.SetForegroundWindow(plg_hwid)
        return
    else:
        pwd = os.getcwd()
        plg_gui = Toplevel(pady=20, padx=20)
        plg_gui.title('Script Pre-Launch')
        plg_gui.iconbitmap(f'{pwd}\Icon.ico')
        plg_gui.configure(bg='#969488')
        plg_gui.protocol("WM_DELETE_WINDOW", plg_gui.destroy)
        plg_gui.geometry(f"{auth_top_width}x{auth_top_height}")

        main_plg_frame = LabelFrame(plg_gui, text="Settings & Info", bg=frame_bg_color, pady=20, padx=20)
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
    start_tile_image, start_equip_image, start_invent_image, _ = get_plg_gui_images(script_name)

    start_info_frame = LabelFrame(main_plg_frame, text="Start Tile | Equipment | Inventory", bg=frame_bg_color, pady=20, padx=20)

    # Start_Tile
    start_tile_img_label = Label(start_info_frame, image=start_tile_image, background=frame_bg_color)
    start_tile_img_label.photo = start_tile_image
    start_tile_img_label.grid(row=1, column=1)

    # Start_Equipment
    start_equip_img_label = Label(start_info_frame, image=start_equip_image, background=frame_bg_color)
    start_equip_img_label.photo = start_equip_image
    start_equip_img_label.grid(row=1, column=2, padx=(25, 0))

    # Start_Inventory
    start_invent_img_label = Label(start_info_frame, image=start_invent_image, background=frame_bg_color)
    start_invent_img_label.photo = start_invent_image
    start_invent_img_label.grid(row=1, column=3, padx=(0, 0))

    start_info_frame.grid(row=2, column=1)

    return


def show_plg_notes_section(main_plg_frame, font_styles, script_name):
    break_font, break_btn_font = font_styles

    notes_label_frame = LabelFrame(main_plg_frame, text="Notes", bg=frame_bg_color, pady=20, padx=20, width=250)
    break_font, break_btn_font = font_styles

    _, _, _, notes_image = get_plg_gui_images(script_name)

    # Note Image
    start_tile_img_label = Label(notes_label_frame, image=notes_image, background=frame_bg_color)
    start_tile_img_label.photo = notes_image
    start_tile_img_label.grid(row=1, column=1)

    notes_label_frame.grid(row=3, column=1, pady=(20, 20))
    return




