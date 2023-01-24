import API.AntiBan
from API.Mouse import mouse_click, mouse_move
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist_in_thresh, does_color_exist_in_sub_image

SCRIPT_NAME = 'Black_Lizards'

AT_TRAP = None

NUM_TRAPS = 5

TRAP_CHECK_ORDER = []

TRAP_TO_FIX = None
TRAP_FIX_REASON = None  #Caught / Down


class SpotCoords:
    def __init__(self, t1_ss_xy, t2_ss_xy, t3_ss_xy, t4_ss_xy, t5_ss_xy,
                 t1_claim_xy, t2_claim_xy, t3_claim_xy, t4_claim_xy, t5_claim_xy,
                 t1_pickup_xy, t2_pickup_xy, t3_pickup_xy, t4_pickup_xy, t5_pickup_xy,
                 t1_reset_caught_xy, t2_reset_caught_xy, t3_reset_caught_xy, t4_reset_caught_xy, t5_reset_caught_xy,
                 t1_reset_down_xy, t2_reset_down_xy, t3_reset_down_xy, t4_reset_down_xy, t5_reset_down_xy):

        self.t1_ss_xy = t1_ss_xy
        self.t2_ss_xy = t2_ss_xy
        self.t3_ss_xy = t3_ss_xy
        self.t4_ss_xy = t4_ss_xy
        self.t5_ss_xy = t5_ss_xy

        self.t1_claim_xy = t1_claim_xy
        self.t2_claim_xy = t2_claim_xy
        self.t3_claim_xy = t3_claim_xy
        self.t4_claim_xy = t4_claim_xy
        self.t5_claim_xy = t5_claim_xy

        self.t1_pickup_xy = t1_pickup_xy
        self.t2_pickup_xy = t2_pickup_xy
        self.t3_pickup_xy = t3_pickup_xy
        self.t4_pickup_xy = t4_pickup_xy
        self.t5_pickup_xy = t5_pickup_xy

        self.t1_reset_caught_xy = t1_reset_caught_xy
        self.t2_reset_caught_xy = t2_reset_caught_xy
        self.t3_reset_caught_xy = t3_reset_caught_xy
        self.t4_reset_caught_xy = t4_reset_caught_xy
        self.t5_reset_caught_xy = t5_reset_caught_xy

        self.t1_reset_down_xy = t1_reset_down_xy
        self.t2_reset_down_xy = t2_reset_down_xy
        self.t3_reset_down_xy = t3_reset_down_xy
        self.t4_reset_down_xy = t4_reset_down_xy
        self.t5_reset_down_xy = t5_reset_down_xy



# From Trap 1
s1f1_region_xys = 723, 360, 767, 415
s2f1_region_xys = 513, 366, 568, 416
s3f1_region_xys = 341, 438, 415, 525
s4f1_region_xys = 586, 593, 634, 703
s5f1_region_xys = 870, 500, 920, 633
# Claim caught lizard
s1f2_claim_xy = 756, 316
s2f1_claim_xy = 540, 324
s3f1_claim_xy = 328, 452
s4f1_claim_xy = 605, 675
s5f1_claim_xy = 901, 578
# Pickup Rope (second click is always directly under)
s1f1_pickup_xy = 740, 404
s2f1_pickup_xy = 527, 403
s3f1_pickup_xy = 402, 483
s4f1_pickup_xy = 612, 624
s5f1_pickup_xy = 904, 525
# Reset xys relative (Caught)
s1f1_reset_caught_xy = 753, 294
s2f1_reset_caught_xy = 650, 352
s3f1_reset_caught_xy = 579, 442
s4f1_reset_caught_xy = 661, 512
s5f1_reset_caught_xy = 841, 515
# Reset xys relative (Down)
s1f2_reset_down_xy = 737, 354
s2f2_reset_down_xy = 737, 358
s3f2_reset_down_xy = 657, 447
s4f2_reset_down_xy = 742, 516
s5f2_reset_down_xy = 761, 512

