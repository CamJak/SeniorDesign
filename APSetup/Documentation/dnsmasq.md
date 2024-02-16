# DNSMASQ Configuration Options

## Introduction

This document describes the configuration options for the DNSMASQ service. The DNSMASQ service is a lightweight DNS forwarder and DHCP server. It is used to provide DNS and, optionally, DHCP services to a small network. The DNSMASQ service is used in the Access Point (AP) setup to provide DNS and DHCP services to the clients connected to the AP.

## Configuration Options

The DNSMASQ service is configured using the `/etc/dnsmasq.conf` file. The configuration file contains a list of options that control the behavior of the DNSMASQ service. The following is a list of the most commonly used options:


### Basic Options

- `domain-needed`: This option specifies whether to ignore DNS queries for domains that are not in the local domain.

- `bogus-priv`: This option specifies whether to ignore DNS queries for private IP addresses.

- `local-service`: This options tells DNSMASQ to only answer queries from hosts that are on the same subnet.

- `localise-queries`: This option will return the local IP address for queries to the local domain.

- `expand-hosts`: This option will expand the domain name in the `/etc/hosts` file to the local domain.

- `domain-needed`: This option tells dnsmasq to never forward A or AAAA queries for plain names, without dots or domain parts, to upstream nameservers.

- `log-async`: This option specifies whether to log asynchronously.

- `cache-size`: This option specifies the size of the DNS cache.

- `log-queries`: This option specifies whether to log DNS queries.

- `log-facility`: This option specifies the facility to use for logging.

- `no-resolv`: This option specifies whether to ignore the `/etc/resolv.conf` file.

### DNS Options

- `server=[IP]`: This option specifies the IP address of the upstream DNS server.


### DHCP Options

- `dhcp-authoritative`: This option specifies whether to act as an authoritative DHCP server.

- `dhcp-sequential-ip`: This option specifies whether to allocate IP addresses sequentially.

- `dhcp-leasefile=[path_to_file]`: This option specifies the location of the DHCP lease file.

- `dhcp-range=[subnet (optional)][start_ip],[end_ip],[subnet_mask],[lease_time]`: This option specifies the range of IP addresses to allocate to clients.

- `dhcp-option=[subnet (optional)],[option_name:option_value]`: This option specifies the DHCP options to send to clients.

- `dhcp-host=[mac_address],[ip_address]`: This option specifies the IP address to allocate to a specific client.