import tkinter as tk
import subprocess

from gui.Popup import Popup
from gui.Terminal import Terminal
from modules.password.hasher import hasher

class PasswordGenerator(tk.Frame):

    def __init__(self, root: tk.Tk):
        tk.Frame.__init__(self, root)

        self.master = root

        self.prompt = """
            passwords are very important, they protect all of your data.
            you should make sure to use strong passwords, 
            because most of them can be hacked.
            """

        self.promptInfoBlurb = Popup(root, self.prompt) # present an info blurb
        self.promptInfoBlurb.lift(self)

        self.inputLabel = tk.Label(root, text="enter a password to test its strength")
        self.inputLabel.pack()

        self.passwordVar = tk.StringVar()

        self.inputBox = tk.Entry(root, textvariable=self.passwordVar)
        self.inputBox.grid=(0,1) # add a textbox for input
        self.inputBox.pack()

        self.inputErrorLabel = tk.Label(root, text="password should be 6-8 characters", fg="red")

        # suggestionContainer = Box(root, layout="grid")
        # suggestionButton = PushButton(root, text="get a password suggestion", command=generate_password) # button to get a suggested password
        # suggestionOutputLabel = Text(root, visible=False) # initially invisible

        self.submitButton = tk.Button(root, text="submit", command=self.submit)
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
        passwd = hasher.hash(self.passwordVar.get()) # hash the input from the textbox
        hasher.unshadow(passwd) # write unshadowed password stuff to file

        title = 'an intro to passwords'
        b = f'your password has been encrypted.\nthis is what it looks like in the OS: {passwd}'
        i = Popup(self.master, b)
        b = "this is done so that your password isn't stored in plaintext for everyone to see"
        i = Popup(self.master, b)
        # another prompt
        b = "however, we are going to crack this password to show how easy it can be"
        i = Popup(self.master, b)
        # popup with john command
        b = "the password cracking tool 'John the Ripper' is going to be used"
        i = Popup(self.master, b)

        term = Terminal(self.master)
        term.run_command(f'john src/etc/cache/fake_unshadow.txt')
        