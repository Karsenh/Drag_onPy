import pyautogui
import API.AntiBan
from API.Debug import write_debug
from GUI.Imports.Skill_Level_Input.Skill_Level_Input import get_skill_level
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot
from API.Mouse import mouse_click, mouse_move, mouse_long_click

SEED_NUM = None


class Tile:
    def __init__(self, plant_xy, water_xy, harvest_xy):
        self.plant_xy = plant_xy
        self.water_xy = water_xy
        self.harvest_xy = harvest_xy


t1_plant = 798, 425
t1_water = 798, 425
tile_1 = Tile(t1_plant, t1_water, t1_plant)

t2_plant = 680, 426
t2_water = 695, 427
tile_2 = Tile(t2_plant, t2_water, t2_plant)

t3_plant = 830, 498
t3_water = 810, 478
tile_3 = Tile(t3_plant, t3_water, t3_plant)

t4_plant = 668, 481
t4_water = 690, 481
tile_4 = Tile(t4_plant, t4_water, t4_plant)

t5_plant = 832, 552
t5_water = 809, 483
tile_5 = Tile(t5_plant, t5_water, t5_plant)

t6_plant = 670, 490
t6_water = 690, 485
tile_6 = Tile(t6_plant, t6_water, t6_plant)

t7_plant = 833, 564
t7_water = 800, 477
tile_7 = Tile(t7_plant, t7_water, t7_plant)

t8_plant = 680, 483
t8_water = 687, 480
tile_8 = Tile(t8_plant, t8_water, t8_plant)

t9_plant = 844, 653
t9_water = 770, 501
tile_9 = Tile(t9_plant, t9_water, t9_plant)

t10_plant = 640, 510
t10_water = 692, 487
tile_10 = Tile(t10_plant, t10_water, t10_plant)

t11_plant = 833, 546
t11_water = 803, 475
tile_11 = Tile(t11_plant, t11_water, t11_plant)

t12_plant = 666, 482
t12_water = 694, 477
tile_12 = Tile(t12_plant, t12_water, t12_plant)

t13_plant = 833, 550
t13_water = 810, 485
tile_13 = Tile(t13_plant, t13_water, t13_plant)

t14_plant = 670, 487
t14_water = 695, 480
tile_14 = Tile(t14_plant, t14_water, t14_plant)

t15_plant = 830, 550
t15_water = 800, 483
tile_15 = Tile(t15_plant, t15_water, t15_plant)

t16_plant = 668, 480
t16_water = 690, 475
tile_16 = Tile(t16_plant, t16_water, t16_plant)

all_tiles = [tile_1, tile_2, tile_3, tile_4, tile_5, tile_6, tile_7, tile_8, tile_9, tile_10, tile_11, tile_12, tile_13, tile_14, tile_15, tile_16]

BACK_TO_FIRST_PLOT_XY = 765, 130

PLANT_FROM_2_XY = 800, 333


