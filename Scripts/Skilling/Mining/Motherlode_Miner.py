import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open
from API.Imaging.Image import get_color_at_coords, does_img_exist, wait_for_img, does_color_exist_in_thresh, does_color_exist_in_sub_image
from API.Mouse import mouse_click, mouse_long_click

CURR_SPOT = 1
SEARCHING_FOR_SPOT = False
MINING_ATTEMPTS = 0


def start_motherlode_mining(curr_loop):
    global CURR_SPOT

    if curr_loop != 1:
        print(f"Not the first loop")
        if is_invent_full():
            # Drop shit off in sluice and deposit ore in bank then return and continue mining
            move_to_midway_from("Ore")
            mine_midway_obstacle("Ore")
            if not move_to_sluice():
                return False
            curr_spot = fix_broken_wheels()
            API.AntiBan.sleep_between(0.3, 0.4)

            load_hopper_from(curr_spot)
            claim_ore()
            if not deposit_ore():
                return False
            move_to_midway_from("Box")
            CURR_SPOT = 1
            if mine_midway_obstacle("Box"):
                if resume_spot_1_from_midway():
                    API.AntiBan.sleep_between(3.0, 3.1)
                    return True
                else:
                    manual_spot_1_xy = 771, 130
                    mouse_click(manual_spot_1_xy)
                    API.AntiBan.sleep_between(3.5, 3.6)
        if not is_mining():
            find_and_mine_next_spot()

    else:
        print(f"This is the first loop")
        setup_interface("west", 2, "up")
        # Start in front of ore 1 on the west side
        start_mining_first_spot()

    return True


def is_mining():
    global SEARCHING_FOR_SPOT
    global MINING_ATTEMPTS

    bright_yellow_xy = 761, 383
    dark_yellow_xy = 747, 414

    bright_yellow_check = 167, 137, 5
    dark_yellow_check = 80, 65, 14

    yellow_check_region = 730, 380, 760, 430

    if does_color_exist_in_sub_image(yellow_check_region, dark_yellow_check, 'Motherlode_Yellow_Check', color_tolerance=10):
        # 167, 137, 5
        print(f"Saw yellow ore wheel. - No longer Mining.")
        SEARCHING_FOR_SPOT = True
        MINING_ATTEMPTS = 0
        return False
    else:
        print(f"Yellow ore wheel not found. - Must still be mining")
        if not wait_for_img(img_name="Mining", category="Exp_Drops", threshold=0.9, max_wait_sec=2):
            print(f'⛏ MINING_ATTEMPTS: {MINING_ATTEMPTS} - Failed to find exp drop in 10 seconds - Must not be mining')
            if MINING_ATTEMPTS > 5:
                SEARCHING_FOR_SPOT = True
                return False
            MINING_ATTEMPTS += 1
            return True
        else:
            MINING_ATTEMPTS = 0
            return True


def is_invent_full():
    global CURR_SPOT
    if does_img_exist(img_name="Too_Full", script_name="Motherlode_Miner", threshold=0.9):
        print(f'Inventory full chat image found')
        return True

    is_tab_open("inventory", True)
    ore_color_xy = 1348, 800  # 31, 34, 31
    exists_color = 35, 35, 35

    if does_color_exist_in_thresh(ore_color_xy, exists_color, 20):
        print(f'Ore found in last inventory slot')
        return True
    else:
        print(f'No ore in last inventory slot')
        return False


def start_mining_first_spot():
    return wait_for_img(img_name="Spot_1_From_1", script_name="Motherlode_Miner", threshold=0.91, should_click=True, click_middle=True)


