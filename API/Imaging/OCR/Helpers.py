from API.Interface.General import *
from API.Imports.Paths import *
from pytesseract import pytesseract
import cv2
import numpy as np
import os


def capture_ocr_region(window_x, window_y, x2, y2, image_name):
    pwd = os.getcwd()
    ROOT_OCR_PATH = fr"{pwd}\API\Imaging\OCR\Captures"
    x1, y1, _, _ = get_bluestacks_region()

    run_x1 = x1 + window_x
    run_y1 = y1 + window_y
    run_x2 = x2
    run_y2 = y2
    img_path = fr'{ROOT_OCR_PATH}\{image_name}.png'

    pag.screenshot(imageFilename=img_path, region=(run_x1, run_y1, run_x2, run_y2))
    return


def invert_image(image):
    # INVERSION
    inverted_img = cv2.bitwise_not(image)
    return inverted_img


def gray_scale_image(inverted_image):
    # GRAYSCALE

    img_gray = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2GRAY)
    return img_gray


def sharpen_image(gray_image, black_intensity=150, white_intensity=250, should_invert=False):
    # THRESHOLD / SHARPENING
    #     sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 20, -1], [-1, -1, -1]])
    sharpen = cv2.filter2D(gray_image, -1, sharpen_kernel)

    if not should_invert:
        thresh = cv2.threshold(sharpen, black_intensity, white_intensity, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    else:
        thresh = cv2.threshold(sharpen, black_intensity, white_intensity, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    return thresh


def noise_removal(image, blur=1):
    # NOISE REMOVAL
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)

    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)

    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    image = cv2.medianBlur(image, blur)

    return image


def ocr_image(noiseless_image):
    ocr_string = pytesseract.image_to_string(noiseless_image, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    return ocr_string


def process_and_ocr(image_name):
    pwd = os.getcwd()
    ROOT_OCR_PATH = fr"{pwd}\API\Imaging\OCR\Captures"
    img = cv2.imread(fr'{ROOT_OCR_PATH}\{image_name}.png')

    # RESIZE
    resized_img = cv2.resize(img, None, fx=7.0, fy=7.0)
    cv2.imwrite(fr'{ROOT_OCR_PATH}\{image_name}_resized_2.png', resized_img)

    # CVT
    cvt_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(fr'{ROOT_OCR_PATH}\{image_name}_cvt_3.png', cvt_img)

    # EXTRACT COLOR
    lows = np.array([0, 105, 0])
    highs = np.array([255, 255, 255])

    color_iso_img = cv2.inRange(cvt_img, lows, highs)
    cv2.imwrite(fr'{ROOT_OCR_PATH}\{image_name}_color_iso_4.png', color_iso_img)

    # SHARPEN
    sharp_img = sharpen_image(color_iso_img, black_intensity=150, white_intensity=250, should_invert=True)
    cv2.imwrite(fr'{ROOT_OCR_PATH}\{image_name}_sharp_5.png', sharp_img)

    # NOISE
    no_noise = noise_removal(sharp_img)
    cv2.imwrite(fr'{ROOT_OCR_PATH}\{image_name}_noiseless_6.png', no_noise)

    # OCR
    ocr_string = ocr_image(no_noise)
    if ocr_string:
        ocr_string = int(ocr_string)
        print(f'OCR STRING: {ocr_string}')

    return ocr_string


