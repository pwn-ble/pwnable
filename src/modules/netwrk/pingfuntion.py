# need to use pip to install the pythonping

#it must be ran in sudo
from gui.Terminal import Terminal
import tkinter as tk
from pythonping import ping
import subprocess
from gui.Popup import Popup
from gui.Prompt import Prompt
import os


class Networking(tk.Frame):

    current_popup: Popup # is this sus?
    prompts: [str] = []
    prompt_index = 0

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root) # call tk superclass constructor
        # cnf doesn't work how i want it to

        # assign attributesls
        self.master = root

        self.master.title("Networking | Sending ICMP Packets to Destination")
        self.master.geometry('800x500')

        self.web_var=tk.StringVar()
        self.ping_var=tk.StringVar()

        self.webaddy_lable = tk.Label(root, text = 'Enter the internet address here')
        self.webaddy_entry = tk.Entry(root,textvariable = self.web_var)

        self.totalpings_lable = tk.Label(root, text = 'Enter the ammount of times you wish to ping this address')
        self.totalpings_entry = tk.Entry(root,textvariable = self.ping_var)
        self.submit_button = tk.Button(root, text="Click here to submit the ping request", command=self.site_submit)

        #puts the stuff in the gui
        self.webaddy_lable.pack()
        self.webaddy_entry.pack()

        self.totalpings_lable.pack()
        self.totalpings_entry.pack()

        self.submit_button.pack()

        self.terminal_instance = Terminal(self.master) # terminal window component
    
        self.get_prompts()

        

        self.current_popup = Popup(self.master, self.prompts[self.prompt_index])
        self.show_popup(self.prompts[self.prompt_index])

        self.helpbutton = tk.Button(root, text="Help", command=self.show_popup)
        self.helpbutton.pack()




    def ping_ammount(self):
        ping_ammt = self.ping_var.get()
        #global ping_ammt
        print ("Number of pings sent: " + ping_ammt)
        #totalpings_lable.configure

    #submit button
    def site_submit(self):
        web_info = self.web_var.get()
        ping_ammt = self.ping_var.get()

        res = "Previously pinged: " + web_info + " " + ping_ammt + " times."
        self.webaddy_lable.configure(text= res)

        # subprocess.run(["ping", "-c", ping_ammt, web_info])
        self.terminal_instance.run_command(f'ping -c {ping_ammt} {web_info}')
        print ("Website Entered: " + web_info)

    def site_entry(self):
        web_info = self.web_var.get()
        print ("Website Entered: " + web_info)

    def get_prompts(self):
        prompt_file = open(os.getcwd() + "/modules/netwrk/pingcommands.txt")
        prompts = prompt_file.readlines()
        prompt_file.close()
        for line in prompts:
            self.prompts += [line] # add each prompt from file

    def show_popup(self, text:str):
        prompt = ""
        for line in self.prompts:
            prompt += line + "\n"


        self.current_popup.blurb.config(text=prompt) # cheange popup text


#Tool to allow the users to find their own IP address 



    #web_var.set("")

    

# Add the functionality to make the terminal pop out into the window.
