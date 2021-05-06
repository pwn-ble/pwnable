import tkinter as tk
from gui.Terminal import Terminal # how to import classes in separate filesystem branch
from gui.Popup import Popup
from gui.Prompt import Prompt
from modules.password.generator import generator

class Tutorial(tk.Frame):

    current_popup: Popup # is this sus?
    current_command: str = ""
    has_popup_open: bool = False # to lock window if popup is open

    def __init__(self, root: tk.Tk):

        self.master = root # keep tkinter root for object reference
        
        self.terminal = Terminal(self.master) # tutorial window

        self.desired_pass = generator.gen(15) # generate a random string to cat to target file
        target_file = open("src/etc/password.txt", 'w')
        target_file.write(self.desired_pass)
        target_file.close()

        # bind terminal input event to the popup lifecycle
        self.master.bind("<<command_entered>>", self.parse_command, self.process_input)
        
        self.run() # challenge task driver function

    def parse_command(self, event):
        """
        read the most recently entered command from the cache file;
        """
        cmd_file = open(self.terminal.temp_cmd_file_path, 'r') # read users command from temp file
        self.current_command = cmd_file.read() # set to class memory
        cmd_file.close() # close file I/O

    def process_input(self, event):
        """
        check to see if the user entered the correct command to satisfy the popup
        """
        print(self.current_command)
        
        if (self.current_popup.compare(self.current_command)): # if the commands match
            self.current_popup.destroy() # close the popup
        else:
            print("should throw an error in the UI")
            # TODO: reflect error in the UI

    def run(self):
        greeting_win = Popup(self.master, text = "welcome to the CLI tutorial")
        greeting_win.pack()
        greeting_win.wait_window()

        self.show_popup("the first thing you'll want to do is find out where you are.\nyou can do this by typing 'pwd'.", "pwd")
        self.show_popup("the output shows you a string of directories, or folders.\nthis is where you are in the file system.\nthe last folder in the string is your 'present working directory', or 'pwd'.")
        self.show_popup("since you know that you are inside of a folder right now, you would naturally want to know what files are in the folder.\nYou can check them out by entering 'ls'", "ls")
        self.show_popup("if you want to see what a file contains, you can 'concatentate' it.\nyou do this by typing 'cat', followed by the filename.", "cat")

        pwd_box = Prompt(self.master, "find the file 'password.txt' and enter its contents below", self.desired_pass)
        pwd_box.wait_window()
        self.destroy()

    def show_popup(self, text: str, cmd: str = ""):
        """
        """
        self.current_popup = Popup(self.master, text = text)
        self.current_popup.set_desired_command(cmd) # attach command we want the user to enter
        self.current_popup.pack()
        self.current_popup.wait_window()
