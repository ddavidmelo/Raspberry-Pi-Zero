#!/usr/bin/python

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import commands
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BsON = '\033[34;47m ON \033[0m'
BsOFF = '\033[0m OFF \033[0m'
APflag = False
APstate = BsON
CPflag = False
CPstate = BsOFF
Bridgeflag = False
Bridgestate = BsOFF
StartWifi = True
StartCP = True
WifiSSID = 'iPhone Raul'

WifiCP= {
      'ssid=': 'ssid=FREE WIFI',
      'wpa=': 'wpa=0'
      }
WifiDefault= {
      'ssid=': 'ssid=PERSONAL WIFI',
      'wpa=': 'wpa=2'
      }

time.sleep(30)

os.system('printf "\n\n Starting ...\n\n" > /dev/tty1')

#Function to change variables in hostapd.conf
def hostapdConf(reps):
    f = open('/etc/hostapd/hostapd.conf','r').read()
    lines = f.split("\n")
    newConf = ""
    for line in lines:
        REPLACED = False
        for key in reps.keys():
            if key in line:
                l = "%s\n"%reps[key]
                REPLACED = True

        if REPLACED == True:
            newConf += l
        else:
            newConf += "%s\n"%line

    new_conf_file = open('/etc/hostapd/hostapd.conf','w')
    new_conf_file.write(newConf)
    new_conf_file.close()

while 1 == 1:
    B_up = GPIO.input(6)
    B_down = GPIO.input(5)
    B_left = GPIO.input(18)
    B_right = GPIO.input(24)
    B_L = GPIO.input(20)
    B_R = GPIO.input(21)
    B_1 = GPIO.input(16)
    B_2 = GPIO.input(12)
    B_3 = GPIO.input(13)
    B_4 = GPIO.input(19)
    
    if B_up == False:
        intf = 'wlan0'
        ipW0 = commands.getoutput("ip address show dev " + intf).split()
        if ipW0[0] == "Device":
           ipW0 = "not connected"
        else:
           ipW0 = ipW0[ipW0.index('inet') + 1].split('/')[0]
 
        intf = 'wlan1'
        ipW1 = commands.getoutput("ip address show dev " + intf).split()
        if ipW1[0] == "Device":
           ipW1 = "not connected"
        else:
           ipW1 = ipW1[ipW1.index('inet') + 1].split('/')[0]

	str="IP interface wlan0="+ipW0+" wlan1="+ipW1
        os.system('printf \"\n'+str+'\n\n\" > /dev/tty1')
        time.sleep(0.2)

    if B_down == False:
        str = commands.getoutput("sudo arp -a | sed -r 's/[()<>]+/ /g' | awk -F '[' '{print $1}' | tr '\n' '@'")
        Nusers = str.count("at")
        os.system("echo "+str+" | tr '@' '\n' > /dev/tty1")
        time.sleep(0.2)
 
    if B_left == False:
        if APflag == False:
            os.system('printf "\nTurn >> OFF << AP \n "  > /dev/tty1')
            #os.system('sudo systemctl stop hostapd')
            APstate = BsOFF
            APflag = True
        else:
            os.system('printf "\nTurn >> ON << AP \n "  > /dev/tty1')
            #os.system('sudo systemctl start hostapd')
            APstate = BsON
            APflag = False
        time.sleep(0.2)
    
    if (B_right == False or StartCP):
        if (CPflag == False or StartCP):
            os.system('printf "\nTurn >> OFF << CP \n "  > /dev/tty1')
            os.system('sudo echo -e "interface=wlan0 \n dhcp-range=192.168.2.3,192.168.2.200,255.255.255.0,24h \n no-resolv \n no-poll \n server=8.8.8.8 \n server=8.8.4.4 " >> /etc/dnsmasq.conf ')
            os.system('sudo service dnsmasq restart')
            time.sleep(0.2)
            CPstate = BsOFF
            CPflag = True
            StartCP = False
        else:
            os.system('printf "\nTurn >> ON << CP \n "  > /dev/tty1')
            os.system('sudo echo -e "interface=wlan0 \n dhcp-range=192.168.2.3,192.168.2.200,255.255.255.0,24h \n address=/#/192.168.2.1 " >> /etc/dnsmasq.conf')
            os.system('sudo service dnsmasq restart')
            time.sleep(0.2)
            CPstate = BsON
            CPflag = False
    
    if B_L == False:
        os.system('printf "\n" > /dev/tty1')
        os.system('printf "\033[34;47m                   \033[0m r - Access Portal  '+APstate+'\n" > /dev/tty1')
	os.system('printf "\033[34;47m   u          1    \033[0m l - Captive Portal '+CPstate+'\n" > /dev/tty1')
	os.system('printf "\033[34;47m l   r      4   2  \033[0m u - Interfaces IP\n" > /dev/tty1')
	os.system('printf "\033[34;47m   d          3    \033[0m d - Clients connected to wlan0\n" > /dev/tty1')
	os.system('printf "\033[34;47m     -L-  -R-      \033[0m L - Menu\n" > /dev/tty1')
	os.system('printf "\033[34;47m                   \033[0m R - Set bridge wlan0-wlan1 '+Bridgestate+'\n" > /dev/tty1')
        os.system('printf "\033[0m 1 - Wifi Default   \033[30;43m'+WifiSSID+'\033[0m \n" > /dev/tty1')
        os.system('printf "\033[0m 2 - Wifi CP        \n\n" > /dev/tty1')
        time.sleep(0.2)
        
    if B_R == False:
        if Bridgeflag == False:
            os.system('printf "\n Bridge OFF \n "  > /dev/tty1')
            os.system('sudo iptables -F')
            os.system('sudo iptables -X')
            Bridgeflag = True
            Bridgestate = BsOFF

        else:
	    os.system('printf "\n Bridge ON \n "  > /dev/tty1')
            os.system('sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE')
            os.system('sudo iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT')
            os.system('sudo iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT')
            Bridgeflag = False
            Bridgestate = BsON
        time.sleep(0.2)

    if (B_1 == False or StartWifi):
        os.system('printf "\nWifi: Default \n "  > /dev/tty1')
        WifiSSID = 'iPhone Raul'
        os.system('sudo service hostapd stop')
        hostapdConf(WifiDefault)
        os.system('sudo service hostapd start')
        StartWifi = False
        time.sleep(0.2)
    
    if B_2 == False:
        os.system('printf "\nWifi: Free Wifi CP \n "  > /dev/tty1')
        WifiSSID = 'CP Free Wifi'
        os.system('sudo service hostapd stop')       
        hostapdConf(WifiCP)
        os.system('sudo service hostapd start')
        time.sleep(0.2)

    if B_3 == False:
        os.system('printf "\n B3 \n "  > /dev/tty1')
        time.sleep(0.2)

    if B_4 == False:
        os.system('printf "\n B4 \n "  > /dev/tty1')
        time.sleep(0.2)
    pass 

