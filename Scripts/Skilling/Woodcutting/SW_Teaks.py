import random

import API.AntiBan
from API.Imaging.Image import wait_for_img, does_img_exist, get_existing_img_xy, get_color_at_coords
from API.Interface.General import setup_interface, is_tab_open, is_otd_enabled, drop_inventory
from API.Mouse import mouse_click

SCRIPT_NAME = "SW_Teaks"

TEAK_THRESH = 0.9
IS_CHOPPING = False
FIND_TEAK_ATTEMPTS = 0
CURR_TEAK_DIR = None


def start_chopping_sw_teaks(curr_loop):
    global IS_CHOPPING

    if curr_loop != 1:
        print(f'Not the first loop - not chopping so checking if inventory full and chopping again')

        if is_invent_full():
            IS_CHOPPING = False
            drop_teaks()
            chop_available_teak()

        spec_if_available()

        if not curr_tree_standing():
            print(f'{CURR_TEAK_DIR}_Teak img (should be cutting this one) - not found')
            IS_CHOPPING = False
            if CURR_TEAK_DIR == "Left":
                opposite_dir = 1
            else:
                opposite_dir = 0

            chop_available_teak(direction=opposite_dir)

        if not is_chopping():
            IS_CHOPPING = False

            if is_invent_full():
                drop_teaks()

            return try_teaks_until_fail()

        return True

    else:
        print(f'First loop!')
        setup_interface('west', 4, 'up')

        if is_invent_full():
            drop_teaks()

        return try_teaks_until_fail()


def try_teaks_until_fail():
    global IS_CHOPPING
    global FIND_TEAK_ATTEMPTS

    while not IS_CHOPPING:
        print(f'Attempting to find teak to chop...')
        IS_CHOPPING = chop_available_teak()
        if IS_CHOPPING:
            FIND_TEAK_ATTEMPTS = 0
            return True
        else:
            FIND_TEAK_ATTEMPTS += 1
        print(f'FIND_TEAK_ATTEMPTS = {FIND_TEAK_ATTEMPTS}')
        if FIND_TEAK_ATTEMPTS > 20:
            print(f'⛔ FIND_TEAK_ATTEMPTS exceeded = {FIND_TEAK_ATTEMPTS}')
            return False


def chop_available_teak(direction=""):
    global CURR_TEAK_DIR
    tree_directions = ["Left", "Right"]

    # If tree direction to check/click is not specified - randomize
    if not direction:
        r_idx = random.randint(0, 1)
    else:
        r_idx = direction

    # Provide appropriate xy offsets based on tree
    if r_idx == 0:
        x_offset = 30
        y_offset = 175
    else:
        x_offset = -10
        y_offset = 190

    if does_img_exist(img_name=f"{tree_directions[r_idx]}_Teak", script_name="SW_Teaks", threshold=0.9):
        left_x, left_y = get_existing_img_xy()
        adjusted_xy = left_x + x_offset, left_y + y_offset
        mouse_click(adjusted_xy)
        CURR_TEAK_DIR = tree_directions[r_idx]
        print(f'Setting CURR_TEAK = {tree_directions[r_idx]}')
        return True

    print(f"⛔ Didn't find any teaks to chop for {tree_directions[r_idx]}_Teak")
    return False


def is_chopping():
    return wait_for_img(img_name="Woodcutting", category="Exp_Drops", max_wait_sec=3)


def is_invent_full():
    teak_color_xy = 1354, 788
    color_code = [177, 146, 92]

    diff_tolerance = 15
    teak_color = get_color_at_coords(teak_color_xy)

    is_tab_open("inventory", True)

    print(f'Teak Color: {teak_color}\nColor_code comparison: {color_code}')

    i = 0
    for val in teak_color:
        curr_diff = val - color_code[i]
        print(f'Val: {val} | Curr_diff: {curr_diff} | (is gt) Tolerance: {diff_tolerance} ?')
        if curr_diff < 0:
            curr_diff = curr_diff * -1
            print(f'Curr_diff was neg: {curr_diff}')
        if curr_diff > diff_tolerance:
            print(f'Returning False')
            return False
        i += 1

    return True


def drop_teaks():
    is_otd_enabled(should_enable=True)
    is_tab_open("inventory", True)
    drop_inventory(from_spot_num=1, to_spot_num=28)
    is_otd_enabled(should_enable=False)
    return


def spec_if_available():
    spec_avail_color = 30, 144, 172

    color_xy = 1242, 273
    curr_color_at_full_spec = get_color_at_coords(color_xy)

    if curr_color_at_full_spec < spec_avail_color:
        print(f'Not enough Spec!')
        return False
    else:
        print(f'We have spec!')
        spec_xy = 1243, 292
        mouse_click(spec_xy)
        return True


def curr_tree_standing():
    global CURR_TEAK_DIR

    return does_img_exist(img_name=f'{CURR_TEAK_DIR}_Teak', script_name=SCRIPT_NAME, threshold=TEAK_THRESH)