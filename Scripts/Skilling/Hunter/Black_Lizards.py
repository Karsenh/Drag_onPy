import API.AntiBan
from API.Mouse import mouse_click, mouse_move
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist_in_thresh

SCRIPT_NAME = 'Black_Lizards'

AT_TRAP = None

NUM_TRAPS = 5

TRAP_CHECK_ORDER = []

TRAP_TO_FIX = None
TRAP_FIX_REASON = None  #Caught / Down


class SpotCoords:
    def __init__(self, t1_yellow_xy, t2_yellow_xy, t3_yellow_xy, t4_yellow_xy, t5_yellow_xy,
                 t1_green_xy, t2_green_xy, t3_green_xy, t4_green_xy, t5_green_xy,
                 t1_claim_xy, t2_claim_xy, t3_claim_xy, t4_claim_xy, t5_claim_xy,
                 t1_pickup_xy, t2_pickup_xy, t3_pickup_xy, t4_pickup_xy, t5_pickup_xy,
                 t1_reset_caught_xy, t2_reset_caught_xy, t3_reset_caught_xy, t4_reset_caught_xy, t5_reset_caught_xy,
                 t1_reset_down_xy, t2_reset_down_xy, t3_reset_down_xy, t4_reset_down_xy, t5_reset_down_xy):

        self.t1_yellow_xy = t1_yellow_xy
        self.t2_yellow_xy = t2_yellow_xy
        self.t3_yellow_xy = t3_yellow_xy
        self.t4_yellow_xy = t4_yellow_xy
        self.t5_yellow_xy = t5_yellow_xy

        self.t1_green_xy = t1_green_xy
        self.t2_green_xy = t2_green_xy
        self.t3_green_xy = t3_green_xy
        self.t4_green_xy = t4_green_xy
        self.t5_green_xy = t5_green_xy

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
# Yellow
s1f1_yellow = 765, 369
s2f1_yellow = 544, 377
s3f1_yellow = 392, 449
s4f1_yellow = 617, 605
s5f1_yellow = 900, 578
# Green
s1f1_green = 760, 376
s2f1_green = 538, 390
s3f1_green = 373, 490
s4f1_green = 619, 672
s5f1_green = 894, 585
# Claim caught lizard
s1f1_claim_xy = 756, 316
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
spot_1_coords = SpotCoords(s1f1_yellow, s2f1_yellow, s3f1_yellow, s4f1_yellow, s5f1_yellow,
                           s1f1_green, s2f1_green, s3f1_green, s4f1_green, s5f1_green,
                           s1f1_claim_xy, s2f1_claim_xy, s3f1_claim_xy, s4f1_claim_xy, s5f1_claim_xy,
                           s1f1_pickup_xy, s2f1_pickup_xy, s3f1_pickup_xy, s4f1_pickup_xy, s5f1_pickup_xy,
                           s1f1_reset_caught_xy, s2f1_reset_caught_xy, s3f1_reset_caught_xy, s4f1_reset_caught_xy, s5f1_reset_caught_xy,
                           s1f2_reset_down_xy, s2f2_reset_down_xy, s3f2_reset_down_xy, s4f2_reset_down_xy, s5f2_reset_down_xy)

# From Trap 2
# Yellow
s1f2_yellow = 976, 366
s2f2_yellow = 750, 371
s3f2_yellow = 617, 446
s4f2_yellow = 823, 602
s5f2_yellow = 1141, 510
# Green
s1f2_green = 958, 371
s2f2_green = 750, 382
s3f2_green = 570, 488
s4f2_green = 819, 672
s5f2_green = 1124, 584
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
s4f2_reset_down_xy = 760, 578
s5f2_reset_down_xy = 761, 519
spot_2_coords = SpotCoords(s1f2_yellow, s2f2_yellow, s3f2_yellow, s4f2_yellow, s5f2_yellow,
                           s1f2_green, s2f2_green, s3f2_green, s4f2_green, s5f2_green,
                           s1f2_claim_xy, s2f2_claim_xy, s3f2_claim_xy, s4f2_claim_xy, s5f2_claim_xy,
                           s1f2_pickup_xy, s2f2_pickup_xy, s3f2_pickup_xy, s4f2_pickup_xy, s5f2_pickup_xy,
                           s1f2_reset_caught_xy, s2f2_reset_caught_xy, s3f2_reset_caught_xy, s4f2_reset_caught_xy, s5f2_reset_caught_xy,
                           s1f2_reset_down_xy, s2f2_reset_down_xy, s3f2_reset_down_xy, s4f2_reset_down_xy, s5f2_reset_down_xy)

