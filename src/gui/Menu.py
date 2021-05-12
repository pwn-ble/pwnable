import tkinter as tk
import os
from PIL import ImageTk, Image
from gui.OverTheWire import OverTheWire
from gui.BinaryConvert import BinaryConvert

class Menu(tk.Frame):

    photosPath = os.getcwd() + "/gui/PwnableLogos/"

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root)

        self.master = root
        # Pwnable window title
        self.master.title("Pwnable - Menu")
        self.master.geometry("800x480")
        
        self.bin_frame = tk.Frame(root)
        # Pwnable menu title

        path = Image.open(self.photosPath + "PwnableLogo-08.png")
        resize = path.resize((300,65), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(resize)
        label = tk.Label(image=self.photo)
        # label.image = photo
        label.pack(pady=(25,0))

        # Module menu title
        module_title = tk.Label(root, text = "Modules", font="Consolas 25 bold")
        module_title.pack()

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
                                command=self.load_converter)

        # display buttons
        self.programming_button.pack()
        self.password_button.pack()
        self.networking_button.pack()
        self.help_button.pack()

        self.back_button = tk.Button(width=6,
                                text="Back",
                                font="Consolas 10 bold",
                                fg="white",
                                bg="gray",
                                command=self.load_menu)
        # self.password_generator_button = tk.Button(width=17,
        #                         text="Password Generator",
        #                         font="Arial 18 bold",
        #                         fg="white",
        #                         bg="black")
        # self.password_cracker_button = tk.Button(width=17,
        #                         text="Password Cracker",
        #                         font="Arial 18 bold",
        #                         fg="white",
        #                         bg="black")

    # programming module command
    def load_cli_module(self):
        print("Loading CLI Module...")

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
        
        # load new buttons
        self.programming_button.pack()
        self.password_button.pack()
        self.networking_button.pack()
        self.help_button.pack()

    def load_converter(self):
        self.programming_button.pack_forget()
        self.password_button.pack_forget()
        self.help_button.pack_forget()
        self.networking_button.pack_forget()

        self.back_button.pack(side=tk.TOP, anchor="nw")
        self.back_button.place(x=45, y=45)
        self.bin_frame = BinaryConvert(self.master)
        self.bin_frame.pack()