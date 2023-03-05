from API.Imaging.Image import wait_for_img
from API.Interface.General import handle_level_dialogue, setup_interface


def start_splashing_ardy_knight(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        handle_level_dialogue()

        if not wait_for_img(img_name='Magic', category='Exp_Drops', threshold=0.7):
            print(f'⛔ Failed to find Magic Exp')
            return False

    else:
        print(f'First loop')
        setup_interface('north', 2, 'up')
    return True
