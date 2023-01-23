import API.AntiBan
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

TRAP_TO_FIX = None
TRAP_FIX_REASON = None  #Caught / Down


class SpotCoords:
    def __init__(self, t1_yellow_xy, t2_yellow_xy, t3_yellow_xy,
                 t1_green_xy, t2_green_xy, t3_green_xy,
                 t1_claim_xy, t2_claim_xy, t3_claim_xy,
                 t1_pickup_xy, t2_pickup_xy, t3_pickup_xy,
                 t1_reset_caught_xy, t2_reset_caught_xy, t3_reset_caught_xy,
                 t1_reset_down_xy, t2_reset_down_xy, t3_reset_down_xy):

        self.t1_yellow_xy = t1_yellow_xy
        self.t2_yellow_xy = t2_yellow_xy
        self.t3_yellow_xy = t3_yellow_xy

        self.t1_green_xy = t1_green_xy
        self.t2_green_xy = t2_green_xy
        self.t3_green_xy = t3_green_xy

        self.t1_claim_xy = t1_claim_xy
        self.t2_claim_xy = t2_claim_xy
        self.t3_claim_xy = t3_claim_xy

        self.t1_pickup_xy = t1_pickup_xy
        self.t2_pickup_xy = t2_pickup_xy
        self.t3_pickup_xy = t3_pickup_xy

        self.t1_reset_caught_xy = t1_reset_caught_xy
        self.t2_reset_caught_xy = t2_reset_caught_xy
        self.t3_reset_caught_xy = t3_reset_caught_xy

        self.t1_reset_down_xy = t1_reset_down_xy
        self.t2_reset_down_xy = t2_reset_down_xy
        self.t3_reset_down_xy = t3_reset_down_xy


# From Trap 1
# Yellow
s1f1_yellow = 822, 420
s2f1_yellow = 750, 285
s3f1_yellow = 613, 402
# Green
s1f1_green = 860, 466
s2f1_green = 750, 304
s3f1_green = 610, 472
# Claim caught lizard
s1f1_claim_xy = 885, 425
s2f1_claim_xy = 742, 232
s3f1_claim_xy = 595, 455
# Pickup Rope (second click is always directly under)
s1f1_pickup_xy = 813, 457
s2f1_pickup_xy = 741, 321
s3f1_pickup_xy = 607, 431
# Reset xys relative (Caught)
s1f1_reset_caught_xy = 905, 414
s2f1_reset_caught_xy = 738, 279
s3f1_reset_caught_xy = 663, 440
# Reset xys relative (Caught)
s1f1_reset_down_xy = 840, 435
s2f1_reset_down_xy = 738, 348
s3f1_reset_down_xy = 742, 500

spot_1_coords = SpotCoords(s1f1_yellow, s2f1_yellow, s3f1_yellow,
                           s1f1_green, s2f1_green, s3f1_green,
                           s1f1_claim_xy, s2f1_claim_xy, s3f1_claim_xy,
                           s1f1_pickup_xy, s2f1_pickup_xy, s3f1_pickup_xy,
                           s1f1_reset_caught_xy, s2f1_reset_caught_xy, s3f1_reset_caught_xy,
                           s1f1_reset_down_xy, s2f1_reset_down_xy, s3f1_reset_down_xy)

# From Trap 2
# Yellow
s1f2_yellow = 906, 550
s2f2_yellow = 824, 402
s3f2_yellow = 679, 520
# Green
s1f2_green = 944, 592
s2f2_green = 819, 414
s3f2_green = 676, 588
# Claim caught lizard
s1f2_claim_xy = 970, 561
s2f2_claim_xy = 820, 355
s3f2_claim_xy = 664, 567
# Pickup Rope (second click is always directly under)
s1f2_pickup_xy = 900, 580
s2f2_pickup_xy = 815, 442
s3f2_pickup_xy = 668, 549
# Reset xys relative Caught
s1f2_reset_caught_xy = 922, 416
s2f2_reset_caught_xy = 817, 328
s3f2_reset_caught_xy = 743, 570
# Reset Down
s1f2_reset_down_xy = 838, 435
s2f2_reset_down_xy = 755, 350
s3f2_reset_down_xy = 742, 512
spot_2_coords = SpotCoords(s1f2_yellow, s2f2_yellow, s3f2_yellow,
                           s1f2_green, s2f2_green, s3f2_green,
                           s1f2_claim_xy, s2f2_claim_xy, s3f2_claim_xy,
                           s1f2_pickup_xy, s2f2_pickup_xy, s3f2_pickup_xy,
                           s1f2_reset_caught_xy, s2f2_reset_caught_xy, s3f2_reset_caught_xy,
                           s1f2_reset_down_xy, s2f2_reset_down_xy, s3f2_reset_down_xy)

