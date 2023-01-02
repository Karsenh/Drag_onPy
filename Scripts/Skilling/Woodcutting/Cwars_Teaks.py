import random

import API.AntiBan
from API.Mouse import mouse_click, mouse_long_click
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot, is_otd_enabled, drop_inventory
from API.Interface.Bank import is_bank_open, is_bank_tab_open, close_bank, deposit_all, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy, get_color_at_coords

SCRIPT_NAME = "Cwars_Teak"

jewelry_tab_num = 2  # for Rod
wc_tab_num = 3       # for Axe

AXE_TYPE = "dragon"
AXE_EQUIPPED = False
ROD_EQUIPPED = False

SHOULD_BANK = False
SHOULD_USE_ROD = True

TEAK_ATTEMPTS = 0
CLICKED_TEAK = False
INVENT_FULL = False

START_LOCATION = "tree"

# OPTIONS
# Bank or Drop logs
# If banking - use RoD or run
# Axe type (Bronze - Dragon)


def start_chopping_teaks(curr_loop):
    global CLICKED_TEAK
    global TEAK_ATTEMPTS
    global AXE_EQUIPPED
    global ROD_EQUIPPED
    global SHOULD_USE_ROD
    global INVENT_FULL
    global START_LOCATION

    if curr_loop != 1:
        print(f'This is not the first loop - doing main shit.')

        # Check if inventory is full - bank or drop if not
        if is_invent_full():
            if SHOULD_BANK:
                if SHOULD_USE_ROD:
                    print(f'Using rod to cwars bank')
                    teleport_to_cwars_bank()
                else:
                    print(f'Running back to cwars bank')
                    run_to_cwars_bank()

                move_to_chest()
                if not open_cwars_bank():
                    move_to_chest()
                    if not open_cwars_bank():
                        print(f'Failed to open cwars bank a couple times. Exiting')
                        return False
                deposit_teaks()
                INVENT_FULL = False
                TEAK_ATTEMPTS = 0
                move_to_teak_tree()
                CLICKED_TEAK = chop_teak()
            else:
                print(f'Dropping logs')
                drop_teaks()
                INVENT_FULL = False
                TEAK_ATTEMPTS = 0
                chop_teak()

        # Check if we're still chopping teak - check if it's because inventory full or if we just need to reclick
        if is_still_chopping():
            CLICKED_TEAK = False
            print(f'SAW EXP - STILL CHOPPING: teak_attemps = {TEAK_ATTEMPTS} (now 0) & clicked_teak = {CLICKED_TEAK}')
            TEAK_ATTEMPTS = 0
            return True

        CLICKED_TEAK = chop_teak()
        print(f'🪓 Clicked to chop teak - clicked_teak = {CLICKED_TEAK}')
        return True

    else:
        print(f'This is the first loop')
        setup_interface("west", 2, "up")

        if START_LOCATION == "bank":
            # (Start at the cwars bank)
            # Open equipment tab to check if we have selected axe equipped
            AXE_EQUIPPED = is_axe_equipped()

            # If should_bank and should_use_rod, check if we have Rod equipped (separate method)
            if SHOULD_BANK:
                if SHOULD_USE_ROD:
                    ROD_EQUIPPED = is_rod_equipped()

            # Open bank
            open_cwars_bank()
            # Deposit inventory
            deposit_all()

            # If no axe equipped - go to wc'ing tab and withdraw - equip
            if not AXE_EQUIPPED:
                if withdraw_axe():
                    deposit_all()

            # If should_use_rod and need_new_rod, go to jewelry tab and withdraw - equip
            if SHOULD_BANK:
                if SHOULD_USE_ROD:
                    if not ROD_EQUIPPED:
                        withdraw_new_rod()

            # Close Bank
            close_bank()

            # Move to teak tree
            if not move_to_teak_tree():
                return False

        # Begin chopping
        CLICKED_TEAK = chop_teak()

        return True


def is_rod_equipped():
    # Open equipment tab
    is_tab_open("equipment", True)
    # Check for ring of dueling
    return does_img_exist(img_name="Equipped_rod", script_name=SCRIPT_NAME)


def is_axe_equipped():
    # Open equipment tab
    is_tab_open("equipment", True)
    # Check for ring of dueling
    return wait_for_img(img_name=f"Equipped_{AXE_TYPE}_axe", script_name=SCRIPT_NAME, max_wait_sec=3)


