<!DOCTYPE html>
<html>
<script>
    function redirect(page) {
        window.location.replace(page);
    };
</script>

<head>
    <title>Router Landing Page</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <h1>Landing Page</h1>
    <div class="container">
        <div>
            <p>Welcome to the CSNA Landing Page!</p>
            <hr>
        </div>
        <div>
            <div class="canvas">
                <canvas id="connectedDevices"></canvas>
            </div>
            <div class="canvas">
                <canvas id="networkTraffic"></canvas>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="scripts.js"></script>

        <div>
            <button onclick="redirect('/admin/home.php')">Go to Admin Homepage</button>
        </div>
    </div>
</body>
</html>