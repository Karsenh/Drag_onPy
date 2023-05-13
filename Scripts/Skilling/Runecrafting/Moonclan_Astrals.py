import API.AntiBan
from API.Actions.Teleporting import teleport_with_spellbook, teleport_with_crafting_cape
from API.Global_Vars import get_global_bank_tab_num
from API.Interface.General import setup_interface, is_tab_open, is_run_gt, is_run_on, relog, is_hp_gt
from API.Interface.Bank import is_bank_open, is_bank_tab_open, is_withdraw_qty, close_bank, deposit_all
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy
from API.Mouse import mouse_click, mouse_long_click
from API.Debug import write_debug
from API.Time import get_curr_runtime, reset_curr_runtime
from Scripts.Skilling.Runecrafting.Cwars_Lavas import wait_for_invent_item_xy

SCRIPT_NAME = 'Moonclan_Astrals'

NEEDS_STAM = False
NEEDS_FOOD = False

USE_CRAFTING_CAPE = True
FOOD_TYPE = 'monkfish'

POUCHES_TO_USE_ARR = ['Small', 'Medium', 'Large', 'Giant']
HAS_ESS_POUCH_ARR = []
DEGRADED_POUCH_EXISTS = False

BANK_TAB_NUM = 1

CACHED_SMALL_FILL_XY = None
CACHED_SMALL_EMPTY_XY = None

CACHED_MEDIUM_FILL_XY = None
CACHED_MEDIUM_EMPTY_XY = None

CACHED_LARGE_FILL_XY = None
CACHED_LARGE_EMPTY_XY = None

CACHED_GIANT_FILL_XY = None
CACHED_GIANT_EMPTY_XY = None

CACHED_EARTHS_XY = None
CACHED_BANKED_ESS_XY = None

CACHED_CWARS_TELE_XY = None
CACHED_DA_TELE_XY = None

CACHED_INVENT_SMALL_POUCH = None
CACHED_INVENT_MEDIUM_POUCH = None
CACHED_INVENT_LARGE_POUCH = None
CACHED_INVENT_GIANT_POUCH = None

CRAFTING_GUILD_BANK_XY = 896, 330


