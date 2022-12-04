import sys
import time
from API.Mouse import *
from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.AntiBan import *
from API.Interface import *
from API.Imports.Coords import *
from enum import Enum
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *
from API.Imaging.OCR.Run_Energy import *
from Scripts.Skilling.Thieving.Stalls.Ardy_Cake import steal_ardy_cake
from API.Imaging.OCR.Total_Exp import wait_for_exp_change
# from Scripts.Skilling.Agility.Gnome_Course import *
from GUI.Auth_GUI import *
from Scripts.Skilling.Fishing.Trout.Barb_Trout import fish_barb_trout
from Scripts.Skilling.Fishing.Barbarian.Barbarian_Fishing import barbarian_fishing
from Scripts.Skilling.Firemaking.GE_Log_Burner import burn_logs_at_ge, burn_logs
import pyautogui as pag

get_bluestacks_xy()
set_bluestacks_window_size()
capture_bluestacks()
clear_debug_log()

# random_human_actions(max_downtime_seconds=12)
# show_main_gui()
# launch_script("ge_log_burner")

random_scroll = random.randint(-350, 350)
write_debug(f'Scrolling: {random_scroll}')
pag.hscroll(random_scroll)
random_scroll = random.randint(-350, 350)
write_debug(f'Scrolling: {random_scroll}')
pag.hscroll(random_scroll)

# curr_loop = 1
# steal_ardy_cake(curr_loop)
# pickpocket_draynor_man()



# does_img_exist("leaping_trout", script_name="Barbarian_Fishing", category="Scripts", threshold=0.8, should_click=True, x_offset=15, y_offset=50)

# cur_loop = 1
# barbarian_fishing(cur_loop)
# print(f'Does shrimp spot exist: {does_img_exist(img_name="shrimp_spot", script_name="Draynor_Shrimp")}')
# print(f'Does shrimp spot exist: {does_img_exist(img_name="bank_spot", script_name="Draynor_Shrimp")}')
#
# xy = get_existing_img_xy()
#
# mouse_click(xy)

# does_img_exist(img_name="bank_booth", script_name="Draynor_Shrimp", threshold=.95, should_click=True)
# curr_loop = 1
# fish_draynor_shrimp(curr_loop)
# wait_for_img(img_to_search="is_fishing", script_name="Draynor_Shrimp", category_name="Scripts", max_wait_sec=4, img_threshold=0.65)

# does_img_exist(img_name="trout_spot", script_name="Barb_Trout", category="Scripts", threshold=0.8, should_click=True, x_offset=20, y_offset=45)
# is_fishing = does_img_exist(img_name="is_fishing_trout", script_name="Barb_Trout", category="Scripts", threshold=0.65, should_click=True)
# print(f'is_fishing_trout: {is_fishing}')

# does_img_exist(img_name="is_fishing_trout", script_name="Barb_Trout", category="Scripts", should_click=True, threshold=0.80)


# capture_total_exp()
# process_and_ocr()
# is_exp_changing(max_wait_sec=10)


# launch_script("barb_trout")
# is_tab_open("inventory", should_open=False)

# # color_xy = 875, 708
# check_color = (63, 214, 221)
# # print(f'Color @ coords {color_xy}: {check_color}')
#
# x, y = find_color_xy(BS_SCREEN_PATH, check_color)
# print(f'x: {x} | y: {y}')
#
# move_to_xy = x[len(x)-1], y[len(y)-1]
# mouse_move(move_to_xy)

# does_exist = does_color_exist(check_color)
# print(f'Does exist? {does_exist}')

# read_run()

# get_color_at_coords(xy)

# show_main_gui()
# show_auth_gui()
# run_gnome_course()
# run_on = 1210, 255
# xy = 724, 735
# print(f'color: {get_color_at_coords(xy)}')

# color = get_color_at_coords(run_on)

# run off = 1211, 255 = (139, 94, 54)
# run on = 1211, 255 = (236, 218, 103)
# capture_bluestacks()
# image = Image.open()
# picture = image.load()



# Run ON    1210, 255 = (236, 218, 103)
# Run OFF   1210, 255 = (145, 100, 59)

