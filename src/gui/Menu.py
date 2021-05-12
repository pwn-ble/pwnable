import tkinter as tk
import os
from PIL import ImageTk, Image
from gui.OverTheWire import OverTheWire
# from gui.BinaryConvert import *
import tkinter.messagebox
import sys
# ,BinaryConvert
def decimal_to_binary(value):
    return bin(int(value))
def decimal_to_hex(value):
    return hex(int(value))
def binary_to_hex(value):
    return hex(int(value, 2))
def binary_to_decimal(value):
    return int(value, 2)
def hex_to_binary(value):
    return bin(int(value, 16))
def hex_to_decimal(value):
    return int(value, 16)

class Menu(tk.Frame):

    C_FONT = ("Consolas", 16)
    C_TXT_MAXLEN = 32

    photosPath = os.getcwd() + "/gui/PwnableLogos/"

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root)

        self.master = root
        # Pwnable window title
        self.master.title("Pwnable - Menu")
        self.master.geometry("800x480")
        
        self.bin_frame = tk.Frame()
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
                                command=self.load_overthewire)
        self.binary_convert_button = tk.Button(width=20,
                                            text="Converter",
                                            font="Consolas 20 bold",
                                            fg="white",
                                            bg="black",
                                            command=self.load_converter)

        # display buttons
        self.programming_button.pack()
        self.password_button.pack()
        self.networking_button.pack()
        self.help_button.pack()
        self.binary_convert_button.pack()

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
        self.num_label = tk.Label(self.master, text="Number:", font=self.C_FONT)
        self.text_input = tk.Entry(self.master, width=20, font=self.C_FONT)

        self.Binary_button = tk.Button(
            self.master, text="Binary", width=7, command=self.evt_bt_bin, font=self.C_FONT)

        self.Decimal_button = tk.Button(
            self.master, text="Decimal",width=7, command=self.evt_bt_dec, font=self.C_FONT)

        self.Hex_button = tk.Button(self.master, text="Hex", width=7, command=self.evt_bt_hex, font=self.C_FONT)

        self.bin_label = tk.Label(self.master, text="Binary:", font=self.C_FONT)

        self._stringvar_bin = tk.StringVar()

        self.bin_output = tk.Entry(
            self.master, textvariable=self._stringvar_bin, state="readonly", font=self.C_FONT)

        self.dec_label = tk.Label(self.master, text="Decimal:", font=self.C_FONT)

        self._stringvar_dec = tk.StringVar()

        self.dec_output = tk.Entry(
            self.master, textvariable=self._stringvar_dec, state="readonly", font=self.C_FONT)

        self.hex_label = tk.Label(self.master, text="Hex:", font=self.C_FONT)

        self._stringvar_hex = tk.StringVar()

        self.hex_output = tk.Entry(
            self.master, textvariable=self._stringvar_hex, state="readonly", font=self.C_FONT)

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
        self.binary_convert_button.pack_forget()

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

        self.num_label.place_forget()
        self.text_input.place_forget()
        self.Binary_button.place_forget()
        self.Decimal_button.place_forget()
        self.Hex_button.place_forget()
        self.bin_label.place_forget()
        self.bin_output.place_forget()
        self.dec_label.place_forget()
        self.dec_output.place_forget()
        self.hex_label.place_forget()
        self.hex_output.place_forget()
        
        # load new buttons
        self.programming_button.pack()
        self.password_button.pack()
        self.networking_button.pack()
        self.help_button.pack()
        self.binary_convert_button.pack()

    def load_converter(self):
        self.programming_button.pack_forget()
        self.password_button.pack_forget()
        self.help_button.pack_forget()
        self.networking_button.pack_forget()
        self.binary_convert_button.pack_forget()

        self.back_button.pack(side=tk.TOP, anchor="nw")
        self.back_button.place(x=45, y=45)

        self.master.title("Pwnable - Binary Converter")
        
        self.num_label.place(x=200,y=140)
        self.text_input.place(x=300,y=140)
        self.Binary_button.place(x=250,y=180)
        self.Decimal_button.place(x=355,y=180)
        self.Hex_button.place(x=460,y=180)
        self.bin_label.place(x=200,y=245)
        self.bin_output.place(x=300,y=245)
        self.dec_label.place(x=200,y=295)
        self.dec_output.place(x=300,y=295)
        self.hex_label.place(x=200,y=345)
        self.hex_output.place(x=300,y=345)
    
    def load_overthewire(self):
        # self.programming_button.pack_forget()
        # self.password_button.pack_forget()
        # self.help_button.pack_forget()
        # self.networking_button.pack_forget()
        # self.binary_convert_button.pack_forget()

        # self.back_button.pack(side=tk.TOP, anchor="nw")
        # self.back_button.place(x=45, y=45)
        
        app = OverTheWire()
        app.mainloop


    def evt_bt_bin(self):
        try:
            bin_value = self.text_input.get().strip().replace(" ", "")
            dec_value = binary_to_decimal(bin_value)
            hex_value = binary_to_hex(bin_value)

            self._set_values(bin_value, dec_value, hex_value)

        except Exception as ex:
            tk.messagebox.showerror("Error", "Invalid conversion")
            print(ex, file=sys.stderr)

    def evt_bt_dec(self):
        try:
            dec_value = self.text_input.get().strip().replace(" ", "")
            bin_value = decimal_to_binary(dec_value)
            hex_value = decimal_to_hex(dec_value)
            
            self._set_values(bin_value, dec_value, hex_value)
            
        except Exception as ex:
            tk.messagebox.showerror("Error", "Invalid conversion")
            print(ex, file=sys.stderr)

    def evt_bt_hex(self):
        try:
            hex_value = self.text_input.get().strip().replace(" ", "")
            bin_value = hex_to_binary(hex_value)
            dec_value = hex_to_decimal(hex_value)
            
            self._set_values(bin_value, dec_value, hex_value)

        except Exception as ex:
            tk.messagebox.showerror("Error", "Invalid conversion")
            print(ex, file=sys.stderr)

    def _set_values(self, bin_value, dec_value, hex_value):
        if not bin_value.startswith("0b"):
            self.bin_value = "0b" + bin_value
        if not hex_value.startswith("0x"):
            self.hex_value = "0x" + hex_value

        self._stringvar_bin.set(bin_value)
        self._stringvar_dec.set(dec_value)
        self._stringvar_hex.set(hex_value)