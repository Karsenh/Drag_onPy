import API.AntiBan
from API.Interface.General import setup_interface
from API.Imaging.Image import wait_for_img, does_img_exist

script_name = "Kourend_Crab_Killer"

clicked_crabs = 0
should_reset_aggro = False


def start_killing_kourend_crabs(curr_loop):
    global clicked_crabs
    global should_reset_aggro
    # if curr_loop == 1:
    #     setup_interface("west", 1, "up")

    if should_reset_aggro:
        for i in range(0, 4):
            if does_img_exist(img_name=f"agro_path_{i}", script_name=script_name, threshold=0.99, should_click=True):
                API.AntiBan.sleep_between(4.5, 4.6)
        should_reset_aggro = False
    else:
        while wait_for_img(img_name="hp_exp", script_name=script_name, max_wait_sec=6, threshold=0.95):
            clicked_crabs = 0
            return True
        else:
            if clicked_crabs > 3:
                should_reset_aggro = True
                return True

        for i in range(1, 10):
            if does_img_exist(img_name=f"crab_{i}", script_name=script_name, threshold=0.95, should_click=True):
                API.AntiBan.sleep_between(4.7, 4.8)
                return True

        clicked_crabs += 1

    return True
