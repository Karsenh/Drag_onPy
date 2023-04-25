from Database.Script_Access import gnome_agility_script, seers_rooftops, canifis_rooftops, cow_killer_script, \
    kourend_crab_killer_script, rogue_cooker_script, ge_glass_blower_script, dhide_bodies_script, poh_larders_script, \
    poh_tables_script, hosidius_plough_script, ge_sulphurous_fertilizer_script, tithe_farmer_script, \
    draynor_shrimp_script, barb_trout_script, barb_fishing_script, ge_dart_fletcher_script, ge_log_burner_script, \
    ge_unf_pots_script, crimson_swift_script, cerulean_twitches, desert_lizards_script, red_lizards_script, \
    black_lizards_script, red_chins_script, pisc_iron_script, motherlode_mine_script, gilded_altar_script, \
    cwars_lavas_script, edge_gold_script, blast_furnace_script, draynor_man_script, ardy_cake_script, \
    hosidius_fruit_script, ardy_knight_script, chop_fletcher_script, sw_teaks_script, cball_smithing_script, \
    ardy_knight_splasher_script, ge_finished_pots_script, ge_bow_stringer_script, ardy_rooftops_script, \
    ge_superheat_gold_script, fishing_trawler_script, nmz_script
from GUI.Imports.GUI_Frames import *
from Scripts.Skilling.Mining.Pisc_Iron_Miner import *
from GUI.Imports.PreLaunch_Gui.PreLaunch_Gui import show_plg
from GUI.Imports.Skill_Level_Input.Skill_Level_Input import show_skill_input_frame

frame_bg_color = '#969488'
label_frame_bg_color = '#a5a195'
btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'
plg_gui_active = 1

SCRIPT_START_BTN_HEIGHT = 30
SCRIPT_START_BTN_WIDTH = 140

SKILL_BTN_HEIGHT = 30
SKILL_BTN_WIDTH = 60

BTN_CURSOR = 'circle'


