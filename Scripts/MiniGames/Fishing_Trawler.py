import random
import API.AntiBan
from API.Interface.General import setup_interface, pitch_camera
from API.Imaging.Image import does_img_exist, wait_for_img
from API.Mouse import mouse_click

game_over = False


def start_trawling(curr_loop):
    global game_over

    if curr_loop == 1:
        setup_interface("north", 3, "up")

    if not game_over:
        pitch_camera(direction="up")

        # move to rewards box
        if not move_to_reward_box():
            return False

        # open rewards box
        if not claim_and_deposit_rewards():
            return False

        # bank all
        move_to_plank_cross()

        # move to plank
        cross_plank()

        # go down ladder
        climb_down_ladder()

        # Wait until we see the charter ship reach the end of the map - wait for 5 min
        if not wait_for_game_to_start():
            return False

        # Click on SOUTH sea to move against south boat wall
        move_to_wall()

        # Intermittently click south of character until 'finished.png' is seen
        game_over = repair_hole_until_finished()
    else:
        if does_img_exist(img_name="rewards_box", script_name="Fishing_Trawler", should_click=False, threshold=0.95):
            game_over = False

    return True


def move_to_reward_box():
    if wait_for_img(img_name="rewards_box", script_name="Fishing_Trawler", category="Scripts", max_wait_sec=5):
        does_img_exist(img_name="rewards_box", script_name="Fishing_Trawler", should_click=True, threshold=0.95)
        API.AntiBan.sleep_between(3.5, 3.6)
        return True
    else:
        return False


def claim_and_deposit_rewards():
    if wait_for_img(img_name="trawling_net", script_name="Fishing_Trawler", max_wait_sec=6):
        if does_img_exist(img_name="trawling_net", script_name="Fishing_Trawler", should_click=True, x_offset=15, y_offset=15, threshold=0.95):
            if wait_for_img(img_name="bank_deposit", script_name="Fishing_Trawler", max_wait_sec=4):
                does_img_exist(img_name="bank_deposit", script_name="Fishing_Trawler", category="Scripts", threshold=0.80, should_click=True, x_offset=10, y_offset=10)
                API.AntiBan.sleep_between(0.4, 1.4)
        return True
    else:
        return False


def move_to_plank_cross():
    plank_tile_xy = 1408, 147
    mouse_click(plank_tile_xy)
    API.AntiBan.sleep_between(9.6, 10.1)
    return


def cross_plank():
    plank_xy = 677, 458
    mouse_click(plank_xy)
    API.AntiBan.sleep_between(4.1, 6.3)
    return


def climb_down_ladder():
    ladder_xy = 612, 530
    mouse_click(ladder_xy, max_x_dev=9, max_y_dev=11)
    return


def wait_for_game_to_start():
    return wait_for_img(img_name="arrival", script_name="Fishing_Trawler", category="Scripts", max_wait_sec=360, threshold=0.95)


def move_to_wall():
    API.AntiBan.sleep_between(4.2, 4.3)
    wall_xy = 1381, 205
    mouse_click(wall_xy)
    API.AntiBan.sleep_between(1.8, 3.7)
    return


def repair_hole_until_finished():
    hole_xy = 748, 520

    while not does_img_exist(img_name="finished", script_name="Fishing_Trawler", category="Scripts", threshold=0.90) \
            or does_img_exist(img_name="finished_1", script_name="Fishing_Trawler", category="Scripts", threshold=0.90) \
            or does_img_exist(img_name="finished_2", script_name="Fishing_Trawler", category="Scripts", threshold=0.90) \
            or does_img_exist(img_name="finished_3", script_name="Fishing_Trawler", category="Scripts", threshold=0.90) \
            or does_img_exist(img_name="rewards_box", script_name="Fishing_Trawler", should_click=False, threshold=0.95):
        mouse_click(hole_xy, max_num_clicks=12)

        if random.randint(1, 50) > 49:
            r_sleep_time = random.uniform(1.3, 5.3)
        else:
            r_sleep_time = random.uniform(0.1, 0.33)

        API.AntiBan.sleep_between(0.1, r_sleep_time)
    return True



