from API.Interface import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *
from Scripts.Skilling.Mining.Iron.Pisc_Iron import *
from enum import Enum

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

    Go = True

    while Go:
        if not is_on_break():
            all_scripts[selected_script]()
        else:

            sleep_between()

    # match script_name:
    #     case "pisc_iron":
    #         print("launch_script: Scripts > Skilling > Mining Launched...")
    #         # mine_iron_pisc()
    #         script_method[0]()
    #     case "edge_gold":
    #         print("launch_script: Scripts > Skilling > Smithing > Edge Gold Launched...")
    #         # smith_gold_edge()
    #         script_method[1]()
    #
    #     case _:
    #         print("Default Switch printing")
    #         exit(-1)
    return


def is_on_break():
    return False