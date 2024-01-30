<?php 
    $env = parse_ini_file('/etc/csna/setupVars.conf');

    if (isset($_POST['username']) && isset($_POST['password'])) {
        $validUname = $env['USERNAME'];
        $validPass = $env['PASSWORD'];

        function validate($data){
    
           $data = trim($data);
    
           $data = stripslashes($data);
    
           $data = htmlspecialchars($data);
    
           return $data;
    
        }

        $uname = validate($_POST['username']);
        $pass = validate($_POST['password']);

        if (empty($uname)) {

            header("Location: index.php?error=User Name is required");
    
            exit();
    
        }else if(empty($pass)){
    
            header("Location: index.php?error=Password is required");
    
            exit();
    
        }else{

            if($uname == $validUname && $pass == $validPass){
    
                header("Location: home.php");
    
                exit();
            }else{
    
                header("Location: index.php?error=Incorrect User Name or Password");
    
                exit();
            }
        }
    }