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
        TODO: wrap popup/wait cycle in an abstraction?
        """
        greeting_popup = self.show_popup("welcome to the cli tutorial") # greet the user
        greeting_popup.wait_window() # wait for the window to be closed before continuing

        ls_p = self.show_popup("the first thing you'll want to do is find out where you are.\nyou can do this by typing 'ls'.")

    def show_popup(self, text: str):
        popup = Popup(self.master, text = text) # greet the user
        popup.lift(self.terminal) # show up before the terminal
        return popup