# From Trap 3
# Yellow
s1f3_yellow = 1139, 421
s2f3_yellow = 901, 417
s3f3_yellow = 748, 496
s4f3_yellow = 982, 655
s5f3_yellow = 1309, 561
# Green
s1f3_green = 1114, 416
s2f3_green = 890, 422
s3f3_green = 711, 534
s4f3_green = 975, 725
s5f3_green = 1289, 636
# Claim caught lizard
s1f3_claim_xy = 1116, 348
s2f3_claim_xy = 888, 362
s3f3_claim_xy = 661, 501
s4f3_claim_xy = 983, 725
s5f3_claim_xy = 1328, 629
# Pickup Rope (second click is always directly under)
s1f3_pickup_xy = 966, 676
s2f3_pickup_xy = 889, 439
s3f3_pickup_xy = 740, 531
s4f3_pickup_xy = 969, 678
s5f3_pickup_xy = 1279, 590
# Reset xys relative (Caught)
s1f3_reset_caught_xy = 760, 594
s2f3_reset_caught_xy = 829, 349
s3f3_reset_caught_xy = 677, 500
s4f3_reset_caught_xy = 840, 511
s5f3_reset_caught_xy = 841, 512
# Reset xys relative (Down)
s1f3_reset_down_xy = 761, 518
s2f3_reset_down_xy = 753, 354
s3f3_reset_down_xy = 658, 450
s4f3_reset_down_xy = 760, 517
s5f3_reset_down_xy = 760, 519
spot_3_coords = SpotCoords(s1f3_yellow, s2f3_yellow, s3f3_yellow, s4f3_yellow, s5f3_yellow,
                           s1f3_green, s2f3_green, s3f3_green, s4f3_green, s5f3_green,
                           s1f3_claim_xy, s2f3_claim_xy, s3f3_claim_xy, s4f3_claim_xy, s5f3_claim_xy,
                           s1f3_pickup_xy, s2f3_pickup_xy, s3f3_pickup_xy, s4f3_pickup_xy, s5f3_pickup_xy,
                           s1f3_reset_caught_xy, s2f3_reset_caught_xy, s3f3_reset_caught_xy, s4f3_reset_caught_xy, s5f3_reset_caught_xy,
                           s1f3_reset_down_xy, s2f3_reset_down_xy, s3f3_reset_down_xy, s4f3_reset_down_xy, s5f3_reset_down_xy)

# From Trap 4
# Yellow
s1f4_yellow = 898, 267
s2f4_yellow = 694, 279
s3f4_yellow = 544, 351
s4f4_yellow = 765, 507
s5f4_yellow = 1058, 411
# Green
s1f4_green = 888, 283
s2f4_green = 694, 290
s3f4_green = 515, 395
s4f4_green = 748, 575
s5f4_green = 1045, 486
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
s5f4_pickup_xy = 1035, 439
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
spot_4_coords = SpotCoords(s1f4_yellow, s2f4_yellow, s3f4_yellow, s4f4_yellow, s5f4_yellow,
                           s1f4_green, s2f4_green, s3f4_green, s4f4_green, s5f4_green,
                           s1f4_claim_xy, s2f4_claim_xy, s3f4_claim_xy, s4f4_claim_xy, s5f4_claim_xy,
                           s1f4_pickup_xy, s2f4_pickup_xy, s3f4_pickup_xy, s4f4_pickup_xy, s5f4_pickup_xy,
                           s1f4_reset_caught_xy, s2f4_reset_caught_xy, s3f4_reset_caught_xy, s4f4_reset_caught_xy, s5f4_reset_caught_xy,
                           s1f4_reset_down_xy, s2f4_reset_down_xy, s3f4_reset_down_xy, s4f4_reset_down_xy, s5f4_reset_down_xy)

# From Trap 5
# Yellow
s1f5_yellow = 624, 369
s2f5_yellow = 403, 372
s3f5_yellow = 259, 444
s4f5_yellow = 469, 592
s5f5_yellow = 764, 514
# Green
s1f5_green = 627, 380
s2f5_green = 420, 384
s3f5_green = 244, 486
s4f5_green = 481, 666
s5f5_green = 766, 580
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
s4f5_reset_caught_xy = 581, 426
s3f5_reset_caught_xy = 664, 520
s5f5_reset_caught_xy = 761, 584
# Reset xys relative (Down)
s1f5_reset_down_xy = 734, 356
s2f5_reset_down_xy = 736, 353
s3f5_reset_down_xy = 658, 432
s4f5_reset_down_xy = 741, 515
s5f5_reset_down_xy = 761, 519
spot_5_coords = SpotCoords(s1f5_yellow, s2f5_yellow, s3f5_yellow, s4f5_yellow, s5f5_yellow,
                           s1f5_green, s2f5_green, s3f5_green, s4f5_green, s5f5_green,
                           s1f5_claim_xy, s2f5_claim_xy, s3f5_claim_xy, s4f5_claim_xy, s5f5_claim_xy,
                           s1f5_pickup_xy, s2f5_pickup_xy, s3f5_pickup_xy, s4f5_pickup_xy, s5f5_pickup_xy,
                           s1f5_reset_caught_xy, s2f5_reset_caught_xy, s3f5_reset_caught_xy, s4f5_reset_caught_xy, s5f5_reset_caught_xy,
                           s1f5_reset_down_xy, s2f5_reset_down_xy, s3f5_reset_down_xy, s4f5_reset_down_xy, s5f5_reset_down_xy)

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
            check_traps_from(get_at_trap())
            attempts += 1

        return True

    else:
        print(f'This is the first loop')
        # setup_interface('west', 3, 'up')
        if not set_initial_traps():
            return False
        is_tab_open('inventory', False)
    return True


