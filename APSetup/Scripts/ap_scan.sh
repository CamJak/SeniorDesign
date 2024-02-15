#!/bin/bash

# This script is used to scan the available APs and display the results
iw_output=$(cat test_data.txt)

ESSID=$(echo "$iw_output" | grep "ESSID" | awk -F\" '{print $2}')
Frequency=$(echo "$iw_output" | grep "Frequency" | awk -F: '{print $2}' | awk '{print $1}' | awk '{print substr ($0, 0, 3)}')
Channel=$(echo "$iw_output" | grep "Frequency" | awk -F: '{print $2}' | awk '{print $4}' | awk -F\) '{print $1}')
Quality=$(echo "$iw_output" | grep "Quality" | awk -F= '{print $2}' | awk -F/ '{print $1}')
Signal=$(echo "$iw_output" | grep "Signal level" | awk '{print $3}' | awk -F= '{print $2}')

ESSIDs=($ESSID)
Frequencies=($Frequency)
Channels=($Channel)
Qualities=($Quality)
Signals=($Signal)

# echo -e "ESSID\t\tFrequency\tChannel\t\tQuality\t\tSignal"
# echo "-----------------------------------------------------------------------------------------"

j=0
for i in "${ESSIDs[@]}"; 
do
    echo 
    echo -e "{ \"ap$j\": {\"ESSID\": \"$i\", \"Frequency\": ${Frequencies[$j]}, \"Channel\": ${Channels[$j]}, \"Quality\": ${Qualities[$j]}, \"Signal\": ${Signals[$j]}}},"
    j=$((j+1))
done