# From Trap 3
# Yellow
s1f3_yellow = 1074, 478
s2f3_yellow = 981, 334
s3f3_yellow = 820, 453
# Green
s1f3_green = 1100, 520
s2f3_green = 971, 351
s3f3_green = 817, 530
# Claim caught lizard
s1f3_claim_xy = 1140, 483
s2f3_claim_xy = 975, 284
s3f3_claim_xy = 815, 516
# Pickup Rope (second click is always directly under)
s1f3_pickup_xy = 1060, 514
s2f3_pickup_xy = 968, 370
s3f3_pickup_xy = 815, 470
# Reset xys relative
s1f3_reset_caught_xy = 923, 416
s2f3_reset_caught_xy = 835, 320
s3f3_reset_caught_xy = 820, 524
# Reset Down
s1f3_reset_down_xy = 838, 436
s2f3_reset_down_xy = 754, 354
s3f3_reset_down_xy = 761, 517
spot_3_coords = SpotCoords(s1f3_yellow, s2f3_yellow, s3f3_yellow,
                           s1f3_green, s2f3_green, s3f3_green,
                           s1f3_claim_xy, s2f3_claim_xy, s3f3_claim_xy,
                           s1f3_pickup_xy, s2f3_pickup_xy, s3f3_pickup_xy,
                           s1f3_reset_caught_xy, s2f3_reset_caught_xy, s3f3_reset_caught_xy,
                           s1f3_reset_down_xy, s2f3_reset_down_xy, s3f3_reset_down_xy)


def start_catching_red_lizards(curr_loop):
    global TRAP_TO_FIX

    if curr_loop != 1:
        print(f'Not first loop')
        attempts = 0
        while attempts < 20:
            check_traps_from(get_at_trap())
            attempts += 1

        return True

    else:
        print(f'This is the first loop')
        # setup_interface('north', 3, 'up')
        if not set_initial_traps():
            return False
        is_tab_open('inventory', False)
    return True


def set_initial_traps():
    for curr_trap_num in range(0, NUM_TRAPS):
        if not wait_for_img(img_name=f"Set_Trap_{curr_trap_num}", script_name=SCRIPT_NAME, threshold=0.8, should_click=True, click_middle=True, max_wait_sec=8):
            print(f'Failed to find Set_Trap_{curr_trap_num} - Exiting.')
            return False
        else:
            update_curr_trap_data(curr_trap_num)
            API.AntiBan.sleep_between(3.5, 3.6)
            if curr_trap_num == 1:
                API.AntiBan.sleep_between(1.0, 1.1)
    API.AntiBan.sleep_between(1.0, 1.1)
    return True


def update_curr_trap_data(curr_trap_num):
    print(f'Updating curr trap data with trap num: {curr_trap_num}')
    # Remove curr_trap_num from arr and place at end to check last
    update_trap_check_order(curr_trap_num)
    # Set current trap to curr_trap_num
    set_at_trap(curr_trap_num)
    return


