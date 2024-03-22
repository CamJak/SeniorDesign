#!/usr/bin/env bash

done_message() {
    echo "Done!"
    echo ""
}

# update and upgrade
echo "Updating and Upgrading packages..."
sudo apt update && sudo apt upgrade -y
done_message

# Install necessary packages
echo "Installing necessary packages..."
sudo apt install iptables dnsmasq hostapd -y
done_message

# Make directories for config files
echo "Creating directories..."
mkdir /etc/csna /var/log/csna
done_message

# Copy files to their correct directories
echo "Copying and moving files..."
current_dir=$(pwd)
cd ../Files/etc
cp "dnsmasq.conf" "/etc/dnsmasq.conf"
cp "iptables.ipv4.nat" "/etc/iptables.ipv4.nat"
cp "sysctl.conf" "/etc/sysctl.conf"
cp "default/hostapd" "/etc/default/hostapd"
cp "dnsmasq.d/csna-dhcp.conf" "/etc/dnsmasq.d/csna-dhcp.conf"
cp "dnsmasq.d/csna-dns.conf" "/etc/dnsmasq.d/csna-dns.conf"
cp "hostapd/hostapd.conf" "/etc/hostapd/hostapd.conf"
cp "network/interfaces" "/etc/network/interfaces"
cp "ssh/csna_banner" "/etc/ssh/csna_banner"
cp "ssh/sshd_config" "/etc/ssh/sshd_config"
cd $current_dir
done_message

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