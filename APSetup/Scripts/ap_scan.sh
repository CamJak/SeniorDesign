#!/bin/bash

# Variables
cls_output=1
json_output=0

# This script is used to scan the available APs and display the results
iw_output=$(sudo iwlist wlan2 scan)

ESSID=$(echo "$iw_output" | grep "ESSID" | awk -F ':' '{print $2 ","}')
Frequency=$(echo "$iw_output" | grep "Frequency" | awk -F: '{print $2}' | awk '{print $1}' | awk '{print substr ($0, 0, 3)}')
Channel=$(echo "$iw_output" | grep "Frequency" | awk -F: '{print $2}' | awk '{print $4}' | awk -F\) '{print $1}')
Quality=$(echo "$iw_output" | grep "Quality" | awk -F= '{print $2}' | awk -F/ '{print $1}')
Signal=$(echo "$iw_output" | grep "Signal level" | awk '{print $3}' | awk -F= '{print $2}')

Frequencies=($Frequency)
Channels=($Channel)
Qualities=($Quality)
Signals=($Signal)

if [ $cls_output = 1 ] && [ $json_output = 0 ]; 
then
    echo -e "\tESSID\t\t\tFrequency\tChannel\tQuality\tSignal"
    echo "-------------------------------------------------------------------------"
    j=1
    for i in ${!Channels[@]}; 
    do
        if [ $(echo $ESSID | awk -F',' '{print $'$j'}' | wc -c) -lt 18 ]; 
        then
            echo -e $(echo $ESSID | awk -F',' ''$j'\t{print $'$j'}')"\t\t"${Frequencies[$i]} GHz"\t\t"${Channels[$i]}"\t"${Qualities[$i]}"\t"${Signals[$i]} dBm
        else
            echo -e $(echo $ESSID | awk -F',' ''$j'{print $'$j'}')"\t"${Frequencies[$i]} GHz"\t\t"${Channels[$i]}"\t"${Qualities[$i]}"\t"${Signals[$i]} dBm
        fi
        j=$((j+1))
    done
fi

if [ $json_output = 1 ] && [ $cls_output = 0 ]; 
then
    n=${#Channels[@]}
    n=$((n-1))
    j=1
    for i in "${!Channels[@]}"; 
    do
        if [ $i -eq 0 ]; 
        then
            echo -e "{{ \"ap$i\": {\"ESSID\": $(echo $ESSID | awk -F',' '{print $'$j'}'), \"Frequency\": ${Frequencies[$i]}, \"Channel\": ${Channels[$i]}, \"Quality\": ${Qualities[$i]}, \"Signal\": ${Signals[$i]}}},"
            j=$((j+1))
        elif [ $i -eq $n ]; 
        then
            echo -e "{ \"ap$i\": {\"ESSID\": $(echo $ESSID | awk -F',' '{print $'$j'}'), \"Frequency\": ${Frequencies[$i]}, \"Channel\": ${Channels[$i]}, \"Quality\": ${Qualities[$i]}, \"Signal\": ${Signals[$i]}}}}"
        else
            echo -e "{ \"ap$i\": {\"ESSID\": $(echo $ESSID | awk -F',' '{print $'$j'}'), \"Frequency\": ${Frequencies[$i]}, \"Channel\": ${Channels[$i]}, \"Quality\": ${Qualities[$i]}, \"Signal\": ${Signals[$i]}}},"
            j=$((j+1))
        fi
    done
fi

if [ $json_output = 1 ] && [ $cls_output = 1 ]; 
then
    echo ""
    echo "Command Line Output"
    echo ""

    echo -e "ESSID\t\t\tFrequency\tChannel\tQuality\tSignal"
    echo "-------------------------------------------------------------------------"
    j=1
    for i in ${!Channels[@]}; 
    do
        if [ $(echo $ESSID | awk -F',' '{print $'$j'}' | wc -c) -lt 18 ]; 
        then
            echo -e $(echo $ESSID | awk -F',' '{print $'$j'}')"\t\t"${Frequencies[$i]} GHz"\t\t"${Channels[$i]}"\t"${Qualities[$i]}"\t"${Signals[$i]} dBm
        else
            echo -e $(echo $ESSID | awk -F',' '{print $'$j'}')"\t"${Frequencies[$i]} GHz"\t\t"${Channels[$i]}"\t"${Qualities[$i]}"\t"${Signals[$i]} dBm
        fi
        j=$((j+1))
    done

    echo ""
    echo "JSON Output"
    echo ""

    n=${#Channels[@]}
    n=$((n-1))
    j=1
    for i in "${!Channels[@]}"; 
    do
        if [ $i -eq 0 ]; 
        then
            echo -e "{{ \"ap$i\": {\"ESSID\": $(echo $ESSID | awk -F',' '{print $'$j'}'), \"Frequency\": ${Frequencies[$i]}, \"Channel\": ${Channels[$i]}, \"Quality\": ${Qualities[$i]}, \"Signal\": ${Signals[$i]}}},"
            j=$((j+1))
        elif [ $i -eq $n ]; 
        then
            echo -e "{ \"ap$i\": {\"ESSID\": $(echo $ESSID | awk -F',' '{print $'$j'}'), \"Frequency\": ${Frequencies[$i]}, \"Channel\": ${Channels[$i]}, \"Quality\": ${Qualities[$i]}, \"Signal\": ${Signals[$i]}}}}"
        else
            echo -e "{ \"ap$i\": {\"ESSID\": $(echo $ESSID | awk -F',' '{print $'$j'}'), \"Frequency\": ${Frequencies[$i]}, \"Channel\": ${Channels[$i]}, \"Quality\": ${Qualities[$i]}, \"Signal\": ${Signals[$i]}}},"
            j=$((j+1))
        fi
    done
fi