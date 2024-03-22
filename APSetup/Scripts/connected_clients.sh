#!/usr/bin/env bash

# Variables
cls_output=1
json_output=1
input_file="/etc/cnsa/dhcp.leases"

# Get the data from the input file
Timestamps=($(awk '{print $1}' $input_file))
MAC_Addresses=($(awk '{print $2}' $input_file))
IP_Addresses=($(awk '{print $3}' $input_file))

while read -r line;
do
    data=$(echo "$line" | awk '{print $4}')
    if [ "$data" = "*" ]; 
    then
        Hostnames+=("N/A")
    else
        Hostnames+=("$data")
    fi
done < "$input_file"

n=${#IP_Addresses[@]}  
for ((i = 0; i < n - 1; i++)); 
do
    min_idx=$i
    for ((j = i + 1; j < n; j++)); 
    do
        data1=$(echo ${IP_Addresses[$j]} | awk -F. '{print $1$2$3$4}')
        data2=$(echo ${IP_Addresses[$min_idx]} | awk -F. '{print $1$2$3$4}')
        if (( data1 < data2)); then
            min_idx=$j
        fi
    done
    # Swap the elements
    temp_timestamp=${Timestamps[$i]}
    temp_ip=${IP_Addresses[$i]}
    temp_mac=${MAC_Addresses[$i]}
    temp_hostname=${Hostnames[$i]}

    Timestamps[$i]=${Timestamps[$min_idx]}
    IP_Addresses[$i]=${IP_Addresses[$min_idx]}
    MAC_Addresses[$i]=${MAC_Addresses[$min_idx]}
    Hostnames[$i]=${Hostnames[$min_idx]}

    Timestamps[$min_idx]=$temp_timestamp
    IP_Addresses[$min_idx]=$temp_ip
    MAC_Addresses[$min_idx]=$temp_mac
    Hostnames[$min_idx]=$temp_hostname
done

if [ $cls_output = 1 ] && [ $json_output = 0 ]; 
then
    echo -e "Timestamp\tMAC Address\t\tIP Address\tHostname"
    echo "-------------------------------------------------------------------------"
    for i in "${!Timestamps[@]}"; 
    do
        echo -e "${Timestamps[$i]}\t${MAC_Addresses[$i]}\t${IP_Addresses[$i]}\t${Hostnames[$i]}"
    done
fi

if [ $json_output = 1 ] && [ $cls_output = 0 ]; 
then
    n=${#Timestamps[@]}
    n=$((n-1))
    for i in "${!Timestamps[@]}"; 
    do
        if [ $i -eq 0 ]; 
        then
            echo -e "{{ \"client$i\": {\"Timestamp\": \"${Timestamps[$i]}\", \"MAC Address\": \"${MAC_Addresses[$i]}\", \"IP Address\": \"${IP_Addresses[$i]}\", \"Hostname\": \"${Hostnames[$i]}\"}},"
        elif [ $i -eq $n ]; 
        then
            echo -e "{ \"client$i\": {\"Timestamp\": \"${Timestamps[$i]}\", \"MAC Address\": \"${MAC_Addresses[$i]}\", \"IP Address\": \"${IP_Addresses[$i]}\", \"Hostname\": \"${Hostnames[$i]}\"}}}"
        else
            echo -e "{ \"client$i\": {\"Timestamp\": \"${Timestamps[$i]}\", \"MAC Address\": \"${MAC_Addresses[$i]}\", \"IP Address\": \"${IP_Addresses[$i]}\", \"Hostname\": \"${Hostnames[$i]}\"}},"
        fi
    done
fi

if [ $json_output = 1 ] && [ $cls_output = 1 ]; 
then
    echo ""
    echo "Command Line Output"
    echo ""

    echo -e "Timestamp\tMAC Address\t\tIP Address\tHostname"
    echo "-------------------------------------------------------------------------"
    for i in "${!Timestamps[@]}"; 
    do
        echo -e "${Timestamps[$i]}\t${MAC_Addresses[$i]}\t${IP_Addresses[$i]}\t${Hostnames[$i]}"
    done

    echo ""
    echo "JSON Output"
    echo ""

    n=${#Timestamps[@]}
    n=$((n-1))
    for i in "${!Timestamps[@]}"; 
    do
        if [ $i -eq 0 ]; 
        then
            echo -e "{{ \"client$i\": {\"Timestamp\": \"${Timestamps[$i]}\", \"MAC Address\": \"${MAC_Addresses[$i]}\", \"IP Address\": \"${IP_Addresses[$i]}\", \"Hostname\": \"${Hostnames[$i]}\"}},"
        elif [ $i -eq $n ]; 
        then
            echo -e "{ \"client$i\": {\"Timestamp\": \"${Timestamps[$i]}\", \"MAC Address\": \"${MAC_Addresses[$i]}\", \"IP Address\": \"${IP_Addresses[$i]}\", \"Hostname\": \"${Hostnames[$i]}\"}}}"
        else
            echo -e "{ \"client$i\": {\"Timestamp\": \"${Timestamps[$i]}\", \"MAC Address\": \"${MAC_Addresses[$i]}\", \"IP Address\": \"${IP_Addresses[$i]}\", \"Hostname\": \"${Hostnames[$i]}\"}},"
        fi
    done
fi