def find_and_mine_next_spot():
    global CURR_SPOT
    global SEARCHING_FOR_SPOT

    attempts = 0
    search_offset = 1

    print(f"Find_and_mine CURR_SPOT: {CURR_SPOT} | SEARCHING_FOR_SPOT = {SEARCHING_FOR_SPOT} | search_offset = {search_offset}")

    if CURR_SPOT > 8:
        is_tab_open("inventory", False)

    if CURR_SPOT == 11:
        is_tab_open("inventory", False)
        if wait_for_img(img_name=f"Back_to_Spot_1_From_{CURR_SPOT}", script_name="Motherlode_Miner", threshold=0.92,
                       should_click=True, click_middle=True, max_wait_sec=4):
            CURR_SPOT = 1
        else:
            # Manually click
            manual_spot_1_xy = 1073, 717
            mouse_click(manual_spot_1_xy)
            CURR_SPOT = 1

        API.AntiBan.sleep_between(3.0, 3.1)
        return

    while SEARCHING_FOR_SPOT:
        print(f'ATTEMPTS: {attempts} | ')
        if CURR_SPOT+search_offset == 12:
            search_offset = 1
            attempts += 1
        if attempts < 4:
            if does_img_exist(img_name=f"Spot_{CURR_SPOT+search_offset}_From_{CURR_SPOT}", script_name="Motherlode_Miner", threshold=0.96, should_click=True, click_middle=True):
                SEARCHING_FOR_SPOT = False
                CURR_SPOT = CURR_SPOT+search_offset
                attempts = 0
                print(f'Found and moving to new ore from {CURR_SPOT-search_offset}- Setting CURR_SPOT: {CURR_SPOT}')
                API.AntiBan.sleep_between(3.5, 3.6)
                return
            else:
                search_offset += 1
        else:
            if does_img_exist(img_name=f"Spot_{search_offset}_From_{CURR_SPOT}", script_name="Motherlode_Miner", threshold=0.97, should_click=True, click_middle=True):
                SEARCHING_FOR_SPOT = False
                attempts = 0
                CURR_SPOT = CURR_SPOT+search_offset
                print(f'Found and moving to new ore from {CURR_SPOT-search_offset}- Setting CURR_SPOT: {CURR_SPOT}')
                API.AntiBan.sleep_between(3.5, 3.6)
                return

    return


def move_to_midway_from(spot="Ore"):
    if spot == "Box":
        xy = 1269, 69
        mouse_click(xy)
        return True
    else:
        if wait_for_img(img_name=f"Minimap_Midway_From_{spot}", script_name="Motherlode_Miner", threshold=0.9, should_click=True, x_offset=5, y_offset=3):
            return True

    return False


def mine_midway_obstacle(from_spot="Ore"):
    if wait_for_img(img_name=f"Midway_Rock_From_{from_spot}", script_name="Motherlode_Miner", threshold=0.94, should_click=True, click_middle=True, max_wait_sec=15):
        # Mine rock Wait for Mining exp drop as confirmation obstacle was cleared
        wait_for_img(img_name="Mining", category="Exp_Drops", threshold=0.90, max_wait_sec=10)
        return True
    else:
        if does_img_exist(img_name=f"Midway_Rock_From_{from_spot}_Clear", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True):
            return True
        if does_img_exist(img_name=f"Midway_Rock_From_{from_spot}_2", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True):
            wait_for_img(img_name="Mining", category="Exp_Drops", threshold=0.90, max_wait_sec=10)
            return True
        if does_img_exist(img_name=f"Midway_Rock_From_{from_spot}_3", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True):
            wait_for_img(img_name="Mining", category="Exp_Drops", threshold=0.90, max_wait_sec=10)
            return True
        else:
            print(f'Should manually click based on from_spot')
    return False


def move_to_sluice():
    # wait_for_img(img_name="Mining", category="Exp_Drops", threshold=0.90, max_wait_sec=10)
    if not does_img_exist(img_name="Minimap_Sluice", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True):
        print(f"Failed to find Minimap Sluice move click")
        return False
    is_tab_open("inventory", False)
    is_water_running()
    return True


def is_water_running():
    return wait_for_img(img_name="Running_Water", script_name="Motherlode_Miner", threshold=0.7, max_wait_sec=10)


