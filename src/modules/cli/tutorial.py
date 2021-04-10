import subprocess
import tkinter as tk

def open_terminal_win():
    popen = subprocess.Popen(["xterm"], stdinstdout=subprocess.PIPE, shell=True)

subprocess.call(['sh', 'tutorial.sh'])
