<!DOCTYPE html>

<?php
    // DEBUG FILE LOCATION
    $env = parse_ini_file('.\\setupVars.conf');
    // $env = parse_ini_file('/etc/csna/setupVars.conf');
    $dns1 = $env['DNS1'];
    $dns2 = $env['DNS2'];

    //$domain = $env['DOMAIN'];
    $dhcp_auth = $env['DHCP_AUTHORITATIVE'];
    $dhcp_seq = $env['DHCP_SEQUENTIAL'];

    // subnets
    $subnet1 = $env['SUBNET1'];
    $dhcp1_start = $env['DHCP1_START'];
    $dhcp1_end = $env['DHCP1_END'];
    $dhcp1_mask = $env['DHCP1_MASK'];

    $subnet2 = $env['SUBNET2'];
    $dhcp2_start = $env['DHCP2_START'];
    $dhcp2_end = $env['DHCP2_END'];
    $dhcp2_mask = $env['DHCP2_MASK'];
?>

<script>
    function redirect(page) {
        window.location.replace(page);
    };
</script>

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
            <p>DNS 1: </p><input type="text" id="dns1" name="dns1" value="<?php echo $dns1; ?>"></br>
            <p>DNS 2: </p><input type="text" id="dns2" name="dns2" value="<?php echo $dns2; ?>"></br>
            <hr>
            <!-- <p>Domain: </p><input type="text" id="domain" name="domain" value="<?php echo $domain; ?>"></br> -->
            <p>Authoritative DHCP Server: </p>
                <input type="radio" id="dhcp_auth_on" name="dhcp_auth" value="on" <?php if ($dhcp_auth == 1) { ?> checked <?php } ?>>
                <label for="dhcp_auth_on">On</label>
                <input type="radio" id="dhcp_auth_off" name="dhcp_auth" value="off" <?php if ($dhcp_auth != 1) { ?> checked <?php } ?>>
                <label for="dhcp_auth_off">Off</label>
                </br>
            <p>DHCP Sequential IPs: </p>
                <input type="radio" id="dhcp_seq_on" name="dhcp_seq" value="on" <?php if ($dhcp_seq == 1) { ?> checked <?php } ?>>
                <label for="dhcp_seq_on">On</label>
                <input type="radio" id="dhcp_seq_off" name="dhcp_seq" value="off" <?php if ($dhcp_seq != 1) { ?> checked <?php } ?>>
                <label for="dhcp_seq_off">Off</label>
                </br>
            <hr>
            <p>Subnet 1 Name: </p><input type="text" id="subnet1" name="subnet1" value="<?php echo $subnet1; ?>"></br>
            <p>Subnet 1 Start Address: </p><input type="text" id="dhcp1_start" name="dhcp1_start" value="<?php echo $dhcp1_start; ?>"></br>
            <p>Subnet 1 End Address: </p><input type="text" id="dhcp1_end" name="dhcp1_end" value="<?php echo $dhcp1_end; ?>"></br>
            <p>Subnet 1 Mask: </p><input type="text" id="dhcp1_mask" name="dhcp1_mask" value="<?php echo $dhcp1_mask; ?>"></br>
            <hr>
            <p>Subnet 2 Name: </p><input type="text" id="subnet2" name="subnet2" value="<?php echo $subnet2; ?>"></br>
            <p>Subnet 2 Start Address: </p><input type="text" id="dhcp2_start" name="dhcp2_start" value="<?php echo $dhcp2_start; ?>"></br>
            <p>Subnet 2 End Address: </p><input type="text" id="dhcp2_end" name="dhcp2_end" value="<?php echo $dhcp2_end; ?>"></br>
            <p>Subnet 2 Mask: </p><input type="text" id="dhcp2_mask" name="dhcp2_mask" value="<?php echo $dhcp2_mask; ?>"></br>
            <hr>
            <input type="submit" value="Save Changes">
        </form>
        <button onclick="redirect('/index.php')">Go back to Home</button>
    </div>
</body>
</html>