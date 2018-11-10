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

Notes: 

    interface > sets the wifi interface to use
    ssid > sets the ssid of the virtual wifi access point
    hw_mode> > sets the mode of wifi, depends upon the devices you will be using. It can be a,b,g,n. Not all cards support 'n'.
    channel > sets the channel for your wifi
    macaddr_acl > macaddr_acl sets options for mac address filtering. 0 means "accept unless in deny list"
    ignore_broadcast_ssid > setting ignore_broadcast_ssid to 1 will disable the  broadcasting of ssid
    auth_algs >
    #Sets authentication algorithm
    #1 - only open system authentication
    #2 - both open system authentication and shared key authentication
    wpa >
    #####Sets WPA and WPA2 authentication (remove this section if you don't need encryption)#####
    #wpa option sets which wpa implementation to use
    #1 - wpa only
    #2 - wpa2 only
    #3 - both
    wpa_passphrase > sets wpa passphrase required by the clients to authenticate themselves on the network
    wpa_key_mgmt > sets wpa key management
    wpa_pairwise > sets encryption used by WPA
    rsn_pairwise > sets encryption used by WPA2

**4.** To enable hostapd to run upon boot you have to edit one last file.

``` sudo nano /etc/default/hostapd ```

    RUN_DAEMON=yes
    DAEMON_CONF="/etc/hostapd/hostapd.conf"

**5.** Configure static IP to wlan0 [our AP]

``` sudo nano /etc/dhcpcd.conf ```

    interface wlan0
        static ip_address=192.168.2.1/24
        nohook wpa_supplicant

**6.** To enable the DHCP server to wlan0 [our AP], you will need to give it a range of IP addresses and DNS to hand out

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


