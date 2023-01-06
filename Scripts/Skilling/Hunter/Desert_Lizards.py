import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Mouse import mouse_click

SCRIPT_NAME = "Desert_Lizards"

AT_TRAP = None
INTL_CHECK = True
TRAP_CHECK_ORDER = []

CAUGHT_THRESH = 0.89
DOWN_THRESH = 0.95


def start_catching_desert_lizards(curr_loop):
    global AT_TRAP

    if curr_loop != 1:
        print(f'Not first loop\nTRAP_CHECK_ORDER = {TRAP_CHECK_ORDER}')

        trap_to_fix = check_traps_from(curr_trap_num=AT_TRAP)

        if trap_to_fix:
            fix_trap(trap_to_fix)

    else:
        print(f'First loop')
        intl_interface_setup()

        set_intl_trap(1)
        set_intl_trap(2)
        set_intl_trap(3)

        # By this point:
        # TRAP_CHECK_ORDER = [ 1, 2, 3]
        # AT_TRAP = 3

    return True


def set_intl_trap(trap_num):
    global AT_TRAP
    global TRAP_CHECK_ORDER

    if wait_for_img(img_name=f"Set_intl_trap_{trap_num}", script_name=SCRIPT_NAME, should_click=True, threshold=0.92, y_offset=10, x_offset=6):
        AT_TRAP = trap_num
        TRAP_CHECK_ORDER.append(trap_num)
        print(f'🟢 Setting initial trap: {trap_num}\n🟢 AT_TRAP set = {AT_TRAP}\n🟢 TRAP_CHECK_ORDER = {TRAP_CHECK_ORDER}')
        API.AntiBan.sleep_between(3.0, 3.1)
    return


def check_traps_from(curr_trap_num):
    global INTL_CHECK
    global TRAP_CHECK_ORDER

    if INTL_CHECK:
        # First time checking - check in FIFO order (oldest)
        check_order = TRAP_CHECK_ORDER
        INTL_CHECK = False
    else:
        # Second time checking and above - check in LIFO order (closest)
        check_order = TRAP_CHECK_ORDER

    print(f'Iterating over check_order: {check_order}')
    for trap_num in check_order:
        print(f'Checking trap: {trap_num}')
        bad_trap = check_trap(check_trap_num=trap_num, at_trap=curr_trap_num)
        if bad_trap:
            return bad_trap

    return None


def check_trap(check_trap_num, at_trap):
    global AT_TRAP

    if wait_for_img(img_name=f"Trap_{check_trap_num}_Caught_From_{at_trap}", script_name=SCRIPT_NAME, threshold=CAUGHT_THRESH, max_wait_sec=5):
        print(f'🟢 TRAP {check_trap_num} 🧤 CAUGHT from {at_trap}')
        return f"{check_trap_num}_Caught"

    if does_img_exist(img_name=f"Trap_{check_trap_num}_Down_From_{at_trap}", script_name=SCRIPT_NAME, threshold=DOWN_THRESH):
        print(f'🟢 TRAP {check_trap_num} 🔻 DOWN from {at_trap}')
        return f"{check_trap_num}_Down"

    return None


def fix_trap(trap_to_fix):
    global AT_TRAP

    print(f'⚙ trap_to_fix = {trap_to_fix}')
    trap_num = trap_to_fix.split("_")[0]
    state = trap_to_fix.split("_")[1]

    # If Caught
    if state == "Caught":
        print(f'STATE = 🧤{state}🧤 for TRAP {trap_num} AT_TRAP {AT_TRAP}')
        x, y = get_existing_img_xy()
        adjusted_xy = x+16, y+25
        if AT_TRAP == 1:
            if trap_num == "3":
                adjusted_xy = x, y-20
        if AT_TRAP == 2:
            if trap_num == "3":
                print(f'❄ Custom offset for caught 3 from 2')
                adjusted_xy = x, y+28
            if trap_num == "1":
                print(f"🔥 Custom offset for caught 1 from 2")
                adjusted_xy = x-12, y-15
        mouse_click(adjusted_xy)
        wait_for_img(img_name="Hunter", category="Exp_Drops")

        is_tab_open("inventory", True)
        does_img_exist(img_name="Drop_Lizard", script_name=SCRIPT_NAME, threshold=0.9, should_click=True)
        is_tab_open("inventory", False)

        print(f'AT_TRAP Before: {AT_TRAP}')
        AT_TRAP = int(trap_num)
        print(f'AT_TRAP NOW: {AT_TRAP}\nTRAP_CHECK_ORDER = {TRAP_CHECK_ORDER}')
        TRAP_CHECK_ORDER.remove(AT_TRAP)
        TRAP_CHECK_ORDER.insert(2, AT_TRAP)
        print(f'TRAP_CHECK_ORDER NOW: {TRAP_CHECK_ORDER}')

        if not wait_for_img(img_name=f"Reset_Trap_{trap_num}_Caught", script_name=SCRIPT_NAME, should_click=True, threshold=0.72, max_wait_sec=3, img_sel="first"):
            wait_for_img(img_name=f"Reset_Trap_{trap_num}_Down", script_name=SCRIPT_NAME, should_click=True, threshold=0.7)
    else:
        print(f'STATE = 🔻{state}🔻 for TRAP {trap_num}')
        x, y = get_existing_img_xy()
        adjusted_xy = x+15, y+12
        mouse_click(adjusted_xy)
        API.AntiBan.sleep_between(3.5, 3.6)

        print(f'AT_TRAP Before: {AT_TRAP}')
        AT_TRAP = int(trap_num)
        print(f'AT_TRAP NOW: {AT_TRAP}\nTRAP_CHECK_ORDER = {TRAP_CHECK_ORDER}')
        TRAP_CHECK_ORDER.remove(AT_TRAP)
        # TRAP_CHECK_ORDER.append(AT_TRAP)
        TRAP_CHECK_ORDER.insert(2, AT_TRAP)
        print(f'TRAP_CHECK_ORDER NOW: {TRAP_CHECK_ORDER}')

        underneath_xy = 750, 470
        mouse_click(underneath_xy, min_num_clicks=2, max_num_clicks=3)

        if not wait_for_img(img_name=f"Reset_Trap_{trap_num}_Caught", script_name=SCRIPT_NAME, should_click=True, threshold=0.75, max_wait_sec=3, img_sel="first"):
            if AT_TRAP == 3:
                wait_for_img(img_name=f"Reset_Trap_{trap_num}_Down", script_name="Desert_Lizards", threshold=0.7,
                             should_click=True)

    API.AntiBan.sleep_between(2.1, 2.2)
    return


# -------
# HELPERS
# -------
def intl_interface_setup():
    setup_interface("west", 3, "up")
    is_tab_open('inventory', False)
    is_otd_enabled(should_enable=True)
    return