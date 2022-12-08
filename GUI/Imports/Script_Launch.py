from Scripts.Skilling.Smithing.Gold.Edge_Gold import smith_gold_edge
from Scripts.Skilling.Mining.Iron.Pisc_Iron import mine_iron_pisc
from Scripts.Skilling.Agility.Gnome_Course import run_gnome_course
from Scripts.Skilling.Fishing.Shrimp.Draynor_Shrimp import fish_draynor_shrimp
from Scripts.Skilling.Fishing.Trout.Barb_Trout import fish_barb_trout
from Scripts.Skilling.Fishing.Barbarian.Barbarian_Fishing import barbarian_fishing
from Scripts.Skilling.Thieving.Pickpocketing.Draynor_Man import pickpocket_draynor_man
from Scripts.Skilling.Thieving.Stalls.Ardy_Cake import steal_ardy_cake
from Scripts.Skilling.Firemaking.GE_Log_Burner import burn_logs_at_ge
from Scripts.MiniGames.Fishing_Trawler import start_trawling
from Scripts.Skilling.Combat.Cow_Killer import start_killing_cows
from Scripts.Skilling.Cooking.Rogue_Cooker import start_rogue_cooking
from Scripts.Skilling.Combination.Lummy_Chop_Fletcher import start_chop_fletching
from Scripts.Skilling.Crafting.GE_Glass_Blower import start_blowing_glass
from Scripts.Skilling.Fletching.GE_Dart_Fletcher import start_fletching_darts
from API.Imaging.OCR.Skill_Levels import get_skill_level, ocr_skill_levels

from enum import Enum
import API
import keyboard
from API.Debug import write_debug
from API.Interface.General import handle_auth_screens
from API.Break_Timer.Break_Handler import is_break_timer_set
from API.Break_Timer.Break_Handler import break_handler

curr_script_iteration = 1
should_continue = True


# script_name passed into individual buttons in GUI corresponding to individual scripts
def launch_script(script_name="pisc_iron"):
    global curr_script_iteration
    global should_continue

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
        DRAYNOR_MAN = 6
        ARDY_CAKE = 7
        GE_LOGS = 8
        TRAWLER = 9
        COW_KILLER = 10
        ROGUE_COOKER = 11
        CHOP_FLETCH = 12
        BLOW_GLASS = 13
        DART_FLETCHER = 14

    all_scripts = [mine_iron_pisc, smith_gold_edge, run_gnome_course,
                   fish_draynor_shrimp, fish_barb_trout, barbarian_fishing,
                   pickpocket_draynor_man, steal_ardy_cake, burn_logs_at_ge,
                   start_trawling, start_killing_cows, start_rogue_cooking,
                   start_chop_fletching, start_blowing_glass, start_fletching_darts]

    match script_name:
        case "pisc_iron":
            selected_script = ScriptEnum.PISC_IRON.value
            # 1 / x
            antiban_likelihood = 50
            # Interval between scrip loops
            antiban_downtime_sec = 0.5
        case "edge_gold":
            selected_script = ScriptEnum.EDGE_GOLD.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "gnome_course":
            selected_script = ScriptEnum.GNOME_COURSE.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "draynor_shrimp":
            selected_script = ScriptEnum.DRAYNOR_SHRIMP.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "barb_trout":
            selected_script = ScriptEnum.BARB_TROUT.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "barbarian_fishing":
            selected_script = ScriptEnum.BARBARIAN_FISHING.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "draynor_man":
            selected_script = ScriptEnum.DRAYNOR_MAN.value
            antiban_likelihood = 50
            antiban_downtime_sec = 0.2
        case "ardy_cake":
            selected_script = ScriptEnum.ARDY_CAKE.value
            antiban_likelihood = 10
            antiban_downtime_sec = 0.4
        case "ge_log_burner":
            selected_script = ScriptEnum.GE_LOGS.value
            antiban_likelihood = 20
            antiban_downtime_sec = 0.5
        case "fishing_trawler":
            selected_script = ScriptEnum.TRAWLER.value
            antiban_likelihood = 20
            antiban_downtime_sec = 0.5
        case "cow_killer":
            selected_script = ScriptEnum.COW_KILLER.value
            antiban_likelihood = 10
            antiban_downtime_sec = 2.3
        case "rogue_cooker":
            selected_script = ScriptEnum.ROGUE_COOKER.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "lummy_chop_fletcher":
            selected_script = ScriptEnum.CHOP_FLETCH.value
            antiban_likelihood = 20
            antiban_downtime_sec = 3
        case "ge_glass_blower":
            selected_script = ScriptEnum.BLOW_GLASS.value
            antiban_likelihood = 10
            antiban_downtime_sec = 4
        case "ge_dart_fletcher":
            selected_script = ScriptEnum.DART_FLETCHER.value
            antiban_likelihood = 20
            antiban_downtime_sec = 4

    is_timer_set = is_break_timer_set()

    if is_timer_set:
        write_debug(f'🚩 Break Timer Set - Entering loop with break_handler()')
        while should_continue:
            should_continue = all_scripts[selected_script](curr_script_iteration)
            API.AntiBan.random_human_actions(max_downtime_seconds=antiban_downtime_sec, likelihood=antiban_likelihood)
            break_handler()

            curr_script_iteration += 1
    else:
        write_debug(f'🏳 NO Break Timer Set - Entering loop WITHOUT break_handler()')
        while should_continue:
            should_continue = all_scripts[selected_script](curr_script_iteration)
            API.AntiBan.random_human_actions(max_downtime_seconds=antiban_downtime_sec, likelihood=antiban_likelihood)

            curr_script_iteration += 1

    return


def quit_prog():
    global should_continue
    should_continue = False
    write_debug(f'User terminated script with ESC hotkey - Exiting...')
    exit(-2)
    return


def set_curr_iteration(new_val):
    global curr_script_iteration
    curr_script_iteration = new_val
    return
