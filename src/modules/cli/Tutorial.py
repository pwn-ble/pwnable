import tkinter as tk
from gui.Terminal import Terminal # how to import classes in separate filesystem branch
from gui.Popup import Popup
from gui.Prompt import Prompt
from modules.password.generator import generator
import os

class Tutorial():

    current_popup: Popup # is this sus?
    prompts: [str] = []
    commands: [str] = []
    prompt_index = 0

    def __init__(self):
        #tk.Frame.__init__(self, root) # tkinter Frame constructor
        self.master = tk.Tk() # keep tkinter root for object reference

        # generate a random string to cat to target file
        self.desired_pass = generator.gen(15)
        target_file = open(os.getcwd() + "/etc/password.txt", 'w')
        target_file.write(self.desired_pass)
        target_file.close()

        self.get_prompts() # read in help prompts from external file
        self.get_commands() # read in corresp commands

        self.greeting_label = tk.Label(self.master, text="Welcome to the CLI tutorial")
        self.greeting_label.pack()
        
        self.terminal = Terminal(self.master) # tutorial window

        # bind terminal input event to the popup lifecycle
        self.master.bind("<<command_entered>>", self.parse_command)

        # initialize Popup component
        self.current_popup = Popup(self.master, self.prompts[self.prompt_index])
        self.show_popup(self.prompts[self.prompt_index], self.commands[self.prompt_index])

        self.master.bind("<<passwd_attempt>>", self.try_level_pass)

    def get_commands(self):
        cmd_file = open(os.getcwd() + "/modules/cli/commands.txt")
        cmds = cmd_file.readlines()
        cmd_file.close()
        for c in cmds:
            self.commands += [c.rstrip()]

    def get_prompts(self):
        prompt_file = open(os.getcwd() + "/modules/cli/prompts.txt")
        prompts = prompt_file.readlines()
        prompt_file.close()
        for line in prompts:
            self.prompts += [line] # add each prompt from file

    def parse_command(self, event):
        """
        read the most recently entered command from the cache file;
        """
        print("parsing command")

        cmd_file = open(self.terminal.temp_cmd_file_path, 'r') # read users command from temp file
        self.current_command = cmd_file.read() # set to class memory
        cmd_file.close() # close file I/O
        self.process_input(event)

    def process_input(self, event):
        """
        check to see if the user entered the correct command to satisfy the popup;
        cycle in the next tutorial prompt 
        """
        if (self.current_popup.compare(self.current_command)): # if the commands match
            if ((self.prompt_index + 1) < len(self.prompts)): # check if hitting the end of the prompts
                # increment the index to grab next prompt
                self.prompt_index += 1
                # cycle in the next prompt to UI
                self.show_popup(self.prompts[self.prompt_index], self.commands[self.prompt_index])
            else:
                self.current_popup.blurb.config(text="use these commands to find the password in 'password.txt'")
                self.open_password_prompt()
        else: # not the correct command entered
            print("should throw an error in the UI")
            # TODO: reflect error in the UI

    def open_password_prompt(self):
        self.password_prompt = Prompt(self.master, "password: ", self.desired_pass)
        self.password_prompt.pack()

    def show_popup(self, text:str, cmd:str = ""):
        self.current_popup.blurb.config(text=text) # cheange popup text
        self.current_popup.set_desired_command(cmd) # attach command we want the user to enter

    def try_level_pass(self, event):
        return
        #if (self.password_prompt.check()): 
            #self.master.winfo_children().