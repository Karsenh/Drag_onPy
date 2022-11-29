# from GUI.Break_Timer.Break_Handler import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *
from Scripts.Skilling.Mining.Iron.Pisc_Iron import *
from Scripts.Skilling.Agility.Gnome_Course import *
from enum import Enum


curr_script_iteration = 0
should_continue = True


# script_name passed into individual buttons in GUI corresponding to individual scripts
def launch_script(script_name="pisc_iron"):
    global curr_script_iteration
    global should_continue

    keyboard.add_hotkey('esc', lambda: quit_prog())

    print("Pre-launch checks:")
    # Check that we're not on dc screen (click continue if so)
    handle_auth_screens()

    class ScriptEnum(Enum):
        PISC_IRON = 0
        EDGE_GOLD = 1
        GNOME_COURSE = 2

    all_scripts = [mine_iron_pisc, smith_gold_edge, run_gnome_course]

    match script_name:
        case "pisc_iron":
            selected_script = ScriptEnum.PISC_IRON.value
        case "edge_gold":
            selected_script = ScriptEnum.EDGE_GOLD.value
        case "gnome_course":
            selected_script = ScriptEnum.GNOME_COURSE.value

    is_timer_set = is_break_timer_set()

    if is_timer_set:
        print(f'🚩 Break Timer Set - Entering loop with break_handler()')
        while should_continue:
            should_continue = all_scripts[selected_script]()
            break_handler()
    else:
        print(f'🚩 NO Break Timer Set - Entering loop WITHOUT break_handler()')
        while should_continue:
            should_continue = all_scripts[selected_script]()

    return


def quit_prog():
    global should_continue
    should_continue = False
    print(f'User terminated script with ESC hotkey - Exiting...')
    exit(-2)
    return
