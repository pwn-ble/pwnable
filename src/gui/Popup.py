import tkinter as tk

class Popup(tk.Frame): # inherit from tkinter's Toplevel window module 

    # TODO: give window padding

    desired_command: str

    def __init__(self, root: tk.Tk, text = "new popup"):

        self.master = root
        self.text = text
        tk.Frame.__init__(self, self.master) # superclass constructor

        # add blurb
        self.blurb = tk.Label(self.master, text = self.text)
        self.blurb.pack()

        # add ok button
        self.bye_button = tk.Button(self.master, text = "OK", command = self.destroy)
        self.bye_button.pack()

    def set_desired_command(self, cmd: str):
        self.desired_command = cmd

    def compare(self, cmd: str):
        return cmd == self.desired_command