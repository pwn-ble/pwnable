import sys
import subprocess
import os

# def add_user(uname: str, passwd: str):
#     with Popen(["users"], stdout=PIPE) as proc:
#         log.write(proc.stdout.read())
    
def check_user(uname: str):
    with Popen(["users"], stdout=PIPE) as proc:
        output = proc.stdout.read()
        print(output) # need to decode
        return output
