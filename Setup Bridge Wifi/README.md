# Setup Bridge connection between two Wifi interfaces

**1.** Firstly, install hostapd and dnsmasq with the following commands:

``` sudo apt-get install dnsmasq hostapd  ```

**2.** After the installation is finished is necessary edit the network interfaces file like that:

``` sudo nano /etc/network/interfaces  ```

    auto lo
    iface lo inet loopback

    # WiFi wlan 1 external dondle
    allow-hotplug wlan1
    iface wlan1 inet manual
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

    # WiFi wlan 0 internal wifi module since I'm using Raspberry pi Zero W
    auto wlan0
    allow-hotplug wlan0
    iface wlan1 inet manual
    wireless-power off

**3.** Now Edit the hostapd.conf file to creat the AP:

``` sudo nano /etc/hostapd/hostapd.conf ```

    # Networking interface
    interface=wlan0

    # WiFi configuration
    ssid=Router_SSID
    channel=7
    hw_mode=g
    country_code=US
    wmm_enabled=0
    macaddr_acl=0
    ignore_broadcast_ssid=0

    # WiFi security
    auth_algs=1
    wpa=2
    wpa_key_mgmt=WPA-PSK
    rsn_pairwise=CCMP
    wpa_pairwise=TKIP
    wpa_passphrase=WifiPassword

**4.** To enable hostapd to run upon boot you have to edit one last file.

``` sudo nano /etc/default/hostapd ```

    RUN_DAEMON=yes
    DAEMON_CONF="/etc/hostapd/hostapd.conf"

**5.** Configure static IP to wlan0 [our APP]

``` sudo nano /etc/dhcpcd.conf ```

    interface wlan0
        static ip_address=192.168.2.1/24
        nohook wpa_supplicant

**6.** To enable the DHCP server to wlan0 [our APP], you will need to give it a range of IP addresses and DNS to hand out

``` sudo nano /etc/dnsmasq.conf ```

    interface=wlan0      # Use the require wireless interface
      dhcp-range=192.168.2.3,192.168.2.200,255.255.255.0,24h
      no-resolv
      no-poll
      server=8.8.8.8
      server=8.8.4.4

**7.** Creat bridge connection
Enable ipv4 ip forwarding

``` sudo nano /etc/sysctl.conf ```

Uncoment the next line

``` net.ipv4.ip_forward=1 ```

Run the next commands

    sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
    sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
    sudo iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
    sudo iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT

**8.** Restart hostapd and dnsmasq: 

    sudo service hostapd restart
    sudo service dnsmasq restart

**9.** Test the hostapd config use this command:

    sudo hostapd /etc/hostapd/hostapd.conf


## References
https://github.com/Phoenix1747/RouteryPi


