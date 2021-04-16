import os
import subprocess
import shlex
import tkinter as tk

# TODO: move this to a UI component file
class Tutorial(tk.Frame):

    def __init__(self, root:tk.Tk, title:str, prompt:str):
        tk.Frame.__init__(self, root) # call tk superclass constructor

        # assign attributes
        self.master = root
        self.master.bind('<Return>', self.handle_input) # submit on return key press

        self.command_var = tk.StringVar() # set up input tracking variable

        # add elements to the app root
        self.window_title = title
        root.wm_title(self.window_title) # set window title

        self.prompt = prompt
        
        # add UI elements
        self.cli_output = tk.Text(self.master, bg="black", fg="green").pack()
        self.prompt_label = tk.Label(self.master, text=self.prompt).pack()
        self.command_input = tk.Entry(self.master, textvariable=self.command_var).pack()
        self.submit_button = tk.Button(self.master, command=self.handle_input).pack()

    # TODO: def clean_input(input: str):
        
    def handle_input(self, event):
        """
        event: does NOT need to be assigned - tkinter passes this from command
        """
        cmd = self.command_var.get() # TODO: clean input for quotes and stuff

        temp_file = open('cmd.sh', 'w') # create a temporary shell script to execute command input
        temp_file.write(cmd) # write command to file
        temp_file.close()

        self.run_command() # open the shell script with our command, get output
        self.command_var.set('') # clear UI input

    def run_command(self):
        cmd_file = open('cmd.sh', 'r')
        cmd = cmd_file.read()
        cmd_file.close()
        
        f = os.popen(cmd)
        for line in f:
            # TODO: strip extra shit
            self.cli_output.delete('1.0', 'end')
            self.cli_output.insert(tk.END, line)
            self.cli_output.update()

"""
driver scripting stuff ...
"""
root = tk.Tk()
tutorial_driver = Tutorial(root, title="big boy window", prompt="say hello")

# # TODO: pass input from Tutorial Frame to terminal proc's STDIN
# # kun here, you can also do 
# # name = input('what is your name?: ')

root.mainloop()
