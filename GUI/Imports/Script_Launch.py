from Scripts.Skilling.Smithing.Edge_Gold import smith_gold_edge
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
from Scripts.MiniGames.Hosidius_Plough import start_ploughing_for_favour
from Scripts.Skilling.Thieving.Stalls.Hosidius_Fruit import start_stealing_fruit
from Scripts.Skilling.Prayer.Gilded_Altar import start_gilded_altar
from Scripts.Skilling.Herblore.Unf_Pots import start_unf_pots
from Scripts.Skilling.Agility.Canifis_Rooftops import start_canifis_rooftops
from Scripts.Skilling.Agility.Seers_Rooftops import start_seers_rooftops
from Scripts.Skilling.Hunter.Single_Trap_Crimsons import start_catching_crimsons
from Scripts.Skilling.Hunter.Double_Trap_Ceruleans import start_trapping_birds
from Scripts.Skilling.Thieving.Pickpocketing.Ardy_Knights import start_pickpocketing_ardy_knights
from Scripts.Skilling.Combat.Kourend_Crab_Killer import start_killing_kourend_crabs
from Scripts.Skilling.Crafting.GE_Dhide_Bodies import start_crafting_dhide_bodies
from Scripts.Skilling.Woodcutting.Cwars_Teaks import start_chopping_teaks
from Scripts.Skilling.Combination.GE_Superheat_Gold import start_superheating_gold
from Scripts.Skilling.Construction.Con_Larders import start_constructing_larders
from Scripts.Skilling.Construction.Con_Mahog_Tables import start_constructing_tables
from Scripts.Skilling.Hunter.Desert_Lizards import start_catching_desert_lizards

from enum import Enum
import API
from API.Debug import write_debug
from API.Interface.General import handle_auth_screens
from API.Break_Timer.Break_Handler import is_break_timer_set
from API.Break_Timer.Break_Handler import break_handler

CURR_SCRIPT_LOOP = 1
SHOULD_CONTINUE = True


