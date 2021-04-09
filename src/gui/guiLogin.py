from guizero import App, Text, TextBox, PushButton, Window
import tkinter as tk


root=tk.Tk()

user_var=tk.StringVar()
passwd_var=tk.StringVar()



def login_input():
    user = user_var.get()
    password = passwd_var.get()

    print ("Welcome : " + user)
    print ("Your password is :" + password)


    user_var.set("")
    passwd_var.set("")


#new label for user using widget label
user_label = tk.Label(root, text = 'Username', font=('arial',20,'bold'))

#new entry for the user label
user_entry = tk.Entry(root,textvariable = user_var, font = ('arial',20,'bold'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('arial',20,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root,textvariable = passwd_var, font = ('arial',20,'bold'), show = '@')

# parameter variables for easy adjustments
button_width = 15
button_font = "Arial 20 bold"

app = App(title="Pwnable")
title_pwnable = Text(app, text="Pwnable", size=50, font="Arial")
module_title = Text(app, text="Login", size=25)

# buttons configuration
main_menu_frame = tk.Frame()

#sub_btn=tk.Button(root,text = 'Submit', command = login_input)


login_button = tk.Button(width=button_width,
                                text="Login",
                                font= "arial 14 bold",
                                fg="red",
                                bg="black",
                                command=login_input)



# display buttons

user_label.grid(row=0,column=0)
user_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)

login_button.pack()

main_menu_frame.pack()


app.display()

