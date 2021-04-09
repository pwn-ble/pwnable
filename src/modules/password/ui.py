from guizero import App, Box, PushButton, Slider, Text, TextBox
import subprocess
from generator import generator
from hasher import hasher

def check_form():
    if (len(usernameBox.value) > 0 and len(passwordBox.value) > 0): # TODO: make more complex, ensure long-ish password
        submitButton.enabled = True

def generate_password(length=15):
    pwd = generator.gen(length) # call password synthesis function
    suggestionOutputLabel.visible = True # show suggestion output label
    suggestionOutputLabel.value = f'Suggested password: {pwd}' # output to the UI

def submit():
    """
    will take the inputs and create a new user from them
    """
    passwd = hasher.hash(passwordBox.value) # hash the input from the textbox
    # passwd1 = subprocess.run(['mkpasswd', passwordBox.value])

    subprocess.Popen(['sudo -S', 'useradd', '-m', '-p', passwd, usernameBox.value], stdin='bonjour') # TODO: add a user with password that got hashed

    # hasher.unshadow(passwd) # write hash to unshadowed john format

    # subprocess.call(['python3', 'modules/password/cracker/ui.py']) # TODO: os.chdir() ? app.py that calls ui.py ?

#
# GuiZero UI components
#

app = App(title="create a user") # create window

inputContainer = Box(app, layout="grid") # box for user, pass inputs

usernameLabel = Text(inputContainer, text="username: ", grid=[0,0])
usernameBox = TextBox(inputContainer, grid=[1,0]) # textbox input for username
usernameBox.update_command(check_form) # ensure input is not empty

passwordLabel = Text(inputContainer, text="password: ", grid=[0,1])
passwordBox = TextBox(inputContainer, grid=[1,1]) # add a textbox for password input
passwordBox.update_command(check_form) # check pass isnt empty

submitButton = PushButton(app, text="submit", enabled=False, command=submit)

app.display() # show window
