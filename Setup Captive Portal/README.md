# Setup Captive Portal

**1.** Firstly, to setup the AP (hotspot) you need to follow the first 5 steps in my other tutorial **Setup Bridge Wifi** ( link [here](https://github.com/ddavidmelo/Raspberry-Pi-Zero/tree/master/Setup%20Bridge%20Wifi) )

**2.** Second, install apache2 with the following command:

``` sudo apt-get install apache2  ```

**3.** After enable and load mod_rewrite:

``` sudo a2enmod rewrite  ```

**4.** Then open apache2.conf and replace “AllowOverride None” with “AllowOverride all”:

``` sudo nano /etc/apache2/apache2.conf ```

    <Directory /var/www/>
      Options Indexes FollowSymLinks
      AllowOverride All
      Require all granted
    </Directory>

**5.** Restart apache web server:

``` sudo service apache2 restart ```

**6.** Finally, create a secret file .htaccess and import the following lines of code

``` sudo nano /var/www/html/.htaccess ```

Code of .htaccess file

    RewriteEngine on
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule . index.html [L]

**7.** To enable the DHCP server to wlan0 [our APP], you will need to give it a range of IP addresses and DNS to hand out and

``` sudo nano /etc/dnsmasq.conf ```

    interface=wlan0      # Use the require wireless interface - usually wlan1
      dhcp-range=192.168.2.3,192.168.2.200,255.255.255.0,24h
      address=/#/192.168.2.1

**8.** Restart dnsmasq: 

    sudo service dnsmasq restart


## References
http://nitlab.inf.uth.gr/mazi-guides/captive.html


