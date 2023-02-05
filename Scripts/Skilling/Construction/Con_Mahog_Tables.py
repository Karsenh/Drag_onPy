import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open
from API.Mouse import mouse_long_click, mouse_click
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
import pyautogui as pag

SCRIPT_NAME = "Con_Mahog_Tables"

BUILD_ATTEMPTS = 0
REMOVE_ATTEMPTS = 0

BUILD_TABLE_XY = None
SEL_BUILD_XY = None

REMOVE_TABLE_XY = None
SEL_REMOVE_XY = None

CACHED_SEL_MAHOG_TABLE = None
CACHED_YES_REMOVE_XY = None

BUILD_NUM = 1


def start_constructing_tables(curr_loop):
    global BUILD_NUM

    if curr_loop != 1:
        print(f'Not first loop')
        if BUILD_NUM == 1:
            if not wait_for_planks(quick=True):
                if call_butler():
                    if need_to_pay_butler():
                        pay_butler()
                    if not wait_for_planks():
                        print(f"⛔ Couldn't find planks and tried to pay butler but something went wrong.")
                        return False
        # If our inventory is NOT full...
        # if not wait_for_planks(quick=True):
        if BUILD_NUM != 3:
            print(f"{BUILD_NUM} - Loop {curr_loop}")
            build_table()
            print(f"{BUILD_NUM} - Loop {curr_loop}")
            remove_table()
        else:
            print(f"Third Build - Loop {curr_loop} - BUILD_NUM = {BUILD_NUM}")
            build_table()
            fetch_planks()
            print(f"Third Remove - Loop {curr_loop}")
            remove_table()

        BUILD_NUM += 1

        if BUILD_NUM == 5:
            print(f"wait_for_planks didn't find planks and BUILD_NUM == 4")

            BUILD_NUM = 1

    else:
        print(f'This is the first loop')
        setup_interface("east", 5, "up")

        # Check inventory to see if we already have planks
        if wait_for_planks(quick=True):
            return True
        else:
            # Get planks if we don't have them
            fetch_planks()
            return wait_for_planks()

    return True


def fetch_planks():
    # Click or Interface Summon Demon Butler
    call_butler()

    if not wait_for_img(img_name="Repeat_Last_Fetch", script_name=SCRIPT_NAME, threshold=0.85, should_click=True):
        if not wait_for_img(img_name="Go_to_Bank", script_name=SCRIPT_NAME, threshold=0.85, should_click=True):
            if not need_to_pay_butler():
                print(f'⛔ Failed to find any servant dialogue...')
                return False
            else:
                print(f'💸 Servant requires payment')
                # Servant requires payment
                pay_butler()
                if wait_for_planks():
                    return True
                else:
                    fetch_planks()
        else:
            # Go to bank selected
            print(f'💨 Go to bank selected')
            # Bring something from bank
            if wait_for_img(img_name="Bring_Something", script_name=SCRIPT_NAME, should_click=True, threshold=0.85):
                tap_to_continue_dialogue()
                API.AntiBan.sleep_between(0.2, 0.3)
                tap_to_continue_dialogue()
                # Select Mahogany Planks & Input 24
                if wait_for_img(img_name="Mahogany_Planks_Selection", script_name="Con_Mahog_Tables", threshold=0.90,
                                should_click=True):
                    if wait_for_img(img_name="Enter_Amount", category="Chatbox", threshold=0.9):
                        pag.press('2')
                        API.AntiBan.sleep_between(0.5, 0.7)
                        pag.press('4')
                        API.AntiBan.sleep_between(0.5, 0.7)
                        pag.press('enter')
    else:
        print(f'🔁 Repeat Last Fetch Selected')

    return True


def wait_for_planks(quick=False):
    # Wait for full inventory planks
    is_tab_open("inventory", should_be_open=True)

    if not quick:
        return wait_for_img(img_name="Full_Inventory_Planks", script_name="Con_Mahog_Tables", threshold=0.92, max_wait_sec=8)
    else:
        return does_img_exist(img_name="Full_Inventory_Planks", script_name="Con_Mahog_Tables", threshold=0.92)


# -------
# HELPERS
# -------
def need_to_pay_butler():
    return wait_for_img(img_name="Needs_Payment", script_name=SCRIPT_NAME, max_wait_sec=2)


def pay_butler():
    pag.press('space')
    wait_for_img(img_name="Pay_Selection", script_name="Con_Mahog_Tables", threshold=0.90, should_click=True)
    API.AntiBan.sleep_between(1.1, 1.2)
    pag.press('space')
    return


