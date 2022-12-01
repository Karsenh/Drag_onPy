from datetime import datetime
import pyautogui as pag
from API.Setup import get_bluestacks_region
from API.Imaging.OCR.Helpers import process_and_ocr, capture_ocr_region
from API.Imports.Paths import *

saved_total_exp = None


# Wait 'x' seconds for total exp to change and returns True if it does within that time - otherwise returns False
def wait_for_exp_change(max_wait_sec=8, DEBUG=True):
    global saved_total_exp
    start_time = datetime.now()
    if DEBUG:
        print(f'⏲ Wait_For_Img Start Time: {start_time}')

    while not is_time_up(start_time, max_wait_sec):
        capture_ocr_region(window_x=1000, window_y=90, x2=100, y2=30, image_name="total_exp")

        curr_total_exp = process_and_ocr(image_name="total_exp")

        if not saved_total_exp:
            print(f'saved_total_exp not set - setting with {curr_total_exp}')
            saved_total_exp = curr_total_exp
        else:
            if curr_total_exp != saved_total_exp:
                print(f'✔ Curr_total_exp != Saved_total_exp | {curr_total_exp} != {saved_total_exp} - Something must be happening...')
                saved_total_exp = None
                return True
            else:
                print(f'🔎 Still OCRing for exp change...\nSaved_total_exp: {saved_total_exp}\ncurr_total_exp: {curr_total_exp}')

    saved_total_exp = None
    print(f'❌ Total_Exp Unchanged! is_exp_changing returning False...')
    return False


def is_time_up(start_time, max_wait_sec, DEBUG=True):
    curr_time = datetime.now()
    time_diff = curr_time - start_time
    if DEBUG:
        print(f'⏲ Time diff seconds: {time_diff.total_seconds()} | is {time_diff} > {max_wait_sec} ?')
    if time_diff.total_seconds() > max_wait_sec:
        print(f'✖ Time is up!')
        return True
    else:
        print(f'Time is not up yet...')
        return False