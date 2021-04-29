import os
import platform
import subprocess
import tkinter as tk
# UI component class imports
from gui.AddUser import AddUser
from gui.Login import Login
from modules.cli.Tutorial import Tutorial

root = tk.Tk() # entire-app TK root instance

# TODO: show menu
# TODO: have menu make user log in or create user

create_user_driver = AddUser(root)
# login_driver = Login(root) # begin by having the user log in
# TODO: check progress, if any
# TODO: launch user into save point
# login_driver.wait_window() # wait for login process to finish

# tutorial_driver = Tutorial(root)

root.mainloop()