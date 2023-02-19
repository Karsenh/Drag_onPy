import tkinter.messagebox

from GUI.Imports.GUI_Buttons import *
from GUI.Imports.GUI_Images import get_all_gui_images
from GUI.Imports.GUI_Frames import get_all_frames
from API.Setup import get_bluestacks_region
from tkinter import *
import os
import win32gui
from pynput import keyboard
import sys


TERMINATION_KEY = "Key.end"
IS_RUNNING = True


def should_be_running():
    return IS_RUNNING


def set_should_be_running(value):
    global IS_RUNNING
    IS_RUNNING = value
    print(f'IS_RUNNING: {IS_RUNNING}')
    return

# Main_Gui images
# def terminate_app(key, root):
#     if str(key) == TERMINATION_KEY:
#         print(f'⛔ Script Terminated by User - MainGUI')
#         root.destroy()
#         sys.exit(-99)


def show_main_gui():
    pwd = os.getcwd()
    root = Tk()
    root.title('Drag_onPy')
    root.iconbitmap(f'{pwd}\Icon.ico')
    root_gui_height = 1050
    root_gui_width = 550  #675
    root.configure(bg='#969488', height=root_gui_height, width=root_gui_width)

    # listener = keyboard.Listener(
    #     on_press=lambda event: terminate_app(event, root))
    # listener.start()

    dragon_py_hwnd = win32gui.FindWindow(None, 'Drag_onPy')
    if not dragon_py_hwnd:
        print(f'⛔ Drag_onPy window not found!')

    x1, y1, x2, y2 = get_bluestacks_region()

    # print(f'bs x1 y1: {x1}, {y1}')
    # x1y1 = x1, y1
    # x, y = translate_coords(x1y1, update_coords=True)
    app_x = x1 - root_gui_width
    app_y = y1

    # print(f'📈 app_x: {app_x} app_y: {app_y}')
    root.geometry(f"{root_gui_width}x{root_gui_height}+{app_x}+{app_y}")

    # win32gui.MoveWindow(dragon_py_hwnd, app_x, app_y, app_y2, app_x2, True)

    main_gui_row = 2
    footer_row = 4

    # Get all Frames & Images to send down into buttons
    all_frames = get_all_frames(root)
    all_images = get_all_gui_images()
    all_btns = get_all_btns(all_frames, all_images, root)

    # Get the Main_Gui from All_Btns  (Gold, Skill, and Minigames buttons not used)
    main_gui_btns, _, _, _ = all_btns

    # Get the Main_Gui btns out to use in root
    gold_btn, skill_btn, minigames_btn, settings_btn, info_btn, bug_report_btn = main_gui_btns

    gold_btn.grid(row=main_gui_row, column=1, pady=(15, 8), padx=15)
    skill_btn.grid(row=main_gui_row, column=2, pady=(15, 8), padx=15)
    minigames_btn.grid(row=main_gui_row, column=3, pady=(15, 8), padx=15)

    settings_btn.grid(row=footer_row, column=1, columnspan=1, pady=(15,10), padx=20)
    info_btn.grid(row=footer_row, column=2, columnspan=1, pady=(15,10))
    bug_report_btn.grid(row=footer_row, column=3, columnspan=1, pady=(15,10))

    def on_closing():

        if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
            set_should_be_running(False)
            root.destroy()

    root.protocol('WM_DELETE_WINDOW', on_closing)

    root.mainloop()

    return


