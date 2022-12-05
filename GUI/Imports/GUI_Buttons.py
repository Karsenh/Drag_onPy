from tkinter import *
from GUI.Imports.GUI_Frames import *
from Scripts.Skilling.Mining.Iron.Pisc_Iron import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *

from GUI.Imports.Script_Launch import *

btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def get_all_btns(all_frames, all_images):

    # ---------- FRAMES ----------
    # Primary Frames
    main_frame, gold_frame, skill_frame, pvm_pvp_frame, skill_sub_frames = all_frames

    # Skill (Secondary) Frames
    mining_frame, smithing_frame, agility_frame, \
    defence_frame, herblore_frame, fishing_frame, \
    ranged_frame, thieving_frame, cooking_frame, \
    prayer_frame, crafting_frame, firemaking_frame, \
    magic_frame, fletching_frame, woodcutting_frame, \
    runecrafting_frame, slayer_frame, farming_frame, \
    construction_frame, hunter_frame = skill_sub_frames

    # ---------- IMAGES ----------
    main_gui_images, gold_gui_images, skill_gui_images, pvm_pvp_gui_images, skilling_sub_gui_images = all_images
    # Main_gui_images
    gold_img, skills_img, skull_img, settings_img, question_mark_img, bug_report_img = main_gui_images
    # Sub_gui_images
    cball_img = gold_gui_images
    attack_img, hp_img, mining_img, \
    strength_img, agility_img, smithing_img, \
    defence_img, herblore_img, fishing_img, \
    ranged_img, thieving_img, cooking_img, \
    prayer_img, crafting_img, firemaking_img, \
    magic_img, fletching_img, woodcutting_img, \
    runecrafting_img, slayer_img, farming_img, \
    construction_img, hunter_img = skill_gui_images

    ags_gmaul_img = pvm_pvp_gui_images

    # Skilling SUB Images
    # (Mining/Smithing/Fishing)
    pisc_iron_img, edge_gold_img, gnome_course_img, draynor_shrimp_map, barb_trout_map, barb_fishing_map = skilling_sub_gui_images


    # MAIN_GUI_BTNS
    main_img_path = "Assets\Images\GUI_Images"
    main_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{main_img_path}\Main_image.png'))

    main_img_label = Label(main_frame, image=main_img, bg=frame_bg_color)
    main_img_label.image = main_img
    main_img_label.grid(row=1, column=1, columnspan=5, pady=60)

    gold_btn = Button(main_frame, text="Gold", bg=btn_bg_color, activebackground=btn_active_bg_color, image=gold_img, command=lambda: show_gold_frame(all_frames, gold_gui_btns, toggle_active_frame, gui_btns))
    skill_btn = Button(main_frame, text="Leveling", bg=btn_bg_color, activebackground=btn_active_bg_color, image=skills_img, command=lambda: show_skill_frame(all_frames, skill_gui_btns, toggle_active_frame, gui_btns))
    pvm_pvp_btn = Button(main_frame, text="PvP-PvM", bg=btn_bg_color, activebackground=btn_active_bg_color, image=skull_img, command=lambda: show_pvm_pvp_frame(all_frames, pvm_pvp_gui_btns, toggle_active_frame, gui_btns))

    settings_btn = Button(main_frame, text="Settings", bg=btn_bg_color, activebackground='#f7881c', image=settings_img, command=lambda: show_settings_frame(), height=50, width=50)
    info_btn = Button(main_frame, text="Info", bg=btn_bg_color, activebackground='#febf56', image=question_mark_img, command=lambda: print('Info test'), height=50, width=50)
    bug_report_btn = Button(main_frame, text="Bug Report", bg=btn_bg_color, activebackground='#81d5fa', image=bug_report_img, command=lambda: print('Bug test'), height=50, width=50)

    # Package up Gui_Btns to access values within each button
    gui_btns = gold_btn, skill_btn, pvm_pvp_btn

    # (Main) Gold_gui_btns
    cball_btn = Button(gold_frame, text="C'Balls", image=cball_img, bg='#545550', activebackground=btn_active_bg_color,)

    skill_btn_width = 100
    skill_btn_height = 60

    # (Main) Skill_gui_btns
    attack_btn = Button(skill_frame, state="disabled", text="Attack", image=attack_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color)
    hp_btn = Button(skill_frame, state="disabled", text="HP", image=hp_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color)
    minining_btn = Button(skill_frame, text="Mining", image=mining_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_mining_frame(all_frames, toggle_active_frame, mining_frame, mining_sub_btns))

    strength_btn = Button(skill_frame, state="disabled", text="Strength", image=strength_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color)
    agility_btn = Button(skill_frame, text="Agility", image=agility_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_agility_frame(all_frames, toggle_active_frame, agility_frame, agility_sub_btns))
    smithing_btn = Button(skill_frame, text="Smithing", image=smithing_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_smithing_frame(all_frames, toggle_active_frame, smithing_frame, smithing_sub_btns))

    defence_btn = Button(skill_frame, state="disabled", text="Defence", image=defence_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_defence_frame(all_frames, toggle_active_frame, defence_frame, defence_sub_btns))
    herblore_btn = Button(skill_frame, state="disabled", text="Herblore", image=herblore_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_herblore_frame(all_frames, toggle_active_frame, herblore_frame, herblore_sub_btns))
    fishing_btn = Button(skill_frame, text="Fishing", image=fishing_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_fishing_frame(all_frames, toggle_active_frame, fishing_frame, fishing_sub_btns))

    ranged_btn = Button(skill_frame, state="disabled", text="Ranged", image=ranged_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_ranged_frame(all_frames, toggle_active_frame, ranged_frame, ranged_sub_btns))
    thieving_btn = Button(skill_frame, text="Thieving", image=thieving_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_thieving_frame(all_frames, toggle_active_frame, thieving_frame, thieving_sub_btns))
    cooking_btn = Button(skill_frame, state="disabled", text="Cooking", image=cooking_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_firemaking_frame(all_frames, toggle_active_frame, cooking_frame, cooking_sub_btns))

    prayer_btn = Button(skill_frame, state="disabled", text="Prayer", image=prayer_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_ranged_frame(all_frames, toggle_active_frame, prayer_frame, prayer_sub_btns))
    crafting_btn = Button(skill_frame, state="disabled", text="Crafting", image=crafting_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_thieving_frame(all_frames, toggle_active_frame, crafting_frame, crafting_sub_btns))
    firemaking_btn = Button(skill_frame, text="Firemaking", image=firemaking_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_firemaking_frame(all_frames, toggle_active_frame, firemaking_frame, firemaking_sub_btns))

    magic_btn = Button(skill_frame, state="disabled", text="Magic", image=magic_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_ranged_frame(all_frames, toggle_active_frame))
    fletching_btn = Button(skill_frame, state="disabled", text="Fletching", image=fletching_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_thieving_frame(all_frames, toggle_active_frame, thieving_sub_btns))
    woodcutting_btn = Button(skill_frame, state="disabled", text="Woodcutting", image=woodcutting_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_firemaking_frame(all_frames, toggle_active_frame, firemaking_frame, firemaking_sub_btns))

    runecrafting_btn = Button(skill_frame, state="disabled", text="RuneCrafting", image=runecrafting_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_ranged_frame(all_frames, toggle_active_frame, runecrafting_frame, runecrafting_sub_btns))
    slayer_btn = Button(skill_frame, state="disabled", text="Slayer", image=slayer_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_thieving_frame(all_frames, toggle_active_frame, thieving_frame, thieving_sub_btns))
    farming_btn = Button(skill_frame, state="disabled", text="Farming", image=farming_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_firemaking_frame(all_frames, toggle_active_frame, firemaking_sub_btns))

    construction_btn = Button(skill_frame, state="disabled", text="Construction", image=construction_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_ranged_frame(all_frames, toggle_active_frame, construction_frame, construction_sub_btns))
    hunter_btn = Button(skill_frame, state="disabled", text="Hunter", image=hunter_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_thieving_frame(all_frames, toggle_active_frame, thieving_frame, thieving_sub_btns))

    # ---- SUB SKILL BTNS ----
    #     Attack

    #     HP

    #     Mining
    iron_pisc_btn = Button(mining_frame, text="Pisc Iron", image=pisc_iron_img, height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("pisc_iron"))
    mining_sub_btns = iron_pisc_btn

    #     Strength

    #     Agility
    gnome_course_btn = Button(agility_frame, text="Gnome Agility", image=gnome_course_img,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("gnome_course"))
    agility_sub_btns = gnome_course_btn

    #     Smithing
    edge_gold_btn = Button(smithing_frame, text="Edge Gold", image=edge_gold_img,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("edge_gold"))
    smithing_sub_btns = edge_gold_btn
    #     Defence
    defence_sub_btns = None
    #     Herblore
    herblore_sub_btns = None
    #     Fishing
    draynor_shrimp_btn = Button(fishing_frame, text="Draynor Shrimp", image=draynor_shrimp_map,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("draynor_shrimp"))
    barb_trout_btn = Button(fishing_frame, text="Barbarian Trout", image=barb_trout_map,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("barb_trout"))
    barb_fishing_btn = Button(fishing_frame, text="Barbarian Fishing", image=barb_fishing_map,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("barbarian_fishing"))
    fishing_sub_btns = draynor_shrimp_btn, barb_trout_btn, barb_fishing_btn

    #     Ranged
    ranged_sub_btns = None
    #     Thieving
    draynor_man_btn = Button(thieving_frame, text="Draynor Man", image=draynor_shrimp_map,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("draynor_man"))
    ardy_cake_btn = Button(thieving_frame, text="Ardougn Cake", image=draynor_shrimp_map,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("ardy_cake"))
    thieving_sub_btns = draynor_man_btn, ardy_cake_btn

    #     Cooking
    cooking_sub_btns = None
    #     Prayer
    prayer_sub_btns = None
    #     Crafting
    crafting_sub_btns = None
    #     Firemaking
    ge_log_burner_btn = Button(firemaking_frame, text="GE Log Burner", image=draynor_shrimp_map,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("ge_log_burner"))
    firemaking_sub_btns = ge_log_burner_btn
    #     Woodcutting

    #     Runecrafting
    runecrafting_sub_btns = None

    #     Construction
    construction_sub_btns = None

    # Pvm_Pvp_Gui_Btns
    ags_gmaul_btn = Button(pvm_pvp_frame, text="Ags_Gmaul", image=ags_gmaul_img, bg='#545550', activebackground=btn_active_bg_color,)

    main_gui_btns = gold_btn, skill_btn, pvm_pvp_btn, settings_btn, info_btn, bug_report_btn

    gold_gui_btns = cball_btn

    skill_gui_btns = attack_btn, hp_btn, minining_btn, \
                     strength_btn, agility_btn, smithing_btn, \
                     defence_btn, herblore_btn, fishing_btn, \
                     ranged_btn, thieving_btn, cooking_btn, \
                     prayer_btn, crafting_btn, firemaking_btn, \
                     magic_btn, fletching_btn, woodcutting_btn, \
                     runecrafting_btn, slayer_btn, farming_btn, \
                     construction_btn, hunter_btn

    pvm_pvp_gui_btns = ags_gmaul_btn

    return main_gui_btns, gold_gui_btns, skill_gui_btns, pvm_pvp_gui_btns




