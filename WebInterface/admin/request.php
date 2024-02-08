<?php
    // DEBUG FILE LOCATION
    $outputFile = fopen('.\\setupVars.conf','w');
    //$outputFile = fopen('/etc/csna/setupVars.conf','w');

    // Function to write to config file with proper formatting
    function writeConfig($varName,$postName,$conf) {
        $temp = $_POST[$postName];
        fwrite($conf, "$varName=$temp\n");
    }

    // Put all sent data into config file
    writeConfig("IP","ipAddress",$outputFile);
    writeConfig("DNS1","dns1",$outputFile);
    writeConfig("DNS2","dns2",$outputFile);

    // Close config file
    fclose($outputFile);

    // Redirect back to home page
    header("Location: home.php");