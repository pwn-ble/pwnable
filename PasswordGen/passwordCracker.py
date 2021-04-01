import random
import string
import time

chars = string.printable
charsList = list(chars)

userPwd = input("Enter Password to check: ")

guessPwd = ""
startTime = time.time()
count = 0
pwdLength = 1
while(guessPwd != userPwd):
    guessPwd = random.choices(charsList, k=pwdLength)

    print("<============" + str(guessPwd) + "============>")
    count+=1
    if(count > 10000):
        count = 0
        pwdLength+=1
    
    if(pwdLength > 10):
        pwdLength = 1

    if(guessPwd == list(userPwd)):
        print("Your password is: " + "".join(guessPwd))
        print("It took %s seconds to crack this password" % (time.time() - startTime))
        print("It took %s minutes to crack this password" % ((time.time() - startTime)/60))
        break