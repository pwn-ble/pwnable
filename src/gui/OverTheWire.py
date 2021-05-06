import tkinter as tk
from PIL import ImageTk, Image

class OverTheWire(tk.Frame):

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root)
        self.master = root
        self.master.title("Pwnable - OverTheWire Walkthrough")
        self.master.geometry("800x480")

        
