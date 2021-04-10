import os
import subprocess

# should be ran after segue from tkinter UI stuff

os.chdir('src/modules/cli/')

print('welcome to the terminal!')

print('what is your name?')
name = input()

print(f'nice to see you, {name}.\nwe are going to learn how to use a terminal')
print('are you ready?')
answer = input()

if (answer == 'yes'):
    print('great!')
elif (answer == 'no'):
    print('well too bad! ')
else:
    print('what? it was a yes or no question.')

print('lets get started')

subprocess.Popen(['/bin/zsh'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
