#!/usr/bin/env bash

#directory & file instances
output_dir="./tshark_outputs"
dumpfile="./tshark_outputs/trafficdump.pcap"
analyzer_dir="./analyzer_outputs"
analyzerpcap="./analyzer_outputs/analyzerdump"



#analyze target
while :
do
	capinfos $dumpfile > $analyzerpcap
	echo cat $analyzerpcap
done