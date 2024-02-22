from scapy.all import sniff, TCP, IP
from collections import defaultdict
import time
import numpy as np
from os import environ


class SessionTracker:
    def __init__(self, cb=None):
        self.raw_sessions = defaultdict(list)
        self.callback = cb

    def add_packet(self, packet):
        #determine the session_id
        session_id = self.assemble_session_id(packet)

        #check if this is a new session
        if packet[TCP].flags == "S":
            #create a new session
            self.raw_sessions[session_id] = [packet]

        #if the connection is being closed
        elif packet[TCP].flags == 'F' or packet[TCP].flags == 'R':

            #ensure that the script wasn't ran right before the connection was closed
            if(session_id in self.raw_sessions.keys() and "S" in [p[TCP].flags for p in self.raw_sessions[session_id]]):
                self.process_session(session_id)
                del self.raw_sessions[session_id]

        #otherwise add the packet to the session
        else:
            self.raw_sessions[session_id].append(packet)

    #neccessary to uniquely identify a session while including both traffic directions
    def assemble_session_id(self, packet):
        src_ip = packet[IP].src
        dest_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dest_port = packet[TCP].dport

        if src_ip < dest_ip or (src_ip == dest_ip and src_port < dest_port):
            return (src_ip, src_port, dest_ip, dest_port)
        else:
            return (dest_ip, dest_port, src_ip, src_port)

    def process_session(self, session_id):
        #ensure that the packets in the session are sorted by time
        self.raw_sessions[session_id].sort(key=lambda x: x.time)

        if(len(self.raw_sessions[session_id]) != 0):
            #separate the forward and backward traffic
            src_ip = self.raw_sessions[session_id][0][IP].src
            dest_ip = self.raw_sessions[session_id][0][IP].dst

            forward_packets = [p for p in self.raw_sessions[session_id] if p[IP].src == src_ip and p[IP].dst == dest_ip] 
            backward_packets = [p for p in self.raw_sessions[session_id] if p[IP].src == dest_ip and p[IP].dst == src_ip]
            all_packets = self.raw_sessions[session_id]

        else:
            print(f"No packets in this session {session_id}")

        #Source_port
        source_port = session_id[1]

        #forward packet feature logic
        if len(forward_packets) == 0 :
            max_interval_forward = 0
            forward_payload_len = 0
            duration_forward = 0
            std_forward_pkt_len = 0

        elif len(forward_packets) == 1 :
            max_interval_forward = 0
            forward_payload_len = len(forward_packets[0][TCP].payload)
            duration_forward = 0
            std_forward_pkt_len = 0
        else:
            #max_Interval_of_arrival_time_of_forward_traffic
            max_interval_forward = max([forward_packets[i+1].time - forward_packets[i].time for i in range(len(forward_packets)-1)])

            #Total_length_of_forward_payload
            forward_payload_len = sum([len(packet[TCP].payload) for packet in forward_packets])

            #duration_forward
            duration_forward = forward_packets[-1].time - forward_packets[0].time

            #std_forward_pkt_length
            std_forward_pkt_len = np.std([len(packet) for packet in forward_packets])


        #backward packet feature logic
        if len(backward_packets) <= 1 :
            max_interval_backwards = 0
            std_interval_backwards = 0
        else:
            #max_Interval_of_arrival_time_of_backward_traffic
            max_interval_backwards = max([backward_packets[i+1].time - backward_packets[i].time for i in range(len(backward_packets)-1)])

            #std_Interval_of_arrival_time_of_backward_traffic
            std_interval_backwards = np.std([backward_packets[i+1].time - backward_packets[i].time for i in range(len(backward_packets)-1)])


        #all packet feature logic
        if len(all_packets) == 0 :
            mean_window = 0
            flow_duration = 0
            std_ip_len = 0
            max_time_diff = 0
            max_tcp_payload_len = 0
            mean_ttl = 0
            std_ttl = 0

        elif len(all_packets) == 1 :
            mean_window = all_packets[0][TCP].window
            flow_duration = 0
            std_ip_len = len(all_packets[0])
            max_time_diff = 0
            max_tcp_payload_len = len(all_packets[0][TCP].payload)
            mean_ttl = all_packets[0][IP].ttl
            std_ttl = 0

        else:
            #mean_TCP_windows_size_value
            mean_window = sum([packet[TCP].window for packet in all_packets])/len(all_packets)

            #flow duration
            flow_duration = all_packets[-1].time - all_packets[0].time

            #std_Length_of_IP_packets
            std_ip_len = np.std([len(packet) for packet in all_packets])

            #max_Time_difference_between_packets_per_session
            max_time_diff = max([all_packets[i+1].time - all_packets[i].time for i in range(len(all_packets)-1)])

            #max_Length_of_TCP_payload
            max_tcp_payload_len = max([len(packet[TCP].payload) for packet in all_packets])

            #mean_time_to_live
            mean_ttl = sum([packet[IP].ttl for packet in all_packets])/len(all_packets)

            #std_time_to_live
            std_ttl = np.std([packet[IP].ttl for packet in all_packets])

        #package the features into a dictionary
        features = {
            "mean_TCP_windows_size_value": mean_window,
            "Source_port": source_port,
            "max_Interval_of_arrival_time_of_forward_traffic": max_interval_forward,
            "max_Interval_of_arrival_time_of_backward_traffic": max_interval_backwards,
            "flow duration": flow_duration,
            "std_Interval_of_arrival_time_of_backward_traffic": std_interval_backwards,
            "Total_length_of_forward_payload": forward_payload_len,
            "std_Length_of_IP_packets": std_ip_len,
            "max_Time_difference_between_packets_per_session": max_time_diff,
            "std_forward_pkt_length": std_forward_pkt_len,
            "max_Length_of_TCP_payload": max_tcp_payload_len,
            "mean_time_to_live": mean_ttl,
            "std_time_to_live": std_ttl,
            "duration_forward": duration_forward,
            "num_packets": len(all_packets)
        }

        self.write_session(features)
        if(flow_duration == 0):
            print(all_packets)

    #ideally this will be changed to instead send the features through the network to the model
    def write_session(self, features):
        if(self.callback):
            self.callback(features)
        else:
            for key, value in features.items():
                print(f"{key}: {value}")
            print("\n\n")
        # with open("features.csv", "a") as f:
        #     f.write(",".join([str(features[feature]) for feature in features]))
        #     f.write("\n")


# #instantiating the session tracker
# tracker = SessionTracker()

# #start sniffing packets
# sniff(iface="enp0s3", prn=lambda x: tracker.add_packet(x) if TCP in x else None)