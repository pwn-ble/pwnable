from guizero import App, PushButton, Slider, Text, TextBox
from generator import generator

def check_password():
    i = inputBox.value # get the textbox input
    strengthSlider.enabled = True # enable it to alter value
    strengthSlider.value = len(i) # alter the value
    strengthSlider.enabled = False # disable it again to prevent manual change

def generate_password(length=15):
    pwd = generator.gen(length) # call password synthesis function
    suggestionOutputLabel.visible = True # show suggestion output label
    suggestionOutputLabel.value = f'Suggested password: {pwd}' # output to the UI

# def test_strength()

#
# GuiZero UI components
#

app = App(title="password strength") # create a window

inputLabel = Text(app, text="enter a password to test strength")

inputBox = TextBox(app) # add a textbox for input
inputBox.update_command(check_password) # check pass strength after any input

sliderLabel = Text(app, text="password strength:")
strengthSlider = Slider(app, enabled=False) # add slider to show pass strength

suggestionButton = PushButton(app, text="get a password suggestion", command=generate_password) # button to get a suggested password

suggestionOutputLabel = Text(app, visible=False) # initially invisible

app.display() # show window