spot_1_coords = SpotCoords(s1f1_region_xys, s2f1_region_xys, s3f1_region_xys, s4f1_region_xys, s5f1_region_xys,
                           s1f2_claim_xy, s2f1_claim_xy, s3f1_claim_xy, s4f1_claim_xy, s5f1_claim_xy,
                           s1f1_pickup_xy, s2f1_pickup_xy, s3f1_pickup_xy, s4f1_pickup_xy, s5f1_pickup_xy,
                           s1f1_reset_caught_xy, s2f1_reset_caught_xy, s3f1_reset_caught_xy, s4f1_reset_caught_xy, s5f1_reset_caught_xy,
                           s1f2_reset_down_xy, s2f2_reset_down_xy, s3f2_reset_down_xy, s4f2_reset_down_xy, s5f2_reset_down_xy)

# From Trap 2
s1f2_region_xys = 931, 363, 980, 407
s2f2_region_xys = 715, 358, 770, 416
s3f2_region_xys = 557, 435, 630, 519
s4f2_region_xys = 796, 588, 839, 706
s5f2_region_xys = 1100, 495, 1146, 617
# Claim caught lizard
s1f2_claim_xy = 961, 306
s2f2_claim_xy = 740, 321
s3f2_claim_xy = 546, 451
s4f2_claim_xy = 817, 669
s5f2_claim_xy = 1142, 570
# Pickup Rope (second click is always directly under)
s1f2_pickup_xy = 956, 391
s2f2_pickup_xy = 741, 404
s3f2_pickup_xy = 611, 483
s4f2_pickup_xy = 814, 623
s5f2_pickup_xy = 1116, 535
# Reset xys relative (Caught)
s1f2_reset_caught_xy = 831, 342
s2f2_reset_caught_xy = 738, 296
s3f2_reset_caught_xy = 581, 451
s4f2_reset_caught_xy = 761, 595
s5f2_reset_caught_xy = 841, 513
# Reset xys relative (Down)
s1f2_reset_down_xy = 754, 355
s2f2_reset_down_xy = 737, 358
s3f2_reset_down_xy = 656, 448
s4f2_reset_down_xy = 760, 516
s5f2_reset_down_xy = 761, 519

spot_2_coords = SpotCoords(s1f2_region_xys, s2f2_region_xys, s3f2_region_xys, s4f2_region_xys, s5f2_region_xys,
                           s1f2_claim_xy, s2f2_claim_xy, s3f2_claim_xy, s4f2_claim_xy, s5f2_claim_xy,
                           s1f2_pickup_xy, s2f2_pickup_xy, s3f2_pickup_xy, s4f2_pickup_xy, s5f2_pickup_xy,
                           s1f2_reset_caught_xy, s2f2_reset_caught_xy, s3f2_reset_caught_xy, s4f2_reset_caught_xy, s5f2_reset_caught_xy,
                           s1f2_reset_down_xy, s2f2_reset_down_xy, s3f2_reset_down_xy, s4f2_reset_down_xy, s5f2_reset_down_xy)

# From Trap 3
s1f3_region_xys = 1080, 396, 1150, 453
s2f3_region_xys = 864, 401, 914, 463
s3f3_region_xys = 672, 486, 770, 565
s4f3_region_xys = 950, 640, 997, 759
s5f3_region_xys = 1250, 546, 1330, 670
# Claim caught lizard
s1f3_claim_xy = 1116, 348
s2f3_claim_xy = 888, 362
s3f3_claim_xy = 661, 501
s4f3_claim_xy = 983, 725
s5f3_claim_xy = 1328, 629
# Pickup Rope (second click is always directly under)
s1f3_pickup_xy = 1113, 438
s2f3_pickup_xy = 889, 439
s3f3_pickup_xy = 740, 531
s4f3_pickup_xy = 969, 678
s5f3_pickup_xy = 1279, 590
# Reset xys relative (Caught)
s1f3_reset_caught_xy = 831, 343
s2f3_reset_caught_xy = 829, 349
s3f3_reset_caught_xy = 677, 500
s4f3_reset_caught_xy = 840, 511
s5f3_reset_caught_xy = 841, 512
# Reset xys relative (Down)
s1f3_reset_down_xy = 756, 355
s2f3_reset_down_xy = 753, 354
s3f3_reset_down_xy = 658, 450
s4f3_reset_down_xy = 760, 517
s5f3_reset_down_xy = 760, 519

