import API.AntiBan
from API.Interface.General import setup_interface, toggle_public_chat, is_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Imports.Coords import INVENT_slot_1
from API.Mouse import mouse_click, mouse_drag, mouse_move, mouse_long_click
import pyautogui as pag

phials_xy = 1353, 133
house_ad_tile_xy = 1326, 221
altar_xy = 1340, 214
# portal_xy =


def start_gilded_altar(curr_loop):

    if curr_loop == 1:
        is_tab_open("inventory", should_open=True)
        API.AntiBan.sleep_between(0.6, 0.7)
        setup_interface("south", 3, "up")
        API.AntiBan.sleep_between(0.6, 0.7)
        toggle_public_chat("off")

    # Start in front of Phials with noted bones & money

    if not unnote_bones():
        return False

    move_to_altar(curr_loop)

    worship_bones()

    return_to_phials()

    return


def unnote_bones():
    global phials_xy
    tries = 0

    # wait till we see phials
    if wait_for_img(img_name="phials", script_name="Gilded_Altar", threshold=0.75, max_wait_sec=10):
        mouse_click(INVENT_slot_1)
        API.AntiBan.sleep_between(0.5, 0.93)
        does_img_exist(img_name="phials", script_name="Gilded_Altar", threshold=0.75, should_click=True)

        if not wait_for_img(img_name="exchange_bones", script_name="Gilded_Altar", should_click=True) and not does_img_exist(img_name="full_invent", script_name="Gilded_Altar", threshold=0.8):
            tries += 1
            if tries > 10:
                return False
            unnote_bones()

    return True


def move_to_altar(curr_loop):
    global house_ad_tile_xy
    global altar_xy

    # Move to the house ad tile near the poh portal
    mouse_click(house_ad_tile_xy)

    # Wait for house_ad image (we're next to house ad)
    if wait_for_img(img_name="house_ad", script_name="Gilded_Altar", threshold=0.75, max_wait_sec=8):
        if curr_loop == 1:
            # mouse click to search for workless ad
            does_img_exist(img_name="house_ad", script_name="Gilded_Altar", threshold=0.75, should_click=True)
            API.AntiBan.sleep_between(2.5, 2.7)
            does_img_exist(img_name="workless_ad", script_name="Gilded_Altar", threshold=0.90, should_click=True,
                           x_offset=700, y_offset=20)
            does_img_exist(img_name="og_ad", script_name="Gilded_Altar", threshold=0.90, should_click=True,
                           x_offset=700, y_offset=20)
            does_img_exist(img_name="og_ad2", script_name="Gilded_Altar", threshold=0.90, should_click=True,
                           x_offset=700, y_offset=20)
        else:
            # visit last
            does_img_exist(img_name="house_ad", script_name="Gilded_Altar", threshold=0.9)
            ad_xy = API.Imaging.Image.get_existing_img_xy()
            mouse_move(ad_xy)
            visit_last_xy = 679, 723
            mouse_drag(from_xy=ad_xy, to_xy=visit_last_xy)

        API.AntiBan.sleep_between(6.0, 6.1)
        mouse_click(altar_xy)
        API.AntiBan.sleep_between(1.0, 1.1)

    return


def worship_bones():
    if does_img_exist(img_name="invent_d_bones", script_name="Gilded_Altar", threshold=0.9):
        d_bone_xy = get_existing_img_xy()
        mouse_long_click(d_bone_xy)
        does_img_exist(img_name="use_d_bones", script_name="Gilded_Altar", should_click=True)

    API.AntiBan.sleep_between(0.3, 0.77)

    # does_img_exist(img_name="gilded_altar", script_name="Gilded_Altar", threshold=0.80, should_click=True)
    altar_xy = 817, 482
    mouse_click(altar_xy)

    if wait_for_img(img_name="level_up", category_name="General", max_wait_sec=27):
        worship_bones()
        API.AntiBan.sleep_between(1.0, 1.1)

    return


def return_to_phials():
    global phials_xy

    portal_xy = 1339, 133
    click_portal_xy = 700, 293

    mouse_click(portal_xy)
    API.AntiBan.sleep_between(5.0, 5.1)

    mouse_click(click_portal_xy)
    API.AntiBan.sleep_between(6.0, 6.1)

    mouse_click(phials_xy)
    API.AntiBan.sleep_between(5.0, 5.1)

    return
