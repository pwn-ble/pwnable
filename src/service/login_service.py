import sys
import subprocess
import os

# def add_user(uname: str, passwd: str):
#     with Popen(["users"], stdout=PIPE) as proc:
#         log.write(proc.stdout.read())

def check_user(uname: str) -> bool:
    """
    uname: the proposed username to assign to a new user

    returns a boolean indicating whether the proposed username is already taken or not
    """
    with subprocess.Popen(['cat', './src/service/fake_users.txt'], stdout=subprocess.PIPE) as checker:
        output = decode_stdout(checker.stdout.read()) # get process output
        
        for user in output.split('\n'):
            if (uname == user): # if user exists in system
                return True # found, so user should try a different username
            else:
                print('should create a new system user')
                # handle user creation
        return False # didn't find a user with that name, should be good to make one on the system

def decode_stdout(input) -> str:
    return input.decode('utf-8').rstrip('\r|\n')
