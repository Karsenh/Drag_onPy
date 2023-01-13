from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from GUI.Imports.Script_Launch import launch_script
from Scripts.Skilling.Runecrafting.Cwars_Lavas import set_equipped_items, set_inventory_items, fill_pouches, \
    withdraw_ess, empty_pouches, teleport_to_duel_arena, craft_lavas, move_to_ruins, move_to_altar, cast_imbue, \
    teleport_to_cwars
import sys
from pynput import keyboard


def terminate_app(key):
    try:
        print(f'Key {key} pressed')

        if str(key) == "Key.end":
            write_debug("☠ Script Terminated by User")
            sys.exit(-1)
    except AttributeError:
        print(f'special key {key} pressed')


def __main__():

    listener = keyboard.Listener(
        on_press=terminate_app)
    listener.start()

    get_bluestacks_xy()
    set_bluestacks_window_size()
    capture_bluestacks()
    clear_debug_log()

    # show_main_gui()

    launch_script("Cwars_Lavas")

    # wait_for_img(img_name="Claim_Sack", script_name="Motherlode_Miner", threshold=0.90, should_click=True, click_middle=True)

    # does_img_exist(img_name="Minimap_Midway_From_Box_Alt", script_name="Motherlode_Miner", threshold=0.95, should_click=True, x_offset=-1)
    # does_img_exist(img_name="Minimap_Midway_From_Box", script_name="Motherlode_Miner", threshold=0.9, should_click=True, y_offset=4)
    # is_tab_open("inventory", False)
    # does_img_exist(img_name="Back_to_Spot_1", script_name="Motherlode_Miner", threshold=0.95, should_click=True, click_middle=True)

    # MOTHERLODE MINER
    # does_img_exist(img_name="Minimap_Midway", script_name="Motherlode_Miner", threshold=0.9, should_click=True)
    # does_img_exist(img_name="Midway_Rock_From_Ore", script_name="Motherlode_Miner", threshold=0.9, should_click=True)

    # Wait for Mining exp drop as confirmation obstacle was cleared
    # wait_for_img(img_name="Mining", category="Exp_Drops", threshold=0.90, max_wait_sec=10)
    # does_img_exist(img_name="Minimap_Sluice", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True)
    # is_tab_open("inventory", False)
    # wait_for_img(img_name="Running_Water", script_name="Motherlode_Miner", threshold=0.5, should_click=True, click_middle=True)

    # does_img_exist(img_name="Broken_Wheel_2_From_1", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True)
    # wait_for_img(img_name="Smithing", category="Exp_Drops", threshold=0.9)

    # does_img_exist(img_name="Broken_Wheel_2", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True)
    # wait_for_img(img_name="Smithing", category="Exp_Drops", threshold=0.9)
    #
    # does_img_exist(img_name="Broken_Wheel_2_From_1", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True)
    # API.AntiBan.sleep_between(1.0, 1.1)
    # wait_for_img(img_name="Smithing", category="Exp_Drops", threshold=0.9)
    #
    # wait_for_img(img_name="Hopper_From_Wheel_2", script_name="Motherlode_Miner", threshold=0.95, should_click=True, click_middle=True)
    # wait_for_img(img_name="Claim_Sack", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True)
    # wait_for_img(img_name="Claimed_Ore", script_name="Motherlode_Miner", threshold=0.98)
    # minimap_deposit_box = 1368, 237
    # mouse_click(minimap_deposit_box)
    # wait_for_img(img_name="Deposit_Box", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True)
    # wait_for_img(img_name="Inventory_Btn", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True)
    # wait_for_img(img_name="Hammer_Box", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True)

    # Something here to move to midway rock
    # wait_for_img(img_name="Back_to_Midway", script_name="Motherlode_Miner", threshold=0.9, should_click=True)

    # wait_for_img(img_name="Midway_Rock_From_Sluice", script_name="Motherlode_Miner", threshold=0.9, should_click=True, click_middle=True)
    #
    # back_to_spot_1 = 753, 206
    # mouse_click(back_to_spot_1)
    # spot = "Corner"
    # does_img_exist(img_name=f"Hopper_From_{spot}", script_name="Motherlode_Miner", threshold=0.95, should_click=True,
    #                click_middle=True)
    # wait_for_img(img_name="Claim_Sack", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True)

    # wait_for_img(img_name="Minimap_Midway_From_Box", script_name="Motherlode_Miner", threshold=0.95, should_click=True, y_offset=3)
    # wait_for_img(img_name="Midway_Rock_From_Box", script_name="Motherlode_Miner", threshold=0.95, should_click=True, y_offset=3)


    # CURR_SPOT = 9
    #
    # does_img_exist(img_name=f"Spot_{CURR_SPOT+1}_From_{CURR_SPOT}", script_name="Motherlode_Miner", threshold=0.98, should_click=True, click_middle=True)
    #
    # wait_for_img(img_name="Mining", category="Exp_Drops", threshold=0.92, max_wait_sec=10)


    return


__main__()


