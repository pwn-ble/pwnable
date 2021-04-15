import os
import subprocess
import tkinter as tk

class Tutorial(tk.Frame):

    def __init__(self, root: tk.Tk):
        tk.Frame.__init__(self, root) # call tk superclass constructor
        self.master = root

        root.wm_title("hwllo from tuorial class") # set window title
        
        # add UI elements


        # print('welcome to the terminal!')
        # # kun here, you can also do 
        # # name = input('what is your name?: ')
        # print('what is your name?')
        # name = input()

        # print(f'nice to see you, {name}.\nwe are going to learn how to use a terminal')
        # # here as well
        # # answer = input('are you ready?: ')
        # print('are you ready?')
        # answer = input()

        # if (answer == 'yes'):
        #     print('great!')
        # elif (answer == 'no'):
        #     print('well too bad! ')
        # else:
        #     print('what? it was a yes or no question.')

        # print('lets get started')

        # open a terminal window for the user
        
    
    # def handle_input():
        # do we need input?

root = tk.Tk()
tutorial_driver = Tutorial(root) # does this need to be an instance object?

# open a terminal for printing UI input's output?
terminal_win = subprocess.Popen(['x-terminal-emulator'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

root.mainloop()
