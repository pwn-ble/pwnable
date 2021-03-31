import random
import string
import time

chars = string.printable
charsList = list(chars)

userPwd = input("Enter Password to check: ")

guessPwd = ""
startTime = time.time()

while(guessPwd != userPwd):
    guessPwd = random.choices(charsList, k=len(userPwd))

    print("<============" + str(guessPwd) + "============>")

    if(guessPwd == list(userPwd)):
        print("Your password is: " + "".join(guessPwd))
        print("It took %s seconds to crack this password" % (time.time() - startTime))
        print(type(time.time()))
        break