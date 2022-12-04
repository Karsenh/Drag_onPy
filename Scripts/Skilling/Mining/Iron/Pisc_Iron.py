import os
import time
import random
import keyboard
import API
from datetime import datetime
from API.AntiBan import sleep_between
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist

from API.Debug import write_debug

ores_clicked = 0
ore_sel = 0


# Start character on the tile between three iron ore in Piscatoris
def mine_iron_pisc(curr_loop):
    global ores_clicked
    global ore_sel

    ore_x = [525, 717, 890]
    ore_y = [450, 306, 484]

    # keyboard.add_hotkey('esc', lambda: quit_script())

    if curr_loop == 1:
        API.Interface.General.is_otd_enabled(should_enable=True)
        API.Interface.General.setup_interface("south", 5, "up")
        API.AntiBan.sleep_between(0.8, 1.4)

    ore_1_xy = 1218, 181
    ore_2_xy = 1363, 291
    # ore_3_xy = 1368, 289
    ore_objs = ore_1_xy, ore_2_xy

    ore_1_color = 56, 90, 76
    ore_2_color = 116, 89, 57
    # ore_3_color = 90, 67, 37
    ore_colors = ore_1_color, ore_2_color

    if does_img_exist("spot_check", script_name="Pisc_Iron"):
        print(f'Ores clicked: {ores_clicked}')
        # On the first loop, randomly select an ore (of the three)
        if ores_clicked == 0:
            ore_sel = random.randint(0, 2)

        write_debug(f'Ore_sel = {ore_sel}\nsel_ore_xy = {ore_x[ore_sel]}, {ore_y[ore_sel]}')

        sel_ore_xy = ore_x[ore_sel], ore_y[ore_sel]

        # Increment the ore_sel for next loop
        mine_iron_at(sel_ore_xy)

        ore_sel += 1
        ores_clicked += 1

        write_debug(f'Ores Clicked post-increment: {ores_clicked}\nOre # selected post-increment: {ore_sel}')

        # If ore_sel is now 4 though, we need to start back at 1 since there are only 3 ores
        if ore_sel == 3:
            ore_sel = 0
            write_debug(f'Since ore_sel == 4, resetting to 1 ({ore_sel})')

    # If we're no longer standing on the right tile to mine, we'll drop out of the previous While loop and into this
    # (We will skip this if script is exited with hotkey)
    # if not is_on_right_tile(ore_objs, ore_colors):
    if not does_img_exist("spot_check", script_name="Pisc_Iron"):
        pwd = os.getcwd()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'⛔ Script Stopping @ [{current_time}]: - is_on_right_tile(obj, colors) failed after {ores_clicked} ores clicked.'
              f'Logging to Script_Stop_Log.txt')
        with open (f'{pwd}\Misc\Stop_Log.txt', 'w') as f:
            f.write(f'{current_time}: is_on_right_tile(obj, colors) failed after {ores_clicked} ores clicked.')
        return False

    return True


def mine_iron_at(xy):
    API.Interface.General.is_inventory_full(should_cont=True, should_drop=True)
    mouse_click(xy, 16, 23, click_direction="left", max_num_clicks=3)
    API.AntiBan.sleep_between(1.5, 1.7)
    return



