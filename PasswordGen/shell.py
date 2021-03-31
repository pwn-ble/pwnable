from guizero import App, PushButton, Slider, Text, TextBox

def check_password():
    # ideally, we want to run a quick crack on the password
        # might use a wordlist or something
        # cant be too intensive and take a long time

    i = inputBox.value # get the textbox input

    strengthSlider.enabled = True # enable it to alter value
    strengthSlider.value = len(i) # alter the value
    strengthSlider.enabled = False # disable it again to prevent manual change

def generate_password():
    # can call the generator.py script here
    # output to the UI
    print("need to finish")

#
# GuiZero UI components
#

app = App(title="password strength") # create a window

inputLabel = Text(app, text="enter a password to test strength")

inputBox = TextBox(app) # add a textbox for input
inputBox.update_command(check_password) # check pass strength after any input

sliderLabel = Text(app, text="password strength:")
strengthSlider = Slider(app, enabled=False) # add slider to show pass strength

# submitButton = PushButton(app, text="check password", command=check_password)
suggestionButton = PushButton(app, text="get a password suggestion", command=generate_password) # open another textbox for length ?

app.display() # show window
