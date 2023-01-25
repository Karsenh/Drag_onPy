import API.AntiBan
from API.Mouse import mouse_click, mouse_move, mouse_long_click
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist_in_thresh, does_color_exist_in_sub_image
import pyautogui as pag


CURR_AT_TRAP = None

TRAP_CHECK_ORDER = []

NUM_TRAPS = 5


class SpotCoords:
    def __init__(self, t1_ss_xy, t2_ss_xy, t3_ss_xy, t4_ss_xy, t5_ss_xy,
                 t1_claim_xy, t2_claim_xy, t3_claim_xy, t4_claim_xy, t5_claim_xy,
                 t1_reset_tile_xy, t2_reset_tile_xy, t3_reset_tile_xy, t4_reset_tile_xy, t5_reset_tile_xy):
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

        self.t1_reset_tile_xy = t1_reset_tile_xy
        self.t2_reset_tile_xy = t2_reset_tile_xy
        self.t3_reset_tile_xy = t3_reset_tile_xy
        self.t4_reset_tile_xy = t4_reset_tile_xy
        self.t5_reset_tile_xy = t5_reset_tile_xy


t1f1_ss_region_xy = 830, 425, 880, 520
t2f1_ss_region_xy = 622, 425, 668, 510
t3f1_ss_region_xy = 840, 663, 885, 745
t4f1_ss_region_xy = 580, 657, 635, 730
t5f1_ss_region_xy = 712, 541, 760, 625

t1f1_claim_xy = 850, 470
t2f1_claim_xy = 616, 456
t3f1_claim_xy = 860, 703
t4f1_claim_xy = 603, 677
t5f1_claim_xy = 733, 595

t1f1_tile_xy = 850, 470
t2f1_tile_xy = 616, 456
t3f1_tile_xy = 766, 603
t4f1_tile_xy = 730, 605
t5f1_tile_xy = 733, 595

spot_1_coords = SpotCoords(t1f1_ss_region_xy, t2f1_ss_region_xy, t3f1_ss_region_xy, t4f1_ss_region_xy, t5f1_ss_region_xy,
                           t1f1_claim_xy, t2f1_claim_xy, t3f1_claim_xy, t4f1_claim_xy, t5f1_claim_xy,
                           t1f1_tile_xy, t2f1_tile_xy, t3f1_tile_xy, t4f1_tile_xy, t5f1_tile_xy)


t1f2_ss_region_xy = 1072, 440, 1112, 528
t2f2_ss_region_xy = 833, 432, 880, 518
t3f2_ss_region_xy = 1086, 670, 1145, 760
t4f2_ss_region_xy = 840, 663, 885, 743
t5f2_ss_region_xy = 960, 546, 1008, 631

t1f2_claim_xy = 1094, 477
t2f2_claim_xy = 854, 460
t3f2_claim_xy = 1110, 708
t4f2_claim_xy = 861, 691
t5f2_claim_xy = 981, 577

t1f2_tile_xy = 883, 476
t2f2_tile_xy = 854, 460
t3f2_tile_xy = 884, 501
t4f2_tile_xy = 762, 600
t5f2_tile_xy = 886, 494

spot_2_coords = SpotCoords(t1f2_ss_region_xy, t2f2_ss_region_xy, t3f2_ss_region_xy, t4f2_ss_region_xy, t5f2_ss_region_xy,
                           t1f2_claim_xy, t2f2_claim_xy, t3f2_claim_xy, t4f2_claim_xy, t5f2_claim_xy,
                           t1f2_tile_xy, t2f2_tile_xy, t3f2_tile_xy, t4f2_tile_xy, t5f2_tile_xy)


t1f3_ss_region_xy = 830, 244, 875, 332
t2f3_ss_region_xy = 596, 234, 647, 320
t3f3_ss_region_xy = 834, 457, 884, 550
t4f3_ss_region_xy = 590, 443, 645, 537
t5f3_ss_region_xy = 717, 341, 762, 423

t1f3_claim_xy = 852, 271
t2f3_claim_xy = 619, 269
t3f3_claim_xy = 858, 490
t4f3_claim_xy = 618, 487
t5f3_claim_xy = 730, 395

t1f3_tile_xy = 762, 353
t2f3_tile_xy = 733, 364
t3f3_tile_xy = 858, 490
t4f3_tile_xy = 618, 487
t5f3_tile_xy = 730, 395

spot_3_coords = SpotCoords(t1f3_ss_region_xy, t2f3_ss_region_xy, t3f3_ss_region_xy, t4f3_ss_region_xy, t5f3_ss_region_xy,
                           t1f3_claim_xy, t2f3_claim_xy, t3f3_claim_xy, t4f3_claim_xy, t5f3_claim_xy,
                           t1f3_tile_xy, t2f3_tile_xy, t3f3_tile_xy, t4f3_tile_xy, t5f3_tile_xy)