def start_tithe_farming(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')
        # Plant Seed & Water all spots (1-16) then return to start
        plant_and_water_seeds()
        return_to_plot_1()

        # Water all spots (1-16) then return to start x2
        click_plants()
        return_to_plot_1()

        # Water all spots (1-16) then return to start x2
        click_plants()
        return_to_plot_1()

        # Harvest all spots (1-16) then return to start
        # harvest_plants()
        click_plants(should_water=False)
        deposit_points()

        # Every 6th loop - refill Gricoller's can and seeds
        if curr_loop % 6 == 0:
            print(f'Replenishing Can & Seeds')
            replenish_can()
            replenish_seeds()

        move_to_plot_start()

    else:
        print(f'First loop')
        # setup_interface('south', 1, 'up')
        set_seed_to_use()
        if not move_to_plot_start():
            print(f'Failed to find plot start - exiting')
            return False

    return True


# MAIN METHODS
def plant_and_water_seeds():
    curr_tile_num = 1

    for tile_coords in all_tiles:
        print(f'🔢 curr_tile_num = {curr_tile_num}')

        # Select seed in inventory
        if not select_inventory_seed():
            print(f'⛔ Failed to find inventory seed.')
            return False

        if curr_tile_num != 1:
            print(f'💤 Sleeping (1/2)...')
            # Sleep while watering
            sleep_between_actions(curr_tile_num, 1)

        # Use it on the current plant_xy (from prev plant)
        print(f'🌱 tile_coords.plant_xy = {tile_coords.plant_xy}')
        mouse_click(tile_coords.plant_xy)

        # Sleep while planting seed
        print(f'💤 Sleeping (2/2)...')
        sleep_between_actions(curr_tile_num, 2)

        mouse_click(tile_coords.water_xy, min_num_clicks=2, max_num_clicks=3)

        # # Long click the plant (from curr plant)
        # print(f'💦 tile_coords.water_xy = {tile_coords.water_xy}')
        # mouse_long_click(tile_coords.water_xy)
        #
        # # Select 'water' option from long click drop-down
        # print(f'Selecting water plant option')
        # if not select_water_plant_option(tile_coords.water_xy):
        #     return False

        if curr_tile_num == 16:
            API.AntiBan.sleep_between(2.3, 2.4)

        curr_tile_num += 1

    print(f'Done Planting & Watering. Need to return.')
    return True


def click_plants(fast_click=True, should_water=True):
    if not should_water:
        # mouse_click(PLANT_FROM_2_XY, min_num_clicks=2, max_num_clicks=3)
        mouse_long_click(PLANT_FROM_2_XY)
        # select_water_plant_option(PLANT_FROM_2_XY)
        if not does_img_exist(img_name='Harvest', script_name='Tithe_Farmer', threshold=0.9, should_click=True, click_middle=True):
            if not does_img_exist(img_name='Cancel', script_name='Tithe_Farmer', should_click=True, click_middle=True):
                return False
            else:
                if not does_img_exist(img_name='Harvest', script_name='Tithe_Farmer', threshold=0.9, should_click=True, click_middle=True):
                    return False
    else:
        mouse_long_click(PLANT_FROM_2_XY)
        select_water_plant_option(PLANT_FROM_2_XY)
    API.AntiBan.sleep_between(4.3, 4.4)

    curr_tile_num = 1

    if not fast_click:
        for tile_coords in all_tiles:
            if curr_tile_num != 1:
                mouse_long_click(tile_coords.plant_xy)
                if not should_water:
                    mouse_click(PLANT_FROM_2_XY, min_num_clicks=2, max_num_clicks=3)
                else:
                    select_water_plant_option(tile_coords.plant_xy)
                sleep_between_actions(curr_tile_num, 1, is_watering=True)

            curr_tile_num += 1
        return
    else:
        for tile_coords in all_tiles:
            if curr_tile_num != 1:
                mouse_click(tile_coords.plant_xy, min_num_clicks=2, max_num_clicks=2)
                sleep_between_actions(curr_tile_num, 1, is_watering=True)

            curr_tile_num += 1
        return


def harvest_plants():

    return


def deposit_points():
    if not wait_for_img(img_name='Deposit_Sack', script_name='Tithe_Farmer', threshold=0.85, should_click=True, click_middle=True):
        print(f'Failed to find points sack')
        return False
    API.AntiBan.sleep_between(3.0, 3.1)
    wait_for_img(img_name='Farming', category='Exp_Drops', threshold=0.85, max_wait_sec=8)
    return


def replenish_can():
    if not does_img_exist(img_name='Gricollers_Can', script_name='Tithe_Farmer', should_click=True, click_middle=True):
        print(f'Failed to find inventory can')
        return False
    if not does_img_exist(img_name='Water_Barrel_From_Points', script_name='Tithe_Farmer', should_click=True, click_middle=True):
        print(f'Failed to find water barrel from points')
        return False
    API.AntiBan.sleep_between(4.0, 4.3)
    return True


def replenish_seeds():
    if not does_img_exist(img_name='Door_From_Water_Barrel', script_name='Tithe_Farmer', should_click=True, click_middle=True, min_clicks=2, max_clicks=3):
        print(f'Failed to find Door from Water Barrel')
        return False
    if not wait_for_img(img_name='Seed_Table', script_name='Tithe_Farmer', should_click=True, click_middle=True, min_clicks=2, max_clicks=3):
        print(f'Failed to find seed table...')
        return False
    select_seeds_from_table()
    wait_for_img(img_name=f'Seed_{SEED_NUM}', script_name="Tithe_Farmer", should_click=True, click_middle=True)
    does_img_exist(img_name='door_enter', script_name='Tithe_Farmer', threshold=0.9, should_click=True, click_middle=True, min_clicks=3, max_clicks=4)
    API.AntiBan.sleep_between(4.0, 4.1)
    return True


def return_to_plot_1():
    print(f'🔁 Returning to first plot section...')
    mouse_click(BACK_TO_FIRST_PLOT_XY)
    API.AntiBan.sleep_between(7.0, 7.1)
    return


def set_seed_to_use():
    global SEED_NUM

    curr_farming_level = get_skill_level('farming')

    if curr_farming_level < 54:
        print(f'Setting seed num 34')
        SEED_NUM = 34
    elif 54 >= curr_farming_level < 74:
        print('Setting seed num 54')
        SEED_NUM = 54
    else:
        print('Setting seed num 74')
        SEED_NUM = 74

    return


def move_to_plot_start():
    if not does_img_exist(img_name="Farm_Start_Flag_Alt", script_name="Tithe_Farmer", threshold=0.92):
        if not wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.92, should_click=True, y_offset=15, max_wait_sec=10):
            print(f'Failed to find Minimap Farm Start')
        else:
            if not wait_for_img(img_name="Farm_Start_Flag_Alt", script_name="Tithe_Farmer", threshold=0.92, max_wait_sec=10):
                return False
    return True


