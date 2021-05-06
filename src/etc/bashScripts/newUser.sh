#!/bin/bash

echo "Creating new user"

useradd -m -p (mkpasswd bonjour) -s /bin/bash pwnable

sleep .25

usermod -aG sudo pwnable

