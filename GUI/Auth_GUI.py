from tkinter import StringVar, LabelFrame, Tk, Label, Entry, Button, Frame
import os
import re

from API.Debug import write_debug
from Database.Script_Access import set_script_access
from GUI.Imports.GUI_Frames import btn_bg_color, btn_active_bg_color, frame_bg_color, label_frame_bg_color
from Database.Connection import get_user
from GUI.Main_GUI import show_main_gui


def show_auth_gui():
    auth_top_height = 500
    auth_top_width = 450

    pwd = os.getcwd()
    auth_top = Tk()
    auth_top.title('Drag_onPy - Login')
    auth_top.iconbitmap(f'{pwd}\Icon.ico')
    auth_top.configure(bg='#676157')
    auth_top.geometry(f"{auth_top_width}x{auth_top_height}")


    # Auth Frame

    form_frame = Frame(auth_top, bg=label_frame_bg_color)

    # Entry value variables
    email_val = StringVar(form_frame)
    pass_val = StringVar(form_frame)

    form_vals = email_val, pass_val

    # Labels and Entries
    email_label = Label(form_frame, text="Email", pady=10, background=label_frame_bg_color)
    email_entry = Entry(form_frame, textvariable=email_val)

    pass_label = Label(form_frame, text="Password", pady=10, background=label_frame_bg_color)
    pass_entry = Entry(form_frame, textvariable=pass_val, show="✖")

    # Positioning
    form_frame.grid(row=1, column=1)
    form_frame.place(anchor="center", relx=0.5, rely=0.5, height=300, width=250)
    # form_frame.place(anchor='center', relx=0.5, rely=0.5)

    email_label.grid(row=2, column=1)
    email_label.place(anchor='w', relx=0.1, rely=0.2)
    email_entry.grid(row=3, column=1, columnspan=1, pady=5, padx=30)
    email_entry.place(anchor='w', relx=0.1, rely=0.30, width=195, height=30)

    pass_label.grid(row=4, column=1)
    pass_label.place(anchor='w', relx=0.1, rely=0.5)
    pass_entry.grid(row=5, column=1, columnspan=1, pady=5, padx=30)
    pass_entry.place(anchor='w', relx=0.1, rely=0.60, width=195, height=30)

    login_btn = Button(form_frame, text="Login", fg='white', width=15, bg=btn_bg_color, activebackground=btn_active_bg_color, command=lambda: authenticate_user(form_vals, auth_top))
    login_btn.grid(row=6, column=1, columnspan=3, pady=20)
    login_btn.place(anchor="center", relx=0.5, rely=0.85, height=30)

    auth_top.mainloop()

    return


def authenticate_user(form_vals, auth_top):
    # Get the entries (email / pass)
    email, password = form_vals

    email = email.get()
    email = email.lower()

    password = password.get()

    print(f'🗝 Authenticating user with:\nEmail: {email}\nPassword: {password}')

    if not validate_input(email, password):
        write_debug(f'⛔ Failed to validate auth input')
        return -1

    # Connect to mongoDb and get user
    authed_user = get_user(email, password)

    if not authed_user:
        print(f'⛔ User not authenticated.')
        return -1
    else:
        print(f'✅ User {authed_user.email} successfully authenticated.')

    # Set script access based on (verified) licenses

    print(f'💳 Checking Licenses...')

    print(f'user_licenses = {authed_user.licenses_arr}')

    if not authed_user.licenses_arr:
        print(f'⛔ No licenses found for user {email}.')
        return -1
    else:
        print(f'✅ Successfully retrieved {len(authed_user.licenses_arr)} licenses for user {email}.')
        set_script_access(authed_user.licenses_arr)

    if authed_user:
        auth_top.destroy()
        show_main_gui()

    return


def validate_input(email, password):
    # **Validate the email REGEX
    regex = '^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(regex, email):
        print(f'✅ Valid email')
    else:
        print(f'⛔ Not a valid email')
        return False

    if not password:
        print(f'⛔ Password field must be provided')
        return False
    else:
        print(f'✅ Password provided')

    return True

