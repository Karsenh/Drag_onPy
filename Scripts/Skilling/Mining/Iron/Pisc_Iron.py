import os
import random
import API
from datetime import datetime
from API.AntiBan import sleep_between
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist
from API.Interface.General import drop_inventory

from API.Debug import write_debug

ores_clicked = 0
ore_sel = 0
total_ores_mined = 0


# Start character on the tile between three iron ore in Piscatoris
def mine_iron_pisc(curr_loop):
    global ores_clicked
    global ore_sel
    global total_ores_mined

    if curr_loop == 1:
        API.Interface.Generalis_otd_enabled(should_enable=True)
        API.Interface.Generalsetup_interface("south", 5, "up")
        API.AntiBan.sleep_between(0.8, 1.4)

    handle_full_inventory()

    write_debug(f'💎 Total ores mined so far: {total_ores_mined}')

    if does_img_exist("Spot_check", script_name="Pisc_Iron", threshold=0.90):
        print(f'Ores clicked: {ores_clicked}')

        # On the first loop, randomly select an ore (of the three)
        if ores_clicked == 0:
            ore_sel = random.randint(1, 3)

        does_img_exist(img_name=f"Iron_{ore_sel}", script_name="Pisc_Iron", threshold=0.90, should_click=True, x_offset=15, y_offset=15)

        ore_sel += 1
        ores_clicked += 1

        write_debug(f'Ores Clicked post-increment: {ores_clicked}\nOre # selected post-increment: {ore_sel}')

        # If ore_sel is now 4 though, we need to start back at 1 since there are only 3 ores
        if ore_sel == 4:
            ore_sel = 1
            write_debug(f'Since ore_sel == 4, resetting to 1 ({ore_sel})')

    if not does_img_exist("Spot_check", script_name="Pisc_Iron", threshold=0.90):
        return API.AntiBan.shutdown("Pisc_Iron", "Couldn't find spot check img.")

    return True


def handle_full_inventory():
    global total_ores_mined
    if does_img_exist(img_name="inventory_full", category="General", threshold=0.85):
        drop_inventory(from_spot_num=1, to_spot_num=27)
        total_ores_mined += 27

    return
