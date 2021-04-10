# need to use pip to install the pythonping

#it must be ran in sudo
import tkinter as tk
from tkinter import messagebox
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


#submit button
def site_submit():
    web_info = web_var.get()
    subprocess.run(["ping", "-c", "4", web_info])
    print ("Website Entered: " + web_info)


#ping ('8.8.8.8', verbose=True)

webaddy_lable = tk.Label(root, text = 'Enter the addy here')
webaddy_entry = tk.Entry(root,textvariable = web_var)

submit_button = tk.Button(root, text="Click here to submit the ping request", command=site_submit)

#puts the stuff in the gui
webaddy_lable.pack()
webaddy_entry.pack()
submit_button.pack()

root.mainloop()