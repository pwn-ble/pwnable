import tkinter as tk

class Popup(tk.Toplevel): # inherit from tkinter's Toplevel window module 

    # TODO: give window padding

    def __init__(self, root: tk.Tk, text = "new popup"):

        self.master = root
        self.text = text
        super().__init__(master = self.master) # superclass constructor

        # add blurb
        self.blurb = tk.Label(self, text = self.text)
        self.blurb.pack()

        # add ok button
        self.bye_button = tk.Button(self, text = "OK", command = self.destroy)
        self.bye_button.pack()