spot_3_coords = SpotCoords(s1f3_region_xys, s2f3_region_xys, s3f3_region_xys, s4f3_region_xys, s5f3_region_xys,
                           s1f3_claim_xy, s2f3_claim_xy, s3f3_claim_xy, s4f3_claim_xy, s5f3_claim_xy,
                           s1f3_pickup_xy, s2f3_pickup_xy, s3f3_pickup_xy, s4f3_pickup_xy, s5f3_pickup_xy,
                           s1f3_reset_caught_xy, s2f3_reset_caught_xy, s3f3_reset_caught_xy, s4f3_reset_caught_xy,
                           s5f3_reset_caught_xy, s1f3_reset_down_xy, s2f3_reset_down_xy, s3f3_reset_down_xy, s4f3_reset_down_xy, s5f3_reset_down_xy)

# From Trap 4
s1f4_region_xys = 864, 248, 907, 315
s2f4_region_xys = 662, 260, 711, 322
s3f4_region_xys = 480, 340, 565, 423
s4f4_region_xys = 733, 488, 790, 610
s5f4_region_xys = 1018, 397, 1120, 520
# Claim caught lizard
s1f4_claim_xy = 885, 210
s2f4_claim_xy = 683, 219
s3f4_claim_xy = 472, 354
s4f4_claim_xy = 760, 558
s5f4_claim_xy = 1066, 466
# Pickup Rope (second click is always directly under)
s1f4_pickup_xy = 885, 302
s2f4_pickup_xy = 688, 306
s3f4_pickup_xy = 542, 386
s4f4_pickup_xy = 758, 527
s5f4_pickup_xy = 1045, 439
# Reset xys relative (Caught)
s1f4_reset_caught_xy = 828, 349
s2f4_reset_caught_xy = 736, 280
s3f4_reset_caught_xy = 582, 430
s4f4_reset_caught_xy = 759, 576
s5f4_reset_caught_xy = 840, 498
# Reset xys relative (Down)
s1f4_reset_down_xy = 757, 355
s2f4_reset_down_xy = 736, 359
s3f4_reset_down_xy = 658, 430
s4f4_reset_down_xy = 760, 576
s5f4_reset_down_xy = 759, 500
spot_4_coords = SpotCoords(s1f4_region_xys, s2f4_region_xys, s3f4_region_xys, s4f4_region_xys, s5f4_region_xys,
                           s1f4_claim_xy, s2f4_claim_xy, s3f4_claim_xy, s4f4_claim_xy, s5f4_claim_xy,
                           s1f4_pickup_xy, s2f4_pickup_xy, s3f4_pickup_xy, s4f4_pickup_xy, s5f4_pickup_xy,
                           s1f4_reset_caught_xy, s2f4_reset_caught_xy, s3f4_reset_caught_xy, s4f4_reset_caught_xy, s5f4_reset_caught_xy,
                           s1f4_reset_down_xy, s2f4_reset_down_xy, s3f4_reset_down_xy, s4f4_reset_down_xy, s5f4_reset_down_xy)

# From Trap 5
s1f5_region_xys = 590, 353, 646, 413
s2f5_region_xys = 377, 362, 443, 420
s3f5_region_xys = 230, 427, 267, 521
s4f5_region_xys = 441, 582, 496, 702
s5f5_region_xys = 733, 495, 790, 610
# Claim caught lizard
s1f5_claim_xy = 612, 310
s2f5_claim_xy = 401, 322
s3f5_claim_xy = 186, 450
s4f5_claim_xy = 448, 663
s5f5_claim_xy = 760, 568
# Pickup Rope (second click is always directly under)
s1f5_pickup_xy = 615, 396
s2f5_pickup_xy = 412, 398
s3f5_pickup_xy = 271, 478
s4f5_pickup_xy = 472, 547
s5f5_pickup_xy = 757, 533
# Reset xys relative (Caught)
s1f5_reset_caught_xy = 663, 366
s2f5_reset_caught_xy = 661, 352
s4f5_reset_caught_xy = 663, 516
s3f5_reset_caught_xy = 580, 425
s5f5_reset_caught_xy = 761, 584
# Reset xys relative (Down)
s1f5_reset_down_xy = 734, 356
s2f5_reset_down_xy = 736, 353
s3f5_reset_down_xy = 658, 432
s4f5_reset_down_xy = 741, 515
s5f5_reset_down_xy = 761, 519
spot_5_coords = SpotCoords(s1f5_region_xys, s2f5_region_xys, s3f5_region_xys, s4f5_region_xys, s5f5_region_xys,
                           s1f5_claim_xy, s2f5_claim_xy, s3f5_claim_xy, s4f5_claim_xy, s5f5_claim_xy,
                           s1f5_pickup_xy, s2f5_pickup_xy, s3f5_pickup_xy, s4f5_pickup_xy, s5f5_pickup_xy,
                           s1f5_reset_caught_xy, s2f5_reset_caught_xy, s3f5_reset_caught_xy, s4f5_reset_caught_xy, s5f5_reset_caught_xy,
                           s1f5_reset_down_xy, s2f5_reset_down_xy, s3f5_reset_down_xy, s4f5_reset_down_xy, s5f5_reset_down_xy)

