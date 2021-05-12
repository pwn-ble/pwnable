import tkinter as tk
from PIL import ImageTk, Image

# https://overthewire.org/wargames/bandit/

label_font = ("Consolas", 25, "bold")
button_font = ("Consolas", 12, "bold")
text_font = ("Consolas", 10, "bold")
class OverTheWire(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        self.title("Pwnable - OverTheWire Walkthrough")
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
        self.textarea.insert("end","This game, like most other games, is organised in levels. You start at Level 0 and try to “beat” or “finish” it. Finishing a level results in information on how to start the next level. The pages on this website for “Level <X>” contain information on how to start level X from the previous level. E.g. The page for Level 1 has information on how to gain access from Level 0 to Level 1. All levels in this game have a page on this website, and they are all linked to from the sidemenu on the left of this page.")
        self.textarea.pack()
        self.textarea.config(state="disabled")

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)        

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
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)

    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="ssh")
        label1.pack()
        label2.pack()


class Level_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 1", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                The password for the next level is stored in a file called - located in the home directory.
                                    """
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label1.pack()
        label2.pack()

class Level_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 2", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in a file called spaces in this filename located in the home directory.
                                    """
                                    , font=text_font, justify="left")
        description_label.pack()
        description_label.place(x=400,y=150,anchor="center")
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    

    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label1.pack()
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
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label1.pack()
        label2.pack()

class Level_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 4", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in the only human-readable file in the inhere directory.
                    Tip: if your terminal is messed up, try the “reset” command.                
                                    """
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label1.pack()
        label2.pack()

class Level_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 5", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

                    human-readable
                    1033 bytes in size
                    not executable
                
                                    """
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find")
        label1.pack()
        label2.pack()

class Level_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 6", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored somewhere on the server and has all of the following properties:

                    owned by user bandit7
                    owned by group bandit6
                    33 bytes in size
                
                                    """
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="ls, cd, cat, file, du, find, grep")
        label1.pack()
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
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label1.pack()
        label2.pack()

class Level_8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 8", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in the file data.txt and is the only line of text that occurs only once                
                                    """
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label1.pack()
        label2.pack()

class Level_9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 9", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.                
                                    """
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label1.pack()
        label2.pack()

class Level_10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Level 10", font=label_font)
        label.pack()

        description_label = tk.Label(self, 
                                    text=
                                    """
                    The password for the next level is stored in the file data.txt, which contains base64 encoded data                
                                    """
                                    , font=text_font, pady=50, justify="left")
        description_label.pack(pady=200)
        description_label.place(x=10,y=50)
        
        commands_button = tk.Button(self, text="Commands", command=self.commands)
        commands_button.place(x=370, y=250)

        solution_button = tk.Button(self, text="Solution", command=self.solution)
        solution_button.place(x=370, y=275)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(Level_Page))
        back_button.place(x=45,y=45)
    
    def solution(self):
        label = tk.Label(self, text="This is the answer")
        label.place(x=300, y=250)
    
    def commands(self):
        label1 = tk.Label(self, text="Here are some commands you may need to solve this level!")
        label2 = tk.Label(self, text="grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd")
        label1.pack()
        label2.pack()




# app = OverTheWire()
# app.mainloop()