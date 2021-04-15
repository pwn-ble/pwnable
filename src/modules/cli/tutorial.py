import os
import subprocess
import shlex
import tkinter as tk

# TODO: move this to a UI component file
class Tutorial(tk.Frame):

    def __init__(self, root:tk.Tk, title:str, prompt:str):
        tk.Frame.__init__(self, root) # call tk superclass constructor

        self.command_var = tk.StringVar() # set up input tracking variable

        self.create_widgets(root, title, prompt) # add elements to the app root

    # TODO: def clean_input(input: str):

    def create_widgets(self, root, title, prompt):
        # assign attributes
        self.master = root
        self.master.bind('<Return>', self.handle_input) # submit on return key press

        self.window_title = title
        self.prompt = prompt

        root.wm_title(self.window_title) # set window title
        
        # add UI elements
        self.prompt_label = tk.Label(self.master, text=self.prompt).pack()
        self.command_input = tk.Entry(self.master, textvariable=self.command_var).pack()
        self.submit_button = tk.Button(self.master, command=self.handle_input).pack()
        
    def handle_input(self, event):
        """
        event: does NOT need to be assigned - tkinter passes this from command
        """
        cmd = shlex.split(self.command_var.get()) # TODO: clean input for quotes and stuff
        self.run_command(self.command_var.get()) # run the command as a subprocess
        self.command_var.set('')

        # self.run_command(self.command_var.get()) # run the command as a subprocess

    def run_command(self, command):
        f = os.popen(command)
        for line in f:
            line = line.strip()
            if line:
                # tfield.insert("end", line+"\n")
                print(line)
        f.close()
        # tfield.get("current linestart", "current lineend")
        # with subprocess.Popen('exec ping -c 2 www.google.com', shell=True, stdout=subprocess.PIPE) as proc:
        #     print(proc.stdout.read().decode('utf-8'))
        #     proc.kill()

"""
driver scripting stuff ...
"""
root = tk.Tk()
tutorial_driver = Tutorial(root, title="big boy window", prompt="say hello")

# open a terminal for printing UI input's output?
# terminal_win = subprocess.Popen(['x-terminal-emulator'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# cmd = 'ping -c 2 google.com'
# output = terminal_win.communicate(input=str.encode(cmd))
# print(output)

# # TODO: pass input from Tutorial Frame to terminal proc's STDIN
# # kun here, you can also do 
# # name = input('what is your name?: ')

root.mainloop()

"""
extra stuff
"""
# ip = '192.168.1.1'

# root = tk.Tk()
# tfield = tk.Text(root)
# tfield.pack()
# f = os.popen('ping %s' % (ip))
# for line in f:
#     line = line.strip()
#     if line:
#         tfield.insert("end", line+"\n")
#         tfield.get("current linestart", "current lineend")

# def get_info(arg):
#     print(tfield.get("1.0", "current lineend"))

# tfield.bind("<Return>", get_info)

# root.mainloop()
# f.close()

"""
opens an embedded terminal
"""
# root = tk.Tk()
# termf = tk.Frame(root, height=400, width=500)

# termf.pack(fill=tk.BOTH, expand=tk.YES)
# wid = termf.winfo_id()
# os.system('xterm -into %d -geometry 40x20 -sb &' % wid)

# root.mainloop()

# root = tk.Tk()
# tfield = tk.Text(root)
# tfield.pack()
# for line in os.popen("run_command", 'r'):
# 	tfield.insert("end", line)

# root.mainloop()
