import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import platform
import os

root = tk.Tk()

user_var=tk.StringVar()
passwd_var=tk.StringVar()

# login function
def login_input():
    user = user_var.get()
    password = passwd_var.get()

    print ("Welcome: " + user)
    print ("Your password is: " + password)

    # messagebox.showinfo('Welcome', 'Have fun ' + user)

    user_var.set("")
    passwd_var.set("")

    module_title.pack()
    main_menu_frame.pack()
    login_frame.pack_forget()
    # login_title.pack_forget()
    # user_label.pack_forget()
    # user_entry.pack_forget()
    # passw_label.pack_forget()
    # passw_entry.pack_forget()
    # sub_btn.pack_forget()

# programming module command
def load_programming_module():
    print("Loading Programming Module...")

# password module command
def load_password_module():
    # change window title
    title = root.title("Password Module")
    # remove main menu
    main_menu_frame.pack_forget()

    # load new buttons
    back_button.pack(side=tk.TOP, anchor="nw")
    back_button.place(x=50, y=30.5)
    password_generator_button.pack()
    password_cracker_button.pack()

def load_password_generator():

    print("Loading Password Generator...")
    
    # path works if you execute the script from this directory
    if (platform.system() == 'Windows'):
        lol = subprocess.call(['python.exe', '.\\modules\\\password\\generator\\generator.py'])
    else:
        lol = subprocess.call(['python3', './modules\password/generator/generator.py'])

# help command
def load_help():
    print("Loading Help...")

# function to load main menu
def load_menu():
    title = root.title("Main Menu")
    main_menu_frame.pack()

    # removes password module buttons
    password_generator_button.pack_forget()
    password_cracker_button.pack_forget()
    back_button.pack_forget()
    back_button.place_forget()

# Pwnable window title
title = root.title("Login")
root.geometry("800x480")

# pwnable logo
path = Image.open("PwnableLogos/PwnableLogo-08.png")
resize = path.resize((269, 55), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resize)
label = tk.Label(image=photo)
label.pack(pady=(25, 0))

# Module menu title
module_title = tk.Label(root, text="Modules", font="Arial 25")

# login page frame
login_frame = tk.Frame()
#login page title
login_title = tk.Label(login_frame,text="Login", font="Arial 25")
login_title.pack()

#new label for user using widget label
user_label = tk.Label(login_frame,text = 'Username', bd = 5, font=('arial',20,'bold'))

#new entry for the user label
user_entry = tk.Entry(login_frame,textvariable = user_var, bd = 5, font = ('arial',20,'bold'))

# creating a label for password
passw_label = tk.Label(login_frame,text = 'Password', bd = 5, font = ('arial',20,'bold'))

# creating a entry for password
passw_entry=tk.Entry(login_frame,textvariable = passwd_var, bd = 5, font = ('arial',20,'bold'), show = '@')

sub_btn=tk.Button(login_frame,text = 'Submit', command = login_input)

#displays login elements
user_label.pack(anchor= 'center')
user_entry.pack(anchor= 'center')
passw_label.pack(anchor= 'center')
passw_entry.pack(anchor= 'center')
sub_btn.pack(anchor= 'center')
login_frame.pack()

# buttons configuration
main_menu_frame = tk.Frame()
programming_button = tk.Button(main_menu_frame, width=15,
                               text="Programming",
                               font="Arial 20 bold",
                               fg="white",
                               bg="black",
                               command=load_programming_module)
password_button = tk.Button(main_menu_frame, width=15,
                            text="Password",
                            font="Arial 20 bold",
                            fg="white",
                            bg="black",
                            command=load_password_module)
networking_button = tk.Button(main_menu_frame, width=15,
                              text="Networking",
                              font="Arial 20 bold",
                              fg="white",
                              bg="black")
help_button = tk.Button(main_menu_frame, width=15,
                        text="Help",
                        font="Arial 20 bold",
                        fg="white",
                        bg="black",
                        command=load_help)

# display main menu buttons
programming_button.pack()
password_button.pack()
networking_button.pack()
help_button.pack()

# Password Module Buttons
back_button = tk.Button(width=8,
                        height=2,
                        text="Back",
                        font="Arial 10 bold",
                        fg="white",
                        bg="gray",
                        command=load_menu)
password_generator_button = tk.Button(width=17,
                                      text="Password Generator",
                                      font="Arial 18 bold",
                                      fg="white",
                                      bg="black",
                                      command=load_password_generator)
password_cracker_button = tk.Button(width=17,
                                    text="Password Cracker",
                                    font="Arial 18 bold",
                                    fg="white",
                                    bg="black")

root.mainloop()
