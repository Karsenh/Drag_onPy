from API.Mouse import mouse_click
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist_in_thresh

SCRIPT_NAME = 'Red_Lizards_v2'

AT_TRAP = None

NUM_TRAPS = 3

TRAP_CHECK_ORDER = []

# Spot 1          Spot 2          Spot 3
spot_1_from_1 = 123, 123
spot_2_from_1 = 123, 123
spot_3_from_1 = 123, 123
col_check_xys_from_1 = [spot_1_from_1, spot_2_from_1, spot_3_from_1]

spot_1_from_2 = 123, 123
spot_2_from_2 = 123, 123
spot_3_from_2 = 123, 123
col_check_xys_from_2 = [spot_1_from_2, spot_2_from_2, spot_3_from_2]

spot_1_from_3 = 1075, 480
spot_2_from_3 = 968, 352
spot_3_from_3 = 820, 548
col_check_xys_from_3 = [spot_1_from_3, spot_2_from_3, spot_3_from_3]

TRAP_COL_CHECK_XY = []


def start_catching_red_lizards(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        if trap_requires_action(get_at_trap()):
            fix_trap()

    else:
        print(f'This is the first loop')
        setup_interface('north', 3, 'up')
        set_initial_traps()
    return True


def set_initial_traps():

    for curr_trap_num in range(1, NUM_TRAPS + 1):
        if not wait_for_img(img_name=f"Set_Trap_{curr_trap_num}", script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True, max_wait_sec=8):
            print(f'Failed to find Set_Trap_{curr_trap_num} - Exiting.')
            return False
        else:
            update_curr_trap_data(curr_trap_num)
    return True


def update_curr_trap_data(curr_trap_num):
    # Remove curr_trap_num from arr and place at end to check last
    update_trap_check(curr_trap_num)
    # Set current trap to curr_trap_num
    set_at_trap(curr_trap_num)
    return


def set_at_trap(new_val):
    global AT_TRAP
    AT_TRAP = new_val
    return


def get_at_trap():
    return AT_TRAP


def trap_requires_action(curr_trap):
    match curr_trap:
        case 1:
            curr_color_check_xys = col_check_xys_from_1
        case 2:
            curr_color_check_xys = col_check_xys_from_2
        case 3:
            curr_color_check_xys = col_check_xys_from_3

    green_color = 123, 123, 123
    red_color = 321, 321, 321
    check_threshold = 20

    curr_check_trap_idx = 0

    # For each pair of coordinates in curr_color_check_xys...
    for xy_coords in curr_color_check_xys:
        # Check if curr coords has trap caught color
        if does_color_exist_in_thresh(xy_coords, green_color, check_threshold):
            print(f'🟢Caught trap no. {curr_check_trap_idx+1} which is index {curr_check_trap_idx}')
            return True

        elif does_color_exist_in_thresh(xy_coords, red_color, check_threshold):
            print(f'🔴Trap no. {curr_check_trap_idx+1} reset. Idx {curr_check_trap_idx}')
            return True

        elif does_img_exist(img_name=f"Trap_{curr_check_trap_idx+1}_Down_From_{get_at_trap()}", script_name=SCRIPT_NAME, threshold=0.9, should_click=True, click_middle=True):
            print(f'🔴Trap no. {curr_check_trap_idx+1} with idx {curr_check_trap_idx} has fallen and needs pickup/reset.')
            return True

        else:
            print(f'🟡Trap no. {curr_check_trap_idx+1} is still live')
            return True

    return False


def update_trap_check(curr_trap_num):
    global TRAP_CHECK_ORDER
    last_idx = NUM_TRAPS - 1
    print(f'Removing Trap no. {curr_trap_num} from TRAP_CHECK_ORDER if found and placing at end of array to check last.')
    TRAP_CHECK_ORDER.remove(curr_trap_num)
    TRAP_CHECK_ORDER.insert(last_idx, curr_trap_num)
    print(f'TRAP_CHECK_ORDER now: {TRAP_CHECK_ORDER}')
    return


def drop_lizard():
    is_otd_enabled(should_enable=True)
    is_tab_open("inventory", True)
    if does_img_exist(img_name="Red_Lizard", script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
        print(f'Dropping found lizard')
    else:
        print(f'No lizard to drop!')
    return
