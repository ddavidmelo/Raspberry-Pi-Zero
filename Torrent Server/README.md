# Torrent Server

## Setting up Pi Torrent Server
### Required programs 
  * Transmission ```sudo apt-get install transmission```    
  * Python ```sudo apt-get install python```    
  * Python ```sudo apt-get install python```, ```and sudo apt-get install python-pip```    
  * Flexget ```sudo pip install flexget```    
  * Gnome-schedule GUI ```sudo install gnome-schedule```    

### Transmission Settings
**1.** Create one directory like this ```/home/pi/complete``` and like this ```/home/pi/incomplete```    
**2.** Run this two comands ```sudo chmod 770 /home/pi/complete``` ```sudo chmod 770 /home/pi/incomplete```    
**3.** Set up this two folders in the tab 'Downloading'      
![ ](https://github.com/ddavidmelo/Raspberry-Pi-Zero/blob/master/Torrent%20Server/transdef.png)      

### Flexget Settings
**1.** Check the version to see if it is installed ```flexget -V```    
**2.** Create one directory like this ```/home/pi/.flexget/config.yml``` and like this ```/home/pi/incomplete```    
**3.** Do your profile in  [Showrss](http://http://showrss.info) and edit the link in the next step with yours (check your profile link in )  [ProfileLink](http://showrss.info/feeds)    
**4.** Set up ```config.yml``` like the one in this project [here](https://github.com/ddavidmelo/Raspberry-Pi-Zero/blob/master/Torrent%20Server/config.yml)     
**5.** Test Flexget ```flexget --test```    
**6.** Run Flexget ```flexget execute```    
**7.** To do this automatically check the next topic    


### Gnome-schedule GUI Setting
