import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
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

#ad


#darkmode variables
buttonBG = "#b3b3b3"
backGround = "#f2f2f2"
accent = ""
textColor = "#0d0d0d"

isDark = bool(False)

root.configure(bg=backGround)




def toggle_dark():
    global isDark
    if (isDark == False):
        
        buttonBG = "#1a1a1a"
        backGround = "#333333"
        textColor = "#e6e6e6"

        isDark = True
        
        root.configure(bg=backGround)
        
        programming_button.config(fg=textColor, bg=buttonBG)
        password_button.config(fg=textColor, bg=buttonBG)
        networking_button.config(fg=textColor, bg=buttonBG)
        help_button.config(fg=textColor, bg=buttonBG)
        darktoggle_button.config(fg=textColor, bg=buttonBG)
        label.config(bg=backGround)
        module_title.config(bg=backGround, fg=textColor)
        
        

    elif (isDark == True):
        buttonBG = "#b3b3b3"
        backGround = "#f2f2f2"
        textColor = "#0d0d0d"

        isDark = False

        root.configure(bg=backGround)
        
        programming_button.config(fg=textColor, bg=buttonBG)
        password_button.config(fg=textColor, bg=buttonBG)
        networking_button.config(fg=textColor, bg=buttonBG)
        help_button.config(fg=textColor, bg=buttonBG)
        darktoggle_button.config(fg=textColor, bg=buttonBG)
        label.config(bg=backGround)
        module_title.config(bg=backGround, fg=textColor)





# Pwnable window title
title = root.title("Pwnable")
root.geometry("800x480")
# Pwnable menu title

path = Image.open("PwnableLogos/PwnableLogo-08.png")
resize=path.resize((269,55), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resize)
label = tk.Label(image=photo, bg=backGround)
# label.image = photo
label.pack(pady=(25,0))

# Module menu title
module_title = tk.Label(root, text = "Modules", font="Arial 25", bg=backGround, fg=textColor)
module_title.pack()

# buttons configuration
main_menu_frame = tk.Frame()
programming_button = tk.Button(width=15,
                               text="Programming",
                               font="Arial 20 bold",
                               fg=textColor,
                               bg=buttonBG,
                               command=load_programming_module)
password_button = tk.Button(width=15,
                            text="Password",
                            font="Arial 20 bold",
                            fg=textColor,
                            bg=buttonBG,
                            command=load_password_module)
networking_button = tk.Button(width=15,
                        text="Networking",
                        font="Arial 20 bold",
                        fg=textColor,
                        bg=buttonBG)
help_button = tk.Button(width=15,
                        text="Help",
                        font="Arial 20 bold",
                        fg=textColor,
                        bg=buttonBG,
                        command=load_help)

darktoggle_button = tk.Button(width=10,
                        text="Dark/Light",
                        font="Arial 12 bold",
                        fg=textColor,
                        bg=buttonBG,
                        anchor="sw",
                        command=toggle_dark)


# display buttons
programming_button.pack()
password_button.pack()
networking_button.pack()
help_button.pack()
darktoggle_button.pack()


password_menu_frame = tk.Frame()
back_button = tk.Button(width=6,
                        text="Back",
                        font="Arial 10 bold",
                        fg=textColor,
                        bg="gray",
                        command=load_menu)
password_generator_button = tk.Button(width=17,
                        text="Password Generator",
                        font="Arial 18 bold",
                        fg=textColor,
                        bg=buttonBG)
password_cracker_button = tk.Button(width=17,
                        text="Password Cracker",
                        font="Arial 18 bold",
                        fg=textColor,
                        bg=buttonBG)
root.mainloop()