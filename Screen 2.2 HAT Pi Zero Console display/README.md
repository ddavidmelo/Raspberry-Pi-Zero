# Set up Console to Screen 2.2 HAT Pi Zero

## Setting up Pi Zero OTG - The quick way (No USB keyboard, mouse, HDMI monitor needed)
For this method, alongside your Pi Zero, MicroUSB cable and MicroSD card, only an additional computer is required, which can be running Windows (with [Bonjour](https://support.apple.com/kb/DL999), iTunes or Quicktime installed), Mac OS or Linux (with Avahi Daemon installed, for example Ubuntu has it built in).

**1.** Flash Raspbian Jessie full or Raspbian Jessie Lite [onto the SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md). Image that I used [2017-11-29-raspbian-stretch-lite](http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/), and [Etcher](https://etcher.io/) to burn this image.

**2.** Once Raspbian is flashed, open up the boot partition (in Windows Explorer, Finder etc) and add to the bottom of the ```config.txt``` file ```dtoverlay=dwc2``` on a new line, then save the file.    

## Reference
https://gist.github.com/975e2db164b3ca2b51ae11e45e8fd40a.git
