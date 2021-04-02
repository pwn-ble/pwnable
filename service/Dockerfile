FROM debian:jessie

RUN apt-get update && apt-get install -y -q \
    python \
    python3

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /etc/systemd/system/
COPY pwnable.service .

WORKDIR /home/
COPY test_service.py .

CMD [ "/sbin/init" ]