from GUI.Imports.GUI_Buttons import *
from GUI.Imports.GUI_Images import get_all_gui_images
from GUI.Imports.GUI_Frames import get_all_frames
from tkinter import *
import os


# Main_Gui images


def show_main_gui():
    pwd = os.getcwd()
    root = Tk()
    root.title('Drag_onPy')
    root.iconbitmap(f'{pwd}\Assets\Images\Icon.ico')
    root_gui_height = 847
    root_gui_width = 675  #675
    root.configure(bg='#969488', height=root_gui_height, width=root_gui_width)

    dragon_py_hwnd = win32gui.FindWindow(None, 'Drag_onPy')
    if not dragon_py_hwnd:
        print(f'⛔ Drag_onPy window not found!')

    x1, y1, x2, y2 = get_bluestacks_region()

    print(f'bs x1 y1: {x1}, {y1}')
    # x1y1 = x1, y1
    # x, y = translate_coords(x1y1, update_coords=True)
    app_x = x1 - root_gui_width
    app_y = y1

    print(f'📈 app_x: {app_x} app_y: {app_y}')
    root.geometry(f"675x847+{app_x}+{app_y}")

    # win32gui.MoveWindow(dragon_py_hwnd, app_x, app_y, app_y2, app_x2, True)

    main_gui_row = 2
    footer_row = 4

    # Get all Frames & Images to send down into buttons
    all_frames = get_all_frames(root)
    all_images = get_all_gui_images()
    all_btns = get_all_btns(all_frames, all_images)

    # Get the Main_Gui from All_Btns  (Gold, Skill, and Pvm_Pvp buttons not used)
    main_gui_btns, _, _, _ = all_btns

    # Get the Main_Gui btns out to use in root
    gold_btn, skill_btn, pvm_pvp_btn, settings_btn, info_btn, bug_report_btn = main_gui_btns

    gold_btn.grid(row=main_gui_row, column=1, pady=20, padx=15)
    skill_btn.grid(row=main_gui_row, column=2, pady=20, padx=15)
    pvm_pvp_btn.grid(row=main_gui_row, column=3, pady=20, padx=15)

    settings_btn.grid(row=footer_row, column=1, columnspan=1, pady=20, padx=20)
    info_btn.grid(row=footer_row, column=2, columnspan=1, pady=20)
    bug_report_btn.grid(row=footer_row, column=3, columnspan=1, pady=20)

    root.mainloop()
    return


def exit_app():
    exit(-1)
    return

