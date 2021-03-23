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

# create pwnable user and group for service daemon
# RUN useradd -m -p <encryptedPassword> -s /bin/bash <username>
# can use whois->mkpasswd to gen encrypted pass
# can also use "python3 -c 'import crypt; print(crypt.crypt("password"))"" ? might be best way for us

# move into root's home dir
WORKDIR /root
# copy the C script into workdir
COPY hello.c .
# compile the C file within the image
RUN gcc ./hello.c
