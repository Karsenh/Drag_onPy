import os
from tkinter import Toplevel, LabelFrame, font, Entry, Label, StringVar
from GUI.Imports.PreLaunch_Gui.plg_images import get_plg_gui_images
from PIL import ImageTk, Image

frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def show_pre_launch_gui(script_name="ardy_knights"):
    break_font = font.Font(family='Helvetica', size=11, weight='normal')
    break_btn_font = font.Font(family='Helvetica', size=11, weight='bold')

    font_styles = break_font, break_btn_font

    pwd = os.getcwd()
    settings_gui = Toplevel(pady=50, padx=50)
    settings_gui.title('Pre-Launch')
    settings_gui.iconbitmap(f'{pwd}\Icon.ico')
    settings_gui.configure(bg='#969488')

    # Subgui
    show_pre_launch_subgui(settings_gui, font_styles)

    return


def show_pre_launch_subgui(settings_gui, font_styles):
    break_m = StringVar(settings_gui)
    break_font, break_btn_font = font_styles

    start_tile_images, start_equipment_images, start_inventory_images = get_plg_gui_images()
    st_ardy_knights = start_tile_images

    st_ardy_knights_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Tile\Ardy_Knights.png'))

    start_info_frame = LabelFrame(settings_gui, text="Start Setup", bg=frame_bg_color, pady=40, padx=40)

    star_tile_image = Label(start_info_frame, image=st_ardy_knights_img)
    start_info_frame.photo = st_ardy_knights_img

    star_tile_image.grid(row=1, column=1)

    start_info_frame.grid(row=1, column=1)

    return
