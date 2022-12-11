from API.Interface.General import setup_interface
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist


def start_stealing_fruit(curr_loop):
    if curr_loop == 1:
        setup_interface("west", 1, "up")

    # Check if inventory is full
    #     - Run to bank - deposit - and run back if so

    # Click fruit stall 'x' times before looping into break

    return True


def click_fruit_stall():
    does_img_exist(img_name="")
    return
