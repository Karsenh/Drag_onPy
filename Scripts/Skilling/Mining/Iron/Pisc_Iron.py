from API.Interface import *
from datetime import datetime

exit_prog = False


# Start character on the tile between three iron ore in Piscatoris
def mine_iron_pisc(DEBUG=True):
    global exit_prog

    first_loop = True
    exit_prog = False
    keyboard.add_hotkey('esc', lambda: quit_script())

    if first_loop:
        check_one_tap_drop_enabled(should_enable=True)
        turn_compass("south")
        zoom_camera(5)
        pitch_camera("up")

        time.sleep(1.5)

        ores_clicked = 0

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
            ore_x = [525, 717, 890]
            ore_y = [450, 306, 484]
            ore_sel = random.randint(0, 2)

        print(f'Ore # selected: {ore_sel}')

        sel_ore_xy = ore_x[ore_sel], ore_y[ore_sel]

        # Increment the ore_sel for next loop
        mine_iron_at(sel_ore_xy)

        ore_sel += 1
        ores_clicked += 1

        if DEBUG:
            print(f'Ores Clicked post-increment: {ores_clicked}')
            print(f'Ore # selected post-increment: {ore_sel}')
        # If ore_sel is now 4 though, we need to start back at 1 since there are only 3 ores
        if ore_sel == 3:
            ore_sel = 0
            if DEBUG:
                print(f'Since ore_sel == 4, resetting to 1 ({ore_sel})')

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

    if exit_prog:
        pwd = os.getcwd()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'⛔ Script Stopping @ [{current_time}]: User executed termination.')
        with open (f'{pwd}\Misc\Stop_Log.txt', 'w') as f:
            f.write(f'{current_time}:  User executed termination after {ores_clicked} ores clicked.')

    return


# set hotkey
def quit_script():
    global exit_prog
    exit_prog = True
    return


def mine_iron_at(xy):
    is_inventory_full(should_cont=True, should_drop=True)
    mouse_click(xy, 16, 23, click_direction="left", max_num_clicks=3)
    # mouse_move(x, y, 17, 23)
    # sleep_between(0.4, 0.88)
    # ag.leftClick()
    sleep_between(1.5, 1.7)
    return



