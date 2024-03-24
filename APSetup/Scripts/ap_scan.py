import sys
import subprocess
import json

def get_aps(filename):
    data = {}
    with open(filename, 'r') as file:
        encryption = False
        for line in file:
            if "Address" in line:
                encryption = False
                mac = line.split()[4]
                data[mac] = {}
                data[mac]['SSID'] = ""
            if "ESSID" in line:
                ssid = line.split("\"")[1]
                data[mac]['SSID'] = ssid
            if "Frequency" in line:
                freq = line.split(':')[1].split()[0]
                data[mac]['Frequency'] = freq
            if "Channel:" in line:
                channel = line.split(':')[1].split("\n")[0]
                data[mac]['Channel'] = channel
            if "Quality" in line:
                quality = line.split()[0].split('=')[1].split('/')[0]
                data[mac]['Quality'] = quality

                signal = line.split()[2].split('=')[1]
                data[mac]['Signal'] = signal
            if "Encryption key:on" in line:
                encryption = True
                data[mac]['Encryption'] = ""
                data[mac]['Authentication'] = ""
            if "Encryption key:off" in line:
                encryption = False
                data[mac]['Encryption'] = "None"
                data[mac]['Authentication'] = "None"
            if "IE: IEEE" in line and encryption:
                if "WPA2" in line:
                    data[mac]['Encryption'] = "WPA2"
                elif "WPA" in line:
                    data[mac]['Encryption'] = "WPA"
                elif "WEP" in line:
                    data[mac]['Encryption'] = "WEP"
                else:
                    data[mac]['Encryption'] = "None"
            if "Authentication Suites" in line and encryption:
                if "PSK" in line:
                    data[mac]['Authentication'] = "PSK"
                elif "802.1x" in line:
                    data[mac]['Authentication'] = "802.1x"
                else:
                    data[mac]['Authentication'] = "None"
    
    return data

def clean_data(data):
    bad_macs = []
    for mac in data:
        if data[mac]['SSID'] == "":
            bad_macs.append(mac)
    for mac in bad_macs:
        data.pop(mac)
    return data

def table_output(data):
    print("{:<20} {:<20} {:<20} {:<15} {:<15} {:<15}".format('MAC Address', 'SSID', 'Frequency', 'Channel', 'Quality', 'Signal'))
    print("="*102)
    for mac in data:
        ssid = data[mac]['SSID'] if len(data[mac]['SSID']) < 18 else data[mac]['SSID'][:12] + "..." + data[mac]['SSID'][-3:]
        freq = data[mac]['Frequency'] + " GHz"
        channel = data[mac]['Channel']
        quality = data[mac]['Quality']
        signal = data[mac]['Signal'] + " dBm"
        print("{:<20} {:<20} {:<20} {:<15} {:<15} {:<15}".format(mac, ssid, freq, channel, quality, signal))

def to_json(data, out_file):
    with open(out_file, 'w') as file:
        json.dump(data, file, indent=4)
    

def main():

    # proc = subprocess.Popen(["iwlist", interface, "scan"], stdout=subprocess.PIPE, universal_newlines=True)
    # out, err = proc.communicate()

    DEBUG = False
    JSON_OUTPUT = True
    TABLE_OUTPUT = False

    filename = "TestData/AP_Scan/large_test_ap_data.txt"
    interface = "wlan2"

    data = get_aps(filename)

    if TABLE_OUTPUT and not JSON_OUTPUT and not DEBUG:
        table_output(data)
    elif JSON_OUTPUT and not TABLE_OUTPUT and not DEBUG:
        to_json(clean_data(data), "TestData/ap_data.json")
    elif DEBUG and not TABLE_OUTPUT and not JSON_OUTPUT:
        print("Table Output")
        print("Raw Data:")
        table_output(data)
        print()
        print("Cleaned Data:")
        table_output(clean_data(data))
        print()
        print("JSON Output")
        print("Raw Data:")
        print(data)
        print()
        print("Cleaned Data:")
        print(clean_data(data))
    else:
        print("Usage: python ap_scan.py [interface] [output file]")

if __name__ == "__main__":
    main() 