def check_traps_from(curr_at_trap_num):
    global TRAP_TO_FIX
    global TRAP_FIX_REASON

    match curr_at_trap_num:
        case 0:
            curr_check_coords = spot_1_coords
        case 1:
            curr_check_coords = spot_2_coords
        case 2:
            curr_check_coords = spot_3_coords

    color_green = 42, 171, 50
    color_yellow = 183, 150, 14
    check_threshold = 15

    curr_check_trap_yellow_coords = [curr_check_coords.t1_yellow_xy, curr_check_coords.t2_yellow_xy, curr_check_coords.t3_yellow_xy]
    curr_check_trap_green_coords = [curr_check_coords.t1_green_xy, curr_check_coords.t2_green_xy, curr_check_coords.t3_green_xy]

    curr_trap_claim_coords = [curr_check_coords.t1_claim_xy, curr_check_coords.t2_claim_xy, curr_check_coords.t3_claim_xy]
    curr_trap_pickup_coords = [curr_check_coords.t1_pickup_xy, curr_check_coords.t2_pickup_xy, curr_check_coords.t3_pickup_xy]
    curr_trap_reset_caught_coord = [curr_check_coords.t1_reset_caught_xy, curr_check_coords.t2_reset_caught_xy, curr_check_coords.t3_reset_caught_xy]
    curr_trap_reset_down_coord = [curr_check_coords.t1_reset_down_xy, curr_check_coords.t2_reset_down_xy, curr_check_coords.t3_reset_down_xy]

    for i in TRAP_CHECK_ORDER:
        print(f'--- Checking Trap {i} From {curr_at_trap_num} ----\nTrap_Check_Order = {TRAP_CHECK_ORDER}')
        if does_color_exist_in_thresh(curr_check_trap_yellow_coords[i], color_yellow, check_threshold):
            print(f'🟡 Found for spot {i} from trap {curr_at_trap_num}')
        elif does_color_exist_in_thresh(curr_check_trap_green_coords[i], color_green, check_threshold):
            print(f'🟢 Found for spot {i} from trap {curr_at_trap_num}')
            mouse_click(curr_trap_claim_coords[i])

            is_tab_open('inventory', True)
            wait_for_img(img_name="Hunter", category="Exp_Drops")
            print(f'✔ Claimed Caught Lizard - Time to reset trap {i} @ {curr_trap_reset_caught_coord[i]}')
            if not drop_lizard():
                print(f'Failed to find lizard to drop')
            is_tab_open('inventory', False)
            mouse_click(curr_trap_reset_caught_coord[i])
            update_curr_trap_data(i)
            API.AntiBan.sleep_between(4.5, 4.6)
            return
        else:
            print(f'🔴 Neither color found for spot {i} - are we transitioning to green or is rope on ground?')
            API.AntiBan.sleep_between(1.4, 1.5)
            if does_color_exist_in_thresh(curr_check_trap_green_coords[i], color_green, check_threshold):
                print(f'🔴🟢 Found green on the second pass - Clicking to Claim trap {i} @ {curr_trap_claim_coords[i]}')
                mouse_click(curr_trap_claim_coords[i])

                is_tab_open('inventory', True)
                wait_for_img(img_name="Hunter", category="Exp_Drops")
                print(f'✔ Claimed Caught Lizard - Time to reset trap {i} @ {curr_trap_reset_caught_coord[i]}')
                if not drop_lizard():
                    print(f'Failed to find lizard to drop')
                is_tab_open('inventory', False)
                mouse_click(curr_trap_reset_caught_coord[i])
                update_curr_trap_data(i)
            else:
                print(f'🥅 must be on the ground - Clicking to Pickup Rope (then net) for trap {i} @ {curr_trap_pickup_coords[i]}')
                mouse_click(curr_trap_pickup_coords[i])

                API.AntiBan.sleep_between(4.0, 4.1)
                second_pickup_xy = 744, 457
                mouse_click(second_pickup_xy, min_num_clicks=2, max_num_clicks=3)
                print(f'✔ Picked up rope and net from ground - Time to reset trap {i} @ {curr_trap_reset_down_coord[i]}')
                mouse_click(curr_trap_reset_down_coord[i])
                update_curr_trap_data(i)
            API.AntiBan.sleep_between(5.0, 5.1)
            return
        i += 1


def fix_trap(from_trap_num, fix_trap_num, fix_reason):
    print(f'FIXING TRAP: {fix_trap_num} FROM TRAP: {from_trap_num} BECAUSE: {fix_reason}')
    return True


# HELPERS
def update_trap_check_order(curr_trap_num):
    global TRAP_CHECK_ORDER
    last_idx = NUM_TRAPS - 1
    print(f'Removing Trap no. {curr_trap_num} from TRAP_CHECK_ORDER if found and placing at end of array to check last.')
    if curr_trap_num in TRAP_CHECK_ORDER:
        TRAP_CHECK_ORDER.remove(curr_trap_num)
    TRAP_CHECK_ORDER.insert(last_idx, curr_trap_num)
    print(f'TRAP_CHECK_ORDER now: {TRAP_CHECK_ORDER}')
    return


def drop_lizard():
    is_otd_enabled(should_enable=True)
    # is_tab_open("inventory", True)
    if wait_for_img(img_name="Red_Lizard", script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
        print(f'Dropping found lizard')
        return True
    else:
        print(f'No lizard to drop!')
        return False


def get_trap_to_fix():
    return TRAP_TO_FIX


def set_trap_to_fix(new_val):
    global TRAP_TO_FIX
    TRAP_TO_FIX = new_val
    return


def set_at_trap(new_val):
    global AT_TRAP
    AT_TRAP = new_val
    return


def get_at_trap():
    return AT_TRAP


def set_fix_reason(new_reason):
    global TRAP_FIX_REASON
    TRAP_FIX_REASON = new_reason
    return


def get_fix_reason():
    return TRAP_FIX_REASON



