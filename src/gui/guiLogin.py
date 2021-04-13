from guizero import App, Text, TextBox, PushButton, Window
import tkinter as tk
from tkinter import messagebox


root=tk.Tk()
root.title("Pwn@ble Login Screen")

root.geometry('800x480')
user_var=tk.StringVar()
passwd_var=tk.StringVar()



def login_input():
    user = user_var.get()
    password = passwd_var.get()

    print ("Welcome : " + user)
    print ("Your password is :" + password)

    messagebox.showinfo('Welcome', 'Have fun' + user)


    user_var.set("")
    passwd_var.set("")


#new label for user using widget label
user_label = tk.Label(root, text = 'Username', bd = 5, font=('arial',20,'bold'))

#new entry for the user label
user_entry = tk.Entry(root,textvariable = user_var, bd = 5, font = ('arial',20,'bold'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', bd = 5, font = ('arial',20,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root,textvariable = passwd_var, bd = 5, font = ('arial',20,'bold'), show = '@')

sub_btn=tk.Button(root,text = 'Submit', command = login_input)

# parameter variables for easy adjustments
button_width = 15
button_font = "Arial 20 bold"

#app = App(title="Pwnable")
#title_pwnable = Text(app, text="Pwnable", size=50, font="Arial")
#module_title = Text(app, text="Login", size=25)

# buttons configuration
#main_menu_frame = tk.Frame()

user_label.place(relx = .5, rely = .15, anchor= 'center')
user_entry.place(relx = .5, rely = .25, anchor= 'center')
passw_label.place(relx = .5, rely = .35, anchor= 'center')
passw_entry.place(relx = .5, rely = .45, anchor= 'center')
sub_btn.place(relx = .5, rely = .7, anchor= 'center')



#login_button = tk.Button(width=button_width,
                                #text="Login",
                                #font= "arial 14 bold",
                                #fg="red",
                                #bg="black",
                                #command=login_input)



# display buttons
#main_menu_frame.pack()

#user_label.pack()
#user_entry.pack()
#passw_label.pack()
#passw_entry.pack()

#login_button.pack()



root.mainloop()

#app.display()

#lil test

