import threading
import os
import keyboard

from Database.Connection import AUTHED_USER, check_client_version, get_authed_user
from Database.Script_Access import set_script_access
from Scripts.Skilling.Smithing.Edge_Gold import smith_gold_edge
from Scripts.Skilling.Mining.Pisc_Iron_Miner import mine_pisc_iron
from Scripts.Skilling.Agility.Gnome_Course_v3 import start_gnome_course
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
from Scripts.Skilling.Prayer.Gilded_Altar_v2 import start_worshipping_bones
from Scripts.Skilling.Herblore.Unf_Pots import start_unf_pots
from Scripts.Skilling.Herblore.GE_Finished_Pots import start_making_finished_potions
from Scripts.Skilling.Agility.Canifis_Rooftops import start_canifis_rooftops
from Scripts.Skilling.Agility.Seers_Rooftops_v2 import start_seers_rooftops
from Scripts.Skilling.Agility.Ardy_Rooftops import start_ardy_rooftops
from Scripts.Skilling.Hunter.Single_Trap_Crimsons import start_catching_crimsons
from Scripts.Skilling.Hunter.Double_Trap_Ceruleans import start_trapping_birds
from Scripts.Skilling.Thieving.Pickpocketing.Ardy_Knights_v3 import start_pickpocketing_knight
from Scripts.Skilling.Combat.Kourend_Crab_Killer import start_killing_kourend_crabs
from Scripts.Skilling.Crafting.GE_Dhide_Bodies_v2 import start_crafting_dhide_bodies
from Scripts.Skilling.Woodcutting.Cwars_Teaks import start_chopping_teaks
from Scripts.Skilling.Woodcutting.SW_Teaks import start_chopping_sw_teaks
from Scripts.Skilling.Combination.GE_Superheat_Gold import start_superheating_gold
from Scripts.Skilling.Construction.Con_Larders import start_constructing_larders
from Scripts.Skilling.Construction.Con_Mahog_Tables import start_constructing_tables
from Scripts.Skilling.Hunter.Desert_Lizards import start_catching_desert_lizards
from Scripts.Skilling.Hunter.Red_Lizards_v2 import start_catching_red_lizards
from Scripts.Skilling.Hunter.Black_Lizards_v2 import start_catching_black_lizards
from Scripts.Skilling.Hunter.Red_Chin_Hunter import start_catching_chins
from Scripts.Skilling.Runecrafting.Cwars_Lavas_v2 import start_crafting_lavas
from Scripts.Skilling.Runecrafting.Moonclan_Astrals import start_crafting_astrals
from Scripts.Skilling.Mining.Motherlode_Miner import start_motherlode_mining
from Scripts.Skilling.Mining.Desert_Granite_Miner import start_mining_granite
from Scripts.Skilling.Mining.Mining_Guild_Iron import start_mining_guild_iron
from Scripts.Skilling.Farming.GE_Sulphurous_Fertilizer import start_making_fertalizer
from Scripts.Skilling.Farming.Tithe_Farmer_v2 import start_tithe_farming
from Scripts.Skilling.Smithing.Blast_Furnace import start_blasting
from Scripts.Skilling.Combat.NMZ import start_training_nmz
from Scripts.Skilling.Magic.Ardy_Knight_Splasher import start_splashing_ardy_knight
from Scripts.Skilling.Fletching.GE_Bow_Stringer import start_stringing_bows
from Scripts.MiniGames.Pest_Control import start_pest_control

import API
from enum import Enum
from API.Debug import write_debug
from API.Interface.General import handle_auth_screens
from API.Break_Timer.Break_Handler import get_is_break_timer_set
from API.Break_Timer.Break_Handler import break_handler

SHOULD_CONTINUE = True
CURR_SCRIPT_LOOP = 1


def stop_script():
    global SHOULD_CONTINUE
    SHOULD_CONTINUE = False
    write_debug(f'⛔ set_should_continue - new_val: {False}')
    set_curr_iteration(1)
    return


def set_curr_iteration(new_val):
    global CURR_SCRIPT_LOOP
    CURR_SCRIPT_LOOP = new_val
    return


