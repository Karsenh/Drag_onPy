from API.Imaging.Image import does_img_exist, wait_for_img
from API.Interface.General import setup_interface, is_tab_open, get_xy_for_invent_slot
import API.AntiBan
from API.Mouse import mouse_click

SEED_TO_USE = "54"

# Spot      PLANT    |    WATER
spot_1 = [[800, 480], [800, 480]]  # ✔
spot_2 = [[670, 460], [700, 460]]  # ✔

spot_3 = [[830, 530], [800, 470]]  # ✔
spot_4 = [[660, 490], [690, 470]]  # ✔

spot_5 = [[830, 560], [800, 490]]  # ✔
spot_6 = [[670, 490], [700, 480]]  # ✔

spot_7 = [[830, 560], [800, 490]]  # ✔
spot_8 = [[680, 490], [690, 490]]  # ✔

plant_and_water_xys = [spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8]

CURR_WATER_CAN_SLOT = 1


def start_tithe_farming(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')
        full_farm_cycle(curr_loop)
    else:
        print(f'First loop - setup')
        setup_interface('south', 1, 'up')
        check_if_at_start()
    return True


def check_if_at_start():
    if not does_img_exist(img_name="Farm_Start_Flag", script_name="Tithe_Farmer", threshold=0.92):
        if wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.9, should_click=True, y_offset=3):
            return wait_for_img(img_name="Farm_Start_Flag", script_name="Tithe_Farmer", threshold=0.92, max_wait_sec=15)
    return True


def full_farm_cycle(curr_loop):
    plant_and_water_both_sections()
    water_both_sections()
    harvest_both_sections(curr_loop)
    return


def plant_and_water_both_sections():
    plant_and_water()
    move_to_section_2()
    increase_can_slot()
    plant_and_water()
    move_back_from_section_2()
    move_to_farm_start()
    increase_can_slot()
    return


def water_both_sections():
    for i in range(1, 3):
        water_plants()
        move_to_section_2()
        increase_can_slot()
        water_plants()
        move_back_from_section_2()
        move_to_farm_start()
        increase_can_slot()
    return


def harvest_both_sections(curr_loop):
    harvest_plants()
    move_to_section_2()
    increase_can_slot()
    harvest_plants()
    # move_back_from_section_2()
    # move_to_water()
    deposit_points()
    move_to_water_from_points()
    fill_empty_cans()
    # Every 5th farm 'run' we'll be out of seeds and need to resupply
    if curr_loop % 6 == 0:
        resupply_seeds()
        API.AntiBan.sleep_between(3.4, 3.5)
    move_to_farm_start()
    increase_can_slot()
    return


def resupply_seeds():
    # From water barrel
    wait_for_img(img_name="Door_In", script_name="Tithe_Farmer", threshold=0.9, should_click=True, click_middle=True)
    wait_for_img(img_name="Seed_Table", script_name="Tithe_Farmer", threshold=0.95, should_click=True, click_middle=True)
    wait_for_img(img_name=f"Seed_{SEED_TO_USE}_Selection", script_name="Tithe_Farmer", threshold=0.9, should_click=True, click_middle=True)
    API.AntiBan.sleep_between(0.2,0.3)
    wait_for_img(img_name=f"Door_Out", script_name="Tithe_Farmer", threshold=0.9, should_click=True, click_middle=True, min_clicks=3,max_clicks=4)
    return


def fill_empty_cans():
    is_tab_open("inventory", True)

    does_img_exist(img_name="Empty_Watering_Can", script_name="Tithe_Farmer", threshold=0.9, should_click=True, click_middle=True)

    wait_for_img(img_name="Water_Barrel", script_name="Tithe_Farmer", threshold=0.85, should_click=True, click_middle=True, max_wait_sec=15)

    API.AntiBan.sleep_between(16.0, 16.1)
    return


def move_to_section_2():
    other_side_xy = 780, 630
    API.AntiBan.sleep_between(0.3, 0.4)
    mouse_click(other_side_xy)
    # API.AntiBan.sleep_between(3.5, 3.6)
    return wait_for_img(img_name="Section_2_Flag", script_name="Tithe_Farmer", threshold=0.8, max_wait_sec=15)


def move_back_from_section_2():
    move_back_xy = 765, 135
    mouse_click(move_back_xy)
    API.AntiBan.sleep_between(7.0, 7.1)
    return wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.9)


def deposit_points():
    if not does_img_exist(img_name="Deposit_Points", script_name="Tithe_Farmer", threshold=0.9, should_click=True, click_middle=True):
        manual_deposit_xy = 854, 253
        mouse_click(manual_deposit_xy)
    API.AntiBan.sleep_between(2.0, 2.1)
    return wait_for_img(img_name="Farming", category="Exp_Drops")


def move_to_water_from_points():
    wait_for_img(img_name="Water_Barrel_From_Points", script_name="Tithe_Farmer", threshold=0.8, should_click=True)
    return


def move_to_water():
    if not wait_for_img(img_name="Minimap_Water", script_name="Tithe_Farmer", threshold=0.85, should_click=True):
        manual_minimap_xy = 1367, 94
        mouse_click(manual_minimap_xy)
    return


def harvest_plants():
    i = 1
    for spot in plant_and_water_xys:
        mouse_click(spot[0])
        wait_between_plants(i, min_even_sec=2.5, min_odd_sec=2.9)
        i += 1
    return


def move_to_farm_start():
    global CURR_WATER_CAN_SLOT
    # From doorway
    wait_for_img(img_name="Minimap_Farm_Start", script_name="Tithe_Farmer", threshold=0.9, should_click=True, y_offset=3)
    return wait_for_img(img_name="Farm_Start_Flag", script_name="Tithe_Farmer", threshold=0.92, max_wait_sec=15)


def plant_and_water():
    # patch_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    is_tab_open("inventory", True)
    i = 1
    for spot in plant_and_water_xys:
        if does_img_exist(img_name="Seed_34", script_name="Tithe_Farmer", should_click=True, click_middle=True):
            # Plant seed
            mouse_click(spot[0])
            # Click water can
            mouse_click(get_xy_for_invent_slot(CURR_WATER_CAN_SLOT))
            wait_between_plants(i)
            mouse_click(spot[1])
            API.AntiBan.sleep_between(1.0, 1.1)
        i += 1
    return


def water_plants():
    is_tab_open("inventory", True)
    i = 1
    for spot in plant_and_water_xys:
        mouse_click(get_xy_for_invent_slot(CURR_WATER_CAN_SLOT))
        mouse_click(spot[0])
        wait_between_plants(i)
        i += 1
    return


def increase_can_slot():
    global CURR_WATER_CAN_SLOT
    CURR_WATER_CAN_SLOT += 1
    if CURR_WATER_CAN_SLOT == 7:
        CURR_WATER_CAN_SLOT = 1
    return


def wait_between_plants(i, min_even_sec=2.4, min_odd_sec=2.8):
    if i % 2 == 0:
        API.AntiBan.sleep_between(min_even_sec, min_even_sec+0.1)
    else:
        API.AntiBan.sleep_between(min_odd_sec, min_odd_sec+0.1)
    return


def reset_can_slot():
    global CURR_WATER_CAN_SLOT
    CURR_WATER_CAN_SLOT = 1
    return

