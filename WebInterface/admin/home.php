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
        <form action="request.php" method="post">
            <hr>
            <p>Router IP Address: </p><input type="text" id="ipAddress" name="ipAddress" value="<?php echo $ipAddress; ?>"></br>
            <p>DNS 1: </p><input type="text" id="dns1" name="dns1" value="<?php echo $dns1; ?>"></br>
            <p>DNS 2: </p><input type="text" id="dns2" name="dns2" value="<?php echo $dns2; ?>"></br>
            <input type="submit" value="Save Changes">
        </form>
        </div>
</body>
</html>