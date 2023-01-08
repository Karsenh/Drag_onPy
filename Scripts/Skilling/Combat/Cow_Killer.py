import API.AntiBan
from API.Setup import get_bluestacks_region, translate_coords, get_bluestacks_window_size
from API.Interface.General import setup_interface, is_tab_open, turn_compass
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy, does_color_exist, get_color_at_coords
from API.Mouse import mouse_click
from API.Debug import write_debug


no_cows_found = 00
curr_dir = "south"

TOTAL_NUM_COW_IMGS = 19


def start_killing_cows(curr_loop):
    global no_cows_found
    global curr_dir

    if curr_loop == 1:
        setup_interface("south", 2, "up")

    is_tab_open("inventory", should_be_open=False)

    minx_x, min_y, max_x, max_y = get_bluestacks_region()
    w, h = get_bluestacks_window_size()
    max_xy = w, h

    coords = 115, 133
    dead_red_col = 200, 0, 0
    alive_green_col = 0, 200, 0

    i = 1

    if get_color_at_coords(coords) != dead_red_col and get_color_at_coords(coords) != alive_green_col:
        seen = False
        # Range has to be one more than we want to iterate over
        while not seen:
            if does_img_exist(img_name='moo', script_name='Cow_Killer'):
                seen = True
                moo_x, moo_y = get_existing_img_xy()
                adjusted_xy = moo_x + 16, moo_y + 31

                print(f'max_xy = {max_xy}\n adjusted_moo_xy = {adjusted_xy}\nis adjusted lt ? {adjusted_xy < max_xy}')

                if adjusted_xy < max_xy:
                    mouse_click(adjusted_xy)
                    API.AntiBan.sleep_between(3.1, 3.5)
                else:
                    print(f'⛔ Cow click off window frame - skipping!')

                break
            if does_img_exist(img_name=f"c{i}", script_name="Cow_Killer", threshold=0.80, should_click=True):
                print(f'Found Cow image')
                API.AntiBan.sleep_between(3.1, 3.5)
                break

            i += 1
            if i == TOTAL_NUM_COW_IMGS + 1:
                i = 1

    if curr_loop % 21 == 0:
        if curr_dir == "south":
            dir = "north"
            setup_interface(dir, 2, "up")
            curr_dir = dir
        else:
            dir = "south"
            setup_interface(dir, 2, "up")
            curr_dir = dir

    return True