# script_name passed into individual buttons in GUI corresponding to individual scripts
def launch_script(script_name="pisc_iron"):
    global CURR_SCRIPT_LOOP
    global SHOULD_CONTINUE

    write_debug(f"Pre-launch checks for: {script_name}")
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
        HOSIDIUS_PLOUGH = 15
        HOSIDIUS_FRUIT = 16
        GILDED_ALTAR = 17
        UNF_POTS = 18
        CANIFIS_ROOFTOPS = 19
        SEERS_ROOFTOPS = 20
        BIRD_SNARER = 21
        DOUBLE_TRAP_CERULEANS = 22
        ARDY_KNIGHTS = 23
        KOUREND_CRABS = 24
        DHIDE_BODIES = 25
        CWARS_TEAK = 26
        GE_SUPERHEAT_GOLD = 27
        CON_LARDERS = 28
        CON_MAHOG_TABLES = 29
        DESERT_LIZARDS = 30
    all_scripts = [mine_iron_pisc, smith_gold_edge, run_gnome_course,
                   fish_draynor_shrimp, fish_barb_trout, barbarian_fishing,
                   pickpocket_draynor_man, steal_ardy_cake, burn_logs_at_ge,
                   start_trawling, start_killing_cows, start_rogue_cooking,
                   start_chop_fletching, start_blowing_glass, start_fletching_darts,
                   start_ploughing_for_favour, start_stealing_fruit, start_gilded_altar,
                   start_unf_pots, start_canifis_rooftops, start_seers_rooftops,
                   start_catching_crimsons, start_trapping_birds, start_pickpocketing_ardy_knights,
                   start_killing_kourend_crabs, start_crafting_dhide_bodies, start_chopping_teaks,
                   start_superheating_gold, start_constructing_larders, start_constructing_tables,
                   start_catching_desert_lizards]

    match script_name:
        case "pisc_iron":
            selected_script = ScriptEnum.PISC_IRON.value
            # 1 / x
            antiban_likelihood = 50
            # Interval between scrip loops
            antiban_downtime_sec = 1
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
            antiban_likelihood = 15
            antiban_downtime_sec = 3
        case "fishing_trawler":
            selected_script = ScriptEnum.TRAWLER.value
            antiban_likelihood = 20
            antiban_downtime_sec = 0.5
        case "cow_killer":
            selected_script = ScriptEnum.COW_KILLER.value
            antiban_likelihood = 25
            antiban_downtime_sec = 2.75
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
        case "hosidius_plough":
            selected_script = ScriptEnum.HOSIDIUS_PLOUGH.value
            antiban_likelihood = 15
            antiban_downtime_sec = 4
        case "hosidius_fruit":
            selected_script = ScriptEnum.HOSIDIUS_FRUIT.value
            antiban_likelihood = 10
            antiban_downtime_sec = 10
        case "gilded_altar":
            selected_script = ScriptEnum.GILDED_ALTAR.value
            antiban_likelihood = 20
            antiban_downtime_sec = 5
        case "unf_pots":
            selected_script = ScriptEnum.UNF_POTS.value
            antiban_likelihood = 25
            antiban_downtime_sec = 8
        case "canifis_rooftops":
            selected_script = ScriptEnum.CANIFIS_ROOFTOPS.value
            antiban_likelihood = 25
            antiban_downtime_sec = 8
        case "Seers_Rooftops":
            selected_script = ScriptEnum.SEERS_ROOFTOPS.value
            antiban_likelihood = 50
            antiban_downtime_sec = 0.5
        case "feldip_single_trap_crimsons":
            selected_script = ScriptEnum.BIRD_SNARER.value
            antiban_likelihood = 30
            antiban_downtime_sec = 1
        case "troll_double_trap_ceruleans":
            selected_script = ScriptEnum.DOUBLE_TRAP_CERULEANS.value
            antiban_likelihood = 100
            antiban_downtime_sec = 1
        case "Ardy_Knights":
            selected_script = ScriptEnum.ARDY_KNIGHTS.value
            antiban_likelihood = 50
            antiban_downtime_sec = .5
        case "Kourend_Crab_Killer":
            selected_script = ScriptEnum.KOUREND_CRABS.value
            antiban_likelihood = 10
            antiban_downtime_sec = 4
        case "GE_Dhide_Bodies":
            selected_script = ScriptEnum.DHIDE_BODIES.value
            antiban_likelihood = 15
            antiban_downtime_sec = 1
        case "Cwars_Teak":
            selected_script = ScriptEnum.CWARS_TEAK.value
            antiban_likelihood = 10
            antiban_downtime_sec = 1
        case "GE_Superheat_Gold":
            selected_script = ScriptEnum.GE_SUPERHEAT_GOLD.value
            antiban_likelihood = 20
            antiban_downtime_sec = 4
        case "Con_Larders":
            selected_script = ScriptEnum.CON_LARDERS.value
            antiban_likelihood = 20
            antiban_downtime_sec = 6
        case "Con_Mahog_Tables":
            selected_script = ScriptEnum.CON_MAHOG_TABLES.value
            antiban_likelihood = 25
            antiban_downtime_sec = 1
        case "Desert_Lizards":
            selected_script = ScriptEnum.DESERT_LIZARDS.value
            antiban_likelihood = 25
            antiban_downtime_sec = 1

    is_timer_set = is_break_timer_set()

    if is_timer_set:
        write_debug(f'🚩 Break Timer Set - Entering loop with break_handler()')
        while SHOULD_CONTINUE:
            if not all_scripts[selected_script](CURR_SCRIPT_LOOP):
                if not handle_auth_screens():
                    SHOULD_CONTINUE = False

            break_handler()

            CURR_SCRIPT_LOOP += 1
            print(f'🔄 MAIN LOOP COUNT: {CURR_SCRIPT_LOOP}')

    else:
        write_debug(f'🏳 NO Break Timer Set - Entering loop WITHOUT break_handler()')
        while SHOULD_CONTINUE:
            if not all_scripts[selected_script](CURR_SCRIPT_LOOP):
                if not handle_auth_screens():
                    SHOULD_CONTINUE = False

            API.AntiBan.random_human_actions(max_downtime_seconds=antiban_downtime_sec, likelihood=antiban_likelihood)

            CURR_SCRIPT_LOOP += 1
            print(f'🔄 MAIN LOOP COUNT: {CURR_SCRIPT_LOOP}')

    return


def set_curr_iteration(new_val):
    global CURR_SCRIPT_LOOP
    CURR_SCRIPT_LOOP = new_val
    return
