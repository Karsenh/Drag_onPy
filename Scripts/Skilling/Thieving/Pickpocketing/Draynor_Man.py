from API.Imaging.Image import does_img_exist, get_existing_img_xy, wait_for_img
from API.Mouse import mouse_drag
from API.AntiBan import sleep_between
from API.Debug import write_debug
from API.Interface.General import setup_interface


def pickpocket_draynor_man(curr_loop):

    # if curr_loop == 1:
    #     setup_interface("east", 3, "up")

    check_coin_pouch()

    if not pickpocket():
        return False

    if check_if_caught():
        write_debug(f'We were caught pickpocketing! - Sleeping between 2.8 and 3.1 sec...')
        sleep_between(4.5, 4.7)

    return True


def pickpocket():
    if not does_img_exist(img_name="man", script_name="Draynor_Man", category="Scripts", threshold=0.65):
        if not does_img_exist(img_name="man_back", script_name="Draynor_Man", category="Scripts", threshold=0.65):
            if not does_img_exist(img_name="man_2", script_name="Draynor_Man", category="Scripts", threshold=0.65):
                if not does_img_exist(img_name="man_2_front", script_name="Draynor_Man", category="Scripts", threshold=0.65):
                    return False
                else:
                    xy = get_existing_img_xy()
                    x, y = xy
                    pickpocket_xy = x + 15, y + 110
                    mouse_drag(from_xy=xy, to_xy=pickpocket_xy)
            else:
                xy = get_existing_img_xy()
                x, y = xy
                pickpocket_xy = x + 15, y + 110
                mouse_drag(from_xy=xy, to_xy=pickpocket_xy)
        else:
            xy = get_existing_img_xy()
            x, y = xy
            pickpocket_xy = x+15, y + 110
            mouse_drag(from_xy=xy, to_xy=pickpocket_xy)
    else:
        xy = get_existing_img_xy()
        x, y = xy
        pickpocket_xy = x+50, y+110
        mouse_drag(from_xy=xy, to_xy=pickpocket_xy)

    return True


def check_coin_pouch():
    return does_img_exist(img_name="max_coins", script_name="Draynor_Man", category="Scripts", threshold=0.8, should_click=True)


def check_if_caught():
    return wait_for_img(img_to_search="caught", script_name="Draynor_Man", category_name="Scripts", max_wait_sec=2)

