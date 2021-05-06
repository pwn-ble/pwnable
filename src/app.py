import os
import platform
import subprocess
import tkinter as tk
# UI component class imports
from gui.Menu import Menu
from gui.Login import Login
from gui.AddUser import AddUser
from gui.Terminal import Terminal
from modules.cli.Tutorial import Tutorial
from gui.PasswordGenerator import PasswordGenerator
from modules.netwrk.pingfuntion import Networking

root = tk.Tk()
# login_driver = Login(root) # begin by having the user log in
# TODO: check progress, if any
# TODO: launch user into save point
# login_driver.wait_window() # wait for login process to finish

# tutorial_driver = Tutorial(root)

# pwd_gen_driver = PasswordGenerator(root)
# pwd_gen_driver.wait_window()
network_driver = Networking(root)

root.mainloop()
