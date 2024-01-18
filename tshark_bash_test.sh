#!/usr/bin/env bash

dumpfile="./trafficdump.pcap"
runtime="10" # tshark run time, in seconds
interface="wlp0s20f3"

if test -f "$dumpfile"; then
    echo "file exists ... will overwrite"
else
    echo "creating $dumpfile"
    touch $dumpfile
    chmod o+w $dumpfile
fi

# run tshark for specified time on specified 
sudo timeout $runtime tshark -i $interface -w $dumpfile

#check for strange http user agents
echo "---- strange user agents: ----"
tshark -r $dumpfile -T fields -e http.user_agent | sort -u >> useragentCheck.txt

if [ ! -s "./useragentCheck.txt" ]; then
    echo "NO STRANGE USER AGENTS FOUND"
else
    cat useragentCheck.txt
fi
echo "---- end strange user agents. ----"

#general analytics
echo "---- general analytics: ----"
tshark -r $dumpfile -z endpoints,tcp -q >> tcp_endpoint_analytics.txt
cat tcp_endpoint_analytics.txt
echo "---- end general analytics ----"

echo "program finished"
