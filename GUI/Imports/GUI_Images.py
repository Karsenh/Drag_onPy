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

    start_btn_img_path = "Assets\Images\GUI_Images\Show_Info_Btn.png"
    start_btn_img = ImageTk.PhotoImage(Image.open(start_btn_img_path))

    skilling_sub_gui_images = start_btn_img

    # -----------------------------------------------------------------------------------------

    return main_gui_images, gold_gui_images, skill_gui_images, minigames_images, skilling_sub_gui_images




