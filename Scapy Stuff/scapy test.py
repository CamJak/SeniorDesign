import json
from scapy.all import sniff, wrpcap

packet_list = []

def packet_callback(packet):
    """
    Callback function to process each captured packet.
    """
    # Extract relevant information from the packet
    packet_info = {
        "timestamp": str(packet.time),
        "source_ip": packet[0][1].src,
        "destination_ip": packet[0][1].dst,
        "protocol": packet[0][1].name,
        "length": len(packet),
        "hex_dump": str(packet)#.encode('utf-8').hex()
        
    }

    # Append the packet information to the list
    packet_list.append(packet_info)

    # print packets to cli
    print(json.dumps(packet_info, indent=4))

# sniff until keyboard interrupt
try:
    print("Capturing packets. Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0)
except KeyboardInterrupt:
    pass

# Save the captured packets to a JSON file
output_file = "captured_packets.json"
with open(output_file, "w") as json_file:
    json.dump(packet_list, json_file, indent=4)

print(f"Packets captured successfully. Saved to {output_file}")