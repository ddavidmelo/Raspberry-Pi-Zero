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
