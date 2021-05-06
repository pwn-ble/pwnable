import os
import platform
import subprocess
import tkinter
from gui.Terminal import Terminal
from modules.netwrk.ipa import Networking


root = tkinter.Tk()
# tutorial_driver = Terminal(root)
network_driver = Networking(root)

# TODO: write challenge prompts
# TODO: build popups to supplement challenge walkthrough

root.mainloop()