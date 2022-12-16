import os
import sys
import time

import API.AntiBan
import Scripts.Skilling.Prayer.Gilded_Altar
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
from Scripts.MiniGames.Fishing_Trawler import repair_hole_until_finished, start_trawling
import pyautogui as pag
from API.Imaging.OCR.Skill_Levels import get_skill_level
from API.Interface.Bank import check_withdraw_qty
from Scripts.Skilling.Thieving.Stalls.Hosidius_Fruit import start_stealing_fruit


get_bluestacks_xy()
set_bluestacks_window_size()
capture_bluestacks()
clear_debug_log()

# random_human_actions(max_downtime_seconds=12)
# show_main_gui()
launch_script("barbarian_fishing")




# UNF POTS



# GILDED ALTAR
# does_img_exist(img_name="phials", script_name="Gilded_Altar", threshold=0.75, should_click=True)
# if wait_for_img(img_name="phials", script_name="Gilded_Altar", threshold=0.75, max_wait_sec=6):
#     does_img_exist(img_name="phials", script_name="Gilded_Altar", threshold=0.75)
#     mouse_click(INVENT_slot_1)
#     phials_xy = get_existing_img_xy()
#     mouse_click(phials_xy)
#     pag.press('3')
#
# API.AntiBan.sleep_between(2.0, 2.1)
#
# # if wait_for_img(img_name="house_ad", script_name="Gilded_Altar", threshold=0.9):
# #     does_img_exist(img_name="house_ad", script_name="Gilded_Altar", threshold=0.9)
# #     ad_xy = API.Imaging.Image.get_existing_img_xy()
# #     mouse_move(ad_xy)
# #     visit_last_xy = 679, 723
# #     mouse_drag(from_xy=ad_xy, to_xy=visit_last_xy)

# Click workless' arrow on house ad
# mouse_click(house_ad_tile_xy)

# # Wait for house_ad image (we're next to house ad)
# if wait_for_img(img_name="house_ad", script_name="Gilded_Altar", threshold=0.75, max_wait_sec=8):
#     if curr_loop == 1:
#         # mouse click to search for workless ad
#         does_img_exist(img_name="house_ad", script_name="Gilded_Altar", threshold=0.75, should_click=True)
#         API.AntiBan.sleep_between(1.5, 1.7)
#         does_img_exist(img_name="workless_ad", script_name="Gilded_Altar", threshold=0.99, should_click=True,
#                        x_offset=700, y_offset=20)
#         does_img_exist(img_name="og_ad", script_name="Gilded_Altar", threshold=0.99, should_click=True,
#                        x_offset=700, y_offset=20)
#     else:
#         # visit last
#         does_img_exist(img_name="house_ad", script_name="Gilded_Altar", threshold=0.9)
#         ad_xy = API.Imaging.Image.get_existing_img_xy()
#         mouse_move(ad_xy)
#         visit_last_xy = 679, 723
#         mouse_drag(from_xy=ad_xy, to_xy=visit_last_xy)
#
#     API.AntiBan.sleep_between(6.0, 6.1)
#     mouse_click(altar_xy)

# cl = 1
# Scripts.Skilling.Prayer.Gilded_Altar.start_gilded_altar(cl)

# scroll_xy = 640, 564
# mouse_move(scroll_xy)
# API.AntiBan.sleep_between(0.8, 1.1)
# pag.hscroll(-22)

# global phials_xy
#
# portal_xy = 1339, 133
# click_portal_xy = 704, 337
#
# mouse_click(portal_xy)
# API.AntiBan.sleep_between(5.0, 5.1)
#
# mouse_click(click_portal_xy)
# API.AntiBan.sleep_between(6.0, 6.1)
#
# mouse_click(phials_xy)
# API.AntiBan.sleep_between(5.0, 5.1)