def open_cwars_bank():
    if wait_for_img(img_name="Cwars_bank", script_name=SCRIPT_NAME):
        API.AntiBan.sleep_between(0.7, 0.8)
        does_img_exist(img_name="Cwars_bank", script_name=SCRIPT_NAME, should_click=True)
    return is_bank_open()


def withdraw_axe():
    is_bank_tab_open(tab_num=wc_tab_num, should_open=True)
    does_img_exist(img_name=f"Banked_{AXE_TYPE}_axe", script_name=SCRIPT_NAME, should_click=True, x_offset=15, y_offset=5)
    API.AntiBan.sleep_between(0.4, 0.6)
    mouse_long_click(get_xy_for_invent_slot(1))
    return wait_for_img(img_name="Wield_axe", script_name=SCRIPT_NAME, should_click=True)


def withdraw_new_rod():
    is_bank_tab_open(tab_num=jewelry_tab_num, should_open=True)
    is_withdraw_qty(qty="1", should_click=True)
    does_img_exist(img_name=f"Banked_rod", script_name=SCRIPT_NAME, should_click=True, x_offset=15, y_offset=5)
    API.AntiBan.sleep_between(0.9, 1.1)
    mouse_long_click(get_xy_for_invent_slot(1))
    return wait_for_img(img_name="Wear_rod", script_name=SCRIPT_NAME, should_click=True)


def deposit_teaks():
    is_withdraw_qty(qty="all", should_click=True)
    invent_teak_xy = get_xy_for_invent_slot(slot_num=random.randint(9, 20))
    mouse_click(invent_teak_xy)
    return


def move_to_teak_tree():
    for i in range(1, 9):
        if i < 8:
            if wait_for_img(img_name=f"teak_path_{i}", script_name=SCRIPT_NAME, threshold=0.93, max_wait_sec=20):
                API.AntiBan.sleep_between(0.7, 0.8)
                if not wait_for_img(img_name=f"teak_path_{i}", script_name=SCRIPT_NAME, threshold=0.90, should_click=True):
                    print(f'does_path_img secondary search failed {i}.')
                    return False
            else:
                print(f"Primary path_img search failed {i}")
                return False
        else:
            if wait_for_img(img_name="teak_path_8", script_name="Cwars_Teak", threshold=0.90, x_offset=-4, y_offset=6):
                if not  wait_for_img(img_name="teak_path_8", script_name="Cwars_Teak", threshold=0.90, x_offset=-4, y_offset=6, should_click=True):
                    print(f'Secondary last path search failed.')
                    return False
            else:
                print(f'Primary path search ({i}) not found')
                return False
    return True


def chop_teak():
    return wait_for_img(img_name="Teak_tree", script_name=SCRIPT_NAME, should_click=True, max_wait_sec=10, threshold=0.8)


def run_to_cwars_bank():
    return


def teleport_to_cwars_bank():
    is_tab_open("equipment", True)
    does_img_exist(img_name="Equipped_rod", script_name=SCRIPT_NAME)
    mouse_long_click(get_existing_img_xy())
    return wait_for_img(img_name="Teleport_Cwars", script_name=SCRIPT_NAME, should_click=True)


def drop_teaks():
    is_otd_enabled(should_enable=True)
    is_tab_open("inventory", True)
    # i = 0
    # while does_img_exist(img_name="Inventory_teak", script_name=SCRIPT_NAME, should_click=True):
    #     i += 1
    #     print(f'Dropping teak log {i} from inventory.')
    drop_inventory(from_spot_num=1, to_spot_num=28)
    is_otd_enabled(should_enable=False)
    return


def is_still_chopping():
    return wait_for_img(img_name="Woodcutting", category="Exp_Drops", max_wait_sec=6)


def move_to_chest():
    return wait_for_img(img_name="bank_minimap", script_name='Cwars_Teak', should_click=True, x_offset=6)


def is_invent_full():
    teak_color_xy = 1354, 788
    color_code = [177, 146, 92]

    diff_tolerance = 10
    teak_color = get_color_at_coords(teak_color_xy)

    print(f'Teak Color: {teak_color}\nColor_code comparison: {color_code}')

    i = 0
    for val in teak_color:
        curr_diff = val - color_code[i]
        print(f'Val: {val} | Curr_diff: {curr_diff} | (is gt) Tolerance: {diff_tolerance} ?')
        if curr_diff < 0:
            curr_diff = curr_diff * -1
            print(f'Curr_diff was neg: {curr_diff}')
        if curr_diff > diff_tolerance:
            print(f'Returning False')
            return False
        i+=1

    return True

# -------
# HELPERS
# -------

