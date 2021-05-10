import tkinter as tk
from tkinter import messagebox
import os



class Login(tk.Frame):

    user_file_path = os.getcwd() + "/etc/users.txt" # for handling user login / add

    def __init__(self, root: tk.Tk):
        tk.Frame.__init__(self, root) # tkinter Frame constructor

        self.master = root # work of intance copy of the Tk root

        self.master.title("Pwn@ble - Login") # alter window title

        self.master.geometry('800x480') # set frame's window size

        # input tracker variables
        self.user_var = tk.StringVar()
        self.passwd_var = tk.StringVar()

        # variables to pass between functions
        self.user_cred = ""
        self.pass_cred = ""

        #new label for user using widget label
        user_label = tk.Label(root, text = 'Username', bd = 5, font=('arial',20,'bold'))
        #new entry for the user label
        user_entry = tk.Entry(root,textvariable = self.user_var, bd = 5, font = ('arial',20,'bold'))
        # creating a label for password
        passw_label = tk.Label(root, text = 'Password', bd = 5, font = ('arial',20,'bold'))
        # creating a entry for password
        passw_entry=tk.Entry(root,textvariable = self.passwd_var, bd = 5, font = ('arial',20,'bold'), show = '@')
        sub_btn=tk.Button(root,text = 'Submit', command = lambda: self.attempt(self.check_user))

        # place components in UI
        user_label.place(relx = .5, rely = .15, anchor= 'center')
        user_entry.place(relx = .5, rely = .25, anchor= 'center')
        passw_label.place(relx = .5, rely = .35, anchor= 'center')
        passw_entry.place(relx = .5, rely = .45, anchor= 'center')
        sub_btn.place(relx = .5, rely = .7, anchor= 'center')

    def check_user(self, uname, passwd) -> bool:
        """
        read user cache file for the provided credentials;
        see if they exist;
        return the result, true or false;
        """
        print(uname)
        print(passwd)

        tmp_file = open(self.user_file_path, 'r') # read the contents of the user cache file
        tmp = tmp_file.read() # read the user entries
        tmp_file.close() # close IO process
        if tmp.__contains__(uname + ", " + passwd): 
            self.destroy()
            return True
        else: return False
            
    def get_input(self):
        # retrieve the user's credentials
        self.user_cred = self.user_var.get()
        self.pass_cred = self.passwd_var.get()

        # clear UI inputs
        self.user_var.set("")
        self.passwd_var.set("")

    def attempt(self, callback):
        self.get_input() # grab user creds
        op_state = callback(self.user_cred, self.pass_cred)
        if op_state:
            print('success')
            # do more
            # self.destroy() # exit the login process
        else:
            print('oh no')
            messagebox.showwarning("Incorrect", "Username or Password was incorrect, please try again!")
