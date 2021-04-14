import sys
import subprocess
import shlex
import os

def add_user(uname: str, passwd: str):
    """
    uname: new username to add to system
    passwd: new password to associate with the account username
    """
    encrypted_passwd = run_process(f'mkpasswd {passwd}') # hash the new password
    print(encrypted_passwd)

    # useradd -m -N -g pwnable -p $(mkpasswd bonjour){uname}


def check_user(uname: str) -> bool:
    """
    uname: the proposed username to assign to a new user
    returns a boolean indicating whether the proposed username is already taken or not
    """
    system_users = run_process('users')
        
    for user in system_users.split('\n'):
        if (uname == user): # if user exists in system
            return True # found, so user should try a different username
    return False # didn't find a user with that name, should be good to make one on the system

def decode_stdout(input) -> str:
    return input.decode('utf-8').rstrip('\r|\n')

def run_process(command: str) -> str:
    """
    command: string formatted command to run
    returns output from command, ran as a subprocess
    """
    with subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE) as proc:
        return decode_stdout(proc.stdout.read())
