import hashlib
import platform
import subprocess
import sys # TODO: get argparse to work instead of sys?

def hash(input):
    """
    takes a password string and hashes it with a salt nonce
    returns a string including the hash and salt info
    """

    # call hash.c with password argument passed to this script
    if (platform.system() == 'Windows'):
        output = subprocess.check_output(f'.\\hasher\\a.exe {input}', shell=True)
    else:
        output = subprocess.check_output(f'./hasher/a.out {input}', shell=True)

    # decode byte-encoded ouput to string
    decoded = output.decode('utf-8')

    return decoded

def unshadow(hash_str, file_name='fake_unshadow'):
    """
    takes a password hash and formats it for reading by John the ripper
    """

    # check if file_name argument has '.txt' extension
    file_name = file_name if (file_name[-4:-1] == '.txt') else f'{file_name}.txt'

    if (open(file_name, 'w')):
        f = open(file_name, 'w')
        # write a fake unshadow /etc/passwd & /etc/shadow entry
        f.write(f'fakeGuy:{hash_str}:1000:1000::/home/pwnable:/bin/bash')
        f.close()

# if the script is called from CLI w/ hash input arg
if (len(sys.argv) > 1): # we got a password to hash
    hashed = hash(sys.argv[1]) # get function output
    print(hashed) # print output
