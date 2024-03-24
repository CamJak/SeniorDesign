import json
import subprocess

# Function to determine if client is connected
def is_client_connected(ip_address):
    try:
        result = subprocess.run(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
        return result.returncode == 0
    except Exception as e:
        return False

# Function to create a list of connected clients
def connected_clients(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            timestamp, mac, ip_address, hostname, _ = line.split()
            if hostname == '*':
                hostname = 'N/A'
            data[ip_address] = {
                'Timestamp': timestamp,
                'MAC Address': mac,
                'Hostname': hostname
            }
        sorted_ips = sorted(data.keys(), key=lambda x: list(map(int, x.split('.'))))
        
        sorted_data = {}
        for ip in sorted_ips:
            sorted_data[ip] = data[ip]

    return sorted_data

# Function to create a table of connected clients
def table_output(data):
    print("{:<15} {:<18} {:<15} {:<20}".format('Timestamp', 'MAC Address', 'IP Address', 'Hostname'))
    print("="*68)
    for ip in data:
        timestamp = data[ip]['Timestamp']
        mac = data[ip]['MAC Address']
        hostname = data[ip]['Hostname']
        print("{:<15} {:<18} {:<15} {:<20}".format(timestamp, mac, ip, hostname))

def to_json(data, out_file):
    with open(out_file, 'w') as file:
        json.dump(data, file, indent=4)  

def main():

    DEBUG = False
    JSON_OUTPUT = True
    TABLE_OUTPUT = False 

    filename = 'TestData/DHCP/test_dhcp_data.txt'

    data = connected_clients(filename)
    # for data in list(data.keys()):
    #     print(is_client_connected(data))

    if TABLE_OUTPUT and not JSON_OUTPUT and not DEBUG:
        table_output(data)
    if JSON_OUTPUT and not TABLE_OUTPUT and not DEBUG:
        to_json(data, 'TestData/dhcp_data.json')
    if DEBUG and not TABLE_OUTPUT and not JSON_OUTPUT:
        print("Table Output")
        table_output(data)
        print()
        print("JSON Output")
        print(data)

if __name__ == "__main__":
    main()