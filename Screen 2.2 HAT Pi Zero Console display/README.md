# Setup Console to Screen 2.2 HAT Pi Zero

**1.** First is necessary to install PIP package manager for Python:

``` sudo apt-get install python-pip ```

**2.** After that, add the install pre-compile module:

    cd /usr/lib/python2.7/
    wget "https://github.com/ddavidmelo/Raspberry-Pi-Zero/blob/master/Screen%202.2%20HAT%20Pi%20Zero%20Console%20display/evdev.tar.gz?raw=true" -O evdev.tar.gz --no-check-certificate
    tar -zxvf evdev.tar.gz
    rm evdev.tar.gz

**3.** The last step, run the next script:

    cd ~
    wget "https://raw.githubusercontent.com/ddavidmelo/Raspberry-Pi-Zero/master/Screen%202.2%20HAT%20Pi%20Zero%20Console%20display/adafruit-pitft.sh"
    chmod +x adafruit-pitft.sh
    sudo ./adafruit-pitft.sh

## Reference
Instalation manual:

https://learn.adafruit.com/adafruit-2-2-pitft-hat-320-240-primary-display-for-raspberry-pi/easy-install

Original adafruit-pitft.sh script:

https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/adafruit-pitft.sh

Screen manual:

https://cdn-learn.adafruit.com/downloads/pdf/adafruit-2-2-pitft-hat-320-240-primary-display-for-raspberry-pi.pdf

Physical connections:

https://learn.adafruit.com/pigrrl-zero/overview

-------------------------------------------------------

image 
sudo fbi -T 2 -d /dev/fb1 -noverbose -a adapiluv320x240.jpg

-------------------------------------------------------

send commands

who (get the user)
echo oi >& /dev/tty1

-------------------------------------------------------

