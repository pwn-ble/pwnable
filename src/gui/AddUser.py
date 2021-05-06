import tkinter as tk
from tkinter import messagebox
import os

from .Login import Login

class AddUser(Login, tk.Frame):

    def __init__(self, root: tk.Tk):
        tk.Frame.__init__(self, root) # tkinter Frame constructor

        self.master = root # work of intance copy of the Tk root

        self.master.title("Pwn@ble - Create User") # alter window title

        self.master.geometry('800x480') # set frame's window size

        # input tracker variables
        self.user_var=tk.StringVar()
        self.passwd_var=tk.StringVar()

        #new label for user using widget label
        self.user_label = tk.Label(root, text = 'Username', bd = 5, font=('arial',20,'bold'))
        #new entry for the user label
        self.user_entry = tk.Entry(root,textvariable = self.user_var, bd = 5, font = ('arial',20,'bold'))
        # creating a label for password
        self.passw_label = tk.Label(root, text = 'Password', bd = 5, font = ('arial',20,'bold'))
        # creating a entry for password
        self.passw_entry = tk.Entry(root,textvariable = self.passwd_var, bd = 5, font = ('arial',20,'bold'), show = '@')
        self.sub_btn = tk.Button(root,text = 'Submit', command = lambda: self.attempt(self.add_user))

        # place components in UI
        self.user_label.place(relx = .5, rely = .15, anchor= 'center')
        self.user_entry.place(relx = .5, rely = .25, anchor= 'center')
        self.passw_label.place(relx = .5, rely = .35, anchor= 'center')
        self.passw_entry.place(relx = .5, rely = .45, anchor= 'center')
        self.sub_btn.place(relx = .5, rely = .7, anchor= 'center')

    def add_user(self, user_name, passwd) -> bool:
        """
        append user/pass entry to the user cache file
        return success status
        """
        tmp = open(self.user_file_path, "a") # open user cache file for appending
        bytes_written = tmp.write(user_name + ", " + passwd + "\n") # try to add the new user to the file
        tmp.close() # close the file IO process

        # return the operation success status
        if bytes_written > 0: return True
        else: return False
    