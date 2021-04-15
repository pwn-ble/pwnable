import os
import subprocess
import tkinter

# should be ran after segue from tkinter UI stuff

os.chdir('src/modules/cli/')

root = tkinter.Tk()

root.mainloop()
print('welcome to the terminal!')
# kun here, you can also do 
# name = input('what is your name?: ')
print('what is your name?')
name = input()

print(f'nice to see you, {name}.\nwe are going to learn how to use a terminal')
# here as well
# answer = input('are you ready?: ')
print('are you ready?')
answer = input()

if (answer == 'yes'):
    print('great!')
elif (answer == 'no'):
    print('well too bad! ')
else:
    print('what? it was a yes or no question.')

print('lets get started')

# open a terminal window for the user
terminal_win = subprocess.Popen(['x-terminal-emulator'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
