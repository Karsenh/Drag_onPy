from tkinter import StringVar, LabelFrame, Tk, Label, Entry, Button
import os
from GUI.Imports.GUI_Frames import btn_bg_color, btn_active_bg_color


def show_auth_gui():
    auth_top_height = 400
    auth_top_width = 400

    pwd = os.getcwd()
    auth_top = Tk()
    auth_top.title('Drag_onPy - Login')
    auth_top.iconbitmap(f'{pwd}\Assets\Images\Icon.ico')
    auth_top.configure(bg='#969488')
    auth_top.geometry(f"{auth_top_width}x{auth_top_height}")


    # Auth Frame
    auth_frame = LabelFrame(auth_top, text="Login")
    auth_frame.grid(row=1, column=1, padx=100, pady=75)
    auth_frame.place(anchor='center', relx=0.5, rely=0.5)

    # Entry value variables
    email_val = StringVar(auth_frame)
    pass_val = StringVar(auth_frame)

    # Labels and Entries
    email_label = Label(auth_frame, text="Email", anchor='w')
    email_entry = Entry(auth_frame, textvariable=email_val)

    pass_label = Label(auth_frame, text="Password")
    pass_entry = Entry(auth_frame, textvariable=pass_val)

    # Positioning
    email_label.grid(row=1, column=1, pady=5, padx=10)
    email_entry.grid(row=2, column=1, pady=5, padx=30)

    pass_label.grid(row=3, column=1, pady=5, padx=10)
    pass_entry.grid(row=4, column=1, pady=5, padx=30)

    login_btn = Button(auth_frame, text="Login", fg='white', width=15, bg=btn_bg_color, activebackground=btn_active_bg_color, command=lambda: print(f'Login fired'))
    login_btn.grid(row=5, column=1, columnspan=3, pady=20)

    auth_top.mainloop()

    return
