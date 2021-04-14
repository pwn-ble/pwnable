import os
import platform
import subprocess
from service import login_service

"""
we should get a way to link packages, relative imports and fix relative paths
i read something about __main__ and directory structure, but need to do some
more research to get that working
"""

def decode_stdout(input):
    return input.decode('utf-8').rstrip('\r|\n')

# lauch pwnable home screen script
with subprocess.Popen(['python3', './src/gui/login.py'], stdout=subprocess.PIPE) as login:
    creds = {} # dictionary for credential key-value-pairs

    for line in login.stdout:
        output = decode_stdout(line) #strip byte-encoding from stdout
        cred_line = output.split() # separate credentials from their label in the stdout
        creds[cred_line[0].strip(':')] = cred_line[1] # add credentials to dictionary as kvp
    login.wait()

    # check for user in system
    with subprocess.Popen(['cat', './src/service/fake_users.txt'], stdout=subprocess.PIPE) as checker:
        output = decode_stdout(checker.stdout.read())
        for user in output.split('\n'):
            if (creds['user'] == user): # 
                print('duplicate username')
            else:
                print('should create a new system user')
                break
