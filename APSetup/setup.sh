#!/usr/bin/env bash

done_message() {
    echo "Done!"
    echo ""
}

phoebus_dir="/etc/phoebus"
phoebus_log_dir="/var/log/phoebus"
dnsmasq_dir="/etc/dnsmasq.d"
hostapd_dir="/etc/hostapd"

# update and upgrade
echo "Updating and Upgrading packages..."
sudo apt update && sudo apt upgrade -y
done_message

# Install necessary packages
echo "Installing necessary packages..."
sudo apt install iptables dnsmasq hostapd -y
done_message

# Make directories for config files
if [ -d "$phoebus_dir" ]; then
    echo "Directory $phoebus_dir already exists."
else
    echo "Creating directories..."
    mkdir /etc/phoebus /var/log/phoebus
    done_message
fi

# Copy files to their correct directories
if [ -d "$dnsmasq_dir" ] && [ -d "$hostapd_dir" ]; then
    echo "Copying and moving files..."
    current_dir=$(pwd)
    cd Files/etc
    cp "dnsmasq.conf" "/etc/dnsmasq.conf"
    cp "iptables.ipv4.nat" "/etc/iptables.ipv4.nat"
    cp "sysctl.conf" "/etc/sysctl.conf"
    cp "default/hostapd" "/etc/default/hostapd"
    cp "dnsmasq.d/phoebus-dhcp.conf" "/etc/dnsmasq.d/phoebus-dhcp.conf"
    cp "dnsmasq.d/phoebus-dns.conf" "/etc/dnsmasq.d/phoebus-dns.conf"
    cp "hostapd/hostapd.conf" "/etc/hostapd/hostapd.conf"
    cp "network/interfaces" "/etc/network/interfaces"
    cp "ssh/phoebus_banner" "/etc/ssh/phoebus_banner"
    cp "ssh/sshd_config" "/etc/ssh/sshd_config"
    cd $current_dir
    done_message
else
    echo "Required directories do not exist! Exiting..."
    exit 1
fi

# Restore firewall rules
echo "Restoring firewall rules..."
sudo iptables-restore /etc/iptables.ipv4.nat
done_message

# Unmask hostapd service
echo "Unmasking and starting hostapd..."
sudo systemctl unmask hostapd
done_message

# Reboot the Pi
echo "Rebooting..."
sudo reboot