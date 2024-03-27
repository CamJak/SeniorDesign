
gui_config_file = "example.conf"
phoebus_dns_file = "../APSetup/dnsmasq.d/phoebus-dns.conf"
phoebus_dhcp_file = "../APSetup/dnsmasq.d/phoebus-dhcp.conf"
dns_file = "dns.conf"
dhcp_file = "dhcp.conf"

def write_data(data, type, file):
    with open(file, 'a') as f:
        if type == "domain":
            f.write(f"{type}={data}\n")
            f.write(f"local=/{data}/\n")
        elif type == "dhcp-range":
            for key in data:
                output = f"{type}={key},{data[key]['Start']},{data[key]['End']},{data[key]['Mask']},{data[key]['Lease']}\n"
                output += f"{type}={key},3,{data[key]['Router']}"
                f.write(f"{output}\n")
        elif type == "dhcp-option":
            for key in data:
                if data[key] == "True":
                    output = f"{key}"
                    f.write(f"{output}\n")
                else:
                    f.write("")
        else:
            for key in data:
                output = f"{type}={data[key]}"
                f.write(f"{output}\n")

def erase_data(file, option=None):
    if option == "dhcp":
        with open(file, 'w') as f:
            f.write("dhcp-leasefile=/etc/phoebus/dhcp.leases\n")
            f.close()
    elif option == "dns":
        with open(file, 'w') as f:
            output = "localise-queries\nno-resolv\ndomain-needed\nexpand-hosts\nbogus-priv\n"
            output += "log-queries\nlog-async\nlog-facility=/var/log/phoebus/phoebus.log\n"
            output += "addn-hosts=/etc/phoebus/local.list\naddn-hosts=/etc/phoebus/custom.list\n"
            output += "dhcp-ignore-names=set:hostname-ignore\ndhcp-name-match=set:hostname-ignore,wpad\n"
            output += "dhcp-name-match=set:hostname-ignore,localhost\ncache-size=10000\n"
            f.write(output)
            f.close()
    else:
        with open(file, 'w') as f:
            f.write("")
            f.close()

def get_data(config_data):
    ifaces = {}
    dns_servers = {}
    dhcp_options = {}
    subnets = {}
    domain_name = None

    is_subnet = False
    subnet_name = None
    for key in config_data:
        if "IFACE" in key:
            ifaces[key] = config_data[key]
        
        if "DNS" in key:
            dns_servers[key] = config_data[key]
        
        if "DHCP_" in key:
            dhcp_options[key] = config_data[key]
        
        if "SUBNET" in key:
            subnet_name = config_data[key]
            subnets[subnet_name] = {}
            is_subnet = True

        if "_START" in key and is_subnet:
            subnets[subnet_name]["Start"] = config_data[key]

        if "_END" in key and is_subnet:
            subnets[subnet_name]["End"] = config_data[key]
        
        if "_MASK" in key and is_subnet:
            subnets[subnet_name]["Mask"] = config_data[key]

        if "_ROUTER" in key and is_subnet:
            subnets[subnet_name]["Router"] = config_data[key]
        
        if "_LEASE" in key and is_subnet:
            subnets[subnet_name]["Lease"] = config_data[key]
            is_subnet = False

        if "DOMAIN" in key:
            domain_name = config_data[key]

    return ifaces, dns_servers, dhcp_options, subnets, domain_name

with open(gui_config_file, "r") as f:
    config_data = {}
    for line in f:
        key = line.split('=')[0]
        value = line.split('=')[1]
        config_data[key] = value.strip("\n")
    f.close()

ifaces, dns_servers, dhcp_options, subnets, domain_name = get_data(config_data)

# Write data to dns file
erase_data(dns_file, "dns")
write_data(ifaces, "interface", dns_file)
write_data(dns_servers, "server", dns_file)

# Write data to dhcp file
erase_data(dhcp_file, "dhcp")
write_data(dhcp_options, "dhcp-option", dhcp_file)
write_data(domain_name, "domain", dhcp_file)
write_data(subnets, "dhcp-range", dhcp_file)