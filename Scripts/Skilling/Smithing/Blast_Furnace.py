import API.AntiBan
from API.Mouse import mouse_click, mouse_move, mouse_long_click
from API.Interface.General import setup_interface, is_otd_enabled, is_tab_open
from API.Imaging.Image import does_img_exist, wait_for_img, does_color_exist_in_thresh, does_color_exist_in_sub_image
import pyautogui as pag


def start_blasting(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
    else:
        print(f'First loop!')
        setup_interface('north', 1, 'up')

    return True


def deposit_money_into_coffer():
    return


# Start at bank chest
# Deposit 72k into coffer
# Withdraw coal bag & ice gloves / equip gloves and bank anything that was equipped
# Fill coal bag
# Withdraw coal
# Click belt to deposit
# Empty coal bag after depositing and deposit again
# Click bank from belt and wait for open
# Fill coal and withdraw adamant ore
# Click belt to deposit
# Empty bag and deposit again
# Click bank
# Start over from withdrawing coal