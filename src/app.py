import os
import platform
import sys # ??
import subprocess

global ROOT_DIR
ROOT_DIR = os.getcwd()

# lauch pwnable home screen script
subprocess.call(['python.exe', '.\\gui\\ui.py']);

# should contain some generic loader functions ??