# MANUAL SET TRAP COORDS
set_trap_0_xy = 660, 446
set_trap_1_xy = 517, 303
set_trap_2_xy = 504, 447
set_trap_3_xy = 990, 747
set_trap_4_xy = 1087, 484

set_trap_xys = [set_trap_0_xy, set_trap_1_xy, set_trap_2_xy, set_trap_3_xy, set_trap_4_xy]


def start_catching_black_lizards(curr_loop):
    global TRAP_TO_FIX

    if curr_loop != 1:
        print(f'Not first loop')
        attempts = 0
        while attempts < 20:
            if not check_traps_from(get_at_trap()):
                return False
            attempts += 1

        return True

    else:
        print(f'This is the first loop')
        setup_interface('west', 3, 'up')
        drop_existing_lizards()
        set_initial_traps()
        is_tab_open('inventory', False)
    return True


def drop_existing_lizards():
    is_tab_open('inventory', True)
    should_drop = True
    while should_drop:
        should_drop = does_img_exist(img_name="Black_Lizard", script_name="Black_Lizards", threshold=0.9, should_click=True, click_middle=True)
    is_tab_open('inventory', False)
    return


def set_initial_traps():
    traps = ["Set_Trap_0", "Set_Trap_1", "Set_Trap_2", "Set_Trap_3", "Set_Trap_4"]
    curr_trap_num = 0
    for trap in traps:
        is_otd_enabled(should_enable=True)
        does_img_exist(img_name=trap, script_name="Black_Lizards", threshold=0.8, should_click=True, click_middle=True)
        match curr_trap_num:
            case 0:
                print(f'First Trap')
                API.AntiBan.sleep_between(4.2, 4.3)
            case 1:
                print(f'First Trap')
                API.AntiBan.sleep_between(5.3, 5.4)
            case 2:
                print(f'First Trap')
                API.AntiBan.sleep_between(5.1, 5.2)
            case 3:
                print(f'First Trap')
                API.AntiBan.sleep_between(5.0, 5.1)
            case 4:
                print(f'First Trap')
                API.AntiBan.sleep_between(5.1, 5.2)
        update_curr_trap_data(curr_trap_num)
        curr_trap_num += 1

    return True


