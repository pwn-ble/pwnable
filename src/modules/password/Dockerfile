# decide what OS to run
FROM debian:latest

# all of the linux modules to include
RUN apt-get update && apt-get install -y -q \
    bash \
    debianutils \
    gcc \
    john \
    python \
    python3 \
    sudo \
    vim \
    whois

# clean apt cache
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# create pwnable user and group for service daemon
RUN useradd -m -p $(mkpasswd bonjour) -s /bin/bash pwnable
# add new user pwnable to sudoers group 
RUN usermod -aG sudo pwnable

# add password generator module scripts
WORKDIR /home/pwnable/

# can add .vimrc -> 'set number' to get numbered lines in vim

# copy in password cracking module
RUN mkdir password
COPY ./ password/
# COPY src/password/hasher/ ./password/hasher/
RUN chown -R pwnable:pwnable ./

# add wordlists for password cracking
WORKDIR /usr/share/
RUN mkdir wordlists/

# open up into pwnable password hashing directory
WORKDIR /home/pwnable/password/hasher/
# compile to a.out executable
RUN gcc unshadow.c -lcrypt
# change binary ownership to pwnable user/group 
RUN chown pwnable a.out && chgrp pwnable a.out
