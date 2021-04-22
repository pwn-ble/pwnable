import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import platform
import os

class Login(tk.Frame):

    path = Image.open("src/gui/PwnableLogos/PwnableLogo-08.png") # pwnable logo

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root) # tkinter superclass constructor

        self.master = root # bind tkinter app root to this frame instance

        root.wm_title('login')

        # set up user input tracking variables
        self.user_var = tk.StringVar()
        self.passwd_var = tk.StringVar()

        #new label for user using widget label
        user_label = tk.Label(self.master, text = 'Username', bd = 5, font=('arial',20,'bold'))
        user_label.pack(anchor = 'center')
        #new entry for the user label
        user_entry = tk.Entry(self.master, textvariable = self.user_var, bd = 5, font = ('arial',20,'bold'))
        user_entry.pack(anchor = 'center')
        # creating a label for password
        passw_label = tk.Label(self.master, text = 'Password', bd = 5, font = ('arial',20,'bold'))
        passw_label.pack(anchor = 'center')
        # creating a entry for password
        passw_entry = tk.Entry(self.master, textvariable = self.passwd_var, bd = 5, font = ('arial',20,'bold'), show = '@')
        passw_entry.pack(anchor = 'center')
        # submit button
        sub_btn = tk.Button(self.master, text = 'Submit', command = self.login_input)
        sub_btn.pack(anchor = 'center')

    def login_input(self):
        # grab input from entry boxes
        user = self.user_var.get()
        password = self.passwd_var.get()

        print ("Welcome: " + user)
        print ("Your password is: " + password)

        # messagebox.showinfo('Welcome', 'Have fun ' + user)

        self.user_var.set("")
        self.passwd_var.set("")

        # module_title.pack()
        # main_menu_frame.pack()
        # self.master.pack_forget()

        # login_title.pack_forget()
        # user_label.pack_forget()
        # user_entry.pack_forget()
        # passw_label.pack_forget()
        # passw_entry.pack_forget()
        # sub_btn.pack_forget()