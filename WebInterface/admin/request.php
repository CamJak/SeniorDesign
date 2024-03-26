<?php
    // DEBUG FILE LOCATION
    $outputFile = fopen('.\\setupVars.conf','w');
    //$outputFile = fopen('/etc/csna/setupVars.conf','w');

    // Function to write to config file with proper formatting
    function writeConfigText($varName,$postName,$conf) {
        $temp = $_POST[$postName];
        fwrite($conf, "$varName=$temp\n");
    }
    function writeConfigRadio($varName,$postName,$conf) {
        $temp = $_POST[$postName];
        if ($temp == "on") {
            fwrite($conf, "$varName=True\n");
        } else {
            fwrite($conf, "$varName=False\n");
        }
    }

    // Put all sent data into config file
    // 'fwrite' used for hardcoding values, functions used for user input
    fwrite($outputFile, "IFACE1=eth0\n");
    fwrite($outputFile, "IFACE2=wlan0\n");
    fwrite($outputFile, "IFACE3=wlan1\n");
    writeConfigText("DNS1","dns1",$outputFile);
    writeConfigText("DNS2","dns2",$outputFile);
    writeConfigRadio("DHCP_AUTHORITATIVE","dhcp_auth",$outputFile);
    writeConfigRadio("DHCP_SEQUENTIAL","dhcp_seq",$outputFile);
    fwrite($outputFile, "DOMAIN=phoebus\n");
    writeConfigText("SUBNET1","subnet1",$outputFile);
    writeConfigText("DHCP1_START","dhcp1_start",$outputFile);
    writeConfigText("DHCP1_END","dhcp1_end",$outputFile);
    writeConfigText("DHCP1_MASK","dhcp1_mask",$outputFile);
    fwrite($outputFile, "DHCP1_LEASE=1h\n");
    fwrite($outputFile, "DHCP1_ROUTER=10.0.0.1\n");
    writeConfigText("SUBNET2","subnet2",$outputFile);
    writeConfigText("DHCP2_START","dhcp2_start",$outputFile);
    writeConfigText("DHCP2_END","dhcp2_end",$outputFile);
    writeConfigText("DHCP2_MASK","dhcp2_mask",$outputFile);
    fwrite($outputFile, "DHCP2_LEASE=1h\n");
    fwrite($outputFile, "DHCP2_ROUTER=10.0.1.1\n");

    // Close config file
    fclose($outputFile);

    // Redirect back to home page
    header("Location: home.php");