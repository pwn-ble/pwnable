import tkinter as tk
from PIL import ImageTk, Image
import os

# https://overthewire.org/wargames/bandit/

label_font = ("Consolas", 25, "bold")
button_font = ("Consolas", 12, "bold")
text_font = ("Consolas", 10, "bold")

class OverTheWire(tk.Tk):

    photosPath = os.getcwd() + "/gui/PwnableLogos/"

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        

        self.title("Pwnable - OverTheWire Walkthrough")        
        
        container = tk.Frame(self)

        back_button = tk.Button(self, text="Home", width=6, command=lambda: self.show_frame(Level_Page))
        back_button.place(x=45,y=45)

        
        tk.Tk.geometry(self,"800x480")
        container.pack(side="top",fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frame = {}

        for F in (Level_Page, Start_Page, Level_1, Level_2, Level_3, Level_4, Level_5, Level_6, Level_7, Level_8, Level_9, Level_10, Explain):

            frame = F(container, self)

            self.frame[F] = frame

            # frame.pack()
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(Level_Page)
    
    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()

class Level_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menu_label = tk.Label(self, text="OverTheWire Walkthrough", font=label_font)
        menu_label.pack()

        button0 = tk.Button(self, text="Start", font=button_font, width=10, command=lambda: controller.show_frame(Start_Page))
        button1 = tk.Button(self, text="Level 1", font=button_font, width=10, command=lambda: controller.show_frame(Level_1))
        button2 = tk.Button(self, text="Level 2", font=button_font, width=10, command=lambda: controller.show_frame(Level_2))
        button3 = tk.Button(self, text="Level 3", font=button_font, width=10, command=lambda: controller.show_frame(Level_3))
        button4 = tk.Button(self, text="Level 4", font=button_font, width=10, command=lambda: controller.show_frame(Level_4))
        button5 = tk.Button(self, text="Level 5", font=button_font, width=10, command=lambda: controller.show_frame(Level_5))
        button6 = tk.Button(self, text="Level 6", font=button_font, width=10, command=lambda: controller.show_frame(Level_6))
        button7 = tk.Button(self, text="Level 7", font=button_font, width=10, command=lambda: controller.show_frame(Level_7))
        button8 = tk.Button(self, text="Level 8", font=button_font, width=10, command=lambda: controller.show_frame(Level_8))
        button9 = tk.Button(self, text="Level 9", font=button_font, width=10, command=lambda: controller.show_frame(Level_9))
        button10 = tk.Button(self, text="Level 10", font=button_font, width=10, command=lambda: controller.show_frame(Level_10))
        button11 = tk.Button(self, text="HELP", font=button_font, width=10, command=lambda: controller.show_frame(Explain))
        
        button0.place(x=150, y=50)
        button1.place(x=150, y=100)
        button2.place(x=250, y=100)
        button3.place(x=350, y=100)
        button4.place(x=450, y=100)
        button5.place(x=550, y=100)
        button6.place(x=150, y=150)
        button7.place(x=250, y=150)
        button8.place(x=350, y=150)
        button9.place(x=450, y=150)
        button10.place(x=550, y=150)
        button11.place(x=150, y=200)
        
class Explain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Explanation", font=label_font)
        label.pack()

        scroll_y = tk.Scrollbar(self, orient="vertical")
        
        self.textarea = tk.Text(self, height=10, width=60, yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right", fill="y")
        scroll_y.config(command=self.textarea.yview)
        self.textarea.insert("end", "\nThis game, like most other games, is organised in levels.\nYou start at Level 0 and try to “beat” or “finish” it.\nFinishing a level results in information on how to start the\nnext level. The buttons for “Level 0-10” contain information\non how to start level 1-10 from the previous level. E.g. The\npage for Level 1 has information on how to gain access from Level 0 to Level 1.")
        self.textarea.pack()
        self.textarea.config(state="disabled")


class Start_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 0", font=label_font)
        label.pack()

        scroll_y = tk.Scrollbar(self, orient="vertical")
        
        description_label = tk.Label(self, 
                                    text=
                                    """
The goal of this level is for you to log into the game using SSH.
The host to which you need to connect is bandit.labs.overthewire.org, on port 2220.
The username is bandit0 and the password is bandit0.
Once logged in, go to the Level 1 page to find out how to beat Level 1.
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")


    def solution(self):
        label = tk.Label(self, text="Type into the terminal: 'ssh bandit0@bandit.labs.overthewire.org -p 2220'")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="ssh")
        label2.pack()

# ls -la\ncat readme\nssh bandit1@localhost

class Level_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 1", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
The password for the next level is stored in a file
called "-" located in the home directory.
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="ls\ncat ./-\nssh bandit2@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label2.pack()

class Level_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 2", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
The password for the next level is stored in a file called 
spaces in this filename located in the home directory."""
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    

    def solution(self):
        label = tk.Label(self, text="ls\ncat 'spaces in this filename'\nssh bandit3@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label2.pack()

class Level_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 3", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in a hidden file in the inhere directory.                
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="ls\ncd inhere/\nls -al\ncat .hidden\nssh bandit4@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label2.pack()

class Level_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 4", font=label_font)
        label.pack()

        description_label = tk.Label(self,
                                    text=
                                    """
                    The password for the next level is stored in the only 
                    human-readable file in the inhere directory.

                    Tip: if your terminal is messed up, try the “reset” command.                
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="ls -la\ncd inhere/\nls\nfile ./*\ncat ./-file07\nssh bandit5@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label2.pack()

class Level_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 5", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
The password for the next level is stored in a file somewhere under 
the inhere directory and has all of the following properties:

                        human-readable
                        1033 bytes in size
                        not executable
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=120,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="cd inehre/\nls\nfind . -size 1033c\ncat ./maybehere07/.file2\nssh bandit6@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label2.pack()

class Level_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 6", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """

The password for the next level is stored somewhere on the server 
and has all of the following properties:

                    owned by user bandit7
                    owned by group bandit6
                    33 bytes in size
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=120,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="find / -user bandit7 -group bandit6 -size 33c\ncat /var/lib/dpkg/info/bandit7.password\nssh bandit7@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find, grep")
        label2.pack()

class Level_7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 7", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in the file data.txt next to the word millionth                
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="ls\ncat data.txt | grep millionth\n ssh bandit8@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label2.pack()

class Level_8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 8", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
The password for the next level is stored in the file data.txt 
and is the only line of text that occurs only once                
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="cat data.txt | sort | uniq -u\nssh bandit9@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label2.pack()

class Level_9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 9", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                        The password for the next level is stored in the file data.txt
                        in one of the few human-readable strings, preceded by several ‘=’ characters.                
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="ls\nstrings data.txt | grep =\nssh bandit10@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label2.pack()

class Level_10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 10", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
The password for the next level is stored in 
the file data.txt, which contains base64 encoded data
                                    """
                                    , font=text_font, justify="left")
        description_label.place(x=400,y=100,anchor="center")

        command_label = tk.Label(self, text="Here are some commands you may need to solve this level!")
        command_label.place(x=400, y=220, anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=400, y=250, anchor="center")

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=400, y=280, anchor="center")

    
    def solution(self):
        label = tk.Label(self, text="ls\ncat data.txt | base64 --decode\nssh bandit11@localhost")
        label.place(x=400, y=340, anchor="center")
    
    def commands(self):
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label2.pack()




# app = OverTheWire()
# app.mainloop()