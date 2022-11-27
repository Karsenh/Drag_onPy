from tkinter import StringVar, LabelFrame, Tk, Label, Entry
import os


def show_auth_gui():
    auth_top_height = 400
    auth_top_width = 600

    pwd = os.getcwd()
    auth_top = Tk()
    auth_top.title('Drag_onPy - Login')
    auth_top.iconbitmap(f'{pwd}\Assets\Images\Icon.ico')
    auth_top.configure(bg='#969488', height=auth_top_height, width=auth_top_width)

    # Auth Frame
    auth_frame = LabelFrame(auth_top, text="Login")
    auth_frame.grid(row=1, column=1, padx=100, pady=75)

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
    email_entry.grid(row=2, column=1, pady=5, padx=10)

    pass_label.grid(row=3, column=1, pady=5, padx=10)
    pass_entry.grid(row=4, column=1, pady=5, padx=10)

    auth_top.mainloop()

    return
