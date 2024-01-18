import subprocess

def scan_network(ip_range):
    command = f"nmap -sP {ip_range}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    ip = mac = hostname = 'N/A'  # Initialize variables outside the loop

    if result.returncode == 0:
        output_lines = result.stdout.splitlines()
        
        print(output_lines)

        IPs = []
        MACs = []
        Vendors = []
        for line in output_lines:
            if 'Nmap scan report for' in line:
                IP=line.split()[4]
                IPs.append(IP)

            if 'MAC Address:' in line:
                mac = line.split()[2]
                MACs.append(mac)
                vender = line.split()[3]
                Vendors.append(vender)

    return IPs, MACs, Vendors

def print_results(ip, mac, hostname):
    for i in range(len(ip)):
        print(f"IP: {ip[i]} | MAC: {mac[i]} | Hostname: {hostname[i]}")

if __name__ == "__main__":
    ip_range = '192.168.0.1/24'  # Replace with your desired IP range
    IPs, MACs, Vendors = scan_network(ip_range)
    print_results(IPs, MACs, Vendors)

