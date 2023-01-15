import os
from PIL import ImageTk, Image
import API.Imports.Paths


def get_all_gui_images():

    # --------
    # MAIN_GUI
    # --------

    # Main_Gui images
    gui_images_path = "Assets\Images\GUI_Images"
    gold_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Gold.png'))
    skills_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Stats2.png'))
    skull_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Minigames.png'))

    settings_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Settings.png'))
    question_mark_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Question_Mark.png'))
    bug_report_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Bug.png'))

    # -----------------------------------------------------------------------------------------

    # --------
    # SUB-GUIs
    # --------

    # Gold_Gui images
    gold_path = "Assets\Images\GUI_Images\Gold"
    cballs_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gold_path}\Cballs.png'))
    unf_pot_img = ImageTk.PhotoImage(Image.open(f"{os.getcwd()}\{gold_path}\Herb_pot.png"))


    # Skills_Gui images
    # First Row
    stats_path = "Assets\Images\GUI_Images\Stats"
    mining_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Mining.png'))
    attack_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Attack.png'))
    hp_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\HP.png'))

    # Second Row
    strength_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Strength.png'))
    agility_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Agility.png'))
    smithing_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Smithing.png'))

    # Third Row
    defence_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Defence.png'))
    herblore_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Herblore.png'))
    fishing_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Fishing.png'))

    # Fourth Row
    ranged_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Ranged.png'))
    thieving_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Thieving.png'))
    cooking_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Cooking.png'))

    # Fifth Row
    prayer_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Prayer.png'))
    crafting_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Crafting.png'))
    firemaking_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Firemaking.png'))

    # Sixth Row
    magic_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Magic.png'))
    fletching_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Fletching.png'))
    woodcutting_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Woodcutting.png'))

    # Seventh Row
    runecrafting_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Runecrafting.png'))
    slayer_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Slayer.png'))
    farming_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Farming.png'))

    # Last Row
    construction_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Construction.png'))
    hunter_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Hunter.png'))

    skill_input_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{stats_path}\Skill_Levels.png'))

    # Minigames images
    minigames_path = "Assets\Images\GUI_Images\Minigames"
    trawler_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{minigames_path}\Fishing_Trawler\Fishing_Trawler.png'))

    main_gui_images = gold_img, skills_img, skull_img, settings_img, question_mark_img, bug_report_img

    gold_gui_images = cballs_img, unf_pot_img

    skill_gui_images = attack_img, hp_img, mining_img, \
                       strength_img, agility_img, smithing_img, \
                       defence_img, herblore_img, fishing_img, \
                       ranged_img, thieving_img, cooking_img, \
                       prayer_img, crafting_img, firemaking_img, \
                       magic_img, fletching_img, woodcutting_img, \
                       runecrafting_img, slayer_img, farming_img, \
                       construction_img, hunter_img, skill_input_img

    minigames_images = trawler_img

    # -----------------------------------------------------------------------------------------
    # ---
    # SUB-SUB-GUIs
    # ---

    # Skill Sub-GUI
    skill_sub_path = "Assets\Images\GUI_Images\Stats"
    map_path = "Assets\Images\GUI_Images\Stats\Map_Images"
    # (Map Button Images)

    # MINING
    #     Pisc_Iron
    iron_pisc_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Piscatoris_Map.png'))
    motherlode_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Motherlode_Mine_Map.png'))

    # SMITHING
    #     Edge_Gold
    edge_gold_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Smithing\Edge_Gold.png'))

    # AGILITY
    #     Gnome Course
    gnome_course_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Gnome_Stronghold_Map.png'))
    canifis_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Agility\canifis_map.png'))
    seers_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Seers_Map.png'))

    # FISHING
    #     Draynor Shrimp
    barb_trout_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Fishing\Barb_Trout_map.png'))
    #     Barb Trout
    draynor_shrimp_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Draynor_Map.png'))
    #     Barbarian_Fishing
    barbarian_fishing_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Fishing\Barbarian_fishing_map.png'))

    # COOKING
    #     Rogue_Cooker
    rogue_den_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Cooking\Rogues_den_map.png'))

    # COMBAT
    #     Cow_Killer
    cow_killer_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Lummy_Map.png'))

    # FLETCHING / CRAFTING
    ge_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\GE_map.png'))

    # HERBLORE
    # uses GE map from above

    # PRAYER
    remmy_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Remmy_map.png'))

    # THIEVING
    ardy_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Ardy_map.png'))
    hosidius_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Hosidius_map.png'))

    # WOODCUTTING
    lummy_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Lummy_Map.png'))
    cwars_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Cwars_Map.png'))

    # HUNTER
    corsair_cove_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Corsair_Cove_Map.png'))
    cerulean_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Keldagrim_Aisle_Map.png'))
    ourania_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Ourania_Map.png'))
    uzer_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{map_path}\Map_Uzer.png'))

    skilling_sub_gui_images = iron_pisc_img, edge_gold_img, gnome_course_img, \
                              draynor_shrimp_map_img, barb_trout_map_img, barbarian_fishing_map_img, \
                              rogue_den_map_img, cow_killer_map_img, ge_map_img, canifis_map_img, \
                              remmy_map_img, ardy_map_img, hosidius_map_img, lummy_map_img, \
                              corsair_cove_map_img, cerulean_map_img, seers_map_img, cwars_map_img, \
                              motherlode_map_img, ourania_map_img, uzer_map_img

    return main_gui_images, gold_gui_images, skill_gui_images, minigames_images, skilling_sub_gui_images

    # -----------------------------------------------------------------------------------------



