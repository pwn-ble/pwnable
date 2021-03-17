## deployment walkthrough & resources

<!-- tutorial: [here](https://learnraspberrypi.com/2020/08/03/build-buildroot-image-for-raspberry-pi-using-docker/) -->

1. build docker image from debian or rasp - something *lite*

<!-- - look at vagrant
    - buildroots tutorial uses it -->

<!-- 2. add `curl -O https://buildroot.org/downloads/Vagrantfile; vagrant up` to dockerfile
 - we want  -->

 <!-- [buildroot manual](https://buildroot.org/downloads/manual/manual.html) -->

2. while in this directory, run `docker build -tag pwnable:0.1`


3. once the image is built, run it with `docker run -it pwnable:01`
- `-i` runs it in interactive mode, so you can directly access the shell

4. inside the container, navigate to `/buildroot`
5. to configure buildroot to configure building for raspberry pi 4 (ARM), run `make raspberry4_defconfig`
- can optionally run `make menuconfig` to access an interactive configuration program to edit this if we need to
6. tell buildroot to compile and generate our `.img` file
- it should output to `/buildroot/output/images/sdcard.img`

** note: to alter makefile config, check out the [Makefile intro](https://www.gnu.org/software/make/manual/html_node/Introduction.html) **

7. exit out of the container instance with `CTRL/CMD-d`
8. copy the `.img` file from the docker container into our local working directory with `docker cp {container-id}:/buildroot/output/images/sdcard.img .`
9. we can now load this into [Raspberry Pi Imager](https://www.raspberrypi.org/software/) and write our image to an SD card
10. insert the SD card into the Pi, and start it up :)
