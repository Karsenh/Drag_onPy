import random

import API.AntiBan
from API.Mouse import mouse_click, mouse_long_click
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot
from API.Interface.Bank import is_bank_open, is_bank_tab_open, close_bank, deposit_all
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy

script_name = "Cwars_Teak"

jewelry_tab_num = 2  # for Rod
wc_tab_num = 3       # for Axe

axe_type = "dragon"
axe_equipped = False
rod_equipped = False

should_use_rod = True
should_bank = False

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
                    teleport_to_cwars()
                else:
                    print(f'Running back to cwars bank')
            else:
                print(f'Dropping logs')
                while does_img_exist(img_name="Inventory_teak", script_name=script_name, should_click=True):
                    print(f'Dropping Teak log from inventory')

        # Check if we're still chopping teak - check if it's because inventory full or if we just need to reclick
        if is_still_chopping():
            clicked_teak = False
            teak_attempts = 0
            return True
        else:
            # If we clicked the teak but we're not still chopping
            if clicked_teak:
                if teak_attempts > 1:
                    inventory_full = True
                teak_attempts += 1

            clicked_teak = chop_teak()

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
            withdraw_axe()

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
    return does_img_exist(img_name=f"Equipped_{axe_type}_axe", script_name=script_name)


def open_cwars_bank():
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
    does_img_exist(img_name=f"Banked_rod", script_name=script_name, should_click=True, x_offset=15, y_offset=5)
    API.AntiBan.sleep_between(0.4, 0.6)
    mouse_long_click(get_xy_for_invent_slot(1))
    return wait_for_img(img_name="Wear_rod", script_name=script_name, should_click=True)


def deposit_teaks():
    # does_img_exist(img_name="Inventory_teak", script_name=script_name, should_click=True)
    invent_teak_xy = get_xy_for_invent_slot(slot_num=random.randint(9, 20))
    mouse_click(invent_teak_xy)
    return


def move_to_teak_tree():
    for i in range(0, 8):
        if not wait_for_img(img_name=f"teak_path_{i}", script_name=script_name, should_click=True, threshold=0.90, max_wait_sec=15, y_offset=6):
            print(f"Couldn't find teak_path_{i} - Exiting.")
            return False
    return True


def chop_teak():
    return wait_for_img(img_name="Teak_tree", script_name=script_name, should_click=True, max_wait_sec=10)


def run_to_cwars_bank():
    return


def teleport_to_cwars():
    is_tab_open("equipment", True)
    does_img_exist(img_name="Equipped_rod", script_name=script_name)
    mouse_long_click(get_existing_img_xy())
    return wait_for_img(img_name="Teleport_Cwars", script_name=script_name, should_click=True)


def drop_teaks():
    return


def is_still_chopping():
    return wait_for_img(img_name="Woodcutting", category="Exp_Drops", max_wait_sec=10)


def move_to_chest():
    return does_img_exist(img_name="bank_minimap", script_name=script_name, should_click=True)

# -------
# HELPERS
# -------

