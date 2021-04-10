import sys
from generator import gen

# make sure the arg provided is an integer > 0
if (len(sys.argv) > 1 and int(sys.argv[1], base=10) > 0):
    pwd = gen(int(sys.argv[1], base=10)) # generate a password

else:
    # enter the length of the password being created
    while (True):
            try:
                length = int(input('Please enter length of password: '))
                if (length <= 0):
                    print("Length can't be zero or negative.")
                    continue
            except ValueError:
                print("Please enter a number.")
            else:
                break

    pwd = gen(length) # generate a password

# TODO: be able to output pwd inside a calling script 
print("Your password is: " + pwd)