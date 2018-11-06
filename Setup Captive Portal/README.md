# Setup Captive Portal

**1.** Firstly, install apache2 with the following command:

``` sudo apt-get install apache2  ```

**2.** After enable and load mod_rewrite:

``` sudo a2enmod rewrite  ```

**3.** Then open apache2.conf and replace “AllowOverride None” with “AllowOverride all”:

``` sudo nano /etc/apache2/apache2.conf ```

    <Directory /var/www/>
      Options Indexes FollowSymLinks
      AllowOverride All
      Require all granted
    </Directory>

**4.** Restart apache web server:

``` sudo service apache2 restart ```

**5.** Finally, create a secret file .htaccess and import the following lines of code

``` sudo nano /var/www/html/.htaccess ```

Code of .htaccess file

    RewriteEngine on
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule . index.html [L]

**6.** To enable the DHCP server to wlan0 [our APP], you will need to give it a range of IP addresses and DNS to hand out and

``` sudo nano /etc/dnsmasq.conf ```

    interface=wlan0      # Use the require wireless interface
      dhcp-range=192.168.2.3,192.168.2.200,255.255.255.0,24h
      no-resolv
      no-poll
      server=8.8.8.8
      server=8.8.4.4

**8.** Restart dnsmasq: 

    sudo service dnsmasq restart


## References
http://nitlab.inf.uth.gr/mazi-guides/captive.html


