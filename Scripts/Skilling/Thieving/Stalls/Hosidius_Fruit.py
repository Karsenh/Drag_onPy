from API.Interface.General import setup_interface, is_tab_open, is_run_gt, is_run_on
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist, wait_for_img
import API


def start_stealing_fruit(curr_loop):
    if curr_loop == 1:
        setup_interface("west", 2, "up")

    is_tab_open(tab="inventory", should_be_open=False)

    steal_from_fruit_stall()

    bank_fruit()

    return True


def steal_from_fruit_stall():
    west_fruit_stall_xy = 752, 406
    # While our inventory is not full...
    while not does_img_exist(img_name="inventory_full", category="General"):
        # If the fruit-stall is empty (someone is there - be competitive)
        if does_img_exist(img_name="west_fruit_empty", script_name="Hosidius_Fruit", threshold=0.85):
            API.AntiBan.sleep_between(0.3, 0.4)
            mouse_click(west_fruit_stall_xy, max_num_clicks=10, min_num_clicks=5, max_int_delay=0.15)
        does_img_exist(img_name="west_fruit", script_name="Hosidius_Fruit", threshold=0.85, should_click=True, x_offset=30, y_offset=20)

    return


def bank_fruit():
    if is_run_gt(percent=10):
        is_run_on(should_click=True)
        sleep1 = 1.4, 1.5
    else:
        sleep1 = 4.0, 4.1

    a, b = sleep1

    if does_img_exist(img_name="closed_door", script_name="Hosidius_Fruit", threshold=0.80, should_click=True):
        bank_last_xy = 746, 93
    else:
        bank_last_xy = 717, 148

    API.AntiBan.sleep_between(a, b)

    if is_run_gt(percent=10):
        sleep2 = 10.1, 10.2
    else:
        sleep2 = 25.0, 25.1

    a, b = sleep2

    bank_1_xy = 1282, 66
    mouse_click(bank_1_xy, max_x_dev=0, max_y_dev=0)
    API.AntiBan.sleep_between(a, b)

    if is_run_gt(percent=10):
        sleep3 = 9.1, 9.2
    else:
        sleep3 = 26.0, 26.1

    a, b = sleep3

    bank_2_xy = 1336, 52
    mouse_click(bank_2_xy, max_x_dev=0, max_y_dev=0)
    API.AntiBan.sleep_between(a, b)

    if is_run_gt(percent=10):
        sleep4 = 2.1, 2.2
    else:
        sleep4 = 7.0, 7.1

    a, b = sleep4

    mouse_click(bank_last_xy, max_x_dev=0, max_y_dev=0)
    API.AntiBan.sleep_between(a, b)

    if not wait_for_img(img_name="deposit_inventory", script_name="Hosidius_Fruit", threshold=0.85, max_wait_sec=6):
        print(f'Cant find deposit inventory button - Checking if we clicked the cier...')
        if does_img_exist(img_name="clicked_crier", script_name="Hosidius_Fruit", threshold=0.80):
            # If we accidentally clicked the crier - click the new deposit box xy
            deposit_box_xy = 745, 347
            mouse_click(deposit_box_xy, max_num_clicks=2)
            does_img_exist(img_name="deposit_inventory", script_name="Hosidius_Fruit", threshold=0.85,
                           should_click=True, x_offset=25, y_offset=25)
    else:
        does_img_exist(img_name="deposit_inventory", script_name="Hosidius_Fruit", threshold=0.85, should_click=True, x_offset=25, y_offset=25)

    API.AntiBan.sleep_between(1.0, 1.1)

    # Make our way back to the fruit stall
    if is_run_gt(percent=10):
        sleep5 = 6.1, 6.2
    else:
        sleep5 = 22.0, 22.1

    a, b = sleep5

    fruit_1_xy = 1355, 289
    mouse_click(fruit_1_xy, max_x_dev=0, max_y_dev=0)
    API.AntiBan.sleep_between(a, b)

    fruit_2_xy = 1329, 291
    mouse_click(fruit_2_xy)

    if is_run_gt(percent=10):
        sleep6 = 7.1, 7.2
    else:
        sleep6 = 21.0, 21.1

    a, b = sleep6

    API.AntiBan.sleep_between(a, b)

    fruit_last_xy = 1414, 233
    # 1415, 227
    mouse_click(fruit_last_xy, max_y_dev=0, max_x_dev=0)
    if is_run_gt(percent=10):
        sleep6 = 5.5, 5.6
    else:
        sleep6 = 18.0, 18.1

    a, b = sleep6

    API.AntiBan.sleep_between(a, b)

    if does_img_exist(img_name="closed_door_return", script_name="Hosidius_Fruit", threshold=0.8, should_click=True,
                      x_offset=2, y_offset=45):
        API.AntiBan.sleep_between(3.0, 3.1)
        fruit_stall_from_door_xy = 829, 374
        mouse_click(fruit_stall_from_door_xy)
        API.AntiBan.sleep_between(3.0, 3.1)

    return


