import API.AntiBan
from API.Actions.Teleporting import teleport_with_crafting_cape
from API.Global_Vars import get_global_bank_tab_num
from API.Interface.General import setup_interface, is_tab_open, is_run_gt, is_run_on, relog
from API.Interface.Bank import is_bank_open, is_bank_tab_open, is_withdraw_qty, close_bank, deposit_all
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Mouse import mouse_click, mouse_long_click
from API.Debug import write_debug


SCRIPT_NAME = 'Cwars_Lavas'

POUCHES_TO_USE_ARR = ['Giant', 'Large', 'Medium', 'Small']
DEGRADED_POUCH_EXISTS = False

# INVENTORY
GIANT_POUCH_XY = 1138, 484
LARGE_POUCH_XY = 1138, 423
MEDIUM_POUCH_XY = 1208, 421
SMALL_POUCH_XY = 1280, 420

EARTH_RUNES_XY = 1138, 541

# BANK
PURE_ESS_XY = 906, 445
RING_XY = 908, 506
NECKLACE_XY = 823, 508

NEEDS_NECKLACE = False
NEEDS_RING = False


def start_crafting_lavas(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        # if check_for_degraded_pouches():
        #     fix_pouches()

        # if not optimal_bank_open():
        #     move_to_bank_chest()
        #     open_bank_from_bank()
        if not open_bank_from_teleport():
            if not open_bank_from_bank():
                print('failed to find both bank images')

        if not resupply():
            print(f'📛 Failed to resupply - exiting...')
            return False

        teleport_to_da()

        if not move_to_ruins():
            print(f'📛 Failed to move to ruins')
            return False

        if not move_to_altar():
            manual_click_xy = 1067, 763
            mouse_click(manual_click_xy)

        API.AntiBan.sleep_between(0.6, 0.7)
        cast_imbue()
        craft_lavas()
        empty_small_pouch()
        empty_medium_pouch()
        empty_large_pouch()
        craft_lavas()
        empty_giant_pouch()
        craft_lavas()

        # teleport_to_cwars()
        if not teleport_with_crafting_cape(is_equipped=False):
            print(f'Failed to teleport with crafting cape')
            return False

        if check_for_degraded_pouches():
            print(f'🎒 Degraded pouch found')
            fix_pouches()
        check_equipment()

    else:
        print(f'First loop')
        setup_interface('north', 1, 'up')
        check_equipment()
        if check_for_degraded_pouches():
            print(f'🎒 Degraded pouch found')
            fix_pouches()

    return True


# METHODS
def open_bank_from_teleport():
    print(f'Checking for open bank from crafting teleport spot...')
    if does_img_exist(img_name='bank_chest_from_teleport', threshold=0.9, script_name=SCRIPT_NAME, should_click=True, click_middle=True):
        return is_bank_open(15)
    else:
        return False


def move_to_bank_chest():
    if does_img_exist(img_name="Bank_Chest", script_name="Cwars_Lavas", threshold=0.7):
        return True
    else:
        return wait_for_img(img_name="Minimap_Bank", script_name="Cwars_Lavas", should_click=True, threshold=0.85, y_offset=4)


def check_equipment():
    is_tab_open('equipment')
    API.AntiBan.sleep_between(0.1, 0.2)
    if not does_img_exist(img_name='Equipped_Necklace', script_name=SCRIPT_NAME, threshold=0.7):
        print('❌ NEED NECKLACE 📿')
        set_needs_necklace(True)

    API.AntiBan.sleep_between(0.6, 0.7)
    if not does_img_exist(img_name='Equipped_Rod', script_name=SCRIPT_NAME):
        print('❌ NEED RING 💍')
        set_needs_ring(True)
    return True


def open_bank_from_bank():
    wait_for_img(img_name="bank_chest_from_bank", script_name="Cwars_Lavas", threshold=0.9, max_wait_sec=8, should_click=True, click_middle=True)
    API.AntiBan.sleep_between(0.8, 0.9)
    does_img_exist(img_name="bank_chest_from_bank", script_name="Cwars_Lavas", should_click=True, threshold=0.85)
    return is_bank_open()


def resupply():
    global NEEDS_RING
    global NEEDS_NECKLACE

    global RING_XY
    global NECKLACE_XY

    global PURE_ESS_XY

    is_bank_tab_open(1)

    if NEEDS_RING:
        print(f'✔ Replenishing ring of dueling 💍')
        is_withdraw_qty('1')
        mouse_click(RING_XY)
        API.AntiBan.sleep_between(1.1, 1.1)

        long_click_xy = 1208, 477
        mouse_long_click(long_click_xy)

        if not wait_for_img(img_name='Wear', category='General', should_click=True, click_middle=True):
            print(f'📛 Failed to find wear ring option')
            return False
        NEEDS_RING = False

    if NEEDS_NECKLACE:
        print(f'✔ Replenishing necklace 📿')
        is_withdraw_qty('1')
        mouse_click(NECKLACE_XY)
        API.AntiBan.sleep_between(1.1, 1.1)

        long_click_xy = 1208, 477
        mouse_long_click(long_click_xy)

        if not wait_for_img(img_name='Wear', category='General', should_click=True, click_middle=True):
            print(f'📛 Failed to find wear ring option')
            return False
        NEEDS_NECKLACE = False

    fill_pouches()
    close_bank()
    return True


def teleport_to_da():
    is_tab_open('equipment')

    equipped_rod_xy = 1336, 670
    mouse_long_click(equipped_rod_xy)

    teleport_da_xy = 1287, 686
    mouse_click(teleport_da_xy)

    API.AntiBan.sleep_between(4.0, 4.1)
    return


def teleport_to_cwars():
    is_tab_open('equipment')

    equipped_rod_xy = 1336, 670
    mouse_long_click(equipped_rod_xy)
    teleport_cwars_xy = 1321, 725
    mouse_click(teleport_cwars_xy)

    # When done teleporting check for necklace and ring in inventory to set 'needs'

    return


def move_to_ruins():
    if not wait_for_img(img_name="Minimap_Ruins_Alt", script_name="Cwars_Lavas", should_click=True, threshold=0.9, y_offset=-130, x_offset=0, max_wait_sec=30):
        write_debug(f"Failed to find Minimap_Ruins... Exiting.")
        return False
    if not wait_for_img(img_name="Enter_Ruins", script_name="Cwars_Lavas", threshold=0.80, max_wait_sec=15, should_click=True, click_middle=True):
        print(f'Couldnt find Enter Ruins image - manually entering')
        manual_enter_ruins_xy = 810, 314
        mouse_click(manual_enter_ruins_xy)
    return wait_for_img(img_name="Entered_Ruins_Flag", script_name="Cwars_Lavas", threshold=0.9, max_wait_sec=12)


def move_to_altar():
    minimap_altar_xy = 1394, 232
    mouse_click(minimap_altar_xy)
    return True


def cast_imbue():
    is_tab_open("magic", True)
    wait_for_img(img_name="Imbue_Spell", script_name="Cwars_Lavas", should_click=True, threshold=0.8, click_middle=True)
    return


def craft_lavas(y_offset=0):
    is_tab_open('inventory')
    earth_runes_xy = EARTH_RUNES_XY
    mouse_click(earth_runes_xy)
    wait_for_img(img_name="Fire_Altar", script_name="Cwars_Lavas", should_click=True, threshold=0.92, x_offset=6, y_offset=y_offset)
    return


def check_for_degraded_pouches():
    global DEGRADED_POUCH_EXISTS

    is_tab_open("inventory", True)

    for pouch_size in POUCHES_TO_USE_ARR:
        if pouch_size != "Small":
            if does_img_exist(img_name=f"Inventory_{pouch_size}_Pouch_Degraded", script_name="Cwars_Lavas", threshold=0.85):
                DEGRADED_POUCH_EXISTS = True
                return True
    return False


def fix_pouches():
    global DEGRADED_POUCH_EXISTS

    if DEGRADED_POUCH_EXISTS:
        is_tab_open("magic", True)
        wait_for_img(img_name="NPC_Contact_Spell", script_name="Cwars_Lavas", threshold=0.9)
        x, y = get_existing_img_xy()
        adj_xy = x+15, y+15
        # Long click npc contact
        mouse_long_click(adj_xy)

        if not wait_for_img(img_name="Cast_Previous", script_name="Cwars_Lavas", threshold=0.9, should_click=True, click_middle=True):
            does_img_exist(img_name="Cast", script_name="Cwars_Lavas", threshold=0.9, should_click=True, click_middle=True)
            wait_for_img(img_name="Dark_Mage_Contact", script_name="Cwars_Lavas", threshold=0.85, should_click=True, click_middle=True)

        wait_for_img(img_name="Tap_To_Cont", script_name="Cwars_Lavas", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=10)
        wait_for_img(img_name="Repair_Pouches", script_name="Cwars_Lavas", should_click=True, click_middle=True, threshold=0.9)
        wait_for_img(img_name="Tap_To_Cont", script_name="Cwars_Lavas", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=10)
        DEGRADED_POUCH_EXISTS = False
    return


# HELPERS
def set_needs_necklace(val):
    global NEEDS_NECKLACE
    NEEDS_NECKLACE = val
    return NEEDS_NECKLACE


def set_needs_ring(val):
    global NEEDS_RING
    NEEDS_RING = val
    return NEEDS_RING


def fill_pouches():
    giant_fill_xy = 1030, 764
    large_fill_xy = 1034, 764
    medium_fill_xy = 1166, 764
    small_fill_xy = 1208, 763

    is_withdraw_qty('all')
    mouse_click(PURE_ESS_XY)

    mouse_long_click(SMALL_POUCH_XY)
    API.AntiBan.sleep_between(0.1, 0.2)
    mouse_click(small_fill_xy)

    mouse_long_click(MEDIUM_POUCH_XY)
    API.AntiBan.sleep_between(0.1, 0.2)
    mouse_click(medium_fill_xy)

    mouse_long_click(LARGE_POUCH_XY)
    API.AntiBan.sleep_between(0.1, 0.2)
    mouse_click(large_fill_xy)

    mouse_click(PURE_ESS_XY)

    mouse_long_click(GIANT_POUCH_XY)
    API.AntiBan.sleep_between(0.1, 0.2)
    mouse_click(giant_fill_xy)

    mouse_click(PURE_ESS_XY)

    return True


def empty_small_pouch():
    empty_xy = 1270, 517

    mouse_long_click(SMALL_POUCH_XY)
    # API.AntiBan.sleep_between(0.1, 0.12)
    mouse_click(empty_xy)
    return


def empty_medium_pouch():
    empty_xy = 1205, 521

    mouse_long_click(MEDIUM_POUCH_XY)
    # API.AntiBan.sleep_between(0.1, 0.12)
    mouse_click(empty_xy)
    return


def empty_large_pouch():
    empty_xy = 1125, 525

    mouse_long_click(LARGE_POUCH_XY)
    # API.AntiBan.sleep_between(0.1, 0.12)
    mouse_click(empty_xy)
    return


def empty_giant_pouch():
    empty_xy = 1121, 587

    mouse_long_click(GIANT_POUCH_XY)
    # API.AntiBan.sleep_between(0.1, 0.12)
    mouse_click(empty_xy)
    return

