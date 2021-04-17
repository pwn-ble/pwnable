import os
import subprocess
import shlex
import tkinter as tk

# TODO: move this to a UI component file
class Tutorial(tk.Frame):

    # TODO: make background black
    # TODO: move input box to the right side of window

    # temp shell
    temp_path = os.getcwd() + "/src/etc/"
    temp_cmd_file_path = temp_path + "/cmd.sh"
    hist_file_path = temp_path + "hist.txt"

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root, cnf={"background":"black"}) # call tk superclass constructor
        # cnf doesn't work how i want it to

        open(self.hist_file_path, 'w').close() # clear history file if it exists

        # assign attributes
        self.master = root
        self.master.bind('<Return>', self.handle_input) # submit on return key press

        self.command_var = tk.StringVar() # set up input tracking variable

        # add elements to the app root
        self.window_title = "pwnable bash"
        root.wm_title(self.window_title) # set window title
        
        # add UI elements
            # separate pack statements to prevent variable value being cleared
        self.cli_output = tk.Text(self.master, bg="black", fg="green")
        self.cli_output.pack()

        self.prompt_label = tk.Label(self.master)
        self.update_command_prompt()
        self.prompt_label.pack()

        self.command_input = tk.Entry(self.master, textvariable=self.command_var)
        # bind arrow keys to the history cycling functions
        self.command_input.bind("<Up>", self.go_up)
        self.command_input.bind("<Down>", self.go_down)
        self.command_input.pack()

    # TODO: def clean_input(input: str):

    def go_up(self, event):
        print("up")
    
    def go_down(self, event):
        print("down")

    def handle_input(self, event):
        """
        event: does NOT need to be assigned - tkinter passes this from command
        """
        cmd = self.command_var.get() # TODO: clean input for quotes and stuff

        temp_file = open(self.temp_cmd_file_path, 'w') # create a temporary shell script to execute command input
        temp_file.write(cmd) # write command to file
        temp_file.close()

        self.run_command() # open the shell script with our command, get output
        self.command_var.set('') # clear UI input

    def parse_command(self, cmd):
        """
        when running a cd command,
        grab the desired directory path to change to;
        """
        path = shlex.split(cmd) # get path to resolve
        return os.path.abspath(path[1]) # return resolved path

    def run_command(self):
        """
        read the command from the user from temp command shell script;
        execute it;
        get the output from command;
        print it to the console window;
        """
        cmd_file = open(self.temp_cmd_file_path, 'r') # read users command from temp file
        cmd = cmd_file.read() # get content
        self.update_command_history(cmd) # add command to history file
        cmd_file.close() # close file I/O

        if (cmd.__contains__("cd")): # if used after a && pipe itll mess up
            path = self.parse_command(cmd) # parse the path to change into
            os.chdir(path) # change into desired directory
        else:
            f = os.popen(cmd) # needs more granular control
            for line in f:
                cli_val = self.cli_output.get("1.0", tk.END) # grab terminal window contents
                if (cli_val): # if the fake terminal already has content
                    self.cli_output.insert(tk.END, "\n" + line) # append to end of content
                else:
                    self.cli_output.insert("1.0", line) # add to the beginning of content

        self.cli_output.update() # reflect new output in UI
        self.update_command_prompt() # update label
        self.cli_output.see('end') # scroll to bottom of terminal window

    def update_command_prompt(self):
        """
        grab pwd and put it on the frame's input label;
        it should look like a terminal prompt
        """
        self.prompt_label.config(text="user@pwnable:" + os.getcwd() + "$ ")

    def update_command_history(self, cmd):
        cmd_hist_file = open(self.hist_file_path, 'a') # open hist file for append
        cmd_hist_file.write("\n" + cmd) # add command to file
        cmd_hist_file.close() # close file I/O

"""
driver scripting stuff ...
"""
root = tk.Tk()
tutorial_driver = Tutorial(root)

# TODO: write challenge prompts
# TODO: build popups to supplement challenge walkthrough

root.mainloop()
