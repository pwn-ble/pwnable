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
    strLength = int(12)

    pwd = ""

    # while loop creates password
    while strLength > 0:
        # randomize the character type with weighted values so the password is mostly letters with a few special characters and numbers, we can change this if we need to
        choices = [0, 1, 2, 3]
        randTypeList = random.choices(choices, weights=(16, 9, 35, 40), k=1)
        # couldn't find a way to do weighted choices without them being output to a string with only one item so this turns it into an int variable
        for i in randTypeList:
            randType = i
        


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

        strLength = strLength - 1  
        print(randType)  

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
