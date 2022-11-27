# from GUI.Break_Timer.Break_Handler import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *
from Scripts.Skilling.Mining.Iron.Pisc_Iron import *
from enum import Enum


# script_name passed into individual buttons in GUI corresponding to individual scripts
def launch_script(script_name="pisc_iron"):
    print("Pre-launch checks:")
    # Check that we're not on dc screen (click continue if so)
    handle_auth_screens()

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

    # if is_break_timer_set():
    while go:
        all_scripts[selected_script]()

    return

