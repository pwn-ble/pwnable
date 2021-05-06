# need to use pip to install the pythonping

#it must be ran in sudo
from gui.Terminal import Terminal
import tkinter as tk
from pythonping import ping
import subprocess

class Networking(tk.Frame):

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root) # call tk superclass constructor
        # cnf doesn't work how i want it to

        # assign attributes
        self.master = root

        self.master.title("Networking | Obtaining the IP address of your device")
        self.master.geometry('800x480')

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

        self.terminal_instance = Terminal(self.master)
    
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

        subprocess.run(["ping", "-c", ping_ammt, web_info])
        print ("Website Entered: " + web_info)

    def site_entry(self):
        web_info = self.web_var.get()
        print ("Website Entered: " + web_info)



#Tool to allow the users to find their own IP address 




    #web_var.set("")

    

# Add the functionality to make the terminal pop out into the window.
