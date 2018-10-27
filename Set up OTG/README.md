# Set up OTG

## Setting up Pi Zero OTG - The quick way (No USB keyboard, mouse, HDMI monitor needed)
For this method, alongside your Pi Zero, MicroUSB cable and MicroSD card, only an additional computer is required, which can be running Windows (with [Bonjour](https://support.apple.com/kb/DL999), iTunes or Quicktime installed), Mac OS or Linux (with Avahi Daemon installed, for example Ubuntu has it built in).

**1.** Flash Raspbian Jessie full or Raspbian Jessie Lite [onto the SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md). Image that I used [2017-11-29-raspbian-stretch-lite](http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/), and [Etcher](https://etcher.io/) to burn this image.

**2.** Once Raspbian is flashed, open up the boot partition (in Windows Explorer, Finder etc) and add to the bottom of the ```config.txt``` file ```dtoverlay=dwc2``` on a new line, then save the file.    

**3.** If using a recent release of Jessie (Dec 2016 onwards), then create a new file simply called ```ssh``` in the SD card as well. By default SSH is now disabled so this is required to enable it. **Remember** - Make sure your file doesn't have an extension (like .txt etc)!    

**4.** Finally, open up the ```cmdline.txt```. Be careful with this file, it is very picky with its formatting! Each parameter is seperated by a single space (it does not use newlines). Insert ```modules-load=dwc2,g_ether``` after ```rootwait```. To compare, an edited version of the ```cmdline.txt``` file at the time of writing, can be found [here](http://pastebin.com/WygSaptQ).
       or, creat this file ```wpa_supplicant.conf``` with the next content:
       ```
       country=AU
       ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
       update_config=1
       network={
              ssid="WiFiNetwork"
              psk="Password"
              key_mgmt=WPA-PSK
       }```
       

**5.** That's it, eject the SD card from your computer, put it in your Raspberry Pi Zero and connect it via USB to your computer. It will take up to 90s to boot up (shorter on subsequent boots). It should then appear as a USB Ethernet device. You can SSH into it using ```raspberrypi.local``` as the address. For this you can use [Putty](https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe).    

**6.** In Putty after log in, use this comands to start VNC server:    
        * ```sudo raspi-config``` , and enable VNC in Interfacing Options    
        * ```sudo vncserver```    
        * ```sudo systemctl enable vncserver-x11-serviced.service```, to have VNC Server start automatically when you power the Pi on.   

## Reference
https://gist.github.com/975e2db164b3ca2b51ae11e45e8fd40a.git
