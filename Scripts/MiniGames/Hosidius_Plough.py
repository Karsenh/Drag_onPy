import API
from API.Imaging.Image import wait_for_img
from API.Mouse import mouse_click
from API.Interface.General import setup_interface, is_tab_open


def start_ploughing_for_favour(curr_loop):
    if curr_loop == 1:
        setup_interface("north", 4, "up")

    API.AntiBan.sleep_between(1.3, 1.5)

    is_tab_open("inventory", should_open=False)

    if curr_loop % 2 == 0:
        plough_west()
    else:
        plough_east()

    return True


def plough_east():
    while not wait_for_img(img_to_search="East_end", script_name="Hosidius_Plough", max_wait_sec=30,
                           img_threshold=0.99):
        repair_east_xy = 1040, 472
        mouse_click(repair_east_xy, max_num_clicks=2)
        API.AntiBan.sleep_between(3.0, 3.1)
        mouse_click(repair_east_xy, max_num_clicks=1)

    east_start_xy = 1215, 490
    mouse_click(east_start_xy)
    API.AntiBan.sleep_between(5.0, 5.1)

    east_plow_xy = 472, 466
    mouse_click(east_plow_xy, max_num_clicks=3)
    return


def plough_west():
    while not wait_for_img(img_to_search="West_end", script_name="Hosidius_Plough", max_wait_sec=30,
                           img_threshold=0.99):
        repair_east_xy = 470, 470
        mouse_click(repair_east_xy, max_num_clicks=2)
        API.AntiBan.sleep_between(3.0, 3.1)
        mouse_click(repair_east_xy, max_num_clicks=1)

    west_start_xy = 230, 474
    mouse_click(west_start_xy)
    API.AntiBan.sleep_between(5.0, 5.1)

    west_plow_xy = 1012, 469
    mouse_click(west_plow_xy)
    return