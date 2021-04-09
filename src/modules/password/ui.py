from guizero import App, Box, PushButton, Slider, Text, TextBox
from generator import generator
from hasher import hasher

def check_password():
    if (len(inputBox.value) >= 6 and len(inputBox.value) <= 8): # between 5 and 8 characters
        submitButton.enabled = True # enable the submit button
        inputErrorLabel.visible = False
    else:
        inputErrorLabel.visible = True
        submitButton.enabled = False

    strengthSlider.enabled = True # enable it to alter value
    strengthSlider.value = len(inputBox.value) # alter the value
    strengthSlider.enabled = False # disable it again to prevent manual change

def generate_password(length=15):
    pwd = generator.gen(length) # call password synthesis function
    suggestionOutputLabel.visible = True # show suggestion output label
    suggestionOutputLabel.value = f'Suggested password: {pwd}' # output to the UI

def submit():
    passwd = hasher.hash(inputBox.value) # hash the input from the textbox
    print(passwd)

    # hasher.unshadow(passwd) # write hash to unshadowed john format


#
# GuiZero UI components
#

app = App(title="password strength") # create a window

inputLabel = Text(app, text="enter a password to test strength")

inputContainer = Box(app, layout="grid")
inputBox = TextBox(inputContainer, grid=[0,1]) # add a textbox for input
inputBox.update_command(check_password) # check pass strength after any input
inputErrorLabel = Text(inputContainer, text="password should be 6-8 characters", grid=[0,0], color="red", visible=False)
sliderLabel = Text(app, text="password strength:")
strengthSlider = Slider(app, enabled=False) # add slider to show pass strength

suggestionContainer = Box(app, layout="grid")
suggestionButton = PushButton(app, text="get a password suggestion", command=generate_password) # button to get a suggested password
suggestionOutputLabel = Text(app, visible=False) # initially invisible

submitButton = PushButton(app, text="submit", enabled=False, command=submit) # TODO: finish with submit command

app.display() # show window
