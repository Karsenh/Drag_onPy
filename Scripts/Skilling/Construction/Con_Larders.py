import API.AntiBan
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Interface.General import setup_interface, is_tab_open
from API.Mouse import mouse_long_click, mouse_click, mouse_move
from API.Skill_Levels import get_skill_level


SCRIPT_NAME = "Con_Larders"
UNNOTE_ATTEMPTS = 0
REMOVE_ATTEMPTS = 0
BUILD_ATTEMPTS = 0
PLANK_TYPE = "Regular"
AUTO_DETECT_PLANKS = False

# NOTES
# Start in front of phials with noted planks, money to unnote, hammer, saw, and nails


def start_constructing_larders(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')
        if not unnote_planks():
            print(f"⛔ We must be out of planks")
            return False
        move_to_portal()
        API.AntiBan.sleep_between(4.0, 4.1)
        click_portal()
        enter_house_building_mode()
        move_to_larder_hotspot()
        construct_larders()
        leave_house()
        move_to_phials()
    else:
        print(f'This is the first loop')
        setup_interface("north", 4, "up")
        set_plank_type()
        if not unnote_planks():
            print(f"⛔ We must be out of planks")
            return False
        move_to_portal()
        API.AntiBan.sleep_between(4.0, 4.1)
        click_portal()
        enter_house_building_mode()
        move_to_larder_hotspot()
        construct_larders()
        leave_house()
        move_to_phials()

    return True


def set_plank_type():
    global PLANK_TYPE
    global AUTO_DETECT_PLANKS

    plank_options = ["Regular", "Oak"]

    if AUTO_DETECT_PLANKS:
        if does_img_exist(img_name="Noted_Inventory_Oak_Planks", script_name="Con_Larders", threshold=0.95, should_click=True):
            PLANK_TYPE = "Oak"

    else:
        con_level = get_skill_level("construction")
        print(f'Construction level: {con_level}')
        if con_level > 32:
            PLANK_TYPE = "Oak"

    print(f'PLANK TYPE SET = {PLANK_TYPE}')
    return True



    get_skill_level()
    return


def unnote_planks():
    global UNNOTE_ATTEMPTS

    if not click_noted_planks():
        return False
    else:
        API.AntiBan.sleep_between(0.3, 0.4)

    click_phials()

    if not exchange_all_planks():
        if not does_img_exist(img_name="Too_Full_Dialogue", script_name=SCRIPT_NAME):
            if UNNOTE_ATTEMPTS < 2:
                if not unnote_planks():
                    UNNOTE_ATTEMPTS += 1
                    return False
            else:
                print(f"Exceeded Unnote planks attempts {UNNOTE_ATTEMPTS}")
                return False
        else:
            print(f'Inventory was too full - continuing anyways since we must have planks')

    return True


def construct_larders():
    for i in range(1, 3):
        build_larder()
        remove_larder()
    return


# -------
# HELPERS
# -------
def click_noted_planks():
    is_tab_open("inventory", True)
    return wait_for_img(img_name=f"Noted_Inventory_{PLANK_TYPE}_Planks", threshold=0.95, script_name=SCRIPT_NAME, should_click=True, max_wait_sec=3)


def click_phials():
    should_keep_checking = True
    num_attempts = 0

    while should_keep_checking and num_attempts < 8:
        for i in range(0, 10):
            if does_img_exist(img_name=f'p_{i}', script_name=SCRIPT_NAME, should_click=True, threshold=0.85):
                should_keep_checking = False
                break
        num_attempts += 1

    print(f'No longer searching for Phials. Num_attempts = {num_attempts}')
    return


def move_to_portal():
    return does_img_exist(img_name="Move_to_Portal", script_name=SCRIPT_NAME, should_click=True, x_offset=55, y_offset=25)


def click_portal():
    return wait_for_img(img_name="Teleport_Portal", script_name="Con_Larders", should_click=True, threshold=0.9, max_wait_sec=10)


def enter_house_building_mode():
    return wait_for_img(img_name="Building_Mode", script_name=SCRIPT_NAME, should_click=True, max_wait_sec=5, threshold=0.9)


def move_to_larder_hotspot():
    return wait_for_img(img_name="Larder_Minimap_Spot", script_name="Con_Larders", should_click=True, x_offset=12, y_offset=5, threshold=0.85, max_wait_sec=15)


def remove_larder():
    global REMOVE_ATTEMPTS

    if not wait_for_img(img_name="Built_Larder", script_name=SCRIPT_NAME):
        print(f"⛔ Couldn't find built larder")
        return False

    mouse_long_click(get_existing_img_xy())

    if not wait_for_img(img_name="Remove", script_name=SCRIPT_NAME, should_click=True):
        print(f"⛔ Couldn't find 'Remove' option after long-clicking Built Larder")
        if REMOVE_ATTEMPTS < 2:
            if not remove_larder():
                REMOVE_ATTEMPTS += 1
                return False
        else:
            print(f'⛔ Tried {REMOVE_ATTEMPTS} times to remove larder and failed to find Remove image')
            return False
    if not wait_for_img(img_name="Yes_Remove", script_name=SCRIPT_NAME, should_click=True):
        print(f"⛔ Couldn't find 'Yes' Dialogue confirmation to remove Larder")
        return False

    return True


def build_larder():
    global BUILD_ATTEMPTS
    global PLANK_TYPE

    if not wait_for_img(img_name="Empty_Larder", script_name="Con_Larders", threshold=0.95):
        print(f"⛔ Couldn't find 'Empty Larder' space to long-click")
        return False

    mouse_long_click(get_existing_img_xy())

    if not wait_for_img(img_name="Build", script_name="Con_Larders", should_click=True):
        print(f"⛔ Couldn't find 'Build option' after long-clicking empty larder hotspot")
        if BUILD_ATTEMPTS < 2:
            if not build_larder():
                BUILD_ATTEMPTS += 1
                return False
            else:
                print(f'Building and removing extra larder to compensate for loop misalignment')
                remove_larder()
                build_larder()
        else:
            print(f'⛔ Tried {BUILD_ATTEMPTS} times to build larder')
            return False
        return False

    if not wait_for_img(img_name=f"{PLANK_TYPE}_Larder_Selection", script_name="Con_Larders", should_click=True):
        print(f"⛔ Couldn't find '{PLANK_TYPE} Larder menu selection' after clicking Build option")

    return wait_for_img(img_name="Construction", category="Exp_Drops", max_wait_sec=30)


def leave_house():
    is_tab_open("settings", should_open=True)

    if not wait_for_img(img_name="House_Control_Settings", category="Interface", should_click=True):
        if not wait_for_img(img_name="Control_Settings_Tab", category="Interface", should_click=True):
            print(f'⛔ Something went wrong trying to find control settings tab in Settings menu')
            return False
        else:
            if not wait_for_img(img_name="House_Control_Settings", category="Interface", should_click=True):
                print(f'⛔ Couldnt find House control settings button')
            else:
                if not wait_for_img(img_name="Leave_House_Control_Setting", category="Interface", should_click=True):
                    print(f'⛔ Couldnt find Button to leave house')
                    return False
    else:
        if not wait_for_img(img_name="Leave_House_Control_Setting", category="Interface", should_click=True):
            print(f'⛔ Clicked House_Control_Settings but cant find Leave House Button')
            return False
        else:
            return wait_for_img(img_name="Left_House_Flag", category="Interface")

    return wait_for_img(img_name="Left_House_Flag", category="Interface")


def move_to_phials():
    phials_xy = 1319, 240
    mouse_click(phials_xy)
    # API.AntiBan.sleep_between(4.5, 4.6)
    return


def exchange_all_planks():
    return wait_for_img(img_name="Exchange_All_Planks", script_name="Con_Larders", should_click=True)