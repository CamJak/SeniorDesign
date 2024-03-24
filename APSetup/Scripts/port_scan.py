import nmap
import json
from connected_clients import connected_clients, is_client_connected

test = nmap.PortScanner()

filename = 'TestData/DHCP/test_dhcp_data.txt'

ips = list(connected_clients(filename).keys())
output = {}
# for ip in ips:
#     if is_client_connected(ip):
#         data = test.scan(ip, '1-1024')
#         sorted_data = {}
#         for host in data['scan']:
#             sorted_data[host] = data['scan'][host]
#         output.update(sorted_data)
data = test.scan("localhost", '1-1024')
sorted_data = {}
for host in data['scan']:
    sorted_data[host] = data['scan'][host]
output.update(sorted_data)

print(output)

json.dump(sorted_data, open('TestData/port_scan.json', 'w'), indent=4)

# for host in data['scan']:
#     print("Client: " + host)
#     for port in data['scan'][host]['tcp']:
#         print("Port: " + str(port) + " - " + data['scan'][host]['tcp'][port]['state'])    