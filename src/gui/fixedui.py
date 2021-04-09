from guizero import App, Text, TextBox, PushButton, Window
import tkinter as tk

# programming module command
def load_programming_module():
    print("Loading Programming Module...")

# password module command
def load_password_module():
    # removes previous buttons
    programming_button.pack_forget()
    password_button.pack_forget()
    help_button.pack_forget()
    
    # load new buttons
    back_button.pack(side=tk.TOP, anchor="nw")
    back_button.place(x=45, y=45)
    password_generator_button.pack()
    password_cracker_button.pack()

# help command
def load_help():
    print("Loading Help...")

def load_menu():
    password_generator_button.pack_forget()
    password_cracker_button.pack_forget()
    back_button.pack_forget()
    back_button.place_forget()

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
main_menu_frame = tk.Frame()
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

password_menu_frame = tk.Frame()

back_button = tk.Button(width=6,
                        text="Back",
                        font="Arial 10 bold",
                        fg="white",
                        bg="gray",
                        command=load_menu)
password_generator_button = tk.Button(width=17,
                        text="Password Generator",
                        font="Arial 18 bold",
                        fg="white",
                        bg="black")
password_cracker_button = tk.Button(width=17,
                        text="Password Cracker",
                        font="Arial 18 bold",
                        fg="white",
                        bg="black")
app.display()
