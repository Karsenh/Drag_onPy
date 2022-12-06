from API.Interface.General import setup_interface, is_tab_open
from API.Imaging.Image import does_img_exist, wait_for_img, get_existing_img_xy
from API.Mouse import mouse_click
from API.Debug import write_debug


no_cows_found = 0


def start_killing_cows(curr_loop):
    global no_cows_found

    if curr_loop == 1:
        setup_interface("south", 2, "up")

    is_tab_open("inventory", should_open=False)

    if not wait_for_img(img_to_search="hp_exp", script_name="Cow_Killer", max_wait_sec=6, img_threshold=0.8):
        for i in range(1, 56):
            if does_img_exist(img_name='c30', script_name='Cow_Killer', x_offset=15, y_offset=30, should_click=True) or does_img_exist(img_name=f"c{i}", script_name="Cow_Killer", threshold=0.76, should_click=True):
                break
        # wait_for_img(img_to_search="c30", script_name="Cow_Killer", max_wait_sec=6, img_threshold=0.8)
        # does_img_exist(img_name='c30', script_name='Cow_Killer', x_offset=15, y_offset=30, should_click=True)
    # if no_cows_found > 10:
    #     write_debug("Couldn't find cow image 10 times. Exiting...")
    #     return False

    return True



