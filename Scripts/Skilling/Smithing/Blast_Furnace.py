import random

import API.AntiBan
from API.Mouse import mouse_click, mouse_move, mouse_long_click
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open, get_xy_for_invent_slot, is_run_on, is_run_gt
from API.Interface.Bank import close_bank, is_bank_open, is_bank_tab_open, is_withdraw_qty
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist_in_thresh, does_color_exist_in_sub_image, get_existing_img_xy
import pyautogui as pag

SCRIPT_NAME = "Blast_Furnace"
BANK_TAB = 1
ORE_TYPE = 'Addy'  # Mith, Addy, Rune, Gold

# Cached coordinates
CACHED_BANKED_COAL_XY = None
CACHED_BANKED_ORE_XY = None
CACHED_INVENT_COAL_BAG_XY = None
CACHED_FILL_COAL_BAG_XY = None
CACHED_EMPTY_XY = None
CACHED_BANK_FROM_BARS_XY = None


def start_blasting(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        # Open the bank from bar claim - wait for it to open and if not return false
        if not open_bank_from_bars():
            return False

        # Deposit bars in inventory
        deposit_bars()
        # Drink stam if necessary
        handle_run()
        # Fill Coal Pouch
        fill_coal_bag()
        # Fill Inventory with coal
        withdraw_coal()
        # Click Belt
        click_belt_from_bank()
        # Wait for coal deposit
        wait_for_belt_deposit('coal')
        # Empty coal bag
        empty_coal_bag()
        # Deposit Coal
        click_belt_from_belt()
        # Wait for coal deposit
        wait_for_belt_deposit('coal')
        # Click bank from belt - wait for bank open (10 seconds) - return false if not
        if not open_bank_from_belt():
            return False
        handle_run()
        # Fill Coal Pouch
        fill_coal_bag()
        # Fill Inventory with ore
        withdraw_ore()
        # Deposit ore on belt
        click_belt_from_bank()
        wait_for_belt_deposit('addy')
        empty_coal_bag()
        click_belt_from_belt()
        # API.AntiBan.sleep_between(0.4, 0.5)
        wait_for_belt_deposit('coal')
        return claim_bars()

    else:
        print(f'First loop!')
        setup_interface('north', 1, 'up')
        open_bank_from_bank()
        handle_run()
        # deposit_money_into_coffer()
        withdraw_coal_bag()
        fill_coal_bag()
        withdraw_coal()
        click_belt_from_bank()
        wait_for_belt_deposit('coal')
        empty_coal_bag()
        click_belt_from_belt()
        wait_for_belt_deposit('coal')
        open_bank_from_belt()
        handle_run()
        fill_coal_bag()
        withdraw_ore()
        click_belt_from_bank()
        wait_for_belt_deposit('addy')
        empty_coal_bag()
        click_belt_from_belt()
        wait_for_belt_deposit('coal')
        return claim_bars()


def deposit_money_into_coffer():
    withdraw_72k()
    close_bank()
    open_coffer_from_bank()
    deposit_72k()
    open_bank_from_coffer()
    return


def handle_run():
    global NEED_STAM

    if not is_run_gt(9):
        print(f"We're low on run energy! Need Stamina pot")
        NEED_STAM = True

        is_withdraw_qty('1', True)

        if not does_img_exist(img_name='Banked_Stamina_4', script_name=SCRIPT_NAME, threshold=0.94, should_click=True, click_middle=True):
            return False

        if not wait_for_img(img_name='Inventory_Stamina_4', script_name=SCRIPT_NAME, img_sel='inventory', threshold=0.9):
            return False

        close_bank()

        is_tab_open('inventory', True)

        x, y = get_existing_img_xy()
        inventory_stamina_xy = x+6, y+6

        for i in range(1, 5):
            mouse_click(inventory_stamina_xy)
            API.AntiBan.sleep_between(1.5, 1.6)

        is_run_on(True)
        API.AntiBan.sleep_between(0.3, 0.4)

        open_bank_from_bank()

        if not is_bank_open():
            return False

        is_withdraw_qty('all', True)

        mouse_click(inventory_stamina_xy)
    return True


def open_bank_from_belt():
    wait_for_img(img_name='Bank_From_Belt', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)
    return is_bank_open(max_wait_sec=10)


def claim_bars():
    can_claim_bars = False
    claim_attempts = 0

    # Move to bar dispenser
    bar_dispenser_xy = 696, 597
    mouse_click(bar_dispenser_xy)

    API.AntiBan.sleep_between(4.0, 4.1)

    bar_claim_region = 292, 140, 350, 167
    green_color = 39, 159, 31

    while not can_claim_bars:
        claim_attempts += 1
        print(f'Checking if we can_claim_bars... claim_attempts: {claim_attempts}')
        can_claim_bars = does_color_exist_in_sub_image(bar_claim_region, green_color, 'Can_Claim_Green_Check', count_min=100, color_tolerance=15)
        if claim_attempts > 30:
            if not handle_level_dialogue():
                return False
            else:
                can_claim_bars = does_color_exist_in_sub_image(bar_claim_region, green_color, 'Can_Claim_Green_Check', count_min=100, color_tolerance=15)

    if can_claim_bars:
        long_click_dispenser()

        if not take_bars():
            print(f'Failed to find "Take" option after right clicking bar claim.')

            if not does_img_exist(img_name='Cancel_Take_Bars', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
                print(f'Failed to find cancel take bars on retry as well')
                return False
            else:
                long_click_dispenser()
                if not take_bars():
                    print(f'Something has really gone wrong... Exiting.')
                    return False

        if not wait_for_img(img_name='Claim_Bars_Open', script_name=SCRIPT_NAME, threshold=0.9, max_wait_sec=10):

            does_img_exist(img_name='Cancel_Take_Bars', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True)

            # print(f'')
            long_click_dispenser()

            if not take_bars():
                print(f'Failed to find "Take" option after right clicking bar claim.')
                if not does_img_exist(img_name='Cancel_Take_Bars', script_name=SCRIPT_NAME, threshold=0.9,
                                      should_click=True, click_middle=True):
                    print(f'Failed to find cancel take bars to retry as well')
                    return False
                else:
                    long_click_dispenser()
                    if not take_bars():
                        print(f'Something has really gone wrong... Exiting.')
                        return False

        # ToDo Add check to make sure 'all' is selected

        if not wait_for_img(img_name='Click_Bar_Chat', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
            print(f'Failed to find bar to click')
            return False

        # pag.press('space')
        return wait_for_img(img_name='Bars_Claimed', script_name=SCRIPT_NAME, threshold=0.9)
    else:
        print(f'Can_Claim_Bars is false... exiting.')
        return False


def wait_for_belt_deposit(ore):
    ore_present = True
    attempts = 0

    print(f'Opening inventory to check when the ore has been deposited on the belt.')

    API.AntiBan.sleep_between(2.0, 2.1)

    is_tab_open('inventory', True)

    while ore_present and attempts < 100:
        ore_present = does_img_exist(img_name=f'Inventory_{ore}', script_name=SCRIPT_NAME, threshold=0.9)
        attempts += 1

    return ore_present


def open_bank_from_bars():
    global CACHED_BANK_FROM_BARS_XY
    print(f'🏦 Opening bank from bar claim')

    if CACHED_BANK_FROM_BARS_XY:
        mouse_click(CACHED_BANK_FROM_BARS_XY)
    else:
        if not does_img_exist(img_name='Bank_From_Bars', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
            bank_from_bar_xy = 1000, 628
            mouse_click(bank_from_bar_xy)
        else:
            x, y = get_existing_img_xy()
            CACHED_BANK_FROM_BARS_XY = x + 6, y + 6
            mouse_click(CACHED_BANK_FROM_BARS_XY)

    return is_bank_open(max_wait_sec=10)


def open_bank_from_coffer():
    if not wait_for_img(img_name="Bank_From_Coffer", script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
        return False
    else:
        return is_bank_open(max_wait_sec=6)


def open_bank_from_bank():
    if not does_img_exist(img_name="Bank_From_Bank", script_name=SCRIPT_NAME, threshold=0.80, should_click=True, click_middle=True):
        return False
    else:
        return is_bank_open(max_wait_sec=5)


def open_coffer_from_bank():
    manual_coffer_xy = 697, 456

    if not wait_for_img(img_name="Coffer_From_Bank", script_name=SCRIPT_NAME, threshold=0.72, should_click=True, click_middle=True, max_wait_sec=3):
        print(f'Failed to find Coffer_From_Bank img - 🤖 Manually clicking')
        mouse_click(manual_coffer_xy)
    return True


# HELPERS
def withdraw_72k():
    is_bank_tab_open(0, True)

    print(f'First loop - withdrawing x')
    if not does_img_exist(img_name='Banked_Coins', script_name=SCRIPT_NAME, threshold=0.9):
        print(f'Banked_Coins Not Found!')
        return False

    x, y = get_existing_img_xy()
    banked_coins_xy = x + 6, y + 6

    mouse_long_click(banked_coins_xy)

    # Click to withdraw 'x' gold
    does_img_exist(img_name='withdraw_x', category='Banking', should_click=True, click_middle=True, threshold=0.95)

    API.AntiBan.sleep_between(0.9, 1.0)

    pag.press('7')
    pag.press('2')

    return does_img_exist(img_name='K', category='Banking', threshold=0.94, should_click=True, click_middle=True)


def deposit_72k():
    if not wait_for_img(img_name='Deposit_Coins', script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
        return False
    wait_for_img(img_name='K', category='Banking', threshold=0.9, should_click=True, click_middle=True)
    # API.AntiBan.sleep_between(0.8, 0.9)
    pag.press('7')
    pag.press('2')
    return does_img_exist(img_name='K', category='Banking', threshold=0.9, should_click=True, click_middle=True)


def withdraw_coal_bag():
    is_bank_tab_open(1, True)
    return does_img_exist(img_name='Banked_Coal_Bag', script_name=SCRIPT_NAME, img_sel="banked", threshold=0.95, should_click=True, click_middle=True)


def fill_coal_bag():
    global CACHED_INVENT_COAL_BAG_XY
    global CACHED_FILL_COAL_BAG_XY

    is_bank_tab_open(BANK_TAB, True)

    if CACHED_INVENT_COAL_BAG_XY:
        print(f'CACHED_INVENT_COAL_BAG: (Exists): {CACHED_INVENT_COAL_BAG_XY}')
        mouse_long_click(CACHED_INVENT_COAL_BAG_XY)
    else:
        if not wait_for_img(img_name='Inventory_Coal_Bag', script_name='Blast_Furnace', img_sel='inventory', threshold=0.9):
            return False
        x, y = get_existing_img_xy()
        CACHED_INVENT_COAL_BAG_XY = x + 6, y + 6
        print(f'CACHED_INVENT_COAL_BAG: (NOT exists): {CACHED_INVENT_COAL_BAG_XY}')
        mouse_long_click(CACHED_INVENT_COAL_BAG_XY)

    if CACHED_FILL_COAL_BAG_XY:
        mouse_click(CACHED_FILL_COAL_BAG_XY)
    else:
        if not does_img_exist(img_name='Fill_Coal_Bag', script_name='Blast_Furnace', threshold=0.9):
            return False
        else:
            x, y = get_existing_img_xy()
            CACHED_FILL_COAL_BAG_XY = x + 6, y + 4
            mouse_click(CACHED_FILL_COAL_BAG_XY)

    API.AntiBan.sleep_between(0.3, 0.4)
    return True


def withdraw_coal():
    global CACHED_BANKED_COAL_XY

    is_withdraw_qty('all', True)

    if CACHED_BANKED_COAL_XY:
        mouse_click(CACHED_BANKED_COAL_XY)
    else:
        if not does_img_exist(img_name='Banked_Coal', script_name=SCRIPT_NAME, threshold=0.95):
            return False
        else:
            x, y = get_existing_img_xy()
            CACHED_BANKED_COAL_XY = x + 6, y + 6
            mouse_click(CACHED_BANKED_COAL_XY)

    API.AntiBan.sleep_between(0.3, 0.4)
    return True


def withdraw_ore():
    global CACHED_BANKED_ORE_XY

    print(f'Withdrawing_Ore')

    is_withdraw_qty('all', None)
    if CACHED_BANKED_ORE_XY:
        mouse_click(CACHED_BANKED_ORE_XY)
    else:
        if not does_img_exist(img_name=f'Banked_{ORE_TYPE}', script_name=SCRIPT_NAME, threshold=0.95):
            return False
        else:
            x, y = get_existing_img_xy()
            CACHED_BANKED_ORE_XY = x + 6, y + 6
            mouse_click(CACHED_BANKED_ORE_XY)

    API.AntiBan.sleep_between(0.1, 0.2)
    return True


def deposit_bars():
    print(f'Depositing Bars')
    r_slot = random.randint(2, 27)
    mouse_click(get_xy_for_invent_slot(r_slot))
    return


def click_belt_from_bank():
    print(f'Clicking_belt_from_bank')
    furnace_xy = 633, 226
    mouse_click(furnace_xy)
    API.AntiBan.sleep_between(0.8, 0.9)
    return


def click_belt_from_belt():
    print(f'Clicking ')
    furance_xy = 778, 455
    mouse_click(furance_xy)
    return


def empty_coal_bag():
    global CACHED_INVENT_COAL_BAG_XY
    global CACHED_EMPTY_XY

    is_tab_open('inventory', True)

    # Long click the inventory coal bag
    if CACHED_INVENT_COAL_BAG_XY:
        mouse_long_click(CACHED_INVENT_COAL_BAG_XY)
    else:
        if not does_img_exist(img_name='Inventory_Coal_Bag', script_name=SCRIPT_NAME, threshold=0.9):
            return False
        x, y = get_existing_img_xy()
        CACHED_INVENT_COAL_BAG_XY = x + 6, y + 6
        mouse_long_click(CACHED_INVENT_COAL_BAG_XY)

    # Click 'Empty'
    if CACHED_EMPTY_XY:
        mouse_click(CACHED_EMPTY_XY)
    else:
        if not does_img_exist(img_name='Empty_Coal_Bag', script_name='Blast_Furnace', threshold=0.9):
            return False

        x, y = get_existing_img_xy()
        CACHED_EMPTY_XY = x + 6, y + 6
        mouse_click(CACHED_EMPTY_XY)

    return wait_for_img(img_name='Coal_Bag_Is_Empty', script_name='Blast_Furnace', threshold=0.9)


def long_click_dispenser():
    if not wait_for_img(img_name='Bar_Claim', script_name=SCRIPT_NAME, threshold=0.9):
        # print(f'Failed to find Bar Dispenser - Exiting.')
        manual_bar_claim = 752, 422
        mouse_long_click(manual_bar_claim)
    else:
        click_to_claim = get_existing_img_xy()
        mouse_long_click(click_to_claim)
    return


def take_bars():
    return does_img_exist(img_name='Take_Bars', script_name=SCRIPT_NAME, threshold=0.94, should_click=True, click_middle=True)


def handle_level_dialogue():
    if does_img_exist("level_up", category="General"):
        pag.press('space')
        API.AntiBan.sleep_between(1.1, 2.3)
        pag.press('space')
        API.AntiBan.sleep_between(0.8, 1.7)
        return True
    else:
        return False