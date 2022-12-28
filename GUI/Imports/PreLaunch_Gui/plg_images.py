import os
from PIL import ImageTk, Image


def get_plg_gui_images():

    start_tile_img_path = f"{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Tile"
    start_equip_img_path = f"{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Equipment"
    start_invent_img_path = f"{os.getcwd()}\Assets\Images\GUI_Images\PreLaunch_Gui\Start_Inventory"

    scripts = ["Ardy_Knights"]

    # Ardy Knights - 0
    st_ardy_knights = ImageTk.PhotoImage(Image.open(f'{start_tile_img_path}\{scripts[0]}.png'))
    se_ardy_knights = ImageTk.PhotoImage(Image.open(f'{start_equip_img_path}\{scripts[0]}.png'))
    si_ardy_knights = ImageTk.PhotoImage(Image.open(f'{start_invent_img_path}\{scripts[0]}.png'))

    start_tile_images = st_ardy_knights
    start_equipment_images = se_ardy_knights
    start_inventory_images = si_ardy_knights

    start_imgs = start_tile_images, start_equipment_images, start_inventory_images

    return start_imgs
