# This document will outline the features we will look to implement in the GUI for the CSNA.

## Features

The following is a list of features that we will look to implement in the GUI for the CSNA:

- **System Information**: This feature will display the system information such as the hostname, IP address, MAC address, the status of the network interfaces, and the version of the operating system.

- **WAN Setup**: This feature will allow the user to configure the WAN interface.
    - **Dynamic IP**: This option will allow the user to configure the WAN interface to obtain an IP address automatically from the ISP.

    - **Static IP**: This option will allow the user to configure the WAN interface with a static IP address, subnet mask, default gateway, and DNS servers.

- **LAN Setup**: This feature will allow the user to configure the LAN interface.
    - **IP Address**: This option will allow the user to configure the IP address, subnet mask, and DHCP server settings for the LAN interface.

    - **DHCP Server**: This option will allow the user to enable or disable the DHCP server for the LAN interface.
        - **DHCP Range**: This option will allow the user to configure the range of IP addresses to allocate to clients.

        - **DHCP Lease Time**: This option will allow the user to configure the lease time for the IP addresses allocated to clients.

        - **Domain Name (optional)**: This option will allow the user to configure the domain name to use for DNS queries.

    - **DNS Server**: This option will allow the user to configure the DNS server settings for the LAN interface.
        - **Primary DNS**: This option will allow the user to configure the IP address of the primary DNS server.

        - **Secondary DNS (optional)**: This option will allow the user to configure the IP address of the secondary DNS server.

- **Wireless Configuration**: This feature will allow the user to configure the wireless interface.
    - **Toggle Wireless**: This option will allow the user to enable or disable the wireless interface.
        - If not enabled, the web interface should allow the interface to act as a WAN interface.

    - **SSID**: This option will allow the user to configure the SSID for the wireless network.

    - **Broadcast SSID**: This option will allow the user to enable or disable the broadcasting of the SSID.

    - **Power Level**: This option will allow the user to configure the power level for the wireless interface.

    - **Channel**: This option will allow the user to configure the channel for the wireless interface. Channels 1, 6, and 11 are the recommended channels for 2.4 GHz networks. Channels 36, 40, 44, and 48 are the recommended channels for 5 GHz networks.

    - **AP Isolation**: This option will allow the user to enable or disable the AP isolation feature. When enabled, this feature prevents wireless clients from communicating with each other.

    - **Security**: This option will allow the user to configure the security settings for the wireless network.
        - **Security Mode**: This option will allow the user to configure the security mode for the wireless network. The available security modes are WEP, WPA, and WPA2.

        - **Passphrase**: This option will allow the user to configure the passphrase for the wireless network.

- **Firewall Configuration**: This feature will allow the user to configure the firewall settings.

    - **Port Forwarding**: This feature will allow the user to configure port forwarding rules.

    - **DMZ Configuration**: This feature will allow the user to configure the DMZ settings.

    - **VPN Configuration**: This feature will allow the user to configure the VPN settings.

- **System Configuration**: This feature will allow the user to configure the system settings.

    - **Summary**: This option will display a summary of all configured settings.

    - **Reboot**: This option will allow the user to reboot the system.

    - **Time and Date**: This option will allow the user to configure the time and date settings.

    - **Logs**: This option will allow the user to view the system logs.

    - **Tools**: This option will allow the user to access various system tools such as ping, traceroute, and nslookup.