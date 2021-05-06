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

menu_driver = Menu(root)
# x = PasswordGenerator(root)
# Login(root)

# TODO: write challenge prompts
# TODO: build popups to supplement challenge walkthroug

# login_driver = Login(root) # begin by having the user log in
# TODO: check progress, if any
# TODO: launch user into save point
# login_driver.wait_window() # wait for login process to finish

# tutorial_driver = Tutorial(root)

root.mainloop()