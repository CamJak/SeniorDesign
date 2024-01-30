<!DOCTYPE html>
<html>
<head>
    <title>Router Login</title>
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        
        h1 {
            text-align: center;
            color: #333;
        }
        
        form {
            max-width: 300px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        
        label {
            display: block;
            margin-bottom: 10px;
            color: #333;
        }
        
        input[type="text"],
        input[type="password"] {
            width: 92%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Router Login</h1>
    <form action="login.php" method="post">
        <div class="image">
            <img src="logo.png" alt="logo" width="310">
        </div>

        <?php if (isset($_GET['error'])) { ?>

            <p class="error"><?php echo $_GET['error']; ?></p>

        <?php } ?>

        <div class="container">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" placeholder="admin" required/>
            <br />
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" placeholder="password" required/>
            <br />
            <input type="submit" value="Login" />
        </div>
    </form>
</body>
</html>