t1f4_ss_region_xy = 1060, 264, 1100, 353
t2f4_ss_region_xy = 830, 255, 875, 347
t3f4_ss_region_xy = 1070, 468, 1114, 564
t4f4_ss_region_xy = 826, 458, 888, 555
t5f4_ss_region_xy = 945, 358, 994, 457

t1f4_claim_xy = 1080, 297
t2f4_claim_xy = 852, 285
t3f4_claim_xy = 1096, 503
t4f4_claim_xy = 854, 489
t5f4_claim_xy = 973, 389

t1f4_tile_xy = 882, 470
t2f4_tile_xy = 760, 358
t3f4_tile_xy = 881, 489
t4f4_tile_xy = 854, 489
t5f4_tile_xy = 885, 469

spot_4_coords = SpotCoords(t1f4_ss_region_xy, t2f4_ss_region_xy, t3f4_ss_region_xy, t4f4_ss_region_xy, t5f4_ss_region_xy,
                           t1f4_claim_xy, t2f4_claim_xy, t3f4_claim_xy, t4f4_claim_xy, t5f4_claim_xy,
                           t1f4_tile_xy, t2f4_tile_xy, t3f4_tile_xy, t4f4_tile_xy, t5f4_tile_xy)


t1f5_ss_region_xy = 942, 351, 993, 448
t2f5_ss_region_xy = 710, 347, 762, 430
t3f5_ss_region_xy = 954, 548, 1003, 643
t4f5_ss_region_xy = 704, 533, 762, 626
t5f5_ss_region_xy = 830, 427, 880, 527

t1f5_claim_xy = 972, 385
t2f5_claim_xy = 740, 380
t3f5_claim_xy = 977, 615
t4f5_claim_xy = 751, 608
t5f5_claim_xy = 856, 474

t1f5_tile_xy = 881, 473
t2f5_tile_xy = 740, 380
t3f5_tile_xy = 882, 490
t4f5_tile_xy = 751, 608
t5f5_tile_xy = 856, 474

spot_5_coords = SpotCoords(t1f5_ss_region_xy, t2f5_ss_region_xy, t3f5_ss_region_xy, t4f5_ss_region_xy, t5f5_ss_region_xy,
                           t1f5_claim_xy, t2f5_claim_xy, t3f5_claim_xy, t4f5_claim_xy, t5f5_claim_xy,
                           t1f5_tile_xy, t2f5_tile_xy, t3f5_tile_xy, t4f5_tile_xy, t5f5_tile_xy)


