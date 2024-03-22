import subprocess

def is_client_connected(ip_address):
    try:
        # Use the ping command to check if the IP address is reachable
        result = subprocess.run(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)

        # Check the return code to determine if the ping was successful
        return result.returncode == 0
    except Exception as e:
        print(f"Error checking connection for {ip_address}: {e}")
        return False

def create_table(file_path):
    # Initialize an empty list to store the extracted data
    data_list = []

    # Open the file and read its lines
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into individual pieces of data
            timestamp, mac_address, ip_address, hostname, _ = line.split()

            # Append the extracted data to the list
            data_list.append({
                'Timestamp': timestamp,
                'MAC Address': mac_address,
                'IP Address': ip_address,
                'Hostname': hostname
            })

    # Sort the data based on IP address
    data_list.sort(key=lambda x: list(map(int, x['IP Address'].split('.'))))

    # Print the table header
    print("{:<15} {:<18} {:<15} {:<20} {:<10}".format('Timestamp', 'MAC Address', 'IP Address', 'Hostname', 'Connected'))
    print("="*81)

    # Print the sorted data in a neat table format with connection status
    for data in data_list:
        connected_status = "Connected" if is_client_connected(data['IP Address']) else "Not Connected"
        print("{:<15} {:<18} {:<15} {:<20} {:<10}".format(data['Timestamp'], data['MAC Address'], data['IP Address'], data['Hostname'], connected_status))

# Replace 'your_file_path.txt' with the actual path to your text file
create_table('/etc/csna/dhcp.leases')
