import hashlib
import sys # TODO: get argparse to work instead of sys?

# can be called from another script
def hasher(input):
    i = input.encode(encoding='UTF-8') # encode the input for hashing
    return hashlib.sha256(i).hexdigest() # hash it

# if the script is called from CLI w/ hash input arg
if (len(sys.argv) > 1): # we got a password to hash
    hashed = hasher(sys.argv[1]) # get function output
    print(hashed) # print output
