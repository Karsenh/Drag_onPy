from GUI.Main_GUI import *
from API.Debug import clear_debug_log
from API.Imaging.Image import *
from API.Imaging.OCR.Run_Energy import *

# from Scripts.Skilling.Agility.Gnome_Course import *


get_bluestacks_xy()
set_bluestacks_window_size()
capture_bluestacks()
clear_debug_log()

# random_human_actions(max_downtime_seconds=12)
# show_main_gui()
launch_script("ge_glass_blower")


# wait_for_img(img_name="mobile_settings_tab", category="Interface", should_click=True)

# wait_for_img(img_name="banked_yew_log", script_name="GE_Log_Burner", threshold=0.95, should_click=True)

# get_skill_level("crafting")


# does_img_exist(img_name="aggro_path_a_0", script_name="Kourend_Crab_Killer", threshold=0.98, should_click=True)


# does_img_exist(img_name=f"inventory_monkfish", script_name="Ardy_Knights", should_click=True, threshold=0.95)

# wait_for_img(img_name="bank_tile", script_name="Ardy_Knights")




# wait_for_img(img_name="jump_1", script_name="Seers_Rooftops", threshold=0.9)

# handle_auth_screens()

# setup_interface("west", 4, "down")


# is_hp_gt(50)

# set_curr_tile()


# wait_for_img(img_name="trap_1_down", script_name="Double_Trap_Ceruleans", threshold=0.80)


# start_seers_rooftops(1)



# wait_for_img(img_name="restart_course", script_name="Seers_Rooftops", threshold=0.9, should_click=True)
# 1. Search for high-alch and click
# if not wait_for_img(img_name='high_alch', script_name='Seers_Rooftops', threshold=0.8, should_click=True):
#     # 2. If not found - check if Magic tab is open and search for high-alch again, clicking if found.
#     if is_tab_open("magic", should_open=True):
#         if not wait_for_img(img_name='high_alch', script_name='Seers_Rooftops', threshold=0.9, should_click=True):
#             print(f"Couldn't find alchemy spell despite magic tab being open")
#             # return False
#     else:
#         print(f"Couldn't open magic tab")
#         # return False
# else:
#     # 3. Hover mouse over magic_long_note with High-alch selected, waiting for agility exp before left clicking
#     if wait_for_img(img_name="magic_long_note", script_name="Seers_Rooftops", x_offset=4, y_offset=4):
#         mouse_move(get_existing_img_xy())
#
#
# if wait_for_img(img_name="agility_exp", script_name="Seers_Rooftops", max_wait_sec=15):
#     pag.leftClick();


# is_tab_open("magic", should_open=True)

# wait_for_img(img_name="Agility_exp", script_name="Seers_Rooftops", threshold=0.9, max_wait_sec=20)

# check_color = 106, 35, 26
# x_arr, y_arr = find_color_xy(BS_SCREEN_PATH, check_color)
#
# if len(x_arr) > 0:
#     x_check = x_arr[len(x_arr) - 8]
#     y_check = y_arr[len(y_arr) - 8]
#     print(f'x: {x_check} y: {y_check}')
#     xy = x_check, y_check
#     mouse_move(xy)
# else:
#     print('Couldnt find the color')




# does_color_exist(check_color)

# wait_for_img(img_name="o4_restart", script_name="Canifis_Rooftops", threshold=0.75, should_click=True, y_offset=4, max_wait_sec=8)
# wait_for_img(img_name="mog_on_2", script_name="Canifis_Rooftops", threshold=0.92, should_click=True, max_wait_sec=6, x_offset=4, y_offset=8)
#

# wait_for_img(img_name="o1_alt", script_name="Canifis_Rooftops", threshold=0.85, should_click=True, max_wait_sec=15,
#              y_offset=13, x_offset=4)

# does_img_exist(img_name="o1_alt", script_name="Canifis_Rooftops", threshold=0.9, should_click=True)

# wait_for_img(img_name='o7_from_broken', script_name="Canifis_Rooftops", threshold=0.9, should_click=True, max_wait_sec=10)


# does_img_exist(img_name="mog_3", script_name="Canifis_Rooftops", threshold=0.9, should_click=True)


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