def set_initial_traps():
    is_tab_open('inventory', False)
    for curr_trap_num in range(0, NUM_TRAPS):
        if not wait_for_img(img_name=f"Set_Trap_{curr_trap_num}", script_name=SCRIPT_NAME, threshold=0.8, should_click=True, click_middle=True, max_wait_sec=8):
            print(f'Failed to find Set_Trap_{curr_trap_num} - Exiting.')
            return False
        else:
            update_curr_trap_data(curr_trap_num)
            API.AntiBan.sleep_between(4.1, 4.2)
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
        case 3:
            curr_check_coords = spot_4_coords
        case 4:
            curr_check_coords = spot_5_coords

    color_green = 42, 171, 50
    color_yellow = 183, 150, 14
    check_threshold = 20

    curr_check_trap_yellow_coords = [curr_check_coords.t1_yellow_xy, curr_check_coords.t2_yellow_xy, curr_check_coords.t3_yellow_xy, curr_check_coords.t4_yellow_xy, curr_check_coords.t5_yellow_xy]
    curr_check_trap_green_coords = [curr_check_coords.t1_green_xy, curr_check_coords.t2_green_xy, curr_check_coords.t3_green_xy, curr_check_coords.t4_green_xy, curr_check_coords.t5_green_xy]

    curr_trap_claim_coords = [curr_check_coords.t1_claim_xy, curr_check_coords.t2_claim_xy, curr_check_coords.t3_claim_xy, curr_check_coords.t4_claim_xy, curr_check_coords.t5_claim_xy]
    curr_trap_pickup_coords = [curr_check_coords.t1_pickup_xy, curr_check_coords.t2_pickup_xy, curr_check_coords.t3_pickup_xy, curr_check_coords.t4_pickup_xy, curr_check_coords.t5_pickup_xy]
    curr_trap_reset_caught_coord = [curr_check_coords.t1_reset_caught_xy, curr_check_coords.t2_reset_caught_xy, curr_check_coords.t3_reset_caught_xy, curr_check_coords.t4_reset_caught_xy, curr_check_coords.t5_reset_caught_xy]
    curr_trap_reset_down_coord = [curr_check_coords.t1_reset_down_xy, curr_check_coords.t2_reset_down_xy, curr_check_coords.t3_reset_down_xy, curr_check_coords.t4_reset_down_xy, curr_check_coords.t5_reset_down_xy]

    for i in TRAP_CHECK_ORDER:
        print(f'--- Checking Trap {i} From {curr_at_trap_num} ----\nTrap_Check_Order = {TRAP_CHECK_ORDER}')
        mouse_move(curr_check_trap_yellow_coords[i])
        API.AntiBan.sleep_between(1.0, 1.1)
        mouse_move(curr_check_trap_green_coords[i])
        API.AntiBan.sleep_between(1.0, 1.1)

        if does_color_exist_in_thresh(curr_check_trap_yellow_coords[i], color_yellow, check_threshold):
            print(f'🟡 Found for spot {i} from trap {curr_at_trap_num}')

        elif does_color_exist_in_thresh(curr_check_trap_green_coords[i], color_green, check_threshold):
            print(f'🟢 Found for spot {i} from trap {curr_at_trap_num}')
            mouse_click(curr_trap_claim_coords[i])

            is_tab_open('inventory', True)
            print(f'✔ Claimed Caught Lizard - Time to reset trap {i} @ {curr_trap_reset_caught_coord[i]}')
            if not drop_lizard():
                print(f'Failed to find lizard to drop')
            is_tab_open('inventory', False)
            mouse_click(curr_trap_reset_caught_coord[i])
            update_curr_trap_data(i)
            API.AntiBan.sleep_between(4.5, 4.6)
            return
        else:
            print(f'🔴 Neither color found for spot {i} - Searching for Green again then Clicking Net to pick up if not found again')
            API.AntiBan.sleep_between(1.4, 1.5)
            if does_color_exist_in_thresh(curr_check_trap_green_coords[i], color_green, check_threshold):
                print(f'🔴🟢 Found green on the second pass - Clicking to Claim trap {i} @ {curr_trap_claim_coords[i]}')
                mouse_click(curr_trap_claim_coords[i])

                is_tab_open('inventory', True)
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



