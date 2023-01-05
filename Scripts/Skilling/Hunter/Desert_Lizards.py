import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled
from API.Imaging.Image import does_img_exist, wait_for_img

SCRIPT_NAME = "Desert_Lizards"

AT_TRAP = None
INTL_CHECK = True
TRAP_CHECK_ORDER = []


def start_catching_desert_lizards(curr_loop):
    global AT_TRAP

    if curr_loop != 1:
        print(f'Not first loop')

        trap_to_fix = check_traps_from(curr_trap_num=AT_TRAP)

        # if trap_to_fix:
        #     fix_trap(trap_to_fix)

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

    if wait_for_img(img_name=f"Set_intl_trap_{trap_num}", script_name=SCRIPT_NAME, should_click=True, threshold=0.95):
        AT_TRAP = trap_num
        TRAP_CHECK_ORDER.append(trap_num)
        print(f'🟢 Setting initial trap: {trap_num}\n🟢 AT_TRAP set = {AT_TRAP}\n🟢 TRAP_CHECK_ORDER = {TRAP_CHECK_ORDER}')
        API.AntiBan.sleep_between(2.0, 2.1)
    return


def check_traps_from(curr_trap_num):
    global INTL_CHECK
    global TRAP_CHECK_ORDER

    if INTL_CHECK:
        # First time checking - check in FIFO order (oldest)
        trap_check_order = TRAP_CHECK_ORDER
        INTL_CHECK = False
    else:
        # Second time checking and above - check in LIFO order (closest)
        trap_check_order = TRAP_CHECK_ORDER.reverse()

    for trap_num in trap_check_order:
        bad_trap = check_trap(curr_trap_num=trap_num)
        if bad_trap:
            return bad_trap

    return None


def fix_trap(trap_to_fix):
    # If Caught

    # If Down
    return


# -------
# HELPERS
# -------
def intl_interface_setup():
    setup_interface("west", 3, "up")
    is_tab_open('inventory', False)
    is_otd_enabled(should_enable=True)
    return


def check_trap(check_trap_num):
    global AT_TRAP

    if does_img_exist(img_name=f"Trap_{check_trap_num}_Caught_From_{AT_TRAP}"):
        print(f'🟢 TRAP {check_trap_num} 🧤 CAUGHT from {AT_TRAP}')
        return f"{check_trap_num}_Caught"
    if does_img_exist(img_name=f"Trap_{check_trap_num}_Down_From_{AT_TRAP}"):
        print(f'🟢 TRAP {check_trap_num} 🔻 DOWN from {AT_TRAP}')
        return f"{check_trap_num}_Down"

    return None
