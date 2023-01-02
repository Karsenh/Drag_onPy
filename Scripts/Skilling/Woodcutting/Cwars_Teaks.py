import random

import API.AntiBan
from API.Mouse import mouse_click, mouse_long_click
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot
from API.Interface.Bank import is_bank_open, is_bank_tab_open, close_bank, deposit_all, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy

script_name = "Cwars_Teak"

jewelry_tab_num = 2  # for Rod
wc_tab_num = 3       # for Axe

axe_type = "dragon"
axe_equipped = False
rod_equipped = False

should_bank = True
should_use_rod = True

teak_attempts = 0
clicked_teak = False
inventory_full = False

# OPTIONS
# Bank or Drop logs
# If banking - use RoD or run
# Axe type (Bronze - Dragon)


def start_chopping_teaks(curr_loop):
    global clicked_teak
    global teak_attempts
    global axe_equipped
    global rod_equipped
    global should_use_rod
    global inventory_full

    if curr_loop != 1:
        print(f'This is not the first loop - doing main shit.')

        # Check if inventory is full - bank or drop if not
        if inventory_full:
            if should_bank:
                if should_use_rod:
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
                inventory_full = False
                move_to_teak_tree()
                clicked_teak = chop_teak()
            else:
                print(f'Dropping logs')
                while does_img_exist(img_name="Inventory_teak", script_name=script_name, should_click=True):
                    print(f'Dropping Teak log from inventory')

        # Check if we're still chopping teak - check if it's because inventory full or if we just need to reclick
        if is_still_chopping():
            clicked_teak = False
            print(f'SAW EXP - STILL CHOPPING: teak_attemps = {teak_attempts} (now 0) & clicked_teak = {clicked_teak}')
            teak_attempts = 0
            return True
        else:
            # If we clicked the teak but we're not still chopping
            if clicked_teak:
                teak_attempts += 1
                print(f"Clicked_teak previously but didn't see exp - increasing teak_attempts = {teak_attempts}")
                if teak_attempts > 1:
                    print(f'Exceeded teak_attempts = {teak_attempts}\nInventory_full = {inventory_full} RETURNING.')
                    inventory_full = True
                    return True

            clicked_teak = chop_teak()
            print(f'🪓 Clicked to chop teak - clicked_teak = {clicked_teak}')
            return True

    else:
        print(f'This is the first loop')
        setup_interface("west", 2, "up")

        # (Start at the cwars bank)
        # Open equipment tab to check if we have selected axe equipped
        axe_equipped = is_axe_equipped()

        # If should_bank and should_use_rod, check if we have Rod equipped (separate method)
        if should_bank:
            if should_use_rod:
                rod_equipped = is_rod_equipped()

        # Open bank
        open_cwars_bank()
        # Deposit inventory
        deposit_all()

        # If no axe equipped - go to wc'ing tab and withdraw - equip
        if not axe_equipped:
            if withdraw_axe():
                deposit_all()

        # If should_use_rod and need_new_rod, go to jewelry tab and withdraw - equip
        if should_bank:
            if should_use_rod:
                if not rod_equipped:
                    withdraw_new_rod()

        # Close Bank
        close_bank()

        # Move to teak tree
        move_to_teak_tree()

        # Begin chopping
        clicked_teak = chop_teak()

        return True


def is_rod_equipped():
    # Open equipment tab
    is_tab_open("equipment", True)
    # Check for ring of dueling
    return does_img_exist(img_name="Equipped_rod", script_name=script_name)


def is_axe_equipped():
    # Open equipment tab
    is_tab_open("equipment", True)
    # Check for ring of dueling
    return wait_for_img(img_name=f"Equipped_{axe_type}_axe", script_name=script_name, max_wait_sec=3)


def open_cwars_bank():
    if wait_for_img(img_name="Cwars_bank", script_name=script_name):
        API.AntiBan.sleep_between(0.7, 0.8)
        does_img_exist(img_name="Cwars_bank", script_name=script_name, should_click=True)
    return is_bank_open()


def withdraw_axe():
    is_bank_tab_open(tab_num=wc_tab_num, should_open=True)
    does_img_exist(img_name=f"Banked_{axe_type}_axe", script_name=script_name, should_click=True, x_offset=15, y_offset=5)
    API.AntiBan.sleep_between(0.4, 0.6)
    mouse_long_click(get_xy_for_invent_slot(1))
    return wait_for_img(img_name="Wield_axe", script_name=script_name, should_click=True)


def withdraw_new_rod():
    is_bank_tab_open(tab_num=jewelry_tab_num, should_open=True)
    is_withdraw_qty(qty="1", should_click=True)
    does_img_exist(img_name=f"Banked_rod", script_name=script_name, should_click=True, x_offset=15, y_offset=5)
    API.AntiBan.sleep_between(0.9, 1.1)
    mouse_long_click(get_xy_for_invent_slot(1))
    return wait_for_img(img_name="Wear_rod", script_name=script_name, should_click=True)


def deposit_teaks():
    is_withdraw_qty(qty="all", should_click=True)
    invent_teak_xy = get_xy_for_invent_slot(slot_num=random.randint(9, 20))
    mouse_click(invent_teak_xy)
    return


def move_to_teak_tree():
    for i in range(0, 9):
        if i < 8:
            if wait_for_img(img_name=f"teak_path_{i}", script_name=script_name, threshold=0.93, max_wait_sec=20):
                if not does_img_exist(img_name=f"teak_path_{i}", script_name=script_name, threshold=0.93, max_wait_sec=20, should_click=True):
                    print(f'does_path_img secondary search failed {i}.')
                    return False
            else:
                print(f"Primary path_img search failed {i}")
                return False
        else:
            if wait_for_img(img_name="teak_path_8", script_name="Cwars_Teak", threshold=0.90, x_offset=-4, y_offset=6):
                if not does_img_exist(img_name="teak_path_8", script_name="Cwars_Teak", threshold=0.90, x_offset=-4, y_offset=6, should_click=True):
                    print(f'Secondary last path search failed.')
                    return False
            else:
                print(f'Primary path search ({i}) not found')
                return False
    return True


def chop_teak():
    return wait_for_img(img_name="Teak_tree", script_name=script_name, should_click=True, max_wait_sec=10, threshold=0.8)


def run_to_cwars_bank():
    return


def teleport_to_cwars_bank():
    is_tab_open("equipment", True)
    does_img_exist(img_name="Equipped_rod", script_name=script_name)
    mouse_long_click(get_existing_img_xy())
    return wait_for_img(img_name="Teleport_Cwars", script_name=script_name, should_click=True)


def drop_teaks():
    return


def is_still_chopping():
    return wait_for_img(img_name="Woodcutting", category="Exp_Drops", max_wait_sec=8)


def move_to_chest():
    return wait_for_img(img_name="bank_minimap", script_name='Cwars_Teak', should_click=True, x_offset=6)

# -------
# HELPERS
# -------

