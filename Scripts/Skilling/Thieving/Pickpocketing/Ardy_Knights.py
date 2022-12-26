from API.Interface.General import setup_interface
from API.Imaging.Image import does_img_exist, wait_for_img

selected_food = 'monkfish'
curr_tile = None
pickpocket_count = 0


def start_pickpocketing_ardy_knights(curr_loop):
    if curr_loop == 1:
        setup_interface("west", 4, "up")
        # Check/set what tile we're on - thieving_tile or bank_tile

        # Check if we have food in inventory
            # If no invent food - click to open bank based on what tile we're on
                #
                # Check if we're in food tab - open if not
                # Check if withdraw 10 is selected - select if not
                # Withdraw the bank_<selected_food> (click twice for 20)
            # If we have invent food - continue

        # Move to thieving tile based on the tile we're currently on

    # Check curr_health_gt(percent=10)
        # If gt 10% - Thieve
        # If lt 10% - Click inventory food
            # If no inventory food - open bank from curr_tile
            # Check if fish tab open - open if not
            #

    # Thieve()
        # Check if coinpouch == 28
        # If == 28 - Click coinpouch to open
        # Else click ardy_knight_pickpocket_xy

    # open_bank_from_curr_tile()
        #
    return True


def set_curr_tile():

    return


