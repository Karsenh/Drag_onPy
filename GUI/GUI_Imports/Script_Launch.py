from API.Interface import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *
from Scripts.Skilling.Mining.Iron.Pisc_Iron import *
from enum import Enum


script_start_time = None


# script_name passed into individual buttons in GUI corresponding to individual scripts
def launch_script(script_name="pisc_iron"):
    print("Pre-launch checks:")
    # Check that we're not on dc screen (click continue if so)
    print(f'Disconnected screen? : {is_on_dc_screen(should_cont=True)}')
    # is_on_dc_screen(should_cont=True)
    # Check that we're not on login screen (click login if so)
    print(f'Login screen? : {is_on_login_screen(should_cont=True)}')
    # is_on_login_screen(should_cont=True)
    # Check that we're not on the welcome screen (click 'Tap Here To Play' if so)
    print(f'Welcome screen? : {is_on_welcome_screen(should_cont=True)}')
    # is_on_welcome_screen(should_cont=True)

    class ScriptEnum(Enum):
        PISC_IRON = 0
        EDGE_GOLD = 1

    all_scripts = [mine_iron_pisc, smith_gold_edge]

    match script_name:
        case "pisc_iron":
            selected_script = ScriptEnum.PISC_IRON.value
        case "edge_gold":
            selected_script = ScriptEnum.EDGE_GOLD.value

    go = True

    while go:
        if not is_on_break():
            all_scripts[selected_script]()
        else:
            sleep_between()

    return


def is_on_break():
    global script_start_time
    # If this is the first loop (if the global last checked time is none - set that along with start time
    break_vals = get_break_times()
    break_t, break_dev_t, interval_t, interval_dev_t = break_vals

    if not script_start_time:
        start_time = datetime.now()
        print(f'First loop - script start set: {start_time}')
        script_start_time = start_time

    curr_time = datetime.now()
    elapsed_time = curr_time - script_start_time
    print(f'Elapsed Time: {elapsed_time}')

    # If this is the first loop - set the start time of the script to now
    # Calculate how long has elapsed since start
    # Check if the elapsed time is greater than or equal to the

    return False