def start_catching_chins(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop - curr_at_trap = {CURR_AT_TRAP}')
        return check_traps_from(CURR_AT_TRAP)

    else:
        print(f'First Loop - performing setup.')
        setup_interface('north', 4, 'up')

        set_initial_traps()

    return True


def set_initial_traps():
    trap_tile_coords = [[615, 454], [1060, 688], [610, 485], [945, 402]]
    is_tab_open('inventory', True)

    curr_trap_num = 0
    for coords in trap_tile_coords:
        print(f'Setting Trap: {curr_trap_num} (i) then moving trap tile {curr_trap_num+1} @ coords: {coords}')
        # update_curr_trap_state(curr_trap_num)
        if not does_img_exist(img_name="Inventory_Box_Trap", script_name="Red_Chins", threshold=0.9, should_click=True, click_middle=True):
            print('Failed to find Inventory Box Trap to set on initial trap setup.')
            return False
        API.AntiBan.sleep_between(2.0, 2.1)
        if not trap_is_set(curr_trap_num):
            return False
        mouse_long_click(coords)
        wait_for_img(img_name="Walk_Here", script_name="Red_Chins", should_click=True, click_middle=True, threshold=0.9)
        API.AntiBan.sleep_between(0.3, 0.4)
        if curr_trap_num == 1:
            API.AntiBan.sleep_between(1.2, 1.3)
        if curr_trap_num == 3:
            API.AntiBan.sleep_between(1.3, 1.4)
            if not does_img_exist(img_name="Inventory_Box_Trap", script_name="Red_Chins", threshold=0.9, should_click=True, click_middle=True):
                return False
        curr_trap_num += 1

    # update_curr_trap_state(NUM_TRAPS-1)
    if not trap_is_set(curr_trap_num):
        return False
    print(f'TRAP_CHECK_ORDER = {TRAP_CHECK_ORDER}')
    is_tab_open('inventory', False)
    API.AntiBan.sleep_between(4.8, 4.9)
    return True


def check_traps_from(curr_at_trap_num):
    print(f'Checking traps from curr_at_trap_num: {curr_at_trap_num}')

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

    yellow_color = 160, 132, 8
    green_color = 29, 163, 51
    red_color = 209, 50, 46

    curr_check_trap_regions = [curr_check_coords.t1_ss_xy, curr_check_coords.t2_ss_xy, curr_check_coords.t3_ss_xy, curr_check_coords.t4_ss_xy, curr_check_coords.t5_ss_xy]
    curr_check_trap_claim_coords = [curr_check_coords.t1_claim_xy, curr_check_coords.t2_claim_xy, curr_check_coords.t3_claim_xy, curr_check_coords.t4_claim_xy, curr_check_coords.t5_claim_xy]
    curr_check_trap_tile_coords = [curr_check_coords.t1_reset_tile_xy, curr_check_coords.t2_reset_tile_xy, curr_check_coords.t3_reset_tile_xy, curr_check_coords.t4_reset_tile_xy, curr_check_coords.t5_reset_tile_xy]

    spot_emojis = [ '', '', '', '', ]

    for curr_check_trap_num in TRAP_CHECK_ORDER:

        print(f'\n --- Checking trap {curr_check_trap_num} from curr_at_trap: {curr_at_trap_num} in TRAP_CHECK_ORDER: {TRAP_CHECK_ORDER}\n')

        if color_exists(curr_check_trap_regions[curr_check_trap_num], yellow_color, 'Chin_Yellow_Check'):
            handle_yellow_found(curr_check_trap_num, curr_at_trap_num, spot_emojis)

        elif color_exists(curr_check_trap_regions[curr_check_trap_num], green_color, 'Chin_Green_Check'):
            return handle_green_found(curr_check_trap_num, curr_at_trap_num, curr_check_trap_claim_coords, curr_check_trap_tile_coords, spot_emojis)

        elif color_exists(curr_check_trap_regions[curr_check_trap_num], red_color, 'Chin_Green_Check'):
            return handle_red_found(curr_check_trap_num, curr_at_trap_num, curr_check_trap_claim_coords, curr_check_trap_tile_coords, spot_emojis)

        else:
            print(f'No color found for spot {curr_check_trap_num} from trap {curr_at_trap_num}')
            spot_emojis.insert(curr_check_trap_num, '✖')
            print(f'Checking again...')
            API.AntiBan.sleep_between(0.4, 0.5)
            attempts = 0
            while attempts <= 6:
                if color_exists(curr_check_trap_regions[curr_check_trap_num], yellow_color, 'Chin_Yellow_Check'):
                    handle_yellow_found(curr_check_trap_num, curr_at_trap_num, spot_emojis)
                    return True

                elif color_exists(curr_check_trap_regions[curr_check_trap_num], green_color, 'Chin_Green_Check'):
                    return handle_green_found(curr_check_trap_num, curr_at_trap_num, curr_check_trap_claim_coords,
                                              curr_check_trap_tile_coords, spot_emojis)

                elif color_exists(curr_check_trap_regions[curr_check_trap_num], red_color, 'Chin_Green_Check'):
                    return handle_red_found(curr_check_trap_num, curr_at_trap_num, curr_check_trap_claim_coords,
                                            curr_check_trap_tile_coords, spot_emojis)
                attempts += 1

            if attempts > 5:
                print(f'Manually picking up presumed down trap since no other colors found')
                mouse_long_click(curr_check_trap_claim_coords[curr_check_trap_num])
                if not wait_for_img(img_name="Lay_Trap", script_name="Red_Chins", threshold=0.8, should_click=True, click_middle=True):
                    if not wait_for_img(img_name="Cancel", script_name="Red_Chins", threshold=0.8, should_click=True, click_middle=True):
                        print(f'Failed to find cancel after failing to find Lay trap in manual reset')
                    else:
                        mouse_long_click(curr_check_trap_claim_coords[curr_check_trap_num])
                        if not wait_for_img(img_name="Lay_Trap", script_name="Red_Chins", threshold=0.8, should_click=True, click_middle=True):
                            if not wait_for_img(img_name="Reset_Trap", script_name="Red_Chins", threshold=0.9,
                                                should_click=True, click_middle=True):
                                print(f'Faied to find ')
                                return False

                API.AntiBan.sleep_between(5.2, 5.3)
                if not trap_is_set(curr_check_trap_num):
                    return False
                print(f'Curr at trap: {get_curr_at_trap()} (post update)')
                return True

    print(f'\n{spot_emojis[1]}  -  {spot_emojis[0]}\n    {spot_emojis[4]}\n{spot_emojis[3]}  -  {spot_emojis[2]}')
    return True


def update_curr_trap_state(new_trap_num):
    print(f'Updating Trap State with new_trap_num: {new_trap_num} FROM {get_curr_at_trap()}')
    update_curr_at_trap(new_trap_num)
    update_curr_trap_order(new_trap_num)
    return


# HELPERS
def update_curr_trap_order(new_trap_num):
    global TRAP_CHECK_ORDER
    last_idx = NUM_TRAPS - 1
    print(f'Removing Trap no. {new_trap_num} from TRAP_CHECK_ORDER if found and placing at end of array to check last.')
    if new_trap_num in TRAP_CHECK_ORDER:
        TRAP_CHECK_ORDER.remove(new_trap_num)
    TRAP_CHECK_ORDER.insert(last_idx, new_trap_num)
    print(f'TRAP_CHECK_ORDER now: {TRAP_CHECK_ORDER}')
    return


def update_curr_at_trap(new_trap_num):
    global CURR_AT_TRAP
    CURR_AT_TRAP = new_trap_num
    return CURR_AT_TRAP


def get_curr_at_trap():
    global CURR_AT_TRAP
    return CURR_AT_TRAP


def set_box_trap():
    is_tab_open('inventory', True)
    did_trap_set = does_img_exist(img_name="Inventory_Box_Trap", script_name="Red_Chins", threshold=0.9, should_click=True, click_middle=True)
    is_tab_open('inventory', False)
    API.AntiBan.sleep_between(5.0, 5.1)
    return did_trap_set


# COLOR CHECK
def color_exists(region, color, img_name):
    print(f'Checking color: {color} @ region: {region}')
    # 25 color tolerance working but not with very little timer remaining - trying 35
    return does_color_exist_in_sub_image(region, color, img_name, color_tolerance=36, count_min=5)


# HANDLE COLORS
def handle_yellow_found(curr_check_trap_num, curr_at_trap_num, spot_emojis):
    print(f'🟡 Found for spot {curr_check_trap_num} from trap {curr_at_trap_num}')
    spot_emojis.insert(curr_check_trap_num, '🟡')
    return


def handle_green_found(curr_check_trap_num, curr_at_trap_num, curr_check_trap_claim_coords, curr_check_trap_tile_coords, spot_emojis):
    print(f'🟢 Found for spot {curr_check_trap_num} from trap {curr_at_trap_num}')
    spot_emojis.insert(curr_check_trap_num, '🟢')

    print(f'Curr_claim_coords: {curr_check_trap_claim_coords[curr_check_trap_num]}')

    mouse_long_click(curr_check_trap_claim_coords[curr_check_trap_num])
    did_click_check_trap = wait_for_img(img_name="Reset_Trap", script_name="Red_Chins", threshold=0.8, should_click=True, click_middle=True)

    if did_click_check_trap:
        saw_exp_drop = wait_for_img(img_name="Hunter", category="Exp_Drops", threshold=0.85)

        if saw_exp_drop:
            print(f'Saw exp drop - waiting for 5 seconds')
            handle_level_dialogue()
            update_curr_trap_state(curr_check_trap_num)
            API.AntiBan.sleep_between(3.1, 3.2)
            return trap_is_set(curr_check_trap_num)

    return False


def handle_red_found(curr_check_trap_num, curr_at_trap_num, curr_check_trap_claim_coords, curr_check_trap_tile_coords, spot_emojis):
    print(f'🔴 Found for spot {curr_check_trap_num} from trap {curr_at_trap_num}')
    spot_emojis.insert(curr_check_trap_num, '🔴')

    print(f'curr_claim_coords: {curr_check_trap_claim_coords[curr_check_trap_num]}')
    mouse_long_click(curr_check_trap_claim_coords[curr_check_trap_num])
    did_click_reset = wait_for_img(img_name="Reset_Trap", script_name="Red_Chins", threshold=0.8, should_click=True, click_middle=True)

    if did_click_reset:
        API.AntiBan.sleep_between(7.1, 7.2)
        return trap_is_set(curr_check_trap_num)


def trap_is_set(curr_check_trap_num):
    yellow_check_region = 835, 430, 881, 475
    yellow_color = 160, 132, 8
    found_yellow = False
    search_attempts = 0

    while not found_yellow and search_attempts <= 50:
        print(f'Searching for yellow adjacent to us @ {yellow_check_region} total of {search_attempts} times')
        update_curr_trap_state(curr_check_trap_num)
        found_yellow = does_color_exist_in_sub_image(yellow_check_region, yellow_color, 'Adj_Yellow_Wait', color_tolerance=25)
        if found_yellow:
            return True
        search_attempts += 1

    print(f'⛔ Returning False from Trap_is_set')
    return False


def handle_level_dialogue():
    if wait_for_img(img_name="level_up", category="General", max_wait_sec=2):
        pag.press('space')
        API.AntiBan.sleep_between(1.1, 2.3)
        pag.press('space')
    return