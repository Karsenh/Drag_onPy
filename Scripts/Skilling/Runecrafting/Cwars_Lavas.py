import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_run_gt, is_run_on
from API.Interface.Bank import is_bank_open, is_bank_tab_open, is_withdraw_qty, close_bank, deposit_all
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Mouse import mouse_click, mouse_long_click
from API.Debug import write_debug

USE_STAMS = True
NEEDS_STAM = False

ROD_EQUIPPED = False
NECK_EQUIPPED = False
TIARA_EQUIPPED = False
STAFF_EQUIPPED = False

RUNE_POUCH_INVENT = False
EARTH_RUNES_INVENT = False

POUCHES_TO_USE_ARR = ["Small", "Medium", "Large"]
HAS_ESS_POUCH_ARR = []
DEGRADED_POUCH_EXISTS = False

MAGIC_BANK_TAB = 1
JEWELRY_BANK_TAB = 1
HERBLORE_BANK_TAK = 1

CACHED_SMALL_FILL_XY = None
CACHED_SMALL_EMPTY_XY = None

CACHED_MEDIUM_FILL_XY = None
CACHED_MEDIUM_EMPTY_XY = None

CACHED_LARGE_FILL_XY = None
CACHED_LARGE_EMPTY_XY = None

CACHED_EARTHS_XY = None
CACHED_BANKED_ESS_XY = None

CACHED_CWARS_TELE_XY = None
CACHED_DA_TELE_XY = None

CACHED_EQUIPPED_ROD_XY = None


