import os
import platform
import subprocess
import tkinter as tk
# UI component class imports
from gui.Menu import Menu
from gui.Login import Login
from gui.AddUser import AddUser
from gui.Terminal import Terminal
# Driver class imports
from modules.cli.Tutorial import Tutorial
# Misc class imports
from gui.PasswordGenerator import PasswordGenerator


root = tk.Tk()
# TODO: show menu
# TODO: have menu make user log in or create user
# menu_driver = Menu(root)

login_driver = Login(root) # begin by having the user log in
# TODO: check progress, if any
# TODO: launch user into save point

# tutorial_driver = Tutorial(root)
# tutorial_driver.wait_window()

# pwd_gen_driver = PasswordGenerator(root)
# pwd_gen_driver.wait_window()

root.mainloop()
