import os
import subprocess
import shlex # need?
import tkinter as tk

# TODO: move this to a UI component file
class Tutorial(tk.Frame):

    # TODO: make background black
    # TODO: move input box to the right side of window
    # TODO: make input label the terminal'user / pwd' prompt
        # TODO: make label update with relevant commands, ie: cd

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root, cnf={"background":"black"}) # call tk superclass constructor
        # cnf doesn't work how i want it to

        # assign attributes
        self.master = root
        self.master.bind('<Return>', self.handle_input) # submit on return key press

        self.command_var = tk.StringVar() # set up input tracking variable

        # add elements to the app root
        self.window_title = "pwnable bash"
        root.wm_title(self.window_title) # set window title

        self.prompt = self.update_command_prompt() # set the terminal command line prompt
        
        # add UI elements
             # separate pack statements to prevent variable value being cleared
        self.cli_output = tk.Text(self.master, bg="black", fg="green")
        self.cli_output.pack()
        self.prompt_label = tk.Label(self.master, text=self.prompt)
        self.prompt_label.pack()
        self.command_input = tk.Entry(self.master, textvariable=self.command_var)
        self.command_input.pack()

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

    # TODO: def parse_command(self, cmd):

    def run_command(self):
        """
        read the command from the user from temp command shell script;
        execute it;
        get the output from command;
        print it to the console window;
        """
        cmd_file = open('cmd.sh', 'r')
        cmd = cmd_file.read()
        cmd_file.close()

        if (cmd.__contains__("cd")): # if used after a && pipe itll mess up
            # parse the path to change into
            print(os.getcwd())
            
            # os.chdir(path)
        else:
            f = os.popen(cmd) # needs more granular control

            for line in f:
                cli_val = self.cli_output.get("1.0", tk.END) # grab terminal window contents
                if (cli_val): # if the fake terminal already has content
                    self.cli_output.insert(tk.END, "\n" + line) # append to end of content
                else:
                    self.cli_output.insert("1.0", line) # add to the beginning of content

        self.cli_output.update()
        self.cli_output.see('end') # scroll to bottom of terminal window

    def update_command_prompt(self):
        """
        grab pwd and put it on the frame's input label;
        it should look like a terminal prompt
        """
        return 'todo'

    # def TODO: update_command_history(self):


"""
driver scripting stuff ...
"""
root = tk.Tk()
tutorial_driver = Tutorial(root)

# TODO: write challenge prompts
# TODO: build popups to supplement challenge walkthrough

root.mainloop()
