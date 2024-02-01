<!DOCTYPE html>

<?php
    // DEBUG FILE LOCATION
    $env = parse_ini_file('.\\setupVars.conf');
    // $env = parse_ini_file('/etc/csna/setupVars.conf');
    $ipAddress = $env['IP'];
    $dns1 = $env['DNS1'];
    $dns2 = $env['DNS2'];
?>

<html>
<head>
    <title>Router Login</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <h1>Admin Homepage</h1>

    <div class="container">
        <h2>Router Configuration Settings</h2>
        <?php if (!empty($ipAddress)) { ?>
            <p>Router IP Address: <?php echo $ipAddress; ?></p>
        <?php } if (!empty($dns1)) { ?>
            <p>Router DNS1: <?php echo $dns1; ?></p>
        <?php } if (!empty($dns2)) { ?>
            <p>Router DNS2: <?php echo $dns2; ?></p>
        <?php } ?>
    </div>
</body>
</html>