def get_all_btns(all_frames, all_images, root):
    global SCRIPT_BTN_SIZE
    global SKILL_BTN_WIDTH
    global SKILL_BTN_HEIGHT

    # ---------- FRAMES ----------
    # Primary Frames
    main_frame, money_making_frame, skill_frame, minigames_frame, skill_sub_frames \
        = all_frames

    # Skill (Secondary) Frames
    mining_frame, smithing_frame, agility_frame, \
    defence_frame, herblore_frame, fishing_frame, \
    ranged_frame, thieving_frame, cooking_frame, \
    prayer_frame, crafting_frame, firemaking_frame, \
    magic_frame, fletching_frame, woodcutting_frame, \
    runecrafting_frame, slayer_frame, farming_frame, \
    construction_frame, hunter_frame, attack_frame, \
    skill_level_input_frame, hp_frame, strength_frame, combat_frame \
        = skill_sub_frames

    # ---------- IMAGES ----------
    main_gui_images, gold_gui_images, skill_gui_images, minigames_images, skilling_sub_gui_images = all_images

    # Main_gui_images
    gold_img, skills_img, skull_img, settings_img, question_mark_img, bug_report_img = main_gui_images

    # Sub_gui_images
    cball_img, unf_pot_img = gold_gui_images
    attack_img, hp_img, mining_img, \
    strength_img, agility_img, smithing_img, \
    defence_img, herblore_img, fishing_img, \
    ranged_img, thieving_img, cooking_img, \
    prayer_img, crafting_img, firemaking_img, \
    magic_img, fletching_img, woodcutting_img, \
    runecrafting_img, slayer_img, farming_img, \
    construction_img, hunter_img, skill_input_img \
        = skill_gui_images

    trawler_img, nmz_img = minigames_images

    # Skilling SUB Images
    # (Mining/Smithing/Fishing)
    start_btn_img = skilling_sub_gui_images

    # MAIN_GUI_BTNS
    main_img_path = "Assets\Images\GUI_Images"
    main_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{main_img_path}\Main_image.png'))

    main_img_label = Label(main_frame, image=main_img, bg=FRAME_BG_COL)
    main_img_label.image = main_img
    main_img_label.grid(row=1, column=1, columnspan=3, pady=(8, 15))

    gold_btn = Button(main_frame, text="Gold", bg=BTN_BG_COL, activebackground=BTN_ACTIVE_BG_COL, image=gold_img, command=lambda: show_gold_frame(all_frames, gold_gui_btns, toggle_active_frame, gui_btns), height=50, width=50)
    skill_btn = Button(main_frame, text="Leveling", bg=BTN_BG_COL, activebackground=BTN_ACTIVE_BG_COL, image=skills_img, command=lambda: show_skill_frame(all_frames, skill_gui_btns, toggle_active_frame, gui_btns), height=50, width=50)
    minigames_btn = Button(main_frame, text="Minigames", bg=BTN_BG_COL, activebackground=BTN_ACTIVE_BG_COL, image=skull_img, command=lambda: show_minigames_frame(all_frames, minigames_sub_btns, toggle_active_frame, gui_btns), height=50, width=50)

    settings_btn = Button(main_frame, text="Settings", bg=BTN_BG_COL, activebackground='#f7881c', image=settings_img, command=lambda: show_settings_frame(), height=25, width=25)
    info_btn = Button(main_frame, text="Info", bg=BTN_BG_COL, activebackground='#febf56', image=question_mark_img, command=lambda: print('Info test'), height=25, width=25)
    bug_report_btn = Button(main_frame, text="Bug Report", bg=BTN_BG_COL, activebackground='#81d5fa', image=bug_report_img, command=lambda: print('Bug test'), height=25, width=25)

    # Package up Gui_Btns to access values within each button
    gui_btns = gold_btn, skill_btn, minigames_btn


    # (Main) Skill_gui_btns
    attack_btn = Button(skill_frame, text="Attack", image=attack_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_combat_frame(all_frames, toggle_active_frame, combat_frame, combat_sub_btns))
    hp_btn = Button(skill_frame, text="HP", image=hp_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_combat_frame(all_frames, toggle_active_frame, combat_frame, combat_sub_btns))
    minining_btn = Button(skill_frame, text="Mining", image=mining_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_mining_frame(all_frames, toggle_active_frame, mining_frame, mining_sub_btns))

    strength_btn = Button(skill_frame, text="Strength", image=strength_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_combat_frame(all_frames, toggle_active_frame, combat_frame, combat_sub_btns))
    agility_btn = Button(skill_frame, text="Agility", image=agility_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_agility_frame(all_frames, toggle_active_frame, agility_frame, agility_sub_btns))
    smithing_btn = Button(skill_frame, text="Smithing", image=smithing_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_smithing_frame(all_frames, toggle_active_frame, smithing_frame, smithing_sub_btns))

    defence_btn = Button(skill_frame, text="Defence", image=defence_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_combat_frame(all_frames, toggle_active_frame, combat_frame, combat_sub_btns))
    herblore_btn = Button(skill_frame, text="Herblore", image=herblore_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_herblore_frame(all_frames, toggle_active_frame, herblore_frame, herblore_sub_btns))
    fishing_btn = Button(skill_frame, text="Fishing", image=fishing_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_fishing_frame(all_frames, toggle_active_frame, fishing_frame, fishing_sub_btns))

    ranged_btn = Button(skill_frame, text="Ranged", image=ranged_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_combat_frame(all_frames, toggle_active_frame, combat_frame, combat_sub_btns))
    thieving_btn = Button(skill_frame, text="Thieving", image=thieving_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_thieving_frame(all_frames, toggle_active_frame, thieving_frame, thieving_sub_btns))
    cooking_btn = Button(skill_frame, text="Cooking", image=cooking_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_cooking_frame(all_frames, toggle_active_frame, cooking_frame, cooking_sub_btns))

    prayer_btn = Button(skill_frame, text="Prayer", image=prayer_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_prayer_frame(all_frames, toggle_active_frame, prayer_frame, prayer_sub_btns))
    crafting_btn = Button(skill_frame, text="Crafting", image=crafting_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_crafting_frame(all_frames, toggle_active_frame, crafting_frame, crafting_sub_btns))
    firemaking_btn = Button(skill_frame, text="Firemaking", image=firemaking_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_firemaking_frame(all_frames, toggle_active_frame, firemaking_frame, firemaking_sub_btns))

    magic_btn = Button(skill_frame, text="Magic", image=magic_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_magic_frame(all_frames, toggle_active_frame, magic_frame, magic_sub_btns))
    fletching_btn = Button(skill_frame, text="Fletching", image=fletching_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_fletching_frame(all_frames, toggle_active_frame, fletching_frame, fletching_sub_btns))
    woodcutting_btn = Button(skill_frame, text="Woodcutting", image=woodcutting_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_woodcutting_frame(all_frames, toggle_active_frame, woodcutting_frame, woodcutting_sub_btns))

    runecrafting_btn = Button(skill_frame, text="RuneCrafting", image=runecrafting_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_runecrafting_frame(all_frames, toggle_active_frame, runecrafting_frame, runecrafting_sub_btns))
    slayer_btn = Button(skill_frame, state="disabled", text="Slayer", image=slayer_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_thieving_frame(all_frames, toggle_active_frame, thieving_frame, thieving_sub_btns))
    farming_btn = Button(skill_frame, text="Farming", image=farming_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_farming_frame(all_frames, toggle_active_frame, farming_frame, farming_sub_btns))

    construction_btn = Button(skill_frame, text="Construction", image=construction_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_construction_frame(all_frames, toggle_active_frame, construction_frame, construction_sub_btns))
    hunter_btn = Button(skill_frame, text="Hunter", image=hunter_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_hunter_frame(all_frames, toggle_active_frame, hunter_frame, hunter_sub_btns))

    skill_level_input_btn = Button(skill_frame, text="Input Skill Levels", image=skill_input_img, height=SKILL_BTN_HEIGHT, width=SKILL_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_skill_input_frame(skill_level_input_frame, toggle_active_frame, all_frames))

    # ---- SUB SKILL BTNS ----
    def new_script_start_btn(script_frame, script_name, script_state, root=root):
        btn_text = script_name.replace('_', ' ')
        return Button(script_frame, state=script_state, text=btn_text, image=start_btn_img, cursor=BTN_CURSOR, height=SCRIPT_START_BTN_HEIGHT, width=SCRIPT_START_BTN_WIDTH, bg='#545550', activebackground=BTN_ACTIVE_BG_COL, command=lambda: show_plg(script_name, root), relief='raised')

    #     Agility
    gnome_course_btn = new_script_start_btn(agility_frame, 'Gnome_Course', gnome_agility_script.btn_state)
    canifis_rooftops_btn = new_script_start_btn(agility_frame, 'Canifis_Rooftops', canifis_rooftops.btn_state)
    seers_rooftops_btn = new_script_start_btn(agility_frame, 'Seers_Rooftops', seers_rooftops.btn_state)
    ardy_rooftops_btn = new_script_start_btn(agility_frame, 'Ardy_Rooftops', ardy_rooftops_script.btn_state)
    agility_sub_btns = gnome_course_btn, canifis_rooftops_btn, seers_rooftops_btn, ardy_rooftops_btn

    #     Combat
    cow_killer_btn = new_script_start_btn(script_frame=combat_frame, script_name='Cow_Killer', script_state=cow_killer_script.btn_state)
    sand_crab_killer_btn = new_script_start_btn(combat_frame, 'Kourend_Crab_Killer', kourend_crab_killer_script.btn_state)
    combat_sub_btns = sand_crab_killer_btn, cow_killer_btn

    #     Cooking
    rogue_cooker_btn = new_script_start_btn(cooking_frame, 'Rogue_Cooker', rogue_cooker_script.btn_state)
    cooking_sub_btns = rogue_cooker_btn

    #     Crafting
    glass_blower_btn = new_script_start_btn(crafting_frame, 'GE_Glass_Blower', ge_glass_blower_script.btn_state)
    dhide_bodies_btn = new_script_start_btn(crafting_frame, 'GE_Dhide_Bodies', dhide_bodies_script.btn_state)
    crafting_sub_btns = glass_blower_btn, dhide_bodies_btn

    #     Construction
    larder_btn = new_script_start_btn(construction_frame, 'Poh_Larders', poh_larders_script.btn_state)
    table_btn = new_script_start_btn(construction_frame, 'Poh_Mahogany_Tables', poh_tables_script.btn_state)
    construction_sub_btns = larder_btn, table_btn

    #     Farming
    hosidius_plough_btn = new_script_start_btn(farming_frame, 'Hosidius_Plough', hosidius_plough_script.btn_state)
    sulfer_fert_btn = new_script_start_btn(farming_frame, 'GE_Sulphurous_Fertilizer', ge_sulphurous_fertilizer_script.btn_state)
    tithe_farmer_btn = new_script_start_btn(farming_frame, 'Tithe_Farmer', tithe_farmer_script.btn_state)
    farming_sub_btns = hosidius_plough_btn, sulfer_fert_btn, tithe_farmer_btn

    #     Fishing
    draynor_shrimp_btn = new_script_start_btn(fishing_frame, 'Draynor_Shrimp', draynor_shrimp_script.btn_state)
    barb_trout_btn = new_script_start_btn(fishing_frame, 'Barb_Trout', barb_trout_script.btn_state)
    barb_fishing_btn = new_script_start_btn(fishing_frame, 'Barbarian_Fishing', barb_fishing_script.btn_state)
    fishing_sub_btns = draynor_shrimp_btn, barb_trout_btn, barb_fishing_btn

    #     Fletching
    ge_dart_fletcher_btn = new_script_start_btn(fletching_frame, 'GE_Dart_Fletcher', ge_dart_fletcher_script.btn_state)
    ge_bow_stringer_btn = new_script_start_btn(fletching_frame, 'GE_Bow_Stringer', ge_bow_stringer_script.btn_state)
    fletching_sub_btns = ge_dart_fletcher_btn, ge_bow_stringer_btn

    #     Firemaking
    ge_log_burner_btn = new_script_start_btn(firemaking_frame, 'GE_Log_Burner', ge_log_burner_script.btn_state)
    firemaking_sub_btns = ge_log_burner_btn

    #     Herblore
    unf_pots_btn = new_script_start_btn(herblore_frame, 'GE_Unf_Pots', ge_unf_pots_script.btn_state)
    finished_pots_btn = new_script_start_btn(herblore_frame, 'GE_Finished_Pots', ge_finished_pots_script.btn_state)
    herblore_sub_btns = unf_pots_btn, finished_pots_btn

    #     Hunter
    crimson_swift_btn = new_script_start_btn(hunter_frame, 'Single_Trap_Crimsons', crimson_swift_script.btn_state)
    cerulean_twitch_btn = new_script_start_btn(hunter_frame, 'Double_Trap_Ceruleans', cerulean_twitches.btn_state)
    orange_lizards_btn = new_script_start_btn(hunter_frame, 'Desert_Lizards', desert_lizards_script.btn_state)
    red_lizards_btn = new_script_start_btn(hunter_frame, 'Red_Lizards', red_lizards_script.btn_state)
    black_lizards_btn = new_script_start_btn(hunter_frame, 'Black_Lizards', black_lizards_script.btn_state)
    red_chins_btn = new_script_start_btn(hunter_frame, 'Red_Chins', red_chins_script.btn_state)
    hunter_sub_btns = crimson_swift_btn, cerulean_twitch_btn, orange_lizards_btn, red_lizards_btn, black_lizards_btn, red_chins_btn

    #     Magic
    ardy_knight_splasher_btn = new_script_start_btn(magic_frame, "Ardy_Knight_Splasher", ardy_knight_splasher_script.btn_state)
    ge_superheat_gold_btn = new_script_start_btn(magic_frame, "GE_Superheat_Gold", ge_superheat_gold_script.btn_state)
    magic_sub_btns = ardy_knight_splasher_btn, ge_superheat_gold_btn

    #     Mining
    pisc_iron_btn = new_script_start_btn(mining_frame, "Pisc_Iron_Miner", pisc_iron_script.btn_state)
    motherlode_miner_btn = new_script_start_btn(mining_frame, "Motherlode_Miner", motherlode_mine_script.btn_state)
    mining_sub_btns = pisc_iron_btn, motherlode_miner_btn

    #     Prayer
    gilded_altar_btn = new_script_start_btn(prayer_frame, 'Gilded_Altar', gilded_altar_script.btn_state)
    prayer_sub_btns = gilded_altar_btn

    #     Runecrafting
    cwars_lavas_btn = new_script_start_btn(runecrafting_frame, 'Cwars_Lavas', cwars_lavas_script.btn_state)
    runecrafting_sub_btns = cwars_lavas_btn

    #     Smithing
    edge_gold_btn = new_script_start_btn(smithing_frame, "Edge_Gold", edge_gold_script.btn_state)
    blast_furnace_btn2 = new_script_start_btn(smithing_frame, "Blast_Furnace", blast_furnace_script.btn_state)
    ge_superheat_gold_btn2 = new_script_start_btn(smithing_frame, "GE_Superheat_Gold", ge_superheat_gold_script.btn_state)
    smithing_sub_btns = edge_gold_btn, blast_furnace_btn2, ge_superheat_gold_btn2

    #     Thieving
    draynor_man_btn = new_script_start_btn(thieving_frame, 'Draynor_Man', draynor_man_script.btn_state)
    ardy_cake_btn = new_script_start_btn(thieving_frame, 'Ardy_Cake', ardy_cake_script.btn_state)
    hosidius_fruit_btn = new_script_start_btn(thieving_frame, 'Hosidius_Fruit', hosidius_fruit_script.btn_state)
    ardy_knights_btn = new_script_start_btn(thieving_frame, 'Ardy_Knights', ardy_knight_script.btn_state)
    thieving_sub_btns = draynor_man_btn, ardy_cake_btn, hosidius_fruit_btn, ardy_knights_btn

    #     Woodcutting
    chop_fletcher_btn = new_script_start_btn(woodcutting_frame, 'Chop_Fletcher', chop_fletcher_script.btn_state)
    sw_teaks_btn = new_script_start_btn(woodcutting_frame, 'SW_Teaks', sw_teaks_script.btn_state)
    woodcutting_sub_btns = chop_fletcher_btn, sw_teaks_btn

    #     Minigames Buttons
    fishing_trawler_btn2 = new_script_start_btn(minigames_frame, "Fishing_Trawler", fishing_trawler_script.btn_state)
    nmz_btn2 = new_script_start_btn(minigames_frame, "NMZ", nmz_script.btn_state)
    tithe_farmer_btn2 = new_script_start_btn(minigames_frame, "Tithe_Farmer", tithe_farmer_script.btn_state)
    minigames_sub_btns = fishing_trawler_btn2, nmz_btn2, tithe_farmer_btn2


    main_gui_btns = gold_btn, skill_btn, minigames_btn, settings_btn, info_btn, bug_report_btn

    # (Main) Gold_gui_btns
    ge_unf_pots_btn = new_script_start_btn(money_making_frame, "GE_Unf_Pots", ge_unf_pots_script.btn_state)
    blast_furnace_btn2 = new_script_start_btn(money_making_frame, "Blast_Furnace", blast_furnace_script.btn_state)
    red_chins_btn2 = new_script_start_btn(money_making_frame, "Red_Chins", blast_furnace_script.btn_state)
    gold_gui_btns = ge_unf_pots_btn, blast_furnace_btn2, red_chins_btn2

    skill_gui_btns = attack_btn, hp_btn, minining_btn, \
                     strength_btn, agility_btn, smithing_btn, \
                     defence_btn, herblore_btn, fishing_btn, \
                     ranged_btn, thieving_btn, cooking_btn, \
                     prayer_btn, crafting_btn, firemaking_btn, \
                     magic_btn, fletching_btn, woodcutting_btn, \
                     runecrafting_btn, slayer_btn, farming_btn, \
                     construction_btn, hunter_btn, skill_level_input_btn

    return main_gui_btns, gold_gui_btns, skill_gui_btns, minigames_sub_btns


