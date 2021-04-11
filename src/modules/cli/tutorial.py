import os
import subprocess
import tkinter

# should be ran after segue from tkinter UI stuff

os.chdir('src/modules/cli/')

root = tkinter.Tk()

# open a terminal window for the user
terminal_win = subprocess.Popen(['x-terminal-emulator'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

root.mainloop()
