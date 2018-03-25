# Set OpenVPN / PiVPN

## Instalation steps

**1.** Install PiVPN 

»sudo apt-get update

»sudo apt-get upgrade

using  »»curl -L https://install.pivpn.io | bash [http://www.pivpn.io/]

or

FTP PiVPN v1.9 [here](https://github.com/pivpn/pivpn/releases/tag/v1.9) to /home/pi

»sudo sh /pivpn-1.9/auto_install/install.sh

**2.** Interface »wlan0 (for Raspberry Pi W)

**3.** Protocol »UDP

**4.** Port »1194

**5.** Encryption key »1024 (use space to select)

**6.** DNS »public DNS      »Google

**7.** Reboot »yes

**8.** »sudo apt-get upgrade

**9.** sudo pivpn add

**10.** Copy ovpn file to your computer using WinSCP.exe. Find in here /home/pi/ovpns/...ovpn

**11.** Forward your Raspberry Pi’s VPN port on your router.

Application   Device	    Log	CONE	Protocol	  Ports	                  Protocolo de trigger	Porta de transição	

OpenVPN	      raspberrypi	No	Yes	  IPv4	TCP	  1194 - 1194	1194 - 1194	---	                  ---		


OpenVPN	      raspberrypi	No	Yes	  IPv4	UDP	  1194 - 1194	1194 - 1194	---	                  ---		


Secure Shell  raspberrypi	No	Yes	  IPv4	TCP	  22 - 22	22 - 22	        ---	                  ---
Server (SSH)	



## Firewall (Fail2Ban)

»sudo apt install fail2ban
»sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

Edit jail.local
»sudo nano /etc/fail2ban/jail.local

[ssh]

enabled  = true

port     = ssh

filter   = sshd

logpath  = /var/log/auth.log

maxretry = 6

bantime  = 3600

[sshd]

port    = ssh

logpath = %(sshd_log)s

backend = %(sshd_backend)s

bantime  = 3600

maxretry = 6

»sudo service fail2ban restart

