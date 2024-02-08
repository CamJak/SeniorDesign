#!/usr/bin/env bash

input_file="/etc/csna/dhcp.leases"
output_file="/etc/csna/modified_dhcp.leases"

awk '{print $3}' $input_file | sort | uniq | while read index
do
    awk -v var=$index '$3 == var { print $0}' $input_file
done > $output_file

echo -e "Timestamp\tMAC Address\t\tIP Address\tHostname\tStatus"
echo "-----------------------------------------------------------------------------------------"

while read -r var1 var2 var3 var4 var5 ; do

    timestamp=$(echo $var1)
    mac_address=$(echo $var2)
    ip_address=$(echo $var3)
    hostname=$(echo "$var4") 

    num_chars=$(echo -n "$hostname" | wc -c)

    if [ $num_chars -lt 8 ]; then
        connected="\t\tUnknown"
    else
        connected="\tUnknown"
    fi

    clients=$(ping -c 1 -w 2 $var3 > /dev/null)

    if [ $? -eq 0 ]; then
        if [ "$hostname" == "*" ]; then
                connected="\t\tConnected"
        else
                connected="\tConnected"
        fi
    fi

    echo -e "$timestamp\t$mac_address\t$ip_address\t$hostname$connected"
    
done < $output_file