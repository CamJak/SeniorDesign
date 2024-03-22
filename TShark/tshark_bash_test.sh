#!/usr/bin/env bash

output_dir="./tshark_outputs"
dumpfile="trafficdump.pcap"
num_packets="40" # amount of packet to cap at a time
interface="any"

common_bad_ports=("20" "21" "23" "80" "137" "139" "161" "443" "445" "1080" "3389" "4444" "6660" "6661" "6662" "6663" "6664" "6665" "6666" "6667" "6668" "6669" "8080" "8443" "31337")

# make necesary file structure for data storage
if [ ! -d "$output_dir" ]; then
    mkdir $output_dir
fi
if test -f "$output_dir/$dumpfile"; then
    echo "file exists ... will overwrite"
else
    echo "creating $output_dir/$dumpfile"
    touch $output_dir/$dumpfile
    chmod o+w $output_dir/$dumpfile
fi

# run tshark to capture num_packets amount of packets 
sudo tshark -i $interface -w $output_dir/$dumpfile -c $num_packets

# check for strange http user agents
echo "---- strange user agents: ----"
tshark -r $output_dir/$dumpfile -T fields -e http.user_agent | sort -u > $output_dir/useragentCheck.txt

if [ ! -s "$output_dir/useragentCheck.txt" ]; then
    echo "NO STRANGE USER AGENTS FOUND"
else
    cat $output_dir/useragentCheck.txt
fi
echo "---- end strange user agents. ----"

#general analytics
echo "---- general analytics: ----"
tshark -r $output_dir/$dumpfile -z endpoints,tcp -q > $output_dir/tcp_endpoint_analytics.txt
cat $output_dir/tcp_endpoint_analytics.txt
echo "---- end general analytics ----"


#port scanner
# Use netstat to get a list of all open ports
echo "---- begin looking for open ports ----"
open_ports=$(netstat -tuln | awk '{print $4}' | grep -oE '[0-9]*$')
echo "open ports:\n $open_ports"

# Iterate over the open ports
for open_port in $open_ports; do
    # Check if the open port is in the list of known ports
    for known_port in "${common_bad_ports[@]}"; do
        if [[ $open_port == $bad_port ]]; then
            echo "Port $open_port is open and is potentially dangerous."
        fi
    done
done

echo "---- end looking for open ports ----"
#### USE nslookup [IP] to resolve ip addresses on network

echo "program finished"
