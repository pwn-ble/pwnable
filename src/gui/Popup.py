import tkinter as tk

class Popup(tk.Frame): # inherit from tkinter's Toplevel window module 

    def __init__(self, root:tk.Tk, text="new popup"):

        # assign args to class props
        self.master = root
        self.text = text

        tk.Frame.__init__(self, self.master) # superclass constructor

        # add blurb
        self.blurb = tk.Label(self.master, text = self.text)
        self.blurb.pack()

        self.desired_command: str = ""

        # add ok button
        # self.bye_button = tk.Button(self.master, text = "OK", command = lambda: self.event_generate("<<ok_pressed>>"))
        # self.bye_button.pack()

    def set_desired_command(self, cmd: str):
        self.desired_command = cmd

    def compare(self, cmd: str):
        print(self.desired_command)
        print(cmd)
        print(cmd.__contains__(self.desired_command))
        print(cmd == self.desired_command)

        return (cmd.__contains__(self.desired_command)) or (cmd == self.desired_command)