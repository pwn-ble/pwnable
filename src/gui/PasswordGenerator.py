import tkinter as tk
import subprocess

from gui.Popup import Popup
from modules.password.hasher import hasher

class PasswordGenerator(tk.Frame):

    def __init__(self, root: tk.Tk):
        tk.Frame.__init__(self, root)

        self.prompt = """
            passwords are very important, they protect all of your data.
            you should make sure to use strong passwords, 
            because most of them can be hacked.
            """

        self.promptInfoBlurb = Popup(root, self.prompt) # present an info blurb
        self.promptInfoBlurb.lift(self)

        self.inputLabel = tk.Text(root)
        self.inputLabel.insert(tk.END, "enter a password to test its strength")
        self.inputLabel.pack()

        # # self.inputContainer = tk.Box(root, layout="grid")

        self.inputBox = tk.Entry(root, cnf = {"update_command": self.check_form})
        self.inputBox.grid=(0,1) # add a textbox for input
        self.inputBox.pack()

        self.inputErrorLabel = tk.Text(root, text="password should be 6-8 characters", grid=[0,0], color="red", visible=False)

        self.sliderLabel = tk.Text(root).insert(tk.END, "password length:")
        self.strengthSlider = tk.Slider(root, enabled=False) # add slider to show pass strength

        # suggestionContainer = Box(root, layout="grid")
        # suggestionButton = PushButton(root, text="get a password suggestion", command=generate_password) # button to get a suggested password
        # suggestionOutputLabel = Text(root, visible=False) # initially invisible

        self.submitButton = tk.PushButton(root, text="submit", enabled=False, command=submit)
        self.submitButton.pack()
        
        # self.inputBox.pack()
        # self.inputErrorLabel.pack()
        # self.sliderLabel.pack()
        # self.strengthSlider.pack()

    def check_form(self):
        if (len(self.usernameBox.value) > 0 and len(self.passwordBox.value) > 0): # TODO: make more complex, ensure long-ish password
            submitButton.enabled = True

    def generate_password(self, length = 15):
        pwd = generator.gen(length) # call password synthesis function
        suggestionOutputLabel.visible = True # show suggestion output label
        suggestionOutputLabel.value = f'Suggested password: {pwd}' # output to the UI

    def submit(self):
        """
        will take the inputs and create a new user from them
        """
        passwd = hasher.hash(passwordBox.value) # hash the input from the textbox
        # passwd1 = subprocess.run(['mkpasswd', passwordBox.value])

        title = 'an intro to passwords'
        b = f'your password has been encrypted.\nthis is what it looks like in the OS: {passwd}'
        i = info(title, b)
        b = "this is done so that your password isn't stored in plaintext for everyone to see"
        i = info(title, b)
        # another prompt
        b = "however, we are going to crack this password to show how easy it can be"
        i = info(title, b)
        # popup with john command
        b = "the password cracking tool 'John the Ripper' is going to be used"
        i = info(title, b)

        # run in terminal, wait for output
        subprocess.call(['/bin/bash'])

        # more?
        