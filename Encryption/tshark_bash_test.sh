#!/usr/bin/env bash

output_dir="./tshark_outputs"
dumpfile="trafficdump.pcap"
num_packets="20" # amount of packet to cap at a time
interface="any"

# make necesary file structure for data storage
if [ ! -d "$output_dir" ]; then
    mkdir $output_dir
fi
if test -f "$output_dir/$dumpfile"; then
    echo "" #"file exists ... will overwrite"
else
    echo "creating $output_dir/$dumpfile"
    touch $output_dir/$dumpfile
    chmod o+w $output_dir/$dumpfile
fi


test()
{
	echo "correct"
}

#capture all IPv4 HTTP packets to and from port 80,
http()
{
	sudo tshark -i $interface -f "tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)" -w $output_dir/$dumpfile -c $num_packets
}




# run tshark to capture num_packets amount of packets 
if [ -z "$1" ]; then
	sudo tshark -i $interface -w $output_dir/$dumpfile -c $num_packets
elif [ -n "$1" ]; then
	$1
fi


# check for strange http user agents
#echo "---- strange user agents: ----"
tshark -r $output_dir/$dumpfile -T fields -e http.user_agent | sort -u > $output_dir/useragentCheck.txt

if [ ! -s "$output_dir/useragentCheck.txt" ]; then
    echo "" #"NO STRANGE USER AGENTS FOUND"
else
    cat $output_dir/useragentCheck.txt
fi
echo "---- end strange user agents. ----"

#general analytics
echo "---- general analytics: ----"
tshark -r $output_dir/$dumpfile -z endpoints,tcp >> $output_dir/tcp_endpoint_analytics.txt
cat $output_dir/tcp_endpoint_analytics.txt

# Check if SSH port is open
#if netstat -tuln | grep ':22'; then
#    echo "Warning: SSH port is open!"

    # Check for potentially vulnerable or compromised states
    netstat -tuln | awk '$6 != "LISTEN" && $6 != "CLOSED" {print "Potentially vulnerable state:", $0}'

    # Use tshark to scan for traffic on the SSH port
#    echo "Scanning for SSH traffic..."
#    sudo tshark -i any -f "port 22" -O ssh
#else
    #echo "SSH port is not open."
#fi
#echo "---- end general analytics ----"



#echo "program finished"