def fix_broken_wheels():
    if does_img_exist(img_name="Broken_Wheel_1", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True):
        wait_for_img(img_name="Smithing", category="Exp_Drops", threshold=0.92, max_wait_sec=15)
        if does_img_exist(img_name="Broken_Wheel_2_From_1", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True):
            API.AntiBan.sleep_between(1.0, 1.1)
            wait_for_img(img_name="Smithing", category="Exp_Drops", threshold=0.92, max_wait_sec=12)
            return "Wheel_2"
        else:
            return "Wheel_1"
    else:
        if does_img_exist(img_name="Broken_Wheel_2", script_name="Motherlode_Miner", threshold=0.92, should_click=True, click_middle=True):
            API.AntiBan.sleep_between(3.0, 3.1)
            wait_for_img(img_name="Smithing", category="Exp_Drops", threshold=0.92, max_wait_sec=12)
            return "Wheel_2"
        else:
            return "Corner"


def load_hopper_from(spot="Corner"):
    # spots: "Corner", "Wheel_1", "Wheel_2"
    moving_to_hopper = does_img_exist(img_name=f"Hopper_From_{spot}", script_name="Motherlode_Miner", threshold=0.95, should_click=True, click_middle=True)

    if moving_to_hopper:
        match spot:
            case "Corner":
                API.AntiBan.sleep_between(8.0, 8.1)
            case "Wheel_1":
                API.AntiBan.sleep_between(7.0, 7.1)
            case "Wheel_2":
                API.AntiBan.sleep_between(5.0, 5.1)
        return True
    else:
        print(f"Failed to find and move to hopper from any of three locations: moving_to_hopper = {moving_to_hopper}")
        return False


def claim_ore():
    if wait_for_img(img_name="Claim_Sack", script_name="Motherlode_Miner", threshold=0.90):

        API.AntiBan.sleep_between(1.0, 1.1)
        does_img_exist(img_name="Claim_Sack", script_name="Motherlode_Miner", threshold=0.90, should_click=True, click_middle=True)

        if wait_for_img(img_name="Collected_Ore", script_name="Motherlode_Miner", threshold=0.92, max_wait_sec=10):
            print(f"Claimed ore from sack - depositing")
            return True
        else:
            if does_img_exist(img_name="Empty_Sack", script_name="Motherlode_Miner", threshold=0.90):
                print(f'Ore NOT claimed from sack for some reason - found empty sack. Water might have stopped.')
                # Increase claim attempts
                corner_xy = 1335, 123
                mouse_click(corner_xy)
                is_tab_open("inventory", False)
                API.AntiBan.sleep_between(3.4, 3.5)
                wait_for_img(img_name="Move_to_Corner", script_name="Motherlode_Miner", threshold=0.99, should_click=True)
                curr_spot = fix_broken_wheels()
                load_hopper_from(curr_spot)
                if claim_ore():
                    return True
                else:
                    return False
    else:
        print(f"Failed to find Claim Sack from Hopper for some reason")
        return False


def deposit_ore():
    minimap_deposit_box = 1372, 233
    mouse_click(minimap_deposit_box)

    if wait_for_img(img_name="Deposit_Box", script_name="Motherlode_Miner", threshold=0.92, should_click=True, click_middle=True, max_wait_sec=10):
        if wait_for_img(img_name="Inventory_Btn", script_name="Motherlode_Miner", threshold=0.85, should_click=True, click_middle=True):
            if wait_for_img(img_name="Hammer_Box", script_name="Motherlode_Miner", threshold=0.85, should_click=True, click_middle=True, max_wait_sec=14):
                if wait_for_img(img_name="Got_Hammer", script_name="Motherlode_Miner", threshold=0.9, max_wait_sec=8):
                    return True

    print(f"Something went wrong while depositing the ore...")
    return False


def resume_spot_1_from_midway():
    return does_img_exist(img_name="Spot_1_From_Midway", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True)



# Run to corner
# If water_is_running