import os
import platform
import subprocess
import tkinter as tk
from gui.Terminal import Terminal
from gui.Login import Login

# lauch pwnable home screen script
# if (platform.system() == 'Windows'):
#     subprocess.call(['python.exe', '.\\gui\\menu.py'])
# else:
#     subprocess.call(['python3', './gui/menu.py'])

# class Application(tk.Frame):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("300x200")

#         tk.Frame.__init__(self, self.root)
#         self.create_widgets()

#     def create_widgets(self):
#         self.root.bind('<Return>', self.parse)
#         self.grid()

#         self.submit = tk.Button(self, text="Submit")
#         self.submit.bind('<Button-1>', self.parse)
#         self.submit.grid()

#     def parse(self, event):
#         print("You clicked?")

#     def start(self):
#         self.root.mainloop()


# Application().start()


root = tk.Tk()
login_instance = Login(root)
# tutorial_driver = Terminal(root)

# TODO: write challenge prompts
# TODO: build popups to supplement challenge walkthrough

root.mainloop()