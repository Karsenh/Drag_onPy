import random
import datetime
import API.AntiBan
import pyautogui as pag
from API.AntiBan import shutdown
from API.Interface.General import setup_interface, is_tab_open
from API.Interface.Bank import is_withdraw_qty, close_bank, is_bank_tab_open, deposit_all, open_ge_bank, \
    withdraw_item_from_tab_num
from API.Imaging.Image import does_img_exist, get_existing_img_xy, wait_for_img
from API.Mouse import mouse_click, mouse_long_click
from API.Interface.General import get_xy_for_invent_slot

SCRIPT_NAME = 'GE_Finished_Pots'

BANK_TAB_NUM = 1

PRIMARY_INGREDIENT = 'snapdragon_potion_unf_3'
SECONDARY_INGREDIENT = 'red_spider_eggs'


def start_making_finished_potions(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        open_ge_bank()
        deposit_all()
        if not withdraw_item_from_tab_num(item=PRIMARY_INGREDIENT, qty='x', tab_num=BANK_TAB_NUM):
            return False
        if not withdraw_item_from_tab_num(item=SECONDARY_INGREDIENT, qty='x', tab_num=BANK_TAB_NUM):
            return False
        close_bank()
        make_inventory()
        API.AntiBan.sleep_between(15, 17)
    else:
        print(f'First loop')
        setup_interface('east', 5, 'up')

    return True


# -------
# METHODS
# -------
def make_inventory():
    r_primary_slot = get_xy_for_invent_slot(random.randint(1, 14))
    r_secondary_slot = get_xy_for_invent_slot(random.randint(15, 28))
    mouse_click(r_primary_slot)
    mouse_click(r_secondary_slot)
    wait_for_img(img_name='crafting_menu_is_open', script_name=SCRIPT_NAME, threshold=0.9)
    pag.press('space')
    return True

# -------
# HELPERS
# -------

