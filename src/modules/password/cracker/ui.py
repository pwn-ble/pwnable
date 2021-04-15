from guizero import App, Box, PushButton, Slider, Text, TextBox
import os
import subprocess

def lauchChallenge():
    print('launching password cracker challenge...')

    # change working directory to add file
    # os.chdir('')

    # TODO: add challenge user ?

    # TODO: implem subprocess
    subprocess.run([''])

#
# GuiZero components
#

app = App(title="password cracker")

prompt = """
Challenge 1:

all you need to do is get the password to access the next level.
the only problem is that it's contained in a password-protected file, too.
follow the steps to pwn the file and move on. 
"""

promptLabel = Text(app, text=prompt) # add prompt to UI

goButton = PushButton(app, text="Let's go!", command=lauchChallenge) # will begin the challenge

app.display() 