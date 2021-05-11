import random
import string
import sys


p = ""

class Generator:
# couldn't find library method to spit out special characters so I just created a list
    

    def __init__(self, length):
        special = "!#$%&*@"
        upperAlph = string.ascii_uppercase
        lowerAlph = string.ascii_lowercase
        pwd = "" # will hold the password through the script
        self.p = ""

        # while loop creates password
        while length > 0:
            # randomize the character type
            randType = int(random.randint(0,3))

            length -= 1

            if randType == 0:
            #append string with random number
                self.p += str(random.randint(0,9))
            elif randType == 1:
            #append string with random special character
                self.p += random.choice(special)
            elif randType == 2:
            #append string with random uppercase letter
                self.p += random.choice(upperAlph)
            elif randType == 3:
            #append with random lowercase letter
                self.p += random.choice(lowerAlph)
            else:
                print("ERROR: randType variable not working")

        
