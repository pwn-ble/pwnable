import tkinter as tk
from gui.Terminal import Terminal # how to import classes in separate filesystem branch
from gui.Popup import Popup

class Tutorial(tk.Frame):

    def __init__(self, root:tk.Tk):

        self.master = root # keep tkinter root for object reference
        
        self.terminal = Terminal(self.master) # tutorial window
        # TODO: be able to read commands from terminal window
            # must satisfy conditions?
            # find file data
        
        self.run() # challenge task driver function

    def run(self):
        """
        TODO: include tutorial scripting stuff in order here
        TODO: wrap popup/wait cycle in an abstraction?
        """
        greeting_popup = self.show_popup("welcome to the cli tutorial").wait_window() # greet the user

        pwd_p = self.show_popup("the first thing you'll want to do is find out where you are.\nyou can do this by typing 'pwd'.").wait_window()
        # TODO: wait for correct terminal command input
        pwd_p2 = self.show_popup("the output shows you a string of directories, or folders.\nthis is where you are in the file system.\nthe last folder in the string is your 'present working directory', or 'pwd'.").wait_window()
        ls_p = self.show_popup("since you know that you are inside of a folder right now, you would naturally want to know what files are in the folder.\nYou can check them out by entering 'ls'").wait_window()
        # TODO: wait for correct terminal command input
        cat_p = self.show_popup("if you want to see what a file contains, you can 'concatentate' it.\nyou do this by typing 'cat', followed by the filename.").wait_window()

    def show_popup(self, text: str):
        popup = Popup(self.master, text = text)
        popup.lift(self.terminal) # show up before the terminal
        return popup