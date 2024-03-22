#!/usr/bin/env bash

#directory & file instances
output_dir="./tshark_outputs"
dumpfile="./tshark_outputs/trafficdump.pcap"
analyzer_dir="./analyzer_outputs"
analyzerdump="./analyzer_outputs/analyzerdump"
endpointdump="./tshark_outputs/tcp_endpoint_analytics.txt"



#analyze target
trafficdump()
{
while :
do
	capinfos $dumpfile > $analyzerdump
	cat $analyzerdump
done
}

endpoint()
{
while :
do
	cat $endpointdump
done
}

test()
{
echo "it worked"
}

$1
