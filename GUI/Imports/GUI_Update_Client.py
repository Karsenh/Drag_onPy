import webbrowser
import os
from Database.Connection import CURR_CLIENT_VERSION, INTENDED_CLIENT_VERSION, get_intended_version
from tkinter import *

DOWNLOAD_LINK = 'http://localhost:3000/install'


def show_update_client_gui():
    update_top_height = 500
    update_top_width = 450

    FRAME_BG_COL = '#969488'
    LABEL_FRAME_BG_COL = '#a5a195'
    BTN_ACTIVE_BG_COL = '#972b29'
    BTN_BG_COL = '#645747'

    pwd = os.getcwd()
    update_client_gui = Tk()
    update_client_gui.title('Drag_onPy - Login')
    update_client_gui.iconbitmap(f'{pwd}\Icon.ico')
    update_client_gui.configure(bg='#676157')
    update_client_gui.geometry(f"{update_top_width}x{update_top_height}")

    # Auth Frame
    form_frame = Frame(update_client_gui, bg=LABEL_FRAME_BG_COL)


    # Entry value variables
    # Labels and Entries
    curr_client_version_label = Label(form_frame, text=f"Your client version: {CURR_CLIENT_VERSION}", pady=10, background=LABEL_FRAME_BG_COL)
    required_client_version_label = Label(form_frame, text=f"Required client version: {get_intended_version()}", pady=10, background=LABEL_FRAME_BG_COL)

    # Positioning
    form_frame.grid(row=1, column=1)
    form_frame.place(anchor="center", relx=0.5, rely=0.5, height=300, width=250)
    # form_frame.place(anchor='center', relx=0.5, rely=0.5)

    curr_client_version_label.grid(row=2, column=1)
    curr_client_version_label.place(anchor='w', relx=0.1, rely=0.2)

    required_client_version_label.grid(row=4, column=1)
    required_client_version_label.place(anchor='w', relx=0.1, rely=0.5)

    update_link_btn = Button(form_frame, text="Update Client", fg='white', width=15, bg=BTN_BG_COL, activebackground=BTN_ACTIVE_BG_COL, command=lambda: open_update_link_in_browser())
    update_link_btn.grid(row=6, column=1, columnspan=3, pady=20)
    update_link_btn.place(anchor="center", relx=0.5, rely=0.85, height=30)

    update_client_gui.mainloop()
    return


def open_update_link_in_browser():
    webbrowser.open(DOWNLOAD_LINK)
    return