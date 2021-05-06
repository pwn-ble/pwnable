import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()

# programming module command
def load_programming_module():
    print("Loading Programming Module...")

# password module command
def load_password_module():
    # removes previous buttons
    programming_button.pack_forget()
    password_button.pack_forget()
    help_button.pack_forget()
    networking_button.pack_forget()

    # load new buttons
    back_button.pack(side=tk.TOP, anchor="nw")
    back_button.place(x=45, y=45)
    password_generator_button.pack()
    password_cracker_button.pack()

# help command
def load_help():
    print("Loading Help...")

def load_menu():
    # removes previous buttons
    password_generator_button.pack_forget()
    password_cracker_button.pack_forget()
    back_button.pack_forget()
    back_button.place_forget()
    
    # load new buttons
    programming_button.pack()
    password_button.pack()
    networking_button.pack()
    help_button.pack()
# parameter variables for easy adjustments

# Pwnable window title
title = root.title("Pwnable")
# set window size
root.geometry("800x480")
# set background color
root.configure(background="black")
# Pwnable logo
path = Image.open("PwnableLogos/PwnableLogo-08.png")
resize=path.resize((269,55), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resize)
label = tk.Label(bg='black',image=photo)
#label.image = photo
label.pack(pady=(25,0))

# Module menu title
module_title = tk.Label(root, bg='black', fg='white', text = "Modules", font="Arial 25")
module_title.pack()

# buttons configuration
main_menu_frame = tk.Frame()
programming_button = tk.Button(width=15,
                               text="CLI",
                               font="Arial 20 bold",
                               fg="white",
                               bg="black",
                               command=load_programming_module)
password_button = tk.Button(width=15,
                            text="Password",
                            font="Arial 20 bold",
                            fg="white",
                            bg="black",
                            command=load_password_module)
networking_button = tk.Button(width=15,
                        text="Networking",
                        font="Arial 20 bold",
                        fg="white",
                        bg="black")
help_button = tk.Button(width=15,
                        text="Help",
                        font="Arial 20 bold",
                        fg="white",
                        bg="black",
                        command=load_help)

# display buttons
programming_button.pack()
password_button.pack()
networking_button.pack()
help_button.pack()


password_menu_frame = tk.Frame()
back_button = tk.Button(width=6,
                        text="Back",
                        font="Arial 10 bold",
                        fg="white",
                        bg="gray",
                        command=load_menu)
password_generator_button = tk.Button(width=17,
                        text="Password Generator",
                        font="Arial 18 bold",
                        fg="white",
                        bg="black")
password_cracker_button = tk.Button(width=17,
                        text="Password Cracker",
                        font="Arial 18 bold",
                        fg="white",
                        bg="black")
root.mainloop()