def call_butler():
    if click_butler():
        return True

    is_tab_open("settings", should_be_open=True)

    if not wait_for_img(img_name="Control_Settings_House_Options", category="Interface", should_click=True):
        if not wait_for_img(img_name="Controls_Settings_Tab", category="Interface", should_click=True):
            print(f'⛔ Something went wrong trying to find control settings tab in Settings menu')
            return False
        else:
            if not wait_for_img(img_name="Control_Settings_House_Options", category="Interface", should_click=True):
                print(f'⛔ Couldnt find House control settings button')
            else:
                if not wait_for_img(img_name="House_Option_Call_Servant", category="Interface", should_click=True):
                    print(f'⛔ Couldnt find Button to Call Servant')
                    return False
    else:
        if not wait_for_img(img_name="House_Option_Call_Servant", category="Interface", should_click=True):
            print(f'⛔ Clicked House_Control_Settings but cant find Call Servant Button')
            return False

    return True


def click_butler():
    for i in range(0, 3):
        if does_img_exist(img_name=f"Butler_{i}", script_name=SCRIPT_NAME, should_click=True, threshold=0.98):
            return True
    return False


def repeat_last_fetch():
    return wait_for_img(img_name="Repeat_Last_Fetch", script_name=SCRIPT_NAME, should_click=True)


def build_table():
    global BUILD_ATTEMPTS
    global BUILD_TABLE_XY
    global SEL_BUILD_XY
    global CACHED_SEL_MAHOG_TABLE

    if not wait_for_img(img_name="Empty_Table", script_name="Con_Mahog_Tables", threshold=0.9, max_wait_sec=3):
        print(f"⛔ Couldn't find empty table - checking if table already there and removing if so.")
        if remove_table():
            print(f'Attempting to build table after removing')
            build_table()
        else:
            print(f'Couldnt build or remove')
            return False

    mouse_long_click(get_existing_img_xy())

    if SEL_BUILD_XY:
        mouse_click(SEL_BUILD_XY)
    else:
        if not wait_for_img(img_name="Build", script_name="Con_Mahog_Tables", threshold=0.9,
                            max_wait_sec=2):
            if BUILD_ATTEMPTS < 2:
                BUILD_ATTEMPTS += 1
                build_table()
            else:
                print(f"⛔ Attempted to build {BUILD_ATTEMPTS} times and failed every time - exiting.")
                return False

        x, y = get_existing_img_xy()
        SEL_BUILD_XY = x + 6, y + 5
        mouse_click(SEL_BUILD_XY)

    if CACHED_SEL_MAHOG_TABLE:
        API.AntiBan.sleep_between(0.6, 0.7)
        mouse_click(CACHED_SEL_MAHOG_TABLE)
    else:
        if not wait_for_img(img_name="Create_Mahogany_Table", script_name="Con_Mahog_Tables", should_click=True, threshold=0.9):
            print(f"⛔ Couldn't find Mahogany Table Selection in Construction Menu")
            return False
        CACHED_SEL_MAHOG_TABLE = get_existing_img_xy()

    # if wait_for_img(img_name="Construction", category="Exp_Drops"):
    #     print(f'Saw exp drop')
    # else:
    #     print(f'No exp drop seen!')

    return True


def remove_table():
    global REMOVE_ATTEMPTS
    global REMOVE_TABLE_XY
    global SEL_REMOVE_XY
    global CACHED_YES_REMOVE_XY

    if not wait_for_img(img_name="Built_Table", script_name="Con_Mahog_Tables", threshold=0.98, max_wait_sec=3):
        print(f"⛔ Couldn't find built table to remove - exiting.")
        return False

    mouse_long_click(get_existing_img_xy())

    if SEL_REMOVE_XY:
        mouse_click(SEL_REMOVE_XY)
    else:
        if not wait_for_img(img_name="Remove", script_name="Con_Mahog_Tables", threshold=0.9, max_wait_sec=3):
            if REMOVE_ATTEMPTS < 2:
                REMOVE_ATTEMPTS += 1
                remove_table()
            else:
                print(f"⛔ Attempted to remove built table {REMOVE_ATTEMPTS} times and failed. Exiting")
                return False
        else:
            x, y = get_existing_img_xy()
            SEL_REMOVE_XY = x + 6, y + 5
            mouse_click(SEL_REMOVE_XY)

    if CACHED_YES_REMOVE_XY:
        API.AntiBan.sleep_between(0.5, 0.6)
        mouse_click(CACHED_YES_REMOVE_XY)
    else:
        if not wait_for_img(img_name="Yes_Remove", script_name="Con_Mahog_Tables", should_click=True, threshold=0.9, max_wait_sec=3):
            return False
        CACHED_YES_REMOVE_XY = get_existing_img_xy()

    return True


def tap_to_continue_dialogue():
    return wait_for_img(img_name="Tap_Continue", script_name="Con_Mahog_Tables", threshold=0.90, should_click=True)