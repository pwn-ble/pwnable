from guizero import App, Text, TextBox, PushButton
import tkinter as tk
import subprocess
import platform
import os

# programming module command
def load_programming_module():
    print("Loading Programming Module...")

# password module command
def load_password_module():
    print("Loading Password Module...")

    # path works if you execute the script from this directory
    if (platform.system() == 'Windows'):
        lol = subprocess.call(['python.exe', '.\\modules\\password\\ui.py'])
    else:
        lol = subprocess.call(['python3', './modules/password/ui.py'])

# help command
def load_help():
    print("Loading Help...")

#parameter variables for easy adjustments
button_width = 15
button_font = "Arial 20 bold"

app = App(title="Pwnable")
#pwnable title
title_pwnable = Text(app, text="Pwnable", size=50, font="Arial")
#module header
module_title = Text(app, text="Modules", size=25)

#buttons
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

#displays buttons
programming_button.pack()
password_button.pack()
help_button.pack()

app.display()
