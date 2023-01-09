from API.Interface.General import setup_interface, is_tab_open
from API.Interface.Bank import is_bank_open, is_bank_tab_open
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Mouse import mouse_click, mouse_long_click

ROD_EQUIPPED = False
NECK_EQUIPPED = False
TIARA_EQUIPPED = False
STAFF_EQUIPPED = False

RUNE_POUCH_INVENT = False
EARTH_RUNES_INVENT = False

POUCHES_TO_USE = ["Small"]
HAS_ESS_POUCH = []

MAGIC_BANK_TAB = 1
JEWELRY_BANK_TAB = 2


def start_crafting_lavas(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')
    else:
        print(f'This is the first loop - setting up interface etc.')
        setup_interface("north", 1, "up")
        set_equipped_items()
        set_inventory_items()
        open_bank_chest()
        withdraw_missing_items()

    return True


def set_equipped_items():
    global ROD_EQUIPPED
    global NECK_EQUIPPED
    global TIARA_EQUIPPED
    global STAFF_EQUIPPED

    is_tab_open("equipment", True)
    ROD_EQUIPPED = does_img_exist(img_name="Equipped_Rod", script_name="Cwars_Lavas", threshold=0.9)
    NECK_EQUIPPED = does_img_exist(img_name="Equipped_Necklace", script_name="Cwars_Lavas", threshold=0.9)
    TIARA_EQUIPPED = does_img_exist(img_name="Equipped_Tiara", script_name="Cwars_Lavas", threshold=0.9)
    STAFF_EQUIPPED = does_img_exist(img_name="Equipped_Staff", script_name="Cwars_Lavas", threshold=0.9)
    print(f'INVENTORY ITEMS:\nrod_equipped: {ROD_EQUIPPED}\nneck_equipped: {NECK_EQUIPPED}\ntiara_equipped: {TIARA_EQUIPPED}\nstaff_equipped: {STAFF_EQUIPPED}')
    return


def set_inventory_items():
    global RUNE_POUCH_INVENT
    global EARTH_RUNES_INVENT
    global POUCHES_TO_USE
    global HAS_ESS_POUCH

    is_tab_open("inventory", True)

    for pouch in POUCHES_TO_USE:
        print(f'Checking Inventory_{pouch}_Pouch')
        HAS_ESS_POUCH.append(does_img_exist(img_name=f"Inventory_{pouch}_Pouch", script_name="Cwars_Lavas", threshold=0.9))

    RUNE_POUCH_INVENT = does_img_exist(img_name="Inventory_Rune_Pouch", script_name="Cwars_Lavas", threshold=0.9)
    EARTH_RUNES_INVENT = does_img_exist(img_name="Inventory_Earth_Runes", script_name="Cwars_Lavas", threshold=0.9)
    print(f'INVENTORY ITEMS:\npouches_to_use: {POUCHES_TO_USE}\nrune_pouch_invent: {RUNE_POUCH_INVENT}\nearth_runes_invent: {EARTH_RUNES_INVENT}\nhas_ess_pouch: {HAS_ESS_POUCH}')
    return


def withdraw_missing_items():
    # Assumes bank is open

    return


def click_bank_minimap():
    return wait_for_img(img_name="Minimap_Bank", script_name="Cwars_Lavas", should_click=True, threshold=0.9)


def open_bank_chest():
    wait_for_img(img_name="Bank_Chest", script_name="Cwars_Lavas", should_click=True, threshold=0.9)
    return is_bank_open()


# PSEUDO-CODE


# Start - cwars bank chest

# Check equipment - Ring of Dueling
    # ROD_EQUIPPED = True
# Check equipment - Binding Necklace
    # NECK_EQUIPPED = True
# Check equipment - Fire tiara
    # TIARA_EQUIPPED = True
# Check equipment - Mist staff
    # STAFF_EQUIPPED = True

