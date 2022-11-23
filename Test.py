import sys
import time
from API.Mouse import *
from GUI.Main_GUI import *
from API.Imaging.Image import *
from API.AntiBan import *
from API.Interface import *
from API.Import_Libs.Coords import *
from Scripts.Skilling.Smithing.Gold.Edge_Gold import *

get_bluestacks_xy()
set_bluestacks_window_size()
capture_bluestacks()

# smith_gold_edge()
# get_color_at_coords(furnace_loc_check)

# check_skill_tab(max_sec=5.0)

# open_tab_color = 106, 35, 26
open_tab_color = 106, 35, 26
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
invent_color_xy = 1363, 291
mouse_move(invent_color_xy)

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

