import tkinter as tk
from .Popup import Popup

class Prompt(tk.Frame):

    def __init__(self, root:tk.Tk, text: str, password: str):
        self.master = root
        self.password = password

        tk.Frame.__init__(self, self.master) # superclass constructor

        self.blurb = tk.Label(self, text = text)
        self.blurb.config(font="Consolas 50")
        self.blurb.pack()

        self.pw_var = tk.StringVar()
        self.pw_input_box = tk.Entry(self, textvariable=self.pw_var)
        self.pw_input_box.pack()

        # add ok button
        self.bye_button = tk.Button(self, text = "OK", command = lambda: self.master.event_generate("<<passwd_attempt>>"))
        self.bye_button.pack()

    def check(self):
        input = self.pw_var.get()

        return (input == self.password)