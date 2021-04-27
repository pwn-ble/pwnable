import os
import platform
import subprocess
import tkinter as tk

from modules.cli.Tutorial import Tutorial # this is a driver script for CLI tutorial

root = tk.Tk()

tutorial_driver = Tutorial(root)

# TODO: should show login frame
    # TODO: process info against login files
    # TODO: check progress, if any
    # TODO: launch user into save point

root.mainloop()