<!DOCTYPE html>
<html>

<script>
    function redirect(page) {
        window.location.replace(page);
    };
</script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="scripts.js"></script>

<head>
    <title>Router Login</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <h1>Landing Page</h1>
    <div class="container">
        <p>Hello!</p>
        <div>
            <canvas id="myChart"></canvas>
        </div>
    </div>
    <button onclick="redirect('/admin/home.php')">Go to Admin Homepage</button>
</body>
</html>