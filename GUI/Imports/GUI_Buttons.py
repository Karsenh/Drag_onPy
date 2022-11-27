from tkinter import *
from GUI.Imports.GUI_Frames import *
from Scripts.Skilling.Mining.Iron.Pisc_Iron import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *

from GUI.Imports.Script_Launch import *

btn_active_bg_color = '#972b29'
btn_bg_color = '#645747'


def get_all_btns(all_frames, all_images):
    # global is_active_gold
    # global is_active_skills
    # global is_active_pvm_pvp

    # ALL FRAMES
    main_frame, gold_frame, skill_frame, pvm_pvp_frame, skill_sub_frames = all_frames

    mining_frame, smithing_frame, agility_frame = skill_sub_frames

    # IMAGES
    main_gui_images, gold_gui_images, skill_gui_images, pvm_pvp_gui_images, skilling_sub_gui_images = all_images
    # Main_gui_images
    gold_img, skills_img, skull_img, settings_img, question_mark_img, bug_report_img = main_gui_images
    # Sub_gui_images
    cball_img = gold_gui_images
    attack_img, hp_img, mining_img, strength_img, agility_img, smithing_img = skill_gui_images
    ags_gmaul_img = pvm_pvp_gui_images

    # Sub_sub_gui_images
    # (Mining/Smithing)
    pisc_iron_img, edge_gold_img, gnome_course_img = skilling_sub_gui_images


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
    attack_btn = Button(skill_frame, text="Attack", image=attack_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color)
    hp_btn = Button(skill_frame, text="HP", image=hp_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color)
    minining_btn = Button(skill_frame, text="Mining", image=mining_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_mining_frame(all_frames, toggle_active_frame, iron_pisc_btn))

    strength_btn = Button(skill_frame, text="Strength", image=strength_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color)
    agility_btn = Button(skill_frame, text="Agility", image=agility_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_agility_frame(all_frames, toggle_active_frame, gnome_course_btn))
    smithing_btn = Button(skill_frame, text="Smithing", image=smithing_img, height=skill_btn_height, width=skill_btn_width, bg='#545550', activebackground=btn_active_bg_color, command=lambda: show_smithing_frame(all_frames, toggle_active_frame, edge_gold_btn))

    # (Sub-Skill) Sub_skill_gui_btns - passed into method directly
    #     Mining
    iron_pisc_btn = Button(mining_frame, text="Pisc Iron", image=pisc_iron_img, height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("pisc_iron"))
    #     Smithing
    edge_gold_btn = Button(smithing_frame, text="Edge Gold", image=edge_gold_img,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("edge_gold"))
    #     Agility
    gnome_course_btn = Button(agility_frame, text="Gnome Agility", image=gnome_course_img,  height=100, width=100, bg='#545550', activebackground=btn_active_bg_color, command=lambda: launch_script("gnome_course"))
    #     RuneCrafting
    #     Herblore
    #     Firemaking
    #     Woodcutting


    # Pvm_Pvp_Gui_Btns
    ags_gmaul_btn = Button(pvm_pvp_frame, text="Ags_Gmaul", image=ags_gmaul_img, bg='#545550', activebackground=btn_active_bg_color,)

    main_gui_btns = gold_btn, skill_btn, pvm_pvp_btn, settings_btn, info_btn, bug_report_btn
    gold_gui_btns = cball_btn
    skill_gui_btns = attack_btn, hp_btn, minining_btn, strength_btn, agility_btn, smithing_btn
    pvm_pvp_gui_btns = ags_gmaul_btn

    return main_gui_btns, gold_gui_btns, skill_gui_btns, pvm_pvp_gui_btns




