# Pi WebPage

## Install Apache
**1.** »sudo apt-get install apache2

## Give permissions to files that you want to read in php
**1.** »sudo chmod 777 file.private

## Block files from being viewed by Web clients
**1.** »cd /etc/apache2

**2.** »sudo nano apache2.conf

**3.** On this AccessFileName .htaccess, add this :

      <FilesMatch "\.private">

      Require all denied

      < / FilesMatch>

**4.** Add this :

      <Directory / >

      Options FollowSymLinks

      AllowOverride None

      Require all denied

      < / Directory>

      <Directory /usr/share>

      AllowOverride None

      Require all granted

      < / Directory>

      <Directory /var/www/>

      Options Indexes FollowSymLinks

      AllowOverride None

      Require all granted

      IndexIgnore *.private

      < / Directory>

## Enable HTTPS
**1.** »sudo apt-get install apache2 openssl

**2.** »sudo mkdir -p /etc/ssl/localcerts

**3.** »sudo mkdir -p /etc/ssl/localcerts

**4.** »sudo openssl req -new -x509 -days 365 -nodes -out /etc/ssl/localcerts/apache.pem -keyout /etc/ssl/localcerts/apache.key

**5.** »sudo chmod 600 /etc/ssl/localcerts/apache*

**6.** »sudo a2ensite ssl     if returns error  »sudo a2ensite default-ssl

**7.**

      »cd /etc/apache2/sites-available

      »ls -la

      »sudo nano default-ssl.conf

      SSLCertificateFile /etc/ssl/localcerts/apache.pem

      SSLCertificateKeyFile /etc/ssl/localcerts/apache.key

**8.** »sudo a2ensite efault-ssl.conf

**9.** »sudo service apache2 restart
