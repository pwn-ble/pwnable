import tkinter as tk
from gui.Terminal import Terminal # how to import classes in separate filesystem branch
from gui.Popup import Popup

class Tutorial(tk.Frame):

    # TODO: write functions

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
        """
        greeting_popup = Popup(self.master, text = "welcome to the cli tutorial") # greet the user
        greeting_popup.lift(self.terminal) # show up before the terminal