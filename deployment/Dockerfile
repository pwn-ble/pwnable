# decide what OS to run
FROM debian:jessie

# all of the linux modules to include
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

# set locale encoding
RUN sed -i "s/^# en_US.UTF-8/en_US.UTF-8/" /etc/locale.gen && locale-gen && update-locale LANG=en_US.UTF-8

# could have this gotten from a python or node script -- need internet conn for that
ENV BR_VERSION 2020.02.4

# download buildroot cross-compiler
RUN wget -qO- http://buildroot.org/downloads/buildroot-$BR_VERSION.tar.gz \
 | tar xz && mv buildroot-$BR_VERSION /buildroot

# create pwnable user and group for service daemon
RUN useradd -m -p $(mkpasswd bonjour) -s /bin/bash pwnable

# add new user pwnable to sudoers group 
RUN usermod -aG sudo pwnable
