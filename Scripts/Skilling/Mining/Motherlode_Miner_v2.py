import API.AntiBan
from API.Interface.General import setup_interface, is_tab_open
from API.Imaging.Image import get_color_at_coords, does_img_exist, wait_for_img, does_color_exist_in_thresh, does_color_exist_in_sub_image
from API.Mouse import mouse_click, mouse_long_click

SCRIPT_NAME = 'Motherlode_Miner_v2'

CURR_SPOT = None


def start_motherlode_mining(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop - CURR_SPOT: {CURR_SPOT}')

    else:
        print(f'First loop - CURR_SPOT: {CURR_SPOT}')
        setup_interface('west', 2, 'up')

    return True


# METHODS
def is_mining():
    curr_spot_wheel_xy = 745, 390
    curr_spot_wheel_region = get_region_for_xy(curr_spot_wheel_xy)
    dark_yellow_check = 80, 65, 14

    if does_color_exist_in_sub_image(region_coords=curr_spot_wheel_region, color=dark_yellow_check, img_name='Motherlode_Yellow_Check',color_tolerance=5, count_min=5):
        print(f'Found dark yellow')
    else:
        print(f'Failed to find dark yellow')
    return


def mine_next_spot(curr_spot):
    # Based on current spot - gets list of all other spot coords to check if they're available to mine
    return


def set_curr_spot(new_spot):
    global CURR_SPOT
    print(f'Setting CURR_SPOT: {CURR_SPOT}\nTo new_spot: {new_spot}')
    CURR_SPOT = new_spot
    return


# HELPERS
def get_region_for_xy(xy_coords):
    x, y = xy_coords
    top_left = x-5, y-5
    bottom_right = x+5, y+5
    region = top_left, bottom_right
    return region


class SpotCoords:
    def __init__(self, spot_1_xy_from_curr, spot_2_xy_from_curr, spot_3_xy_from_curr, spot_4_xy_from_curr):
        self.spot_1_xy = spot_1_xy_from_curr
        self.spot_2_xy = spot_2_xy_from_curr
        self.spot_3_xy = spot_3_xy_from_curr
        self.spot_4_xy = spot_4_xy_from_curr


# Spot 1 from 1
s1f1 = 743, 392
s2f1 = 753, 392

s3f1 = 938, 150
s4f1 = 900, 150
s5f1 = 860, 150

# s6f1 = 938, 150
# s7f1 = 900, 150
# s8f1 = 860, 150


spot_1 = SpotCoords(s1f1, s2f1, s3f1, s4f1)
