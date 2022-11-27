from API.Imaging.OCR.Helpers import *


def read_run():
    # Take screenshot of run energy

    # Capture screenshot of run energy
    capture_run_energy()

    # img_path = fr'{ROOT_SCREENSHOTS_PATH}\Comparators\General\run_energy.png'
    #
    # # Read the run energy image
    # run_img = cv2.imread(img_path)
    #
    # # Invert the image
    # inverted_img = invert_image(run_img)
    #
    # # Grayscale image
    # gray_img = gray_scale_image(inverted_img)
    #
    # # Sharpen image
    # sharp_img = sharpen_image(gray_img)
    #
    # # Sharpen image a different way
    # sharp_alt_img, thresh = alt_sharpen_image(gray_img)
    #
    # # Remove noise
    # no_noise_img = noise_removal(sharp_img)
    #
    # dpi_img = Image.fromarray(no_noise_img)
    # dpi_img.save(fr'{ROOT_SCREENSHOTS_PATH}\Comparators\General\run_energy_dpi.png')
    #
    # ocr_string1 = ocr_image(dpi_img)
    # print(f'OCR string 🅰: {ocr_string1}')
    #
    # no_noise_img_alt = noise_removal_alt(sharp_alt_img)
    #
    # dpi_img2 = Image.fromarray(no_noise_img_alt)
    # dpi_img2.save(fr'{ROOT_SCREENSHOTS_PATH}\Comparators\General\run_energy_dpi_alt.png')
    #
    # ocr_string2 = ocr_image(dpi_img2)
    # print(f'OCR string (alt) 🅱: {ocr_string2}')

    # process_and_ocr()
    # process_and_ocr2()

    return
