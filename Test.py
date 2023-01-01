import random

from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *


get_bluestacks_xy()
set_bluestacks_window_size()
capture_bluestacks()
clear_debug_log()

# random_human_actions(max_downtime_seconds=12)
# show_main_gui()
launch_script("Cwars_Teak")

# #
# for i in range(6, 8):
#     if not wait_for_img(img_name=f"teak_path_{i}", script_name="Cwars_Teak", should_click=True, threshold=0.95, max_wait_sec=15, y_offset=2, x_offset=2):
#         print(f"Couldn't find teak_path_{i} - Exiting.")

# does_img_exist(img_name="Teak_path_7", script_name="Cwars_Teak", threshold=0.9, should_click=True)

# setup_interface("west", 2, "up")
# wait_for_img(img_name="Ge_bank", script_name="GE_Dhide_Bodies", threshold=0.85, should_click=True, x_offset=30)
# wait_for_img(img_name="Banked_green_leather", script_name="GE_Dhide_Bodies", should_click=True, x_offset=35, img_sel="first")




