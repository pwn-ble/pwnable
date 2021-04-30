import os
import platform
import subprocess
import tkinter as tk
from gui.Terminal import Terminal
from gui.Login import Login
from gui.Menu import Menu

root = tk.Tk()
menu_driver = Menu(root)

# TODO: write challenge prompts
# TODO: build popups to supplement challenge walkthrough

root.mainloop()