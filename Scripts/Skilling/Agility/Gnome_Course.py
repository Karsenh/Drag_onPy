import random
import time

from API.Interface import *

first_loop = True
run_sleep_times = [5, 10, 4, 2, 8, 3, 5, 9]
walk_sleep_times = [5, 14, 4, 2, 8, 4, 7, 9]

obstacle_xys = [[743, 496], [160, 540], [723, 620], [745, 485], [972, 466], [893, 492], [767, 202], [754, 291]]

second_loop_start_spot_color = 76, 61, 30
second_loop_start_spot_xy = 724, 735

i = 0


def run_gnome_course():
    global first_loop
    global i

    # Define two sleep time lists; run_sleep_seconds & walk_sleep_seconds
    # Zoom - 2
    # Turn - North
    # Camera - Up
    if first_loop:
        zoom_camera(notches=2)
        turn_compass(direction="north")
        pitch_camera(direction="up")

        first_loop = False
        if is_pipe_start():
            i = 1
            print(f'Starting at pipe with i = {i}')
        elif does_color_exist(second_loop_start_spot_color, second_loop_start_spot_xy):
            i = 2
            print(f"We're entering the course from the second obstacle... i = {i}")
        else:
            i = 0
            print(f'Starting in front of log i = {i}')

    print(f'♾ ITERATION: {i} - Clicking xy: {obstacle_xys[i]}')
    if i == 1:
        if not does_img_exist("pipe_start", script_name="Gnome_Course"):
            print(f"⛔ We should be in front of the pipe but it appears we're not...")
            exit(-1)

    if is_run_gt(percent=10):
        if is_run_on():
            sleep_times = run_sleep_times
        else:
            run_xy = 1210, 255
            mouse_click(run_xy)
            sleep_times = run_sleep_times
    else:
        sleep_times = walk_sleep_times

    mouse_click(obstacle_xys[i], max_num_clicks=2)

    print(f'Sleeping for {sleep_times[i]} seconds...')
    # r_sleep_dev = random.uniform(1.0, 3.4)
    # sleep_between(sleep_times[i], sleep_times[i]+r_sleep_dev)
    time.sleep(sleep_times[i])

    if i == 0:
        i = 1

    i += 1
    if i == 8:
        i = 1

    return


def is_pipe_start():
    if does_img_exist("pipe_start", script_name="Gnome_Course"):
        return True
    else:
        return False
