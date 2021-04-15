from guizero import App, Text, TextBox, PushButton, Window
import tkinter as tk


# programming module command
def load_programming_module():
    print("Loading Programming Module...")


# password module command
def load_password_module():
    # setup frame
    password_frame = tk.Frame()
    # buttons configuration
    back_button = tk.Button(width=button_width,
                            text="Back",
                            font=button_font,
                            fg="white",
                            bg="gray",
                            command=load_menu)
    one_button = tk.Button(width=button_width,
                           text="Hello",
                           font=button_font,
                           fg="white",
                           bg="black"
                           )
    two_button = tk.Button(width=button_width,
                           text="Passwordssss",
                           font=button_font,
                           fg="white",
                           bg="black")


    # removes previous buttons
    programming_button.pack_forget()
    password_button.pack_forget()
    help_button.pack_forget()
    # load new buttons
    back_button.pack()
    one_button.pack()
    two_button.pack()
    # loads frame
    password_frame.pack()

# help command
def load_help():
    print("Loading Help...")

def load_menu():
    menu_frame = tk.Frame()
    programming_button = tk.Button(width=button_width,
                                   text="Programming",
                                   font=button_font,
                                   fg="white",
                                   bg="black",
                                   command=load_programming_module)
    password_button = tk.Button(width=button_width,
                                text="Password",
                                font=button_font,
                                fg="white",
                                bg="black",
                                command=load_password_module)
    help_button = tk.Button(width=button_width,
                            text="Help",
                            font=button_font,
                            fg="white",
                            bg="black",
                            command=load_help)

    one_button = tk.Button()
    two_button = tk.Button()
    one_button.pack_forget()
    two_button.pack_forget()

    programming_button.pack()
    password_button.pack()
    help_button.pack()

# parameter variables for easy adjustments
button_width = 15
button_font = "Arial 20 bold"

app = App(title="Pwnable")
title_pwnable = Text(app, text="Pwnable", size=50, font="Arial")
module_title = Text(app, text="Modules", size=25)
# buttons configuration
programming_button = tk.Button(width=button_width,
                               text="Programming",
                               font=button_font,
                               fg="white",
                               bg="black",
                               command=load_programming_module)
password_button = tk.Button(width=button_width,
                            text="Password",
                            font=button_font,
                            fg="white",
                            bg="black",
                            command=load_password_module)
help_button = tk.Button(width=button_width,
                        text="Help",
                        font=button_font,
                        fg="white",
                        bg="black",
                        command=load_help)

# display buttons
programming_button.pack()
password_button.pack()
help_button.pack()

app.display()
