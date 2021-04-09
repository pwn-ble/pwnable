import os
import platform
import subprocess

# lauch pwnable home screen script
if (platform.system() == 'Windows'):
    subprocess.call(['python.exe', '.\\gui\\menu.py']);
else:
    subprocess.call(['python3', './gui/menu.py'])

# should contain some generic loader functions ??
