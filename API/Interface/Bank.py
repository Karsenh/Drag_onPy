from API.Imports.Coords import *
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist
from API.AntiBan import sleep_between, print_to_log


def deposit_all(include_equipment=False):
    # TODO: Check if bank is open - if not, check if we're in front of the bank (click if so) - if not - exit
    # If the bank is not open
    mouse_click(BANK_dep_inventory)
    sleep_between(0.5, 0.7)
    if include_equipment:
        mouse_click(BANK_dep_equipment)
    return



def check_if_bank_tab_open(tab_num=0, should_open=True, double_check=True):
    # If the bank tab IS open...
    if does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
        # return true
        return True
    # Else, the bank tab is NOT open...
    else:
        # If it's not open, but we SHOULD open it...
        if should_open:
            # Click that tab xy to open
            mouse_click(BANK_all_tab_xys[tab_num])
            # Check for tab again after clicking (if double check is true)
            if double_check:
                if not does_img_exist(f"tab_{tab_num}", category="Banking", threshold=0.9):
                    print(f"Couldn't find expected tab no. {tab_num} despite having tried to click... Exiting")
                    # Print this issue to log file
                    log_text = f"Couldn't find Bank Tab {tab_num} after trying to click it."
                    print_to_log(log_text)
                    exit(-1)
            #         It's now open
            return True
        # Still closed because should_open is false
        return False