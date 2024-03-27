
gui_config_file = "example.conf"
phoebus_dns_file = "../APSetup/dnsmasq.d/phoebus-dns.conf"
phoebus_dhcp_file = "../APSetup/dnsmasq.d/phoebus-dhcp.conf"
dns_file = "dns.conf"
dhcp_file = "dhcp.conf"

### Function to write data to the dns and dhcp files
# data: dictionary containing the data to be written
# type: the syntax that dnsmasq uses for its config file
# file: the output file that the data will be written to 
def write_data(data, type, file):

    # Open the file in append mode
    with open(file, 'a') as f:

        # Functionality for the type: Domain 
        if type == "domain":
            f.write(f"{type}={data}\n")
            f.write(f"local=/{data}/\n")

        # Functionality for the type: dhcp-range (creates the subnet)
        elif type == "dhcp-range":
            for key in data:
                output = f"{type}={key},{data[key]['Start']},{data[key]['End']},{data[key]['Mask']},{data[key]['Lease']}\n"
                output += f"dhcp-option={key},3,{data[key]['Router']}"
                f.write(f"{output}\n")

        # Functionality for the boolean options
        elif type == "dhcp-option":
            for key in data:
                if data[key] == "True":
                    output = f"{key}"
                    f.write(f"{output}\n")
                else:
                    f.write("")

        # For any other type use the format: type=data
        else:
            for key in data:
                output = f"{type}={data[key]}"
                f.write(f"{output}\n")

        f.close()

### Function to erase data from the dns and dhcp files
# file: the file to be erased
# option: specifies if the dns or dhcp data should be rewritten to the file
# otherwise the entire file will be erased
def erase_data(file, option=None):

    with open(file, 'w') as f:
        # If the option is dhcp, write the unchangeable dhcp options back to the file.
        if option == "dhcp":
            f.write("dhcp-leasefile=/etc/phoebus/dhcp.leases\n")
    
        # If the option is dns, write the unchangeable dns options back to the file.
        elif option == "dns":
            output = "localise-queries\nno-resolv\ndomain-needed\nexpand-hosts\nbogus-priv\n"
            output += "log-queries\nlog-async\nlog-facility=/var/log/phoebus/phoebus.log\n"
            output += "addn-hosts=/etc/phoebus/local.list\naddn-hosts=/etc/phoebus/custom.list\n"
            output += "dhcp-ignore-names=set:hostname-ignore\ndhcp-name-match=set:hostname-ignore,wpad\n"
            output += "dhcp-name-match=set:hostname-ignore,localhost\ncache-size=10000\n"
            f.write(output)

        # If the option is none, erase the entire file
        else:
            f.write("")

        f.close()

### Function to get the data from the config file
# config_file: the file to get the data from
def get_data(config_file):

    ifaces = {}
    dns_servers = {}
    dhcp_options = {}
    subnets = {}
    domain_name = None

    # Open the config file in read mode
    with open(config_file, "r") as f:

        # variables to check if a subnet has been initialized
        is_subnet = False
        subnet_name = None

        for line in f:
            key = line.split('=')[0]
            value = line.split('=')[1].strip("\n")

            if "IFACE" in key:
                ifaces[key] = value
            
            if "DNS" in key:
                dns_servers[key] = value
            
            if "DHCP_" in key:
                dhcp_options[key] = value
            
            if "SUBNET" in key:
                subnet_name = value
                subnets[subnet_name] = {}
                is_subnet = True

            if "_START" in key and is_subnet:
                subnets[subnet_name]["Start"] = value

            if "_END" in key and is_subnet:
                subnets[subnet_name]["End"] = value
            
            if "_MASK" in key and is_subnet:
                subnets[subnet_name]["Mask"] = value

            if "_ROUTER" in key and is_subnet:
                subnets[subnet_name]["Router"] = value
            
            if "_LEASE" in key and is_subnet:
                subnets[subnet_name]["Lease"] = value
                is_subnet = False

            if "DOMAIN" in key:
                domain_name = value

        f.close()

    return ifaces, dns_servers, dhcp_options, subnets, domain_name

# Get data from the config file
ifaces, dns_servers, dhcp_options, subnets, domain_name = get_data(gui_config_file)

# Write data to dns file
erase_data(dns_file, "dns")
write_data(ifaces, "interface", dns_file)
write_data(dns_servers, "server", dns_file)

# Write data to dhcp file
erase_data(dhcp_file, "dhcp")
write_data(dhcp_options, "dhcp-option", dhcp_file)
write_data(domain_name, "domain", dhcp_file)
write_data(subnets, "dhcp-range", dhcp_file)