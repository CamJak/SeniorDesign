# This script runs on Python 3
import socket, threading
from connected_clients import connected_clients, is_client_connected

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'open'
        TCPsock.close()
    except:
        TCPsock.close()
        output[port_number] = ''

def scan_ports(host_ip, delay):
    output = {}         # For printing purposes
    for i in range(10):
        threads = []        # To run TCP_connect concurrently

        # Spawning threads to scan ports
        for j in range(1000):
            n = i * 1000 + j
            t = threading.Thread(target=TCP_connect, args=(host_ip, n, delay, output))
            threads.append(t)

        # Starting threads
        for j in range(1000):
            threads[j].start()

        # Locking the main thread until all threads complete
        for j in range(1000):
            threads[j].join()

        # Printing listening ports from small to large
        for j in range(1000):
            n = i * 1000 + j
            if output[n] == 'open':
                print(str(n) + ': ' + output[n])

def main():

    delay = 0.5

    # ips = list(connected_clients('TestData/DHCP/test_dhcp_data.txt').keys())
    
    # for ip in ips:
    #     if is_client_connected(ip):
    #         scan_ports(ip, delay)
    scan_ports("localhost", delay)

if __name__ == "__main__":
    main() 