def select_water_plant_option(retry_xy):
    attempts = 0

    while attempts < 2:
        if not does_img_exist(img_name='Water_Plant', script_name='Tithe_Farmer', threshold=0.9, should_click=True,
                              click_middle=True):
            # Click cancel and try again
            if not does_img_exist(img_name='Cancel', script_name='Tithe_Farmer', threshold=0.9, should_click=True,
                                  click_middle=True):
                print(f'⛔ Failed to find cancel after trying to find water xy')
                return False
            mouse_long_click(retry_xy)

            attempts += 1
        else:
            return True
    return False


# HELPERS
def select_inventory_seed():
    return does_img_exist(img_name=f'Seed_{SEED_NUM}', script_name="Tithe_Farmer", should_click=True, click_middle=True)


def sleep_between_actions(curr_tile, sleep_num, is_watering=False):
    if curr_tile == 1:
        API.AntiBan.sleep_between(2.0, 2.1)
        return

    if curr_tile == 9 and (sleep_num == 2 or is_watering):
        API.AntiBan.sleep_between(4.5, 4.55)
        return

    if curr_tile % 2 == 0:
        # Left side
        print(f'Left side - Curr_tile: {curr_tile} - sleep_num: {sleep_num}')
        if sleep_num == 1:
            API.AntiBan.sleep_between(2.1, 2.2)
        else:
            API.AntiBan.sleep_between(2.2, 2.3)
    else:
        print(f'Right side - Curr_tile: {curr_tile} - sleep_num: {sleep_num}')
        if sleep_num == 1:
            API.AntiBan.sleep_between(2.3, 2.4)
        else:
            API.AntiBan.sleep_between(2.2, 2.3)

    return


def select_seeds_from_table():
    return wait_for_img(img_name=f'grab_seed_{SEED_NUM}', script_name='Tithe_Farmer', threshold=0.9, should_click=True, click_middle=True)

