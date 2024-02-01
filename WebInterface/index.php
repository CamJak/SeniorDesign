<!DOCTYPE html>
<html>

<script>
    function redirect(page) {
        window.location.replace(page);
    };
</script>

<head>
    <title>Router Login</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <h1>Test Landing Page</h1>
    <button onclick="redirect('/admin/home.php')">Go to Admin Homepage</button>
</body>
</html>