# need to use pip to install the pythonping

#it must be ran in sudo
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from pythonping import ping
import subprocess


#pulls the info directly from the string
#or have it pull a .sh file that the user created prior to this where they were asked to input a websites ip address
#into a file and then save it as a .sh script

#to preface that, you could have the user find the ip address themselves using nslookup or some tool.

root=tk.Tk()
root.title("Networking | Ping tool")
root.geometry('800x480')

web_var=tk.StringVar()
ping_var=tk.StringVar()




#trying to make a notification pop up to explain whats happening
#notification =wi()
#root.wm_withdraw()
#messagebox.showinfo('This is the ping tool', 'Any internet address entered will be pinged with 4 ICMP packets. They should return with TTL' )
#notification.destroy()

#entery boxfor website

def site_entry():
    web_info = web_var.get()
    print ("Website Entered: " + web_info)

    #web_var.set("")

def ping_ammount():
    ping_ammt = ping_var.get()
    #global ping_ammt
    print ("Number of pings sent: " + ping_ammt)
    #totalpings_lable.configure


#submit button
def site_submit():
    web_info = web_var.get()
    ping_ammt = ping_var.get()

    
    res = "Previously pinged: " + web_info + " " + ping_ammt + " times."
    webaddy_lable.configure(text= res)

    subprocess.run(["ping", "-c", ping_ammt, web_info])
    print ("Website Entered: " + web_info)
    

# Add the functionality to make the terminal pop out into the window.

webaddy_lable = tk.Label(root, text = 'Enter the internet address here')
webaddy_entry = tk.Entry(root,textvariable = web_var)

totalpings_lable = tk.Label(root, text = 'Enter the ammount of times you wish to ping this address')
totalpings_entry = tk.Entry(root,textvariable = ping_var)

submit_button = tk.Button(root, text="Click here to submit the ping request", command=site_submit)

#puts the stuff in the gui
webaddy_lable.pack()
webaddy_entry.pack()

totalpings_lable.pack()
totalpings_entry.pack()

submit_button.pack()

root.mainloop()

#win = tk.Tk()

#win.geometry("200x200")

#def open():
#    top = Toplevel(win)
#    top.mainloop()

#btn = Button(win, text="open", command=open)

#btn.place(x=75, y=50)

#win.mainloop()