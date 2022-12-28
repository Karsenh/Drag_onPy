import os
from PIL import ImageTk, Image


def get_plg_gui_images(script_name):

    start_tile_img_path = f"{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Tile"
    start_equip_img_path = f"{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Equipment"
    start_invent_img_path = f"{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Inventory"
    script_notes_img_path = f"{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Script_Notes"

    start_tile_image = ImageTk.PhotoImage(Image.open(f'{start_tile_img_path}\{script_name}.png'))
    start_equip_image = ImageTk.PhotoImage(Image.open(f'{start_equip_img_path}\{script_name}.png'))
    start_invent_image = ImageTk.PhotoImage(Image.open(f'{start_invent_img_path}\{script_name}.png'))
    notes_image = ImageTk.PhotoImage(Image.open(f'{script_notes_img_path}\{script_name}.png'))

    plg_images = start_tile_image, start_equip_image, start_invent_image, notes_image

    return plg_images
