# Password Generator
# https://projects.raspberrypi.org/en/projects/password-generator

import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""
for i in range(10):
    password += random.choice(characters)
print("Password:", password)
