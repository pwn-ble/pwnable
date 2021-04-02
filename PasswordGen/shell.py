from guizero import App, PushButton, Slider, Text, TextBox
import random
import string

def check_password():
    # ideally, we want to run a quick crack on the password
        # might use a wordlist or something
        # cant be too intensive and take a long time

    i = inputBox.value # get the textbox input

    strengthSlider.enabled = True # enable it to alter value
    strengthSlider.value = len(i) # alter the value
    strengthSlider.enabled = False # disable it again to prevent manual change

pwdExample = ""

def generate_password():
   # couldn't find library method to spit out special characters so I just created a list
    special = "!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~"
    upperAlph = string.ascii_uppercase
    lowerAlph = string.ascii_lowercase

#enter the length of the password being created
    while (True):
            try:
                length = int(12)
                if (length <= 0):
                    print("Length can't be zero or negative.")
                    continue
            except ValueError:
                print("Please enter a number.")
            else:
                break

    pwd = ""

    # while loop creates password
    while length > 0:
        # randomize the character type
        randType = int(random.randint(0,3))

        length-=1


        if randType == 0:
            #append string with random number
            pwd+=str(random.randint(0,9))
        elif randType == 1:
            #append string with random special character
            pwd+=random.choice(special)
        elif randType == 2:
            #append string with random uppercase letter
            pwd+=random.choice(upperAlph)
        elif randType == 3:
            #append with random lowercase letter
            pwd+=random.choice(lowerAlph)
        else:
            print("ERROR: randType variable not working")

    print("Your password is: " + pwd)
    pwdSuggestion = TextBox(app, text= pwd, width= 15)


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

pwdSuggestionLabel = Text(app, text="Password suggestion:")

app.display() # show window
