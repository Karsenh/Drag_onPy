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
    skills_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Stats.png'))
    skull_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Skull.png'))

    settings_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Settings.png'))
    question_mark_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Question_Mark.png'))
    bug_report_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gui_images_path}\Bug.png'))


    # --------
    # SUB-GUIs
    # --------

    # Gold_Gui images
    gold_path = "Assets\Images\GUI_Images\Gold"
    cballs_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{gold_path}\Cballs.png'))

    # Skills_Gui images
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

    # PvM-PvP_Gui images
    pvm_pvp_path = "Assets\Images\GUI_Images\PvMPvP"
    ags_gmaul_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{pvm_pvp_path}\PvP\Ags_gmaul.png'))

    main_gui_images = gold_img, skills_img, skull_img, settings_img, question_mark_img, bug_report_img
    gold_gui_images = cballs_img
    skill_gui_images = attack_img, hp_img, mining_img, strength_img, agility_img, smithing_img, defence_img, herblore_img, fishing_img
    pvmpvp_gui_images = ags_gmaul_img

    # ---
    # SUB-SUB-GUIs
    # ---

    # Skill Sub-GUI
    skill_sub_path = "Assets\Images\GUI_Images\Stats"
    # (Map Button Images)
    #     Pisc_Iron
    iron_pisc_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Mining\Iron_Pisc.png'))
    #     Edge_Gold
    edge_gold_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Smithing\Edge_Gold.png'))
    #     Gnome Course
    gnome_course_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Agility\gnome_map.png'))
    # FISHING
    #     Draynor Shrimp
    barb_trout_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Fishing\Barb_Trout_map.png'))
    #     Barb Trout
    draynor_shrimp_map_img = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\{skill_sub_path}\Fishing\Draynor_Shrimp_map.png'))

    skilling_sub_gui_images = iron_pisc_img, edge_gold_img, gnome_course_img, draynor_shrimp_map_img, barb_trout_map_img

    return main_gui_images, gold_gui_images, skill_gui_images, pvmpvp_gui_images, skilling_sub_gui_images



