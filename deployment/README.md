# deployment walkthrough & resources

 We want our box to run smoothly, so it should only have what we need for our softwaret to work.
 To do that, we can build a docker image from a lightweight linux distro.
 - TODO: refine the dockerfile
 - TODO: build our local code into the docker container via dockerfile
    

 <!-- [buildroot manual](https://buildroot.org/downloads/manual/manual.html) -->

## Walkthrough to run the current toolchain:
tutorial: [here](https://learnraspberrypi.com/2020/08/03/build-buildroot-image-for-raspberry-pi-using-docker/)

note: to alter makefile config, check out the [Makefile intro](https://www.gnu.org/software/make/manual/html_node/Introduction.html)
1. while in this directory in your favorite IDE, run `docker build --tag pwnable:0.1 .`
2. once the image is built, run it with `docker run -it pwnable:0.1`
    - `-i` runs it in interactive mode, so you can directly access the shell
3. inside the container, navigate to `/buildroot`
4. to configure buildroot to configure building for raspberry pi 4 (ARM), run `make raspberrypi4_defconfig`
    - can optionally run `make menuconfig` to access an interactive configuration program to edit this if we need to
5. tell buildroot to compile and generate our `.img` file
    - it should output to `/buildroot/output/images/sdcard.img`
6. exit out of the container instance with `CTRL/CMD-d`
7. copy the `.img` file from the docker container into our local working directory with `docker cp {container-id}:/buildroot/output/images/sdcard.img .`
8. we can now load this into [Raspberry Pi Imager](https://www.raspberrypi.org/software/) and write our image to an SD card
9. insert the SD card into the Pi, and start it up :)