# Run OUT   93+     - 1206, 230 = (14, 14, 14)
# Run OUT   85+     - 1214, 233 = (12, 12, 12)
# Run OUT   80+     - 1219, 235 = (11, 11, 11)
# Run OUT   76+     - 1219, 236 = (11, 11, 11)
# Run OUT   70+     - 1219, 241 = (6, 5, 4)
# Run OUT   12+     - 1215, 265 = (11, 11, 11)

# xy = 1215, 265
# off_color = 11, 11, 11
# if get_color_at_coords(xy) > off_color:
#     print(f'We have more than 10% run energy!')
# else:
#     print(f'LESS THAN 10% REMAINING!')
#
# is_run_gt(percent=10)



# capture_bluestacks()
# pyautogui.screenshot(imageFilename=fr'{ROOT_SCREENSHOTS_PATH}\Test.png')
#
# image = Image.open(f'{ROOT_SCREENSHOTS_PATH}\Test.png')
# picture = image.load()
# colors = image.getpixel((3113, 307))
# xy = 3113, 307
# print(f'colors: {colors}')
#  3116 443


# print(f'RGB Color @ {x}, {y} = {picture[x, y]}')
# smith_gold_edge()
# get_color_at_coords(furnace_loc_check)

# check_skill_tab(max_sec=5.0)

# open_tab_color = 106, 35, 26

# class script_enum(Enum):
#     PISC_IRON = 0
#     EDGE_GOLD = 1
#
#
# open_tab_color = 106, 35, 26


# inventory_tab_xy      1426, 392
# equipment_tab_xy      1426, 460
# stat_tab_xy           1431, 522
# quest_tab_xy          1426, 591
# music_tab_xy          1426, 655
# settings_tab_xy       1426, 722
# exit_tab              1426, 787

# x, y = find_color_xy(BS_SCREEN_PATH, open_tab_color)
#
# open_tab_coords = x[len(x)-3], y[len(y)-3]
# print(f'Current open tab coords = {open_tab_coords}')
# check_if_tab_open("quest")
# get_color_at_coords(SKILL_tab_xy)
# check_if_tab_open("quest", should_open=True)
# sleep_between(0.5, 0.9)
# quest_list_hover_xy = 1212, 574
# mouse_move(quest_list_hover_xy, 21, 19)
# sleep_between(0.3, 1.2)
# random_scroll = random.randint(-389, -320)
# print(f'{random_scroll}')
# pag.hscroll(random_scroll)
# sleep_between(0.5, 1.6)

# xy =
# mouse_move(xy)

#

# GETTING COLORS & LOCATIONS

# coords = 1363, 291
# print(f'Color: {get_color_at_coords(INVENT_tab_xy)}')
# invent_color_xy = 1363, 291
# mouse_move(invent_color_xy)

# r, g, b = get_color_at_coords(BANK_qty_all)

# obj_1_xy = 1218, 181
# obj_2_xy = 741, 800
# obj_3_xy = 1268, 270
# objs_to_check = [obj_1_xy, obj_2_xy, obj_3_xy]
# for obj_xy in objs_to_check:
#     curr_color = get_color_at_coords(obj_xy)
#     print(f'Color at xy: {obj_xy} = {curr_color}')

    # ore_1_xy = 1218, 181
    # ore_2_xy = 741, 800
    # ore_3_xy = 1268, 270
    # ore_objs = ore_1_xy, ore_2_xy, ore_3_xy
    #
    # ore_1_color = 56, 90, 76
    # ore_2_color = 108, 78, 50
    # ore_3_color = 99, 111, 153
    # ore_colors = ore_1_color, ore_2_color, ore_3_color
# does_img_exist("goldsmith_gauntlets", script_name='Edge_Gold', threshold=.99)

# BANKING
# check_if_bank_tab_open(1)
# check_if_bank_tab_open(3)
# check_if_bank_tab_open(6)
# does_img_exist("goldsmith_gauntlets", script_name="Edge_Gold", threshold=0.99)
# print(f'xy = {get_existing_img_xy()}')
# xy = get_existing_img_xy()
# x, y = xy
# new_xy = x+30, y+20
# mouse_click(new_xy)


# INVENTORY
# drop_inventory(5, 10)



# MOUSE
# from_xy = 700, 440
# to_xy = 1200, 440
# mouse_drag(from_xy, to_xy)
#
# from_xy = 700, 440
# to_xy = 1225, 440
# mouse_drag(from_xy, to_xy)

