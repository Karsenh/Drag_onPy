import API.AntiBan
from API.Imaging.OCR.Helpers import capture_ocr_region, process_and_ocr
from API.Interface.General import is_tab_open
from API.Debug import write_debug
from API.Mouse import mouse_click

levels = []


def ocr_skill_levels():
    global levels

    is_tab_open(tab="skill", should_be_open=True)

    API.AntiBan.sleep_between(0.9, 1.4)

    total_xp_xy = 1351, 780

    mouse_click(total_xp_xy)
    API.AntiBan.sleep_between(0.6, 0.9)
    mouse_click(total_xp_xy)

    start_x = 1140
    start_y = 388

    curr_x_diff = 0
    curr_y_diff = 0

    for i in range(1, 24):
        # add 105 every x (horizontal) step
        # add 53 every thrid (mod 3 == 0) (vertical) step

        curr_x = start_x + curr_x_diff
        curr_y = start_y + curr_y_diff

        print(f'X {curr_x} | Y: {curr_y}')

        capture_ocr_region(curr_x, curr_y, 26, 19, image_name=f"Skill_Lvl_{i}")
        curr_level_string = process_and_ocr(image_name=f"Skill_Lvl_{i}")
        if curr_level_string:
            levels.append(int(curr_level_string))
        else:
            levels.append("n/a")

        curr_x_diff += 106.5

        if i % 3 == 0:
            print(f'End of the line - increasing Y(53) and resetting x(from: {curr_x_diff} to 0)')
            curr_x_diff = 0
            curr_y_diff += 53.5

    is_tab_open(tab="inventory", should_be_open=True)

    print(f'Levels: {levels}')
    return
