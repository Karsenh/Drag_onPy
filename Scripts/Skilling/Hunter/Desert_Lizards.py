import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Mouse import mouse_click

SCRIPT_NAME = "Desert_Lizards"

AT_TRAP = None
INTL_CHECK = True
TRAP_CHECK_ORDER = []

CHECK_TRAP_THRESH = 0.9


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

    print(f'Iterating over check_order: {check_order.reverse()}')
    for trap_num in check_order:
        print(f'Checking trap: {trap_num}')
        bad_trap = check_trap(check_trap_num=trap_num, at_trap=curr_trap_num)
        if bad_trap:
            return bad_trap

    return None


def check_trap(check_trap_num, at_trap):
    global AT_TRAP

    if wait_for_img(img_name=f"Trap_{check_trap_num}_Caught_From_{at_trap}", script_name=SCRIPT_NAME, threshold=CHECK_TRAP_THRESH, max_wait_sec=2):
        print(f'🟢 TRAP {check_trap_num} 🧤 CAUGHT from {at_trap}')
        return f"{check_trap_num}_Caught"
    if wait_for_img(img_name=f"Trap_{check_trap_num}_Down_From_{at_trap}", script_name=SCRIPT_NAME, threshold=CHECK_TRAP_THRESH, max_wait_sec=2):
        print(f'🟢 TRAP {check_trap_num} 🔻 DOWN from {at_trap}')
        return f"{check_trap_num}_Down"

    return None


def fix_trap(trap_to_fix):
    global AT_TRAP

    print(f'⚙ trap_to_fix = {trap_to_fix}')
    trap_num = trap_to_fix.split("_")[0]
    state = trap_to_fix.split("_")[1]

    # does_img_exist(img_name=f"Trap_{trap_num}_{state}_From_{AT_TRAP}", script_name=SCRIPT_NAME, threshold=0.9, should_click=True)

    # If Down
    if state == "Down":
        print(f'STATE = 🔻{state}🔻 for TRAP {trap_num}')
    # If Caught
    else:
        print(f'STATE = 🧤{state}🧤 for TRAP {trap_num}')

        # match (trap_num):
        #     case

        mouse_click(get_existing_img_xy())
        wait_for_img(img_name="Hunter", category="Exp_Drops")

    #
    return


# -------
# HELPERS
# -------
def intl_interface_setup():
    setup_interface("west", 3, "up")
    is_tab_open('inventory', False)
    is_otd_enabled(should_enable=True)
    return