import os
import random
import API
from datetime import datetime
from API.AntiBan import sleep_between
from API.Mouse import mouse_click
from API.Imaging.Image import does_img_exist
from API.Interface.General import drop_inventory
from API.Debug import write_debug

SCRIPT_NAME = 'Pisc_Iron_Miner'

ORES_CLICKED = 0
ORE_SEL = 0
TOTAL_ORES_MINED = 0

# TODO: Refine this script to drop ore between ore clicks to be more efficient


# Start character on the tile between three iron ore in Piscatoris
def mine_pisc_iron(curr_loop):
    global ORES_CLICKED
    global ORE_SEL
    global TOTAL_ORES_MINED

    if curr_loop == 1:
        API.Interface.General.is_otd_enabled(should_enable=True)
        API.Interface.General.setup_interface("south", 5, "up")
        API.AntiBan.sleep_between(0.8, 1.4)

    handle_full_inventory()

    write_debug(f'💎 Total ores mined so far: {TOTAL_ORES_MINED}')

    if does_img_exist("Spot_check", script_name=SCRIPT_NAME, threshold=0.90):
        print(f'Ores clicked: {ORES_CLICKED}')

        # On the first loop, randomly select an ore (of the three)
        if ORES_CLICKED == 0:
            ORE_SEL = random.randint(1, 3)

        does_img_exist(img_name=f"Iron_{ORE_SEL}", script_name=SCRIPT_NAME, threshold=0.90, should_click=True, x_offset=15, y_offset=15)

        ORE_SEL += 1
        ORES_CLICKED += 1

        write_debug(f'Ores Clicked post-increment: {ORES_CLICKED}\nOre # selected post-increment: {ORE_SEL}')

        # If ore_sel is now 4 though, we need to start back at 1 since there are only 3 ores
        if ORE_SEL == 4:
            ORE_SEL = 1
            write_debug(f'Since ore_sel == 4, resetting to 1 ({ORE_SEL})')

    if not does_img_exist("Spot_check", script_name=SCRIPT_NAME, threshold=0.90):
        return API.AntiBan.shutdown(SCRIPT_NAME, "Couldn't find spot check img.")

    return True


def handle_full_inventory():
    global TOTAL_ORES_MINED
    if does_img_exist(img_name="inventory_full", category="General", threshold=0.85):
        drop_inventory(from_spot_num=1, to_spot_num=27)
        TOTAL_ORES_MINED += 27

    return
