import os
import platform
import subprocess
from service import login_service

"""
we should get a way to link packages, relative imports and fix relative paths
i read something about __main__ and directory structure, but need to do some
more research to get that working
"""

# lauch pwnable home screen script
with subprocess.Popen(['python3', './src/gui/login.py'], stdout=subprocess.PIPE) as login:
    creds = {} # dictionary for credential key-value-pairs

    for line in login.stdout:
        output = login_service.decode_stdout(line) # strip byte-encoding from stdout
        cred_line = output.split() # separate credentials from their label in the stdout
        creds[cred_line[0].strip(':')] = cred_line[1] # add credentials to dictionary as kvp
    login.wait()

    # check for user in system
    if (login_service.check_user(creds['user'])):
        print('user already exists')
        # should have them try a different usrname
    else:
        print('great, lets get you set up...')
        login_service.add_user(creds['user'], creds['password'])