import subprocess
import sys

# call hash.c with password argument passed to this script
output = subprocess.check_output(f'./a.out {sys.argv[1]}', shell=True)
# decode byte-encoded ouput to string
decoded = output.decode('utf-8')

# open a file to write hash info to
if (open('fake_unshadow.txt', 'w')):
    f = open('fake_unshadow.txt', 'w')
    # write a fake unshadow /etc/passwd & /etc/shadow entry
    f.write(f'fakeGuy:{decoded}:1000:1000::/home/pwnable:/bin/bash')
    f.close()
