from API.Setup import get_bluestacks_region
from pytesseract import pytesseract
import pyautogui as pag
from API.Import_Libs.Paths import *
from PIL import Image

pytesseract.run_tesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_run():
    # Take screenshot of run energy
    x1, y1, x2, y2 = get_bluestacks_region()

    run_x1 = x1 + 1142
    run_y1 = y1 + 240
    run_x2 = 45
    run_y2 = 30

    pag.screenshot(imageFilename=fr'{ROOT_SCREENSHOTS_PATH}\Comparators\General\run_energy.png', region=(run_x1, run_y1, run_x2, run_y2))

    # Perform OCR
    run_img =  Image.open(fr'{ROOT_SCREENSHOTS_PATH}\Comparators\General\run_energy.png')

    test_string = pytesseract.image_to_string(run_img, config='--psm 6')

    print(f'test string: {test_string}')

    # Return integer value
    return