# script_name passed into individual buttons in GUI corresponding to individual scripts
def launch_script(script_name="pisc_iron"):
    global SHOULD_CONTINUE
    global CURR_SCRIPT_LOOP

    keyboard.add_hotkey("End", lambda: os.kill(os.getpid(), 9))
    keyboard.add_hotkey("~", lambda: stop_script())

    CURR_SCRIPT_LOOP = 1
    SHOULD_CONTINUE = True

    reopen_invent = True
    always_sleep = True

    # for thread in threading.enumerate():
    #     print(f'Thread name: {thread.name}')

    # authed_user = get_authed_user()
    #
    # set_script_access(authed_user.email, authed_user.licenses)

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
        RED_LIZARDS = 31
        SW_TEAKS = 32
        CWARS_LAVAS = 33
        MOTHERLODE_MINER = 34
        SULPHUROUS_FERTILIZER = 35
        TITHE_FARMER = 36
        BLACK_LIZARDS = 37
        RED_CHINS = 38
        BLAST_FURNACE = 39
        NMZ = 40
        ARDY_KNIGHT_SPLASHER = 41
        PEST_CONTROL = 42
        GE_FINISHED_POTS = 43
        ARDY_ROOFTOPS = 44
        GE_BOW_STRINGER = 45
        MOONCLAN_ASTRALS = 46
        DESERT_GRANITE_MINER = 47
        MINING_GUILD_IRON = 48

    all_scripts = [mine_pisc_iron, smith_gold_edge, start_gnome_course,
                   fish_draynor_shrimp, fish_barb_trout, barbarian_fishing,
                   pickpocket_draynor_man, steal_ardy_cake, burn_logs_at_ge,
                   start_trawling, start_killing_cows, start_rogue_cooking,
                   start_chop_fletching, start_blowing_glass, start_fletching_darts,
                   start_ploughing_for_favour, start_stealing_fruit, start_worshipping_bones,
                   start_unf_pots, start_canifis_rooftops, start_seers_rooftops,
                   start_catching_crimsons, start_trapping_birds, start_pickpocketing_knight,
                   start_killing_kourend_crabs, start_crafting_dhide_bodies, start_chopping_teaks,
                   start_superheating_gold, start_constructing_larders, start_constructing_tables,
                   start_catching_desert_lizards, start_catching_red_lizards, start_chopping_sw_teaks,
                   start_crafting_lavas, start_motherlode_mining, start_making_fertalizer, start_tithe_farming,
                   start_catching_black_lizards, start_catching_chins, start_blasting, start_training_nmz,
                   start_splashing_ardy_knight, start_pest_control, start_making_finished_potions, start_ardy_rooftops,
                   start_stringing_bows, start_crafting_astrals, start_mining_granite, start_mining_guild_iron]

    match script_name:
        case "Pisc_Iron_Miner":
            selected_script = ScriptEnum.PISC_IRON.value
            # 1 / x
            antiban_likelihood = 50
            # Interval between scrip loops
            antiban_downtime_sec = 1
        case "Edge_Gold":
            selected_script = ScriptEnum.EDGE_GOLD.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "Gnome_Course":
            selected_script = ScriptEnum.GNOME_COURSE.value
            antiban_likelihood = 5
            antiban_downtime_sec = 2
        case "Draynor_Shrimp":
            selected_script = ScriptEnum.DRAYNOR_SHRIMP.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "Barb_Trout":
            selected_script = ScriptEnum.BARB_TROUT.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "Barbarian_Fishing":
            selected_script = ScriptEnum.BARBARIAN_FISHING.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "Draynor_Man":
            selected_script = ScriptEnum.DRAYNOR_MAN.value
            antiban_likelihood = 50
            antiban_downtime_sec = 0.2
        case "Ardy_Cake":
            selected_script = ScriptEnum.ARDY_CAKE.value
            antiban_likelihood = 10
            antiban_downtime_sec = 0.4
        case "GE_Log_Burner":
            selected_script = ScriptEnum.GE_LOGS.value
            antiban_likelihood = 15
            antiban_downtime_sec = 3
        case "Fishing_Trawler":
            selected_script = ScriptEnum.TRAWLER.value
            antiban_likelihood = 20
            antiban_downtime_sec = 0.5
        case "Cow_Killer":
            selected_script = ScriptEnum.COW_KILLER.value
            antiban_likelihood = 25
            antiban_downtime_sec = 2.75
        case "Rogue_Cooker":
            selected_script = ScriptEnum.ROGUE_COOKER.value
            antiban_likelihood = 10
            antiban_downtime_sec = 6
        case "Lummy_Chop_And_Fletcher":
            selected_script = ScriptEnum.CHOP_FLETCH.value
            antiban_likelihood = 20
            antiban_downtime_sec = 3
        case "GE_Glass_Blower":
            selected_script = ScriptEnum.BLOW_GLASS.value
            antiban_likelihood = 10
            antiban_downtime_sec = 4
        case "GE_Dart_Fletcher":
            selected_script = ScriptEnum.DART_FLETCHER.value
            antiban_likelihood = 5
            antiban_downtime_sec = 2
        case "Hosidius_Plough":
            selected_script = ScriptEnum.HOSIDIUS_PLOUGH.value
            antiban_likelihood = 15
            antiban_downtime_sec = 4
        case "Hosidius_Fruit":
            selected_script = ScriptEnum.HOSIDIUS_FRUIT.value
            antiban_likelihood = 10
            antiban_downtime_sec = 10
        case "Gilded_Altar":
            selected_script = ScriptEnum.GILDED_ALTAR.value
            antiban_likelihood = 20
            antiban_downtime_sec = 5
        case "Unf_Pots":
            selected_script = ScriptEnum.UNF_POTS.value
            antiban_likelihood = 25
            antiban_downtime_sec = 8
        case "Canifis_Rooftops":
            selected_script = ScriptEnum.CANIFIS_ROOFTOPS.value
            antiban_likelihood = 25
            antiban_downtime_sec = 8
        case "Seers_Rooftops":
            selected_script = ScriptEnum.SEERS_ROOFTOPS.value
            antiban_likelihood = 0
            antiban_downtime_sec = 0.5
        case "Feldip_1t_Crimson":
            selected_script = ScriptEnum.BIRD_SNARER.value
            antiban_likelihood = 30
            antiban_downtime_sec = 1
        case "Troll_2t_Cerulean":
            selected_script = ScriptEnum.DOUBLE_TRAP_CERULEANS.value
            antiban_likelihood = 100
            antiban_downtime_sec = 1
        case "Ardy_Knights":
            selected_script = ScriptEnum.ARDY_KNIGHTS.value
            antiban_likelihood = 2
            antiban_downtime_sec = 1
        case "Kourend_Crab_Killer":
            selected_script = ScriptEnum.KOUREND_CRABS.value
            antiban_likelihood = 10
            antiban_downtime_sec = 4
        case "GE_Dhide_Bodies":
            selected_script = ScriptEnum.DHIDE_BODIES.value
            antiban_likelihood = 2
            antiban_downtime_sec = 1
        case "Cwars_Teak":
            selected_script = ScriptEnum.CWARS_TEAK.value
            antiban_likelihood = 10
            antiban_downtime_sec = 1
        case "GE_Superheat_Gold":
            selected_script = ScriptEnum.GE_SUPERHEAT_GOLD.value
            antiban_likelihood = 20
            antiban_downtime_sec = 4
        case "Poh_Larders":
            selected_script = ScriptEnum.CON_LARDERS.value
            antiban_likelihood = 20
            antiban_downtime_sec = 6
        case "Poh_Mahogany_Tables":
            selected_script = ScriptEnum.CON_MAHOG_TABLES.value
            antiban_likelihood = 0
            antiban_downtime_sec = 0.5
        case "Desert_Lizards":
            selected_script = ScriptEnum.DESERT_LIZARDS.value
            antiban_likelihood = 25
            antiban_downtime_sec = 1
            reopen_invent = False
        case "Red_Lizards":
            selected_script = ScriptEnum.RED_LIZARDS.value
            antiban_likelihood = 25
            antiban_downtime_sec = 1
            reopen_invent = False
        case "SW_Teaks":
            selected_script = ScriptEnum.SW_TEAKS.value
            antiban_likelihood = 15
            antiban_downtime_sec = 4
            reopen_invent = True
        case "Cwars_Lavas":
            selected_script = ScriptEnum.CWARS_LAVAS.value
            antiban_likelihood = 9
            antiban_downtime_sec = 4
            reopen_invent = True
            always_sleep = False
        case "Motherlode_Miner":
            selected_script = ScriptEnum.MOTHERLODE_MINER.value
            antiban_likelihood = 5
            antiban_downtime_sec = 4
            reopen_invent = True
            always_sleep = False
        case "GE_Sulphurous_Fertilizer":
            selected_script = ScriptEnum.SULPHUROUS_FERTILIZER.value
            antiban_likelihood = 25
            antiban_downtime_sec = 3
            reopen_invent = True
            always_sleep = False
        case "Tithe_Farmer":
            selected_script = ScriptEnum.TITHE_FARMER.value
            antiban_likelihood = 10
            antiban_downtime_sec = 3
            reopen_invent = True
            always_sleep = False
        case "Black_Lizards":
            selected_script = ScriptEnum.BLACK_LIZARDS.value
            antiban_likelihood = 10
            antiban_downtime_sec = 3
            reopen_invent = False
            always_sleep = False
        case "Red_Chins":
            selected_script = ScriptEnum.RED_CHINS.value
            antiban_likelihood = 5
            antiban_downtime_sec = 2
            reopen_invent = False
            always_sleep = False
        case "Blast_Furnace":
            selected_script = ScriptEnum.BLAST_FURNACE.value
            antiban_likelihood = 5
            antiban_downtime_sec = 2
            reopen_invent = False
            always_sleep = False
        case "NMZ":
            selected_script = ScriptEnum.NMZ.value
            antiban_likelihood = 2
            antiban_downtime_sec = 3
            reopen_invent = False
            always_sleep = False
        case "Ardy_Knight_Splasher":
            selected_script = ScriptEnum.ARDY_KNIGHT_SPLASHER.value
            antiban_likelihood = 20
            antiban_downtime_sec = 1
            reopen_invent = False
            always_sleep = False
        case "Pest_Control":
            selected_script = ScriptEnum.PEST_CONTROL.value
            antiban_likelihood = 20
            antiban_downtime_sec = 1
            reopen_invent = False
            always_sleep = False
        case "GE_Finished_Pots":
            selected_script = ScriptEnum.GE_FINISHED_POTS.value
            antiban_likelihood = 6
            antiban_downtime_sec = 2
            reopen_invent = True
            always_sleep = False
        case "Ardy_Rooftops":
            selected_script = ScriptEnum.ARDY_ROOFTOPS.value
            antiban_likelihood = 2
            antiban_downtime_sec = 2
            reopen_invent = True
            always_sleep = False
        case "GE_Bow_Stringer":
            selected_script = ScriptEnum.GE_BOW_STRINGER.value
            antiban_likelihood = 2
            antiban_downtime_sec = 2
            reopen_invent = True
            always_sleep = False
        case "Moonclan_Astrals":
            selected_script = ScriptEnum.MOONCLAN_ASTRALS.value
            antiban_likelihood = 2
            antiban_downtime_sec = 4
            reopen_invent = True
            always_sleep = False
        case "Desert_Granite_Miner":
            selected_script = ScriptEnum.DESERT_GRANITE_MINER.value
            antiban_likelihood = 2
            antiban_downtime_sec = 4
            reopen_invent = True
            always_sleep = False
        case "Mining_Guild_Iron":
            selected_script = ScriptEnum.MINING_GUILD_IRON.value
            antiban_likelihood = 2
            antiban_downtime_sec = 4
            reopen_invent = True
            always_sleep = False

    is_bt_set = get_is_break_timer_set()
    API.Time.start_script_timer()

    if is_bt_set:
        write_debug(f'🚩 Break Timer Set - Entering loop with break_handler()')
        while SHOULD_CONTINUE:
            if not all_scripts[selected_script](CURR_SCRIPT_LOOP):
                if not handle_auth_screens():
                    SHOULD_CONTINUE = False

            break_handler()

            CURR_SCRIPT_LOOP += 1
            print(f'🔄 MAIN LOOP COUNT: {CURR_SCRIPT_LOOP}')
            print(f'⏳ {API.Time.get_curr_runtime()}')

    else:
        write_debug(f'🏳 NO Break Timer Set - Entering loop WITHOUT break_handler()')
        while SHOULD_CONTINUE:
            if not all_scripts[selected_script](CURR_SCRIPT_LOOP):
                write_debug(f'❌ Script returned false - checking if we logged out...')
                if not handle_auth_screens():
                    SHOULD_CONTINUE = False

            API.AntiBan.random_human_actions(max_downtime_seconds=antiban_downtime_sec, likelihood=antiban_likelihood,
                                             always_sleep=always_sleep,  reopen_inventory=reopen_invent)

            CURR_SCRIPT_LOOP += 1
            print(f'🔄 MAIN LOOP COUNT: {CURR_SCRIPT_LOOP}')
            print(f'⏳ {API.Time.get_curr_runtime()}')

    return




