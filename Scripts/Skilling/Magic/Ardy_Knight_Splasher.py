from API.Imaging.Image import wait_for_img
from API.Interface.General import handle_level_dialogue, setup_interface


NUM_TIMES_FAILED = 0


def start_splashing_ardy_knight(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        handle_level_dialogue()

        if not wait_for_img(img_name='Magic', category='Exp_Drops', threshold=0.7, max_wait_sec=15):
            print(f'⛔ Failed to find Magic Exp: {get_num_times_failed()}/3')
            inc_num_times_failed()
            if get_num_times_failed() > 4:
                return False
        else:
            reset_num_times_failed()

    else:
        print(f'First loop')
        setup_interface('north', 2, 'up')
    return True


def inc_num_times_failed():
    global NUM_TIMES_FAILED
    NUM_TIMES_FAILED += 1
    return


def reset_num_times_failed():
    global NUM_TIMES_FAILED
    NUM_TIMES_FAILED = 0
    return

def get_num_times_failed():
    return NUM_TIMES_FAILED

