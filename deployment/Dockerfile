FROM debian:jessie

RUN apt-get update && apt-get install -y -q \
    bash \
    bc \
    binutils \
    build-essential \
    bzip2 \
    ca-certificates \
    cpio \
    debianutils \
    file \
    g++ \
    gcc \
    git \
    graphviz \
    gzip \
    libncurses5-dev \
    locales \
    make \
    patch \
    perl \
    python \
    python3 \
    python-matplotlib \
    rsync \
    sed \
    sudo \
    tar \
    unzip \
    vim \
    wget \
    whois \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i "s/^# en_US.UTF-8/en_US.UTF-8/" /etc/locale.gen && locale-gen && update-locale LANG=en_US.UTF-8

ENV BR_VERSION 2020.02.4

RUN wget -qO- http://buildroot.org/downloads/buildroot-$BR_VERSION.tar.gz \
 | tar xz && mv buildroot-$BR_VERSION /buildroot
# from https://github.com/learnraspberry/buildroot-docker/blob/master/Dockerfile, thanks

# WORKDIR /root
# COPY ./pass_gen.py .

# create pwnable user and group for service daemon
RUN useradd -m -p $(mkpasswd bonjour) -s /bin/bash pwnable
# add new user pwnable to sudoers group 
RUN usermod -aG sudo pwnable

# WORKDIR /pwnable

# move into root's home dir
# WORKDIR /root
# copy the C script into workdir
# COPY hello.c .
# compile the C file within the image
# RUN gcc ./hello.c