def start_crafting_astrals(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')

        teleport_with_spellbook('moonclan')

        move_1()
        if not move_2():
            print(f'⛔ Failed to find move_2')
            return False
        if not move_3():
            print(f'⛔ Failed to find move_3')
            return False
        if not move_4():
            print(f'⛔ Failed to find move_4')
            return False
        else:
            API.AntiBan.sleep_between(8.0, 8.1)

        click_astral_altar_initally()
        empty_pouches()
        craft_astrals()

        if check_for_degraded_pouches():
            fix_pouches()

        if USE_CRAFTING_CAPE:
            teleport_with_crafting_cape(is_equipped=False)
        else:
            teleport_with_spellbook('moonclan')

        if not open_bank():
            print(f'⛔ Failed to open bank')
            return False

        if not resupply():
            return False

    else:
        print(f'First loop')
        setup_interface('east', 1, 'up')

        if not open_bank():
            print(f'⛔ Failed to open bank')
            return False

        if not resupply():
            return False

        curr_rt = get_curr_runtime()

        if curr_rt.total_seconds() > 19800:
            relog()
            setup_interface("east", 1, "up")
            reset_curr_runtime()

    return True


def move_1():
    API.AntiBan.sleep_between(2.1, 2.2)
    wait_for_img(img_name='moonclan_island_flag', script_name=SCRIPT_NAME, threshold=0.9, max_wait_sec=5)
    mini_map_coords = 1458, 175
    mouse_click(mini_map_coords)
    return True


def move_2():
    return wait_for_img(img_name='move_2', script_name=SCRIPT_NAME, should_click=True, click_middle=True, max_wait_sec=15, threshold=0.90)


def move_3():
    if not wait_for_img(img_name='move_3', script_name=SCRIPT_NAME, max_wait_sec=15, threshold=0.98):
        return False

    x, y = get_existing_img_xy()

    adj_xy = x+28, y+13
    mouse_click(adj_xy)
    return True


def move_4():
    if not wait_for_img(img_name='move_4', script_name=SCRIPT_NAME, max_wait_sec=15, threshold=0.98):
        return False

    x, y = get_existing_img_xy()

    adj_xy = x+50, y+26
    mouse_click(adj_xy)

    return True


def click_astral_altar_initally():
    if not wait_for_img(img_name='astral_altar_1', script_name=SCRIPT_NAME, threshold=0.75):
        print(f'⛔ Failed to find astral_altar_1')
        if not does_img_exist(img_name='astral_altar_2', script_name=SCRIPT_NAME, threshold=0.8):
            print(f'⛔ Failed to find astral_altar_2 as well - exiting...')
            return False

    altar_x, altar_y = get_existing_img_xy()
    adj_altar_xy = altar_x + 45, altar_y + 45
    mouse_click(adj_altar_xy)

    return True


def craft_astrals():
    if not does_img_exist(img_name='astral_altar_2', script_name='Moonclan_Astrals', threshold=0.8, should_click=True, click_middle=True):
        print(f'⛔ Failed to find astral altar 2')
        return False
    return True


def open_bank():
    global NEEDS_FOOD
    global NEEDS_STAM

    if USE_CRAFTING_CAPE:
        if not does_img_exist(img_name='crafting_guild_bank', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
            mouse_click(CRAFTING_GUILD_BANK_XY)
    else:
        print(f'Bank at moonclan island')

    if not is_hp_sufficient():
        NEEDS_FOOD = True
    if not is_run_sufficient():
        NEEDS_STAM = True

    if not is_bank_open(max_wait_sec=15):
        print(f'⛔ Failed to find bank open')
        return False

    return is_bank_tab_open(BANK_TAB_NUM)


def resupply():
    global NEEDS_FOOD
    global NEEDS_STAM
    print(f'Resupplying...')

    # Check health
    if NEEDS_FOOD:
        print(f'HP not sufficient - 🦈 handling eat food...')
        if not handle_eat_food():
            print(f'⛔ Failed to eat food for some reason - exiting...')
            return False

    # Check run
    if NEEDS_STAM:
        print(f'Run is not sufficient - 🏃🏼‍🧪️ handling stamina pot...')
        if not handle_stamina_pot():
            print(f'⛔ Failed to handle stamina pot for some reason - exiting...')
            return False

    withdraw_ess()
    fill_pouches()
    close_bank()
    return True


# HELPERS
def is_run_sufficient():
    return is_run_gt(20)


def handle_stamina_pot():
    global NEEDS_STAM

    is_bank_tab_open(BANK_TAB_NUM, True)
    # deposit_ess()
    is_withdraw_qty("1", True)
    if not does_img_exist(img_name="Banked_Stam_4", script_name="Cwars_Lavas", threshold=0.92, should_click=True,
                   click_middle=True):
        print(f'Failed to find Banked_Stam_4 pot')
        return False
    close_bank()
    does_img_exist(img_name="Inventory_Stam", script_name="Cwars_Lavas", threshold=0.9)
    x, y, = get_existing_img_xy()
    adj_stam_xy = x+2, y+12
    for i in range(4):
        API.AntiBan.sleep_between(3.0, 3.1)
        mouse_click(adj_stam_xy)
    if wait_for_img(img_name="Inventory_Vial", script_name="Cwars_Lavas", threshold=0.97, max_wait_sec=3):
        x, y = get_existing_img_xy()
        adj_vial_xy = x+2, y+16
        mouse_long_click(adj_vial_xy)
        does_img_exist(img_name="Drop", category="General", threshold=0.9, should_click=True, click_middle=True)

    NEEDS_STAM = False

    open_bank()

    is_run_on(True)
    return True


def is_hp_sufficient():
    return is_hp_gt(50)


def handle_eat_food():
    global NEEDS_FOOD
    is_bank_open(BANK_TAB_NUM)

    is_withdraw_qty('1')

    if not does_img_exist(img_name=f'banked_{FOOD_TYPE}', category='Banking', threshold=0.9, should_click=True, click_middle=True):
        print(f'⛔ Failed to find food ({FOOD_TYPE})')
        return False

    if not wait_for_img(img_name=f'inventory_{FOOD_TYPE}', category='Banking', threshold=0.85, img_sel='inventory'):
        print(f'⛔ Failed to find inventory food')
        return False

    invent_x, invent_y = get_existing_img_xy()

    adj_xy = invent_x + 10, invent_y + 10

    attempts = 0
    while attempts < 2:
        mouse_long_click(adj_xy)

        if not does_img_exist(img_name='eat_option', category='Interface', threshold=0.85, should_click=True, click_middle=True):
            print(f'⛔ Failed to find eat option for food...')
            if not does_img_exist(img_name='cancel_option', category='Interface', threshold=0.8, should_click=True, click_middle=True):
                print(f'⛔ Failed to find cancel option on food eat')
                return False
        attempts += 1

    NEEDS_FOOD = False

    open_bank()

    return True


def empty_pouches():
    global POUCHES_TO_USE_ARR
    is_tab_open('inventory')

    for pouch_size in POUCHES_TO_USE_ARR:
        if pouch_size == "Giant":
            craft_astrals()
        empty_pouch(pouch_size)
    return


def empty_pouch(pouch_size):
    global DEGRADED_POUCH_EXISTS

    global CACHED_SMALL_EMPTY_XY
    global CACHED_MEDIUM_EMPTY_XY
    global CACHED_LARGE_EMPTY_XY
    global CACHED_GIANT_EMPTY_XY

    global CACHED_INVENT_SMALL_POUCH
    global CACHED_INVENT_MEDIUM_POUCH
    global CACHED_INVENT_LARGE_POUCH
    global CACHED_INVENT_GIANT_POUCH

    match pouch_size:
        case "Small":
            if CACHED_INVENT_SMALL_POUCH:
                print(f'CACHED INVENT SMALL POUCH')
                mouse_long_click(CACHED_INVENT_SMALL_POUCH)
            else:
                if does_img_exist(img_name=f"Inventory_Small_Pouch", script_name="Cwars_Lavas", threshold=0.95, img_sel="first") or does_img_exist(img_name=f"Inventory_Small_Pouch_Degraded", script_name="Cwars_Lavas",threshold=0.90):
                    x, y = get_existing_img_xy()
                    adj_xy = x + 6, y + 6
                    mouse_long_click(adj_xy)
                else:
                    return

            wait_for_img(img_name='Runecrafting', category='Exp_Drops', max_wait_sec=10)

            if CACHED_SMALL_EMPTY_XY:
                print(f'CACHED SMALL EMPTY')
                mouse_click(CACHED_SMALL_EMPTY_XY)
            else:
                if wait_for_img(img_name="Empty", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=2):
                    CACHED_SMALL_EMPTY_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find SMALL Empty image to save XY - returning")
                    return

        case "Medium":
            if CACHED_INVENT_MEDIUM_POUCH:
                mouse_long_click(CACHED_INVENT_MEDIUM_POUCH)
            else:
                if does_img_exist(img_name=f"Inventory_Medium_Pouch", script_name="Cwars_Lavas", threshold=0.95, img_sel="first") or does_img_exist(img_name=f"Inventory_Medium_Pouch_Degraded", script_name="Cwars_Lavas", threshold=0.90):
                    x, y = get_existing_img_xy()
                    adj_xy = x + 6, y + 6
                    mouse_long_click(adj_xy)

            if CACHED_MEDIUM_EMPTY_XY:
                mouse_click(CACHED_MEDIUM_EMPTY_XY)
            else:
                if wait_for_img(img_name="Empty", category="General", should_click=True, click_middle=True,
                                threshold=0.9, max_wait_sec=2):
                    CACHED_MEDIUM_EMPTY_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find MEDIUM Empty image to save XY - returning")
                    return

        case "Large":
            if CACHED_INVENT_LARGE_POUCH:
                mouse_long_click(CACHED_INVENT_LARGE_POUCH)
            else:
                if does_img_exist(img_name=f"Inventory_Large_Pouch", script_name="Cwars_Lavas", threshold=0.95, img_sel="first") or does_img_exist(img_name=f"Inventory_Large_Pouch_Degraded", script_name="Cwars_Lavas", threshold=0.90):
                    x, y = get_existing_img_xy()
                    adj_xy = x + 6, y + 6
                    mouse_long_click(adj_xy)

            if CACHED_LARGE_EMPTY_XY:
                mouse_click(CACHED_LARGE_EMPTY_XY)
            else:
                if wait_for_img(img_name="Empty", category="General", should_click=True, click_middle=True,
                                threshold=0.9, max_wait_sec=2):
                    CACHED_LARGE_EMPTY_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find LARGE Empty image to save XY - returning")
                    return

        case "Giant":
            if CACHED_INVENT_GIANT_POUCH:
                mouse_long_click(CACHED_INVENT_GIANT_POUCH)
            else:
                if does_img_exist(img_name=f"Inventory_Giant_Pouch", script_name="Cwars_Lavas", threshold=0.95, img_sel="first") or does_img_exist(img_name=f"Inventory_Giant_Pouch_Degraded", script_name="Cwars_Lavas", threshold=0.90):
                    x, y = get_existing_img_xy()
                    adj_xy = x + 6, y + 6
                    mouse_long_click(adj_xy)

            if CACHED_GIANT_EMPTY_XY:
                mouse_click(CACHED_GIANT_EMPTY_XY)
            else:
                if wait_for_img(img_name="Empty", category="General", should_click=True, click_middle=True,
                                threshold=0.9, max_wait_sec=2):
                    CACHED_GIANT_EMPTY_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find GIANT Empty image to save XY - returning")
                    return
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


def check_for_degraded_pouches():
    global DEGRADED_POUCH_EXISTS

    is_tab_open("inventory", True)

    for pouch_size in POUCHES_TO_USE_ARR:
        if pouch_size != "Small":
            if does_img_exist(img_name=f"Inventory_{pouch_size}_Pouch_Degraded", script_name="Cwars_Lavas", threshold=0.85):
                DEGRADED_POUCH_EXISTS = True
                return True
    return False


def fill_pouch(pouch_size):
    global CACHED_SMALL_FILL_XY
    global CACHED_MEDIUM_FILL_XY
    global CACHED_LARGE_FILL_XY
    global CACHED_GIANT_FILL_XY

    global CACHED_INVENT_SMALL_POUCH
    global CACHED_INVENT_MEDIUM_POUCH
    global CACHED_INVENT_LARGE_POUCH
    global CACHED_INVENT_GIANT_POUCH

    print(f'small pouch fill vals: {CACHED_SMALL_FILL_XY}\nmedium: {CACHED_MEDIUM_FILL_XY}\nlarge: {CACHED_LARGE_FILL_XY}')

    match pouch_size:
        case "Small":
            if CACHED_INVENT_SMALL_POUCH:
                mouse_long_click(CACHED_INVENT_SMALL_POUCH)
            else:
                if not wait_for_invent_item_xy("Inventory_Small_Pouch", threshold=0.92):
                    return

                # does_img_exist(img_name=f"Inventory_Small_Pouch", script_name="Cwars_Lavas", threshold=0.95,
                #                img_sel="first")
                x, y = get_existing_img_xy()
                adj_xy = x+6, y+6
                CACHED_INVENT_SMALL_POUCH = adj_xy
                mouse_long_click(CACHED_INVENT_SMALL_POUCH)

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
            if CACHED_INVENT_MEDIUM_POUCH:
                mouse_long_click(CACHED_INVENT_MEDIUM_POUCH)
            else:
                if not wait_for_invent_item_xy("Inventory_Medium_Pouch", threshold=0.92):
                    return

                # does_img_exist(img_name=f"Inventory_Medium_Pouch", script_name="Cwars_Lavas", threshold=0.95,
                #                img_sel="first")
                x, y = get_existing_img_xy()
                adj_xy = x + 6, y + 6
                CACHED_INVENT_MEDIUM_POUCH = adj_xy
                mouse_long_click(CACHED_INVENT_MEDIUM_POUCH)

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
            if CACHED_INVENT_LARGE_POUCH:
                mouse_long_click(CACHED_INVENT_LARGE_POUCH)
            else:
                if not wait_for_invent_item_xy("Inventory_Large_Pouch", threshold=0.92):
                    return

                # does_img_exist(img_name=f"Inventory_Large_Pouch", script_name="Cwars_Lavas", threshold=0.95,
                #                img_sel="first")
                x, y = get_existing_img_xy()
                adj_xy = x + 6, y + 6
                CACHED_INVENT_LARGE_POUCH = adj_xy
                mouse_long_click(CACHED_INVENT_LARGE_POUCH)

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

        case "Giant":
            if CACHED_INVENT_GIANT_POUCH:
                mouse_long_click(CACHED_INVENT_GIANT_POUCH)
            else:
                if not wait_for_invent_item_xy("Inventory_Giant_Pouch", threshold=0.92):
                    return
                # does_img_exist(img_name=f"Inventory_Giant_Pouch", script_name="Cwars_Lavas", threshold=0.96,
                #                img_sel="first")
                x, y = get_existing_img_xy()
                adj_xy = x + 6, y + 6
                CACHED_INVENT_GIANT_POUCH = adj_xy
                mouse_long_click(CACHED_INVENT_GIANT_POUCH)

            if CACHED_GIANT_FILL_XY:
                print(f'Cached_giant_fill_xy = {CACHED_GIANT_FILL_XY}')
                mouse_click(CACHED_GIANT_FILL_XY)
            else:
                if wait_for_img(img_name="Fill", category="General", should_click=True, click_middle=True, threshold=0.9, max_wait_sec=1):
                    CACHED_GIANT_FILL_XY = get_existing_img_xy()
                else:
                    print(f"Couldn't find Large Fill Image to save XY - returning.")
                    if does_img_exist(img_name="Empty", category="General", threshold=0.9):
                        x, y = get_existing_img_xy()
                        adj_xy = x + 10, y + 8
                        CACHED_GIANT_FILL_XY = adj_xy
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


def withdraw_ess():
    global CACHED_BANKED_ESS_XY

    is_bank_tab_open(BANK_TAB_NUM, True)
    is_withdraw_qty("all", True)
    if CACHED_BANKED_ESS_XY:
        mouse_click(CACHED_BANKED_ESS_XY)
        return True
    else:
        if wait_for_img(img_name="Banked_Ess", script_name="Cwars_Lavas", threshold=0.90, should_click=True, click_middle=True, img_sel="last"):
            x, y = get_existing_img_xy()
            adj_xy = x+22, y+6
            CACHED_BANKED_ESS_XY = adj_xy
            return True
        else:
            return False