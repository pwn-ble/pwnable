import tkinter as tk
import os
from PIL import ImageTk, Image
from modules.cli.Tutorial import Tutorial

class PasswordModule(tk.Frame):

    photosPath = os.getcwd() + "/gui/PwnableLogos/"

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root)

        self.master = root
        # Pwnable window title
        self.master.title("Pwnable - Password Best Practices")
        self.master.geometry("800x480")
        
        


        # Module menu title

        self.terminal_frame = tk.Frame()
        self.terminal_frame.pack()
        
        self.info_output = tk.Text(self.master, bg="black", fg="green")
        self.info_output.config(height=15, width=55)#Resizes terminal window height so the prompt text isnt cut off
        self.info_output.pack()

       
   