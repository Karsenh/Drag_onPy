from API.Imaging.Image import wait_for_img
from API.Interface.General import setup_interface
from GUI.Imports.PreLaunch_Gui.Plg_Script_Options import Global_Script_Options

SHOULD_ALCH = None
SCRIPT_NAME = 'Gnome_Course'
CURR_JUMP_NUM = 0

def start_gnome_course(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')

        # Loop through jumps
        handle_jump_num(CURR_JUMP_NUM)

        if SHOULD_ALCH is not None or 'none':
            print(f'SHOULD_ALCH: {SHOULD_ALCH}')

    else:
        print(f'First loop')
        if is_on_start_tile():
            setup_interface("north", 2, "up")
            get_script_options()
    return True


#########
# METHODS
#########
def get_script_options():
    global SHOULD_ALCH

    for option in Global_Script_Options.options_arr:
        print(f'option: {option}')
        print(f'option.name: {option.name}')
        if option.name == 'High Alch':
            print(f'Found Food Type option - Setting to: {option.value}')
            SHOULD_ALCH = option.value
    return


def wait_for_agility_exp():
    return wait_for_img(img_name='Agility', category='Exp_Drops')


def handle_jump_num(curr_jump_num):
    print(f'Handling Curr_Jump_Num: {curr_jump_num}')

    wait_for_img(img_name=f'obst_{curr_jump_num}', script_name=SCRIPT_NAME, threshold=0.85, should_click=True, click_middle=True)
    return True


#########
# HELPERS
#########
def is_on_start_tile():
    return wait_for_img(img_name='obst_0', script_name=SCRIPT_NAME, should_click=True, click_middle=True)