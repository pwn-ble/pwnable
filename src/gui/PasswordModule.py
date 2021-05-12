import tkinter as tk
import os
from PIL import ImageTk, Image
import random
from tkinter import messagebox
from gui.Generator import Generator



class PasswordModule(tk.Frame):

    photosPath = os.getcwd() + "/gui/PwnableLogos/"

    def __init__(self, root:tk.Tk):
        tk.Frame.__init__(self, root)

        self.master = root
        # Pwnable window title
        self.master.title("Pwnable - Password Best Practices")
        self.master.geometry("800x480")
        
        


        # Module menu title

        self.terminal_frame = tk.Frame()
        self.terminal_frame.pack()
        info_text = "Passwords are very important. They\nare the first line of defense against \nunathorized access of your personal \ninformation."
        self.info_output = tk.Label(self.master, bg="black", fg="green", font="Consolas 18 bold", text=info_text)
        self.info_output.config(width=45, height=7)
        self.info_output.pack()
        
        self.next_btn = tk.Button(self.master, width=10, text="next", command=self.next1)
        self.next_btn.place(rely=0.9, relx=0.7)
    
    
    def badGuess(self):  
        messagebox.showerror(title="Incorrect",message="Remember, a good password should be around 12 characters and include uppercase, lowercase, a special character, and not use words that could be easily guessed.")

    def generatePwd(self):
        strongPass= Generator(12).p
        self.genedPass.config(width=25, height=2, text=strongPass)
    

    def next1(self):
        info_text= "In this module we are going to \nlearn about secure passwords. \nA secure password significantly \ndecreases your chances of having \nyour data breached."
        self.info_output.config(text=info_text, width=45, height=7)
        self.next_btn.config(command=self.next2)
        
    def next2(self):
        info_text= "There are a few different types \nof attacks a hacker might use to \ngain access to your password."
        self.info_output.config(text=info_text, width=45, height=7)
        self.next_btn.config(command=self.next3)
        
    def next3(self):
        info_text= "The main type of attack we will \nfocus on is a 'brute force' attack. \nA brute force attack is when a \nhacker will try various passwords \nover and over until one works."
        self.info_output.config(text=info_text, width=45, height=7)
        self.next_btn.config(command=self.next4)
        
    def next4(self):
        info_text= "Doing this manually is time consuming \nand borderline impossible. They will \nusually automate the process with \na program."
        self.info_output.config(text=info_text, width=45, height=7)
        self.next_btn.config(command=self.next5)
    
    def next5(self):
        info_text= "A strong password will significantly \nincrease the amount of time it takes \nto crack a password with the brute \nforce method."
        self.info_output.config(text=info_text, width=45, height=7)
        self.next_btn.config(command=self.next6)
        
    def next6(self):
        info_text= "Click the button below to create a \nstrong password. Note that the \npassword is 12 characters and contains \nnumbers, upper and lower case letters, \nas well as special characters."
        self.info_output.config(text=info_text, width=45, height=7)
        self.next_btn.config(command=self.nextFinal)
        
        self.passGenBtn = tk.Button(self.master, width=15, text="Generate Password", bg="black", fg="green", command=self.generatePwd)
        self.passGenBtn.place(rely=0.9, relx=0.1)
        
        self.genedPass = tk.Label(self.master, bg="black", fg="white", font="Consolas 10 bold", text="Test")
        self.genedPass.config(width=25, height=2)
        self.genedPass.place(rely=0.87, relx=0.37)
      
      
      
      
      
    def nextFinal(self):
        info_text= "Pop Quiz: Choose the strongest password!"
        self.next_btn.destroy()
        self.passGenBtn.destroy()
        self.genedPass.destroy()
        self.info_output.config(text=info_text, width=45, height=2)
        self.next_btn.pack_forget()
        badPassList=["password123","L2$li","W2[5","$2+mS;", "zkh5b", "goldenDoodle1", "sgbrkhbjjl", "hpotter1$", "B95XD]",
                     "nr?7vd", "ILoveFortnite13", "12$31#", "ABC123", "qwerty09", "ASdf45", "myPassword", "Sparky!", "drowssap1", "Henry43!", "hello145!", "letmein1!"]
        badPass1=random.choice(badPassList)
        badPass2=random.choice(badPassList)
        badPass3=random.choice(badPassList)
        badPass4=random.choice(badPassList)
        badPass5=random.choice(badPassList)
        badPass6=random.choice(badPassList)
        goodPass= Generator(12).p
        
        #quiz buttons
        self.guess1 = tk.Button(self.master, width=10, text=badPass1, bg="black", fg="green", command=self.badGuess)
        self.guess1.place(rely=0.5, relx=0.2)
        self.guess2 = tk.Button(self.master, width=10, text=badPass2, bg="black", fg="green", command=self.badGuess)
        self.guess2.place(rely=0.5, relx=0.4)
        self.guess3 = tk.Button(self.master, width=10, text=badPass3, bg="black", fg="green", command=self.badGuess)
        self.guess3.place(rely=0.5, relx=0.6)
        self.guess4 = tk.Button(self.master, width=10, text=goodPass, bg="black", fg="green", command=self.back)
        self.guess4.place(rely=0.65, relx=0.2)
        self.guess5 = tk.Button(self.master, width=10, text=badPass4, bg="black", fg="green", command=self.badGuess)
        self.guess5.place(rely=0.65, relx=0.4)
        self.guess6 = tk.Button(self.master, width=10, text=badPass5, bg="black", fg="green", command=self.badGuess)
        self.guess6.place(rely=0.65, relx=0.6)
        
        
        
    def back(self):
        self.info_output.destroy()
        
        
        self.guess1.destroy()
        self.guess2.destroy()
        self.guess3.destroy()
        self.guess4.destroy()
        self.guess5.destroy()
        self.guess6.destroy()
        messagebox.showinfo(title="Correct!",message="Congrats, you guessed correctly! Click the menu button to go to another Module.")
        
        
        
        
   