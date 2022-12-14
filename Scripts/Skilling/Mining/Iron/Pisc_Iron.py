import os
import random
import API
from datetime import datetime
from API.Interface.General import is_otd_enabled, setup_interface
from API.AntiBan import sleep_between
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist

from API.Debug import write_debug

ores_clicked = 0
ore_sel = 0
no_ore_found = 0


# Start character on the tile between three iron ore in Piscatoris
def mine_iron_pisc(curr_loop):
    global ores_clicked
    global ore_sel
    global no_ore_found

    ore_x = [525, 717, 890]
    ore_y = [450, 306, 484]

    if curr_loop == 1:
        is_otd_enabled(should_enable=True)
        setup_interface("south", 5, "up")
        API.AntiBan.sleep_between(0.8, 1.4)

    if does_img_exist("Spot_check", script_name="Pisc_Iron", threshold=0.90):
        print(f'Ores clicked: {ores_clicked}')
        # On the first loop, randomly select an ore (of the three)
        if ores_clicked == 0:
            ore_sel = random.randint(0, 2)

        write_debug(f'Ore_sel = {ore_sel}\nsel_ore_xy = {ore_x[ore_sel]}, {ore_y[ore_sel]}')

        if not does_img_exist(img_name=f"Iron_{ore_sel}", script_name="Pisc_Iron", threshold=0.90, should_click=True, x_offset=15, y_offset=15):
            no_ore_found += 1

        if no_ore_found > 10:
            return API.AntiBan.shutdown("Pisc_Iron", "Couldn't find ore more than 10 times.")

        ore_sel += 1
        ores_clicked += 1

        write_debug(f'Ores Clicked post-increment: {ores_clicked}\nOre # selected post-increment: {ore_sel}')

        # If ore_sel is now 4 though, we need to start back at 1 since there are only 3 ores
        if ore_sel == 3:
            ore_sel = 0
            write_debug(f'Since ore_sel == 4, resetting to 1 ({ore_sel})')

    if not does_img_exist("Spot_check", script_name="Pisc_Iron", threshold=0.90):
        return API.AntiBan.shutdown("Pisc_Iron", "Couldn't find spot check img.")

    return True

