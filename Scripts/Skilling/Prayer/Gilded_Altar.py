import datetime

import API.AntiBan
from API.Interface.General import setup_interface, toggle_public_chat, is_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Imports.Coords import INVENT_slot_1
from API.Mouse import mouse_click, mouse_drag, mouse_move, mouse_long_click
import pyautogui as pag

phials_xy = 1353, 133
house_ad_tile_xy = 1326, 221
altar_xy = 1340, 214
should_return_normally = True


def start_gilded_altar(curr_loop):
    global should_return_normally

    if curr_loop == 1:
        is_tab_open("inventory", should_be_open=True)
        API.AntiBan.sleep_between(0.6, 0.7)
        setup_interface("south", 3, "up")
        API.AntiBan.sleep_between(0.6, 0.7)
        toggle_public_chat("off")

    # Start in front of Phials with noted bones & money

    if not unnote_bones():
        return False

    if not move_to_altar(curr_loop):
        return False

    worship_bones()

    if should_return_normally:
        return_to_phials()
    else:
        should_return_normally = True

    return True


def unnote_bones():
    global phials_xy
    tries = 0

    is_tab_open("inventory", True)

    # wait till we see phials
    if wait_for_img(img_name="phials", script_name="Gilded_Altar", threshold=0.75, max_wait_sec=10):
        mouse_click(INVENT_slot_1)
        API.AntiBan.sleep_between(0.3, 0.5)
        # does_img_exist(img_name="phials", script_name="Gilded_Altar", threshold=0.75, should_click=True)
        wait_for_img(img_name="phials", script_name="Gilded_Altar", threshold=0.75, max_wait_sec=10, should_click=True, x_offset=10, y_offset=-10)
        if not wait_for_img(img_name="exchange_bones_gen", script_name="Gilded_Altar", should_click=True) \
                and not does_img_exist(img_name="full_invent", script_name="Gilded_Altar", threshold=0.8) \
                and not does_img_exist(img_name="exchange_bones2", script_name="Gilded_Altar", should_click=True):
            tries += 1
            if tries > 10:
                return False
            unnote_bones()

    return True


def move_to_altar(curr_loop):
    global house_ad_tile_xy
    global altar_xy

    ads_to_check = ["workless", "workless2", "og", "og2", "wiseold", "wiseold2"]

    # Move to the house ad tile near the poh portal
    mouse_click(house_ad_tile_xy)

    API.AntiBan.sleep_between(5.0, 5.1)

    # Wait for house_ad image (we're next to house ad)
    if wait_for_img(img_name="house_ad", script_name="Gilded_Altar", threshold=0.75, max_wait_sec=8):
        if curr_loop == 1:
            # mouse click to search for home owner ads
            does_img_exist(img_name="house_ad", script_name="Gilded_Altar", threshold=0.75, should_click=True)
            API.AntiBan.sleep_between(2.5, 2.7)

            owner_not_found = 0

            for name in ads_to_check:
                if not does_img_exist(img_name=f"{name}_ad", script_name="Gilded_Altar", threshold=0.90, should_click=True, x_offset=700, y_offset=25):
                    owner_not_found += 1
                    print(f'Owner_not_found for {name}: {owner_not_found} ')

            print(f'Ads_to_check len = {len(ads_to_check)}')
            if owner_not_found == len(ads_to_check):
                scroll_xy = 640, 564
                mouse_move(scroll_xy)
                API.AntiBan.sleep_between(0.8, 1.1)
                pag.hscroll(-55)
                API.AntiBan.sleep_between(1.0, 1.1)
                owner_not_found = 0

                for name in ads_to_check:
                    if not does_img_exist(img_name=f"{name}_ad", script_name="Gilded_Altar", threshold=0.95,
                                          should_click=True, x_offset=700, y_offset=20):
                        owner_not_found += 1

                    if owner_not_found == len(ads_to_check):
                        print(f'Couldnt find any owners online - exiting...')
                        return False

        else:
            # visit last
            does_img_exist(img_name="house_ad", script_name="Gilded_Altar", threshold=0.9)
            ad_xy = API.Imaging.Image.get_existing_img_xy()
            x, y = ad_xy
            safe_ad_xy = x+15, y+25
            mouse_long_click(safe_ad_xy)
            does_img_exist(img_name="visit_last", script_name="Gilded_Altar", threshold=0.9, should_click=True)

        API.AntiBan.sleep_between(5.0, 5.1)
        mouse_click(altar_xy)
        API.AntiBan.sleep_between(1.0, 1.1)

    return True


def worship_bones(wait_sec=60):
    global phials_xy
    global should_return_normally

    start_time = datetime.datetime.now()
    if does_img_exist(img_name="invent_d_bones", script_name="Gilded_Altar", threshold=0.9):
        d_bone_xy = get_existing_img_xy()
        mouse_long_click(d_bone_xy)
        does_img_exist(img_name="use_d_bones", script_name="Gilded_Altar", should_click=True)

    API.AntiBan.sleep_between(0.6, 0.98)

    # does_img_exist(img_name="gilded_altar", script_name="Gilded_Altar", threshold=0.80, should_click=True)
    altar_xy = 846, 487
    mouse_click(altar_xy)

    API.AntiBan.sleep_between(1.0, 1.1)

    if wait_for_img(img_name="level_up", category="General", max_wait_sec=wait_sec):
        time_elapsed = datetime.datetime.now() - start_time
        time_remaining = 60 - time_elapsed.total_seconds()
        print(f'ELAPSED: {time_elapsed}\nREMAINING: {time_remaining}')
        API.AntiBan.sleep_between(2.0, 2.1)
        worship_bones(time_remaining)

    if does_img_exist(img_name="owner_logged", script_name="Gilded_Altar", threshold=0.9):
        should_return_normally = False
        mouse_click(phials_xy)
        API.AntiBan.sleep_between(5.0, 5.1)

    return


def return_to_phials():
    global phials_xy

    portal_xy = 1339, 133
    click_portal_xy = 721, 322

    mouse_click(portal_xy)
    API.AntiBan.sleep_between(5.0, 5.1)

    mouse_click(click_portal_xy)
    API.AntiBan.sleep_between(4.0, 4.1)

    mouse_click(phials_xy)
    API.AntiBan.sleep_between(5.0, 5.1)

    return