def start_crafting_lavas(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')

        # Add check for run energy gt however much needed for full run - if not wd stam and use
        check_run()

        # Add check for degraded pouches
        fix_pouches()

        if not optimal_bank_open():
            move_to_bank_chest()
            open_bank_chest()

        if not replenish_missing_items():
            write_debug(f"Something went wrong while replenishing items... Exiting.")
            return False
        withdraw_ess()
        fill_pouches()
        close_bank()
        teleport_to_duel_arena()
        if not move_to_ruins():
            return False
        if not move_to_altar():
            manual_click_xy = 1067, 763
            mouse_click(manual_click_xy)
        API.AntiBan.sleep_between(0.6, 0.7)
        cast_imbue()
        craft_lavas()
        empty_pouches()
        craft_lavas()
        teleport_to_cwars()
        API.AntiBan.sleep_between(0.5, 0.6)
    else:
        print(f'This is the first loop - setting up interface etc.')
        setup_interface("north", 1, "up")
        set_inventory_items(curr_loop)
        set_equipped_items(curr_loop)

    return True


def optimal_bank_open():
    if does_img_exist(img_name="Far_Bank_Open", script_name="Cwars_Lavas", threshold=0.70, should_click=True):
        return is_bank_open(max_wait_sec=8)
    return False


def set_equipped_items(curr_loop):
    global ROD_EQUIPPED
    global NECK_EQUIPPED
    global TIARA_EQUIPPED
    global STAFF_EQUIPPED

    if curr_loop == 2:
        return

    is_tab_open("equipment", True)
    ROD_EQUIPPED = does_img_exist(img_name="Equipped_Rod", script_name="Cwars_Lavas", threshold=0.9)
    NECK_EQUIPPED = does_img_exist(img_name="Equipped_Necklace", script_name="Cwars_Lavas", threshold=0.9)
    if curr_loop != 1:
        return
    TIARA_EQUIPPED = does_img_exist(img_name="Equipped_Tiara", script_name="Cwars_Lavas", threshold=0.9)
    STAFF_EQUIPPED = does_img_exist(img_name="Equipped_Staff", script_name="Cwars_Lavas", threshold=0.9)
    print(f'INVENTORY ITEMS:\nrod_equipped: {ROD_EQUIPPED}\nneck_equipped: {NECK_EQUIPPED}\ntiara_equipped: {TIARA_EQUIPPED}\nstaff_equipped: {STAFF_EQUIPPED}')
    return


def set_inventory_items(curr_loop):
    global RUNE_POUCH_INVENT
    global EARTH_RUNES_INVENT
    global POUCHES_TO_USE_ARR
    global HAS_ESS_POUCH_ARR

    is_tab_open("inventory", True)

    for pouch in POUCHES_TO_USE_ARR:
        print(f'Checking Inventory_{pouch}_Pouch')
        HAS_ESS_POUCH_ARR.append(does_img_exist(img_name=f"Inventory_{pouch}_Pouch", script_name="Cwars_Lavas", threshold=0.9))

    RUNE_POUCH_INVENT = does_img_exist(img_name="Inventory_Rune_Pouch", script_name="Cwars_Lavas", threshold=0.9)
    EARTH_RUNES_INVENT = does_img_exist(img_name="Inventory_Earth_Runes", script_name="Cwars_Lavas", threshold=0.9)
    print(f'INVENTORY ITEMS:\npouches_to_use: {POUCHES_TO_USE_ARR}\nrune_pouch_invent: {RUNE_POUCH_INVENT}\nearth_runes_invent: {EARTH_RUNES_INVENT}\nhas_ess_pouch: {HAS_ESS_POUCH_ARR}')
    return


def replenish_missing_items():
    # Assumes bank is open
    global ROD_EQUIPPED
    global NECK_EQUIPPED
    global TIARA_EQUIPPED
    global STAFF_EQUIPPED
    global RUNE_POUCH_INVENT
    global EARTH_RUNES_INVENT
    global POUCHES_TO_USE_ARR
    global HAS_ESS_POUCH_ARR

    global NEEDS_STAM

    print(f'⁉️ROD_EQUIPPED = {ROD_EQUIPPED}'
          f'\nNECK_EQUIPPED = {NECK_EQUIPPED}'
          f'\nTIARA_EQUIPPED = {TIARA_EQUIPPED}'
          f'\nSTAFF_EQUIPPED = {STAFF_EQUIPPED}'
          f'\nRUNE_POUCH_INVENT = {RUNE_POUCH_INVENT}'
          f'\nEARTH_RUNES_INVENT = {EARTH_RUNES_INVENT}'
          f'\nPOUCHES_TO_USE_ARR = {POUCHES_TO_USE_ARR}'
          f'\nHAS_ESS_POUCH_ARR = {HAS_ESS_POUCH_ARR}')

    if NEEDS_STAM:
        is_bank_tab_open("6", True)
        deposit_ess()
        is_withdraw_qty("1", True)
        does_img_exist(img_name="Banked_Stam_4", script_name="Cwars_Lavas", threshold=0.97, should_click=True,
                       click_middle=True)
        close_bank()
        does_img_exist(img_name="Inventory_Stam", script_name="Cwars_Lavas", threshold=0.95, should_click=True, click_middle=True)
        x, y, = get_existing_img_xy()
        adj_stam_xy = x+2, y+12
        for i in range(3):
            API.AntiBan.sleep_between(3.0, 3.1)
            mouse_click(adj_stam_xy)
        if wait_for_img(img_name="Inventory_Vial", script_name="Cwars_Lavas", threshold=0.97, max_wait_sec=3):
            x, y = get_existing_img_xy()
            adj_vial_xy = x+2, y+16
            mouse_long_click(adj_vial_xy)
            does_img_exist(img_name="Drop", category="General", threshold=0.9, should_click=True, click_middle=True)
        NEEDS_STAM = False
        open_bank_chest()

    if not ROD_EQUIPPED:
        is_bank_tab_open(JEWELRY_BANK_TAB, True)
        deposit_ess()
        is_withdraw_qty(qty="1", should_click=True)
        does_img_exist(img_name="Banked_Rod", script_name="Cwars_Lavas", should_click=True, threshold=0.97)
        API.AntiBan.sleep_between(1.5, 1.6)
        wait_for_img(img_name="Inventory_Rod", script_name="Cwars_Lavas", threshold=0.95, img_sel="last")
        mouse_long_click(get_existing_img_xy())
        wait_for_img(img_name="Wear", category="General", should_click=True, click_middle=True)
        ROD_EQUIPPED = True

    if not NECK_EQUIPPED:
        is_bank_tab_open(JEWELRY_BANK_TAB, True)
        deposit_ess()
        is_withdraw_qty("1", True)
        if not does_img_exist(img_name="Banked_Necklace", script_name="Cwars_Lavas", threshold=0.97, should_click=True, click_middle=True):
            write_debug(f"Failed to find banked Binding Necklace")
            return False
        API.AntiBan.sleep_between(1.5, 1.6)
        wait_for_img(img_name="Inventory_Necklace", script_name="Cwars_Lavas", threshold=0.95)
        mouse_long_click(get_existing_img_xy())
        wait_for_img(img_name="Wear", category="General", should_click=True, click_middle=True)
        NECK_EQUIPPED = True

    if TIARA_EQUIPPED and STAFF_EQUIPPED and RUNE_POUCH_INVENT and EARTH_RUNES_INVENT and all(HAS_ESS_POUCH_ARR):
        print(f'Skipping bottom replenish with vals: {TIARA_EQUIPPED} | {STAFF_EQUIPPED} | {RUNE_POUCH_INVENT} | {HAS_ESS_POUCH_ARR}')
        return True

    # deposit_all()
    # RUNE_POUCH_INVENT = False

    if not TIARA_EQUIPPED:
        is_bank_tab_open(MAGIC_BANK_TAB, True)
        deposit_ess()
        is_withdraw_qty("1", True)
        if not does_img_exist(img_name="Banked_Tiara", script_name="Cwars_Lavas", should_click=True, click_middle=True,
                       threshold=0.95):
            write_debug(f"Failed to find banked Tiara")
            return False
        API.AntiBan.sleep_between(1, 1.1)
        wait_for_img(img_name="Inventory_Tiara", script_name="Cwars_Lavas", threshold=0.95, img_sel="first")
        mouse_long_click(get_existing_img_xy())
        TIARA_EQUIPPED = wait_for_img(img_name="Wear", category="General", should_click=True, click_middle=True)
        deposit_all()

    if not STAFF_EQUIPPED:
        is_bank_tab_open(MAGIC_BANK_TAB, True)
        deposit_ess()
        is_withdraw_qty("1", True)
        if not wait_for_img(img_name="Banked_Steam_Staff", script_name="Cwars_Lavas", threshold=0.992, should_click=True,
                       click_middle=True):
            write_debug(f"Failed to find required mystic steam staff in bank")
            return False
        API.AntiBan.sleep_between(1, 1.1)
        if wait_for_img(img_name="Inventory_Staff", script_name="Cwars_Lavas", threshold=0.95, img_sel="first"):
            mouse_long_click(get_existing_img_xy())
            wait_for_img(img_name="Wield", category="General", should_click=True, click_middle=True)
            deposit_all()
            STAFF_EQUIPPED = True

    if not RUNE_POUCH_INVENT:
        print(f'Rune Pouch Missing')
        is_bank_tab_open(MAGIC_BANK_TAB, True)
        deposit_ess()
        is_withdraw_qty(qty="1", should_click=True)
        RUNE_POUCH_INVENT = does_img_exist(img_name="Banked_Rune_Pouch", script_name="Cwars_Lavas", should_click=True, click_middle=True)

    if not any(HAS_ESS_POUCH_ARR):
        print(f'Missing at least one essence pouch')
        is_bank_tab_open(MAGIC_BANK_TAB, True)
        deposit_ess()
        is_withdraw_qty(qty="1", should_click=True)
        pouch_idx = 0
        for has_pouch in HAS_ESS_POUCH_ARR:
            if not has_pouch:
                need_pouch_size = POUCHES_TO_USE_ARR[pouch_idx]
                does_img_exist(img_name=f"Banked_{need_pouch_size}_Pouch", script_name="Cwars_Lavas", threshold=0.94, should_click=True, click_middle=True)

            pouch_idx += 1

    if not EARTH_RUNES_INVENT:
        print(f'Earth Runes Missing')
        is_bank_tab_open(MAGIC_BANK_TAB, True)
        deposit_ess()
        is_withdraw_qty(qty="all", should_click=True)
        EARTH_RUNES_INVENT = does_img_exist(img_name="Banked_Earth_Runes", script_name="Cwars_Lavas", should_click=True, click_middle=True, threshold=0.98)

    return True


def deposit_ess():
    is_withdraw_qty("all", True)
    if does_img_exist(img_name="Inventory_Ess", script_name="Cwars_Lavas", threshold=0.9):
        x, y = get_existing_img_xy()
        if x > 1000:
            adj_xy = x+7, y+6
            mouse_click(adj_xy)

    return


def withdraw_ess():
    global CACHED_BANKED_ESS_XY

    is_bank_tab_open(MAGIC_BANK_TAB, True)
    is_withdraw_qty("all", True)
    if CACHED_BANKED_ESS_XY:
        mouse_click(CACHED_BANKED_ESS_XY)
        return True
    else:
        if wait_for_img(img_name="Banked_Ess", script_name="Cwars_Lavas", threshold=0.97, should_click=True, click_middle=True, img_sel="last"):
            x, y = get_existing_img_xy()
            adj_xy = x+22, y+6
            CACHED_BANKED_ESS_XY = adj_xy
            return True
        else:
            return False


def move_to_bank_chest():
    if does_img_exist(img_name="Bank_Chest", script_name="Cwars_Lavas", threshold=0.7):
        return True
    else:
        return wait_for_img(img_name="Minimap_Bank", script_name="Cwars_Lavas", should_click=True, threshold=0.85, y_offset=4)


def open_bank_chest():
    wait_for_img(img_name="Bank_Chest", script_name="Cwars_Lavas", threshold=0.7, max_wait_sec=8)
    API.AntiBan.sleep_between(0.8, 0.9)
    does_img_exist(img_name="Bank_Chest", script_name="Cwars_Lavas", should_click=True, threshold=0.7)
    return is_bank_open()


def fill_pouch(pouch_size):
    global CACHED_SMALL_FILL_XY
    global CACHED_MEDIUM_FILL_XY
    global CACHED_LARGE_FILL_XY

    global CACHED_SMALL_EMPTY_XY
    global CACHED_MEDIUM_EMPTY_XY
    global CACHED_LARGE_EMPTY_XY

    does_img_exist(img_name=f"Inventory_{pouch_size}_Pouch", script_name="Cwars_Lavas", threshold=0.95, img_sel="first")
    mouse_long_click(get_existing_img_xy())

    print(f'small pouch fill vals: {CACHED_SMALL_FILL_XY}\nmedium: {CACHED_MEDIUM_FILL_XY}\nlarge: {CACHED_LARGE_FILL_XY}')

    match pouch_size:
        case "Small":
            if CACHED_SMALL_FILL_XY:
                print(f'Cached_small_fill_xy = {CACHED_SMALL_FILL_XY}')
                mouse_click(CACHED_SMALL_FILL_XY)
            else:
                if wait_for_img(img_name="Fill", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=1):
                    CACHED_SMALL_FILL_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find Small Fill Image to save XY - Checking for Empty.")
                    if does_img_exist(img_name="Empty", category="General", threshold=0.9):
                        x, y = get_existing_img_xy()
                        adj_xy = x + 10, y + 8
                        CACHED_SMALL_FILL_XY = adj_xy
                        does_img_exist(img_name="Cancel", script_name="Cwars_Lavas", threshold=0.9, should_click=True, click_middle=True)
            return

        case "Medium":
            if CACHED_MEDIUM_FILL_XY:
                print(f'Cached_medium_fill_xy = {CACHED_MEDIUM_FILL_XY}')
                mouse_click(CACHED_MEDIUM_FILL_XY)
            else:
                if wait_for_img(img_name="Fill", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=1):
                    CACHED_MEDIUM_FILL_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find Medium Fill Image to save XY - returning.")
                    if does_img_exist(img_name="Empty", category="General", threshold=0.9):
                        x, y = get_existing_img_xy()
                        adj_xy = x + 10, y + 8
                        CACHED_MEDIUM_FILL_XY = adj_xy
                        does_img_exist(img_name="Cancel", script_name="Cwars_Lavas", threshold=0.9, should_click=True, click_middle=True)
            return

        case "Large":
            if CACHED_LARGE_FILL_XY:
                print(f'Cached_large_fill_xy = {CACHED_LARGE_FILL_XY}')
                mouse_click(CACHED_LARGE_FILL_XY)
            else:
                if wait_for_img(img_name="Fill", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=1):
                    CACHED_LARGE_FILL_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find Large Fill Image to save XY - returning.")
                    if does_img_exist(img_name="Empty", category="General", threshold=0.9):
                        x, y = get_existing_img_xy()
                        adj_xy = x + 10, y + 8
                        CACHED_LARGE_FILL_XY = adj_xy
                        does_img_exist(img_name="Cancel", script_name="Cwars_Lavas", threshold=0.9, should_click=True, click_middle=True)
            return
    return


def fill_pouches():
    global POUCHES_TO_USE_ARR

    for pouch_size in POUCHES_TO_USE_ARR:
        if pouch_size == "Giant":
            withdraw_ess()
        fill_pouch(pouch_size)

    withdraw_ess()
    return


def empty_pouch(pouch_size):
    global DEGRADED_POUCH_EXISTS

    global CACHED_SMALL_EMPTY_XY
    global CACHED_MEDIUM_EMPTY_XY
    global CACHED_LARGE_EMPTY_XY

    if not does_img_exist(img_name=f"Inventory_{pouch_size}_Pouch", script_name="Cwars_Lavas", threshold=0.95, img_sel="first"):
        if does_img_exist(img_name=f"Inventory_{pouch_size}_Pouch_Degraded", script_name="Cwars_Lavas", threshold=0.90):
            print(f'Found Degraded {pouch_size} pouch - setting Degraded Exists to True')
            DEGRADED_POUCH_EXISTS = True
            return
    else:
        mouse_long_click(get_existing_img_xy())

        match pouch_size:
            case "Small":
                if CACHED_SMALL_EMPTY_XY:
                    mouse_click(CACHED_SMALL_EMPTY_XY)
                else:
                    if wait_for_img(img_name="Empty", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=2):
                        CACHED_SMALL_EMPTY_XY = get_existing_img_xy()
                    else:
                        print(f"Couldn't find Small Empty image to save XY - returning")
                        return
            case "Medium":
                if CACHED_MEDIUM_EMPTY_XY:
                    mouse_click(CACHED_MEDIUM_EMPTY_XY)
                else:
                    if wait_for_img(img_name="Empty", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=2):
                        CACHED_MEDIUM_EMPTY_XY = get_existing_img_xy()
                    else:
                        print(f"Couldn't find Medium Empty image to save XY - returning")
                        return
            case "Large":
                if CACHED_LARGE_EMPTY_XY:
                    mouse_click(CACHED_LARGE_EMPTY_XY)
                else:
                    if wait_for_img(img_name="Empty", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=2):
                        CACHED_LARGE_EMPTY_XY = get_existing_img_xy()
                    else:
                        print(f"Couldn't find Large Empty image to save XY - returning")
                        return
        return


def empty_pouches():
    global POUCHES_TO_USE_ARR

    for pouch_size in POUCHES_TO_USE_ARR:
        if pouch_size == "Giant":
            craft_lavas()
        empty_pouch(pouch_size)
    return


def teleport_to_duel_arena():
    global CACHED_DA_TELE_XY
    global CACHED_EQUIPPED_ROD_XY

    is_tab_open("equipment", True)
    if CACHED_EQUIPPED_ROD_XY:
        mouse_long_click(CACHED_EQUIPPED_ROD_XY)
    else:
        if wait_for_img(img_name="Equipped_Rod", script_name="Cwars_Lavas", threshold=0.9):
            x, y = get_existing_img_xy()
            adj_xy = x+10, y+10
            CACHED_EQUIPPED_ROD_XY = adj_xy
            mouse_long_click(CACHED_EQUIPPED_ROD_XY)
        else:
            write_debug(f"Failed to find Equipped rod")
            return False

    if CACHED_DA_TELE_XY:
        mouse_click(CACHED_DA_TELE_XY)
    else:
        wait_for_img(img_name="Duel_Arena", category="Teleports", threshold=0.8, should_click=True, click_middle=True)
        x, y = get_existing_img_xy()
        adj_xy = x+8, y+5
        CACHED_DA_TELE_XY = adj_xy
    return


def move_to_ruins():
    if not wait_for_img(img_name="Minimap_Ruins", script_name="Cwars_Lavas", should_click=True, threshold=0.90, y_offset=4, x_offset=-6, max_wait_sec=30):
        write_debug(f"Failed to find Minimap_Ruins... Exiting.")
        return False
    if not wait_for_img(img_name="Enter_Ruins", script_name="Cwars_Lavas", threshold=0.80, max_wait_sec=15, should_click=True, click_middle=True):
        print(f'Couldnt find Enter Ruins image - manually entering')
        manual_enter_ruins_xy = 810, 314
        mouse_click(manual_enter_ruins_xy)
    return wait_for_img(img_name="Entered_Ruins_Flag", script_name="Cwars_Lavas", threshold=0.9)


def move_to_altar():
    minimap_altar_xy = 1394, 232
    mouse_click(minimap_altar_xy)
    # wait_for_img(img_name="Move_to_altar", script_name="Cwars_Lavas", threshold=0.96, should_click=True, x_offset=60, y_offset=-12)
    return True


def cast_imbue():
    is_tab_open("magic", True)
    wait_for_img(img_name="Imbue_Spell", script_name="Cwars_Lavas", should_click=True, threshold=0.8, click_middle=True)
    return


def craft_lavas(y_offset=0):
    global CACHED_EARTHS_XY

    is_tab_open("inventory", True)
    if CACHED_EARTHS_XY:
        mouse_click(CACHED_EARTHS_XY)
    else:
        wait_for_img(img_name="Inventory_Earth_Runes", script_name="Cwars_Lavas", should_click=True, click_middle=True, threshold=0.85)
        CACHED_EARTHS_XY = get_existing_img_xy()

    wait_for_img(img_name="Fire_Altar", script_name="Cwars_Lavas", should_click=True, threshold=0.92, x_offset=6, y_offset=y_offset)
    return


def teleport_to_cwars():
    global ROD_EQUIPPED
    global NECK_EQUIPPED
    global CACHED_EQUIPPED_ROD_XY
    global CACHED_CWARS_TELE_XY

    is_tab_open("equipment", True)

    if not does_img_exist(img_name="Equipped_Necklace", script_name="Cwars_Lavas", threshold=0.9):
        NECK_EQUIPPED = False

    if CACHED_EQUIPPED_ROD_XY:
        mouse_long_click(CACHED_EQUIPPED_ROD_XY)
    else:
        does_img_exist(img_name="Equipped_Rod", script_name="Cwars_Lavas", threshold=0.95)
        x, y = get_existing_img_xy()
        adjusted_xy = x+10, y+10
        CACHED_EQUIPPED_ROD_XY = adjusted_xy
        mouse_long_click(CACHED_EQUIPPED_ROD_XY)

    if does_img_exist(img_name="Last_Rod_Charge", script_name="Cwars_Lavas", threshold=0.85):
        ROD_EQUIPPED = False

    if CACHED_CWARS_TELE_XY:
        mouse_click(CACHED_CWARS_TELE_XY)
    else:
        wait_for_img(img_name="Castle_Wars", category="Teleports", should_click=True, click_middle=True, threshold=0.95)
        x, y = get_existing_img_xy()
        adj_xy = x + 10, y + 5
        CACHED_CWARS_TELE_XY = adj_xy
    return


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


def check_run():
    global USE_STAMS
    global NEEDS_STAM

    if not is_run_gt(percent=9):
        NEEDS_STAM = True

    return