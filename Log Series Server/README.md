# Set Server

## Pythnon libraries
**1.** »sudo apt-get install python-pip

**2.** »sudo pip install requests 

## Firewall (Fail2Ban)

»sudo apt install fail2ban
»sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

Edit jail.local
»sudo nano /etc/fail2ban/jail.local

[ssh]\n
enabled  = true\n
port     = ssh\n
filter   = sshd\n
logpath  = /var/log/auth.log\n
maxretry = 6\n
bantime  = 3600

[sshd]\n
port    = ssh\n
logpath = %(sshd_log)s\n
backend = %(sshd_backend)s\n
bantime  = 3600\n
maxretry = 6\n

»sudo service fail2ban restart

