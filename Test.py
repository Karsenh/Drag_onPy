import random

from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *
from API.Imports.Paths import BS_SCREEN_PATH
from Scripts.Skilling.Woodcutting.Cwars_Teaks import is_rod_equipped, withdraw_new_rod


get_bluestacks_xy()
set_bluestacks_window_size()
capture_bluestacks()
clear_debug_log()

# random_human_actions(max_downtime_seconds=12)
# show_main_gui()
launch_script("GE_Dhide_Bodies")


# wait_for_img(img_name="Ge_bank", script_name="GE_Dhide_Bodies", threshold=0.88, should_click=True, x_offset=20)
# teak_color_xy = 1354, 788
# color_code = [177, 146, 92]  # 178, 147, 92
#
# diff_tolerance = 10
# teak_color = get_color_at_coords(teak_color_xy)
#
# i = 0
# for val in teak_color:
#     curr_diff = val - color_code[i]
#     if curr_diff < 0:
#         curr_diff * -1
#     if curr_diff > diff_tolerance:
#         print(f'Returning False')



# teak_color_xy = 1354, 788
# color_code = 177, 146, 92
# if color_code == get_color_at_coords(teak_color_xy):
#     print('FOUND COLOR')
# else:
#     print(f'No Color Found!')

# does_img_exist(img_name="teak_path_8", script_name="Cwars_Teak", threshold=0.90, should_click=True, x_offset=-4)


# does_img_exist(img_name="Teak_tree", script_name="Cwars_teak", should_click=True, threshold=0.8)
# open_color = 106, 35, 26
# find_color_xy(BS_SCREEN_PATH, open_color)

# does_img_exist(img_name="Equipped_rod", script_name="Cwars_Teak")
# wait_for_img(img_name="Teak_tree", script_name="Cwars_Teak", should_click=True, max_wait_sec=10)

# for i in range(3, 8):
#     if i < 8:
#         if wait_for_img(img_name=f"teak_path_{i}", script_name="Cwars_Teak", threshold=0.92, max_wait_sec=20):
#             if not does_img_exist(img_name=f"teak_path_{i}", script_name="Cwars_Teak", threshold=0.92,
#                                   should_click=True):
#                 print(f'does_path_img secondary search failed {i}.')
#         else:
#             print(f"Primary path_img search failed {i}")
#     else:
#         if wait_for_img(img_name="teak_path_8", script_name="Cwars_Teak", threshold=0.90, x_offset=-4, y_offset=6):
#             if not does_img_exist(img_name="teak_path_8", script_name="Cwars_Teak", threshold=0.90, x_offset=-4,
#                                   y_offset=6, should_click=True):
#                 print(f'Secondary last path search failed.')
#         else:
#             print(f'Primary path search ({i}) not found')

# does_img_exist(img_name="Teak_path_7", script_name="Cwars_Teak", threshold=0.9, should_click=True)

# setup_interface("west", 2, "up")
# wait_for_img(img_name="Ge_bank", script_name="GE_Dhide_Bodies", threshold=0.85, should_click=True, x_offset=30)
# wait_for_img(img_name="Banked_green_leather", script_name="GE_Dhide_Bodies", should_click=True, x_offset=35, img_sel="first")