def set_initial_traps_manually():
    i = 0
    for xy in set_trap_xys:
        mouse_click(xy)
        API.AntiBan.sleep_between(4.125, 4.25)
        if i == 1:
            API.AntiBan.sleep_between(1.0, 1.1)
        i += 1
    API.AntiBan.sleep_between(1.0, 1.1)
    return


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
        case 3:
            curr_check_coords = spot_4_coords
        case 4:
            curr_check_coords = spot_5_coords

    color_green = 29, 163, 51
    color_yellow = 160, 132, 8
    color_tolerance = 15

    curr_check_trap_region_xys = [curr_check_coords.t1_ss_xy, curr_check_coords.t2_ss_xy, curr_check_coords.t3_ss_xy, curr_check_coords.t4_ss_xy, curr_check_coords.t5_ss_xy]

    curr_trap_claim_coords = [curr_check_coords.t1_claim_xy, curr_check_coords.t2_claim_xy, curr_check_coords.t3_claim_xy, curr_check_coords.t4_claim_xy, curr_check_coords.t5_claim_xy]
    curr_trap_pickup_coords = [curr_check_coords.t1_pickup_xy, curr_check_coords.t2_pickup_xy, curr_check_coords.t3_pickup_xy, curr_check_coords.t4_pickup_xy, curr_check_coords.t5_pickup_xy]
    curr_trap_reset_caught_coord = [curr_check_coords.t1_reset_caught_xy, curr_check_coords.t2_reset_caught_xy, curr_check_coords.t3_reset_caught_xy, curr_check_coords.t4_reset_caught_xy, curr_check_coords.t5_reset_caught_xy]
    curr_trap_reset_down_coord = [curr_check_coords.t1_reset_down_xy, curr_check_coords.t2_reset_down_xy, curr_check_coords.t3_reset_down_xy, curr_check_coords.t4_reset_down_xy, curr_check_coords.t5_reset_down_xy]

    for i in TRAP_CHECK_ORDER:
        print(f'--- Checking Trap {i} From {curr_at_trap_num} ----\nTrap_Check_Order = {TRAP_CHECK_ORDER}')

        if does_color_exist_in_sub_image(curr_check_trap_region_xys[i], color_yellow, 'Yellow_Check', color_tolerance=color_tolerance):
            print(f'🟡 Found for spot {i} from trap {curr_at_trap_num}')

        elif does_color_exist_in_sub_image(curr_check_trap_region_xys[i], color_green, 'Green_Check'):
            print(f'🟢 Found for spot {i} from trap {curr_at_trap_num}')
            mouse_click(curr_trap_claim_coords[i])

            is_tab_open('inventory', True)
            print(f'✔ Claimed Caught Lizard - Time to reset trap {i} @ {curr_trap_reset_caught_coord[i]}')
            if not drop_lizard():
                print(f'Failed to find lizard to drop')
                return False
            is_tab_open('inventory', False)
            mouse_click(curr_trap_reset_caught_coord[i])
            update_curr_trap_data(i)
            API.AntiBan.sleep_between(4.5, 4.6)
            return True
        else:
            print(f'🔴 Neither color found for spot {i} - Searching for Green again then Clicking Net to pick up if not found again')
            if wait_for_img(img_name=f"trap_down_{i}_from_{curr_at_trap_num}", script_name="Black_Lizards", threshold=0.92, should_click=True, click_middle=True, max_wait_sec=2):
                API.AntiBan.sleep_between(2.8, 2.9)
                second_pickup_xy = 744, 457
                if i == 4 and curr_at_trap_num == 2:
                    API.AntiBan.sleep_between(0.6, 0.7)
                    second_pickup_xy = 752, 466
                if i == 2 and curr_at_trap_num == 4:
                    API.AntiBan.sleep_between(0.6, 0.7)
                    second_pickup_xy = 752, 466

                mouse_click(second_pickup_xy, min_num_clicks=2, max_num_clicks=3)
                API.AntiBan.sleep_between(0.2, 0.3)
                print(f'✔ Picked up rope and net from ground - Time to reset trap {i} @ {curr_trap_reset_down_coord[i]}')
                mouse_click(curr_trap_reset_down_coord[i])
                update_curr_trap_data(i)
            elif does_color_exist_in_sub_image(curr_check_trap_region_xys[i], color_green, 'Trap_Color_Sec_Check'):
                print(f'🔴🟢 Found green on the second pass - Clicking to Claim trap {i} @ {curr_trap_claim_coords[i]}')
                mouse_click(curr_trap_claim_coords[i])

                is_tab_open('inventory', True)
                print(f'✔ Claimed Caught Lizard - Time to reset trap {i} @ {curr_trap_reset_caught_coord[i]}')
                if not drop_lizard():
                    print(f'Failed to find lizard to drop')
                    return False
                is_tab_open('inventory', False)
                mouse_click(curr_trap_reset_caught_coord[i])
                update_curr_trap_data(i)
            else:
                print(f'🥅 must be on the ground and couldnt find image - Clicking to Pickup Rope (then net) for trap {i} @ {curr_trap_pickup_coords[i]}')
                mouse_click(curr_trap_pickup_coords[i])
                API.AntiBan.sleep_between(3.4, 3.5)
                second_pickup_xy = 744, 457
                mouse_click(second_pickup_xy, min_num_clicks=2, max_num_clicks=3)
                print(f'✔ Picked up rope and net from ground - Time to reset trap {i} @ {curr_trap_reset_down_coord[i]}')
                mouse_click(curr_trap_reset_down_coord[i])
                update_curr_trap_data(i)
            API.AntiBan.sleep_between(5.0, 5.1)
            return True


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
    if wait_for_img(img_name="Black_Lizard", script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True):
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



