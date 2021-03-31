import random
import string

# couldn't find library method to spit out special characters so I just created a list
special = "!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~"
upperAlph = string.ascii_uppercase
lowerAlph = string.ascii_lowercase

#enter the length of the password being created
length = int(input('Please enter length of password: '))
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