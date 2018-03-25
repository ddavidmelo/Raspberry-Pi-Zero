# Set Server

## Pythnon libraries
**1.** »sudo apt-get install python-pip

**2.** »sudo pip install requests 

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

