# from GUI.Break_Timer.Break_Handler import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *
from Scripts.Skilling.Mining.Iron.Pisc_Iron import *
from Scripts.Skilling.Agility.Gnome_Course import *
from Scripts.Skilling.Fishing.Shrimp.Draynor_Shrimp import fish_draynor_shrimp
from Scripts.Skilling.Fishing.Trout.Barb_Trout import fish_barb_trout
from Scripts.Skilling.Fishing.Barbarian.Barbarian_Fishing import barbarian_fishing
from enum import Enum


curr_script_iteration = 1
should_continue = True


# script_name passed into individual buttons in GUI corresponding to individual scripts
def launch_script(script_name="pisc_iron"):
    global curr_script_iteration
    global should_continue

    keyboard.add_hotkey('esc', lambda: quit_prog())

    write_debug("Pre-launch checks:")
    # Check that we're not on dc screen (click continue if so)
    handle_auth_screens()

    class ScriptEnum(Enum):
        PISC_IRON = 0
        EDGE_GOLD = 1
        GNOME_COURSE = 2
        DRAYNOR_SHRIMP = 3
        BARB_TROUT = 4
        BARBARIAN_FISHING = 5

    all_scripts = [mine_iron_pisc, smith_gold_edge, run_gnome_course, fish_draynor_shrimp, fish_barb_trout, barbarian_fishing]

    match script_name:
        case "pisc_iron":
            selected_script = ScriptEnum.PISC_IRON.value
        case "edge_gold":
            selected_script = ScriptEnum.EDGE_GOLD.value
        case "gnome_course":
            selected_script = ScriptEnum.GNOME_COURSE.value
        case "draynor_shrimp":
            selected_script = ScriptEnum.DRAYNOR_SHRIMP.value
        case "barb_trout":
            selected_script = ScriptEnum.BARB_TROUT.value
        case "barbarian_fishing":
            selected_script = ScriptEnum.BARBARIAN_FISHING.value

    is_timer_set = is_break_timer_set()

    if is_timer_set:
        write_debug(f'🚩 Break Timer Set - Entering loop with break_handler()')
        while should_continue:
            should_continue = all_scripts[selected_script](curr_script_iteration)
            API.AntiBan.random_human_actions(6)
            break_handler()

            curr_script_iteration += 1
    else:
        write_debug(f'🏳 NO Break Timer Set - Entering loop WITHOUT break_handler()')
        while should_continue:
            should_continue = all_scripts[selected_script](curr_script_iteration)
            API.AntiBan.random_human_actions(6)

            curr_script_iteration += 1

    return


def quit_prog():
    global should_continue
    should_continue = False
    write_debug(f'User terminated script with ESC hotkey - Exiting...')
    exit(-2)
    return
