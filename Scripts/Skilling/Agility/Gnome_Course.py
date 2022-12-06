from API.Interface.General import *


first_loop = True
run_sleep_times = [5.0, 10.0, 4.0, 3.0, 8.0, 3.0, 5.6, 9.0]
walk_sleep_times = [5.0, 14.0, 4.0, 3.0, 8.0, 4.0, 7.0, 9.0]

obstacle_xys = [[743, 496], [160, 540], [723, 620], [745, 485], [972, 466], [893, 492], [767, 202], [754, 291]]

second_loop_start_spot_color = 76, 61, 30
second_loop_start_spot_xy = 724, 735

i = 0


def run_gnome_course(_):
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
            print(f'🚽 PIPE START i = {i}')
        elif is_net_start():
            i = 2
            print(f"🥅 NET START... i = {i}")
        else:
            i = 0
            print(f'🪓 LOG START i = {i}')

    curr_msg = get_iteration_msg(i)

    print(f'♾ ITERATION: {i} - Clicking {curr_msg} @ xy: {obstacle_xys[i]}')

    if is_run_gt(percent=10):
        if is_run_on():
            sleep_times = run_sleep_times
        else:
            run_xy = 1210, 255
            mouse_click(run_xy)
            sleep_times = run_sleep_times
    else:
        sleep_times = walk_sleep_times

    check_for_level_dialogue()

    if i == 1:
        print(f'Checking if we are on the expected tile...')
        on_right_tile = is_pipe_start()
        if not on_right_tile:
            print(f'⛔ Not on pipe tile as we expect to be. Exiting...')
            return False
        else:
            print(f'✔ Still on course.')

    mouse_click(obstacle_xys[i], max_num_clicks=2)

    r_sleep_length = random.randint(1, 20)
    if r_sleep_length < 19:
        r_sleep_dev = random.uniform(0.1, 1.3)
    else:
        r_sleep_dev = random.uniform(0.1, 1.3)

    API.AntiBan.sleep_between(sleep_times[i], sleep_times[i]+r_sleep_dev)

    if i == 0:
        i = 1

    i += 1
    if i == 8:
        i = 1

    return True


def is_pipe_start():
    return does_img_exist(img_name="pipe_start", script_name="Gnome_Course")


def is_net_start():
    return does_img_exist(img_name="net_start", script_name="Gnome_Course")


def get_iteration_msg(curr_iteration):
    match curr_iteration:
        case 0:
            return "Log Balance obstacle from near..."
        case 1:
            return "Log Balance obstacle from Pipe obstacle..."
        case 2:
            return "Net obstacle (up)..."
        case 3:
            return "Branch obstacle (up)..."
        case 4:
            return "Rope Balance obstacle..."
        case 5:
            return "Branch obstacle (down)..."
        case 6:
            return "Net obstacle (over)..."
        case 7:
            return "Pipe obstacle - END."


def check_for_level_dialogue():
    if does_img_exist(img_name="level_up", category="General"):
        print(f'Level-up detected. Spacing through...')
        keyboard.press('space')
        API.AntiBan.sleep_between(1.1, 2.6)
        keyboard.press('space')
        print(f'Should be through all chat-box dialogue now. Continuing...')
    return
