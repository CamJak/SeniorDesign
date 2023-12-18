# This file will define the configuration files for the CSNA.

The **_files/etc/config_** directory will contain all of the configuration files for the CSNA.

It will contain the following files:

- **_network_** - This file will define the architecture and infrastructure of the CSNA.
- **_wireless_** - This file will define the wireless architecture of the CSNA.
- **_firewall_** - This file will define the firewall rules for the CSNA.

## Naming Convention

In order for the CSNA to work properly, the following naming convention must be followed:

- **_network_** - This file must be named **_network_**.
- **_wireless_** - This file must be named **_wireless_**.
- **_firewall_** - This file must be named **_firewall_**.

The config directory contains several different configurations for the CSNA. If you would like to use a certain network structure or define the network interfaces in a different way, make sure you rename the files accordingly.

For example, if you would like the Pi to use the ethernet port as the WAN port, you would need to rename the **_eth0_wan_** file to **_network_** and rename or delete the **_network_** file.

The different network configurations are defined below.

## Network Configurations

### 1. eth0_wan

This configuration will use the ethernet port as the WAN port and pull an IP address from your ISP or router.

```bash
config interface 'lan'
    option proto 'static'
    option ipaddr '192.168.1.1'
    option netmask '255.255.255.0'
 
config interface 'wan'
    option ifname 'eth0'
    option proto 'dhcp'
```

##### Section 1 - LAN

The first section defines the LAN interface. Here, we are defining the IP address and subnet mask for the local network. The IP address can be changed to whatever you would like along with the subnet mask.

##### Section 2 - WAN

The second section defines the WAN interface. Here, we are defining the ethernet port as the WAN port and pulling an IP address from the ISP or router.

### 2. eth0_lan

**Note:** This configuration is the default configuration for the CSNA.

This configuration will use the ethernet port as the LAN port and use the wireless interface as the WAN port.

```bash
config device
        option name 'br-lan'
        option type 'bridge'
        list ports 'eth0'

config interface 'lan'
        option device 'br-lan'
        option proto 'static'
        option ipaddr '192.168.1.1'
        option netmask '255.255.255.0'
        option ip6assign '60'
        option force_link '1'

config interface 'wwan'
        option proto 'dhcp'
        option peerdns '0'
        option dns '1.1.1.1 8.8.8.8'
```

##### Section 1 - Bridge

The first section defines a new device called **_br-lan_**. This device is a bridge between the ethernet port and the wireless interface. 

##### Section 2 - LAN

The second section defines the LAN interface. Here, we are defining the IP address and subnet mask for the local network. The IP address can be changed to whatever you would like along with the subnet mask.

##### Section 3 - WWAN

The third section defines the Wireless WAN interface. Here, we are defining the wireless interface as the WAN port and pulling an IP address from the ISP or router.

## Wireless Configurations

On startup, the CSNA will act as an access point with the SSID: **OpenWrt**. This is true for both the **_eth0_wan_** and **_eth0_lan_** network configurations.

Because of this, we do not need multiple wireless configurations. However, if you would like to change the default SSID that the CSNA broadcast on first boot, you can do so by modifying the **_wireless_** file. Any changes can also be made using the web interface.

The default wireless configuration is defined below:

```bash
config wifi-device 'radio0'
        option type 'mac80211'
        option channel '7'
        option hwmode '11g'
        option htmode 'HT20'
        option disabled '0'

config wifi-iface 'default_radio0'
        option device 'radio0'
        option network 'lan'
        option mode 'ap'
        option ssid 'OpenWrt'
        option encryption 'none'
```

##### Section 1 - Device (radio0)

The first section defines the wireless device. Here, radio0 is the default wifi interface on the Raspberry Pi. External wifi adapters will be named radio1, radio2, etc.

##### Section 2 - Interface (default_radio0)

The second section defines the wireless interface. Here, we are defining the wireless interface to act as an access point with the SSID: **OpenWrt**. The SSID can be changed to whatever you would like. Other configurations like the type of encryption can be changed using the web interface.

## Firewall Configurations

The firewall configurations are defined in the **_firewall_** file. The default firewall configurations will be used for now. If you would like to change the firewall rules, you can do so by modifying the **_firewall_** file. Any changes can also be made using the web interface.
