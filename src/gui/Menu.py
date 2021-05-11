import tkinter as tk
import os
from PIL import ImageTk, Image
from modules.cli.Tutorial import Tutorial

class Menu(tk.Frame):

    photosPath = os.getcwd() + "/gui/PwnableLogos/"

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root)

        self.master = root
        # Pwnable window title
        self.master.title("Pwnable - Menu")
        self.master.geometry("800x480")
        
        
        # Pwnable menu title

        path = Image.open(self.photosPath + "PwnableLogo-08.png")
        resize = path.resize((300,65), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(resize)
        self.label = tk.Label(image=self.photo)
        # label.image = photo
        self.label.pack(pady=15)

        # Module menu title
        self.module_title = tk.Label(root, text = "Modules", font="Consolas 25 bold")
        self.module_title.pack()

        self.terminal_frame = tk.Frame()
        self.terminal_frame.pack()

        # buttons configuration
        self.programming_button = tk.Button(width=20,
                                    text="CLI",
                                    font="Consolas 20 bold",
                                    fg="white",
                                    bg="black",
                                    command=self.load_cli_module)
        self.password_button = tk.Button(width=20,
                                    text="Password",
                                    font="Consolas 20 bold",
                                    fg="white",
                                    bg="black",
                                    command=self.load_password_module)
        self.networking_button = tk.Button(width=20,
                                text="Networking",
                                font="Consolas 20 bold",
                                fg="white",
                                bg="black")
        self.help_button = tk.Button(width=20,
                                text="OverTheWire",
                                font="Consolas 20 bold",
                                fg="white",
                                bg="black",
                                command=self.load_help)

        # display buttons
        self.programming_button.pack()
        self.password_button.pack()
        self.networking_button.pack()
        self.help_button.pack()

        self.back_button = tk.Button(width=4,
                                text="Back",
                                font="Consolas 8 bold",
                                fg="white",
                                bg="gray",
                                command=self.load_menu)

    # programming module command
    def load_cli_module(self):
        print("Loading CLI Module...")
        # removes previous buttons
        self.master.title("Password Module")
        self.programming_button.pack_forget()
        self.password_button.pack_forget()
        self.help_button.pack_forget()
        self.networking_button.pack_forget()

        # load new buttons
        self.back_button.pack(side=tk.TOP, anchor="nw")
        self.back_button.place(x=10, y=21)#back button placement so it isnt covering the terminal screen
        self.module_title.pack_forget()
        self.label.pack_forget()
        Tutorial(self.terminal_frame)
        self.terminal_frame.pack()


    # password module command
    def load_password_module(self):
        # removes previous buttons
        self.master.title("Password Module")
        self.programming_button.pack_forget()
        self.password_button.pack_forget()
        self.help_button.pack_forget()
        self.networking_button.pack_forget()

        # load new buttons
        self.back_button.pack(side=tk.TOP, anchor="nw")
        self.back_button.place(x=45, y=45)

    # help command
    def load_help(self):
        print("Loading Help...")

    def load_menu(self):
        # removes previous buttons
        self.master.title("Pwnable - Menu")
        self.back_button.pack_forget()
        self.back_button.place_forget()
        self.label.pack()
        self.module_title.pack()
        
        # load new buttons
        self.programming_button.pack()
        self.password_button.pack()
        self.networking_button.pack()
        self.help_button.pack()
        self.terminal_frame.pack_forget()