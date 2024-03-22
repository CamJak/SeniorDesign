# Preface

Below is the documentation of my work on the web-based GUI for our project. NGINX serves as the web server, serving up PHP/HTML to the user to give them control over the device through a web interface. The documentation details my process of setting up the tools needed, and designing the interface itself, as well as listing any resources I used to get me there. - Cam

# NGINX (engine-ex) Installation
> sudo apt-get install nginx

> sudo nginx -v (verify install)

## NGINX Info
Interact with the nginx process:
> sudo systemctl start nginx
- can also use commands: stop, restart, status, enable (sets nginx to auto-start on reboot)

Important locations:
- NGINX config: /etc/nginx/nginx.conf 
- Other config: /etc/nginx/sites-available/default (this one seems to be the better one)
- Web root: /var/www/html
  - Updates imediately when changes are made!

# PHP Installation

Had to install php on the Pi to use it with nginx, followed these docs:
https://www.php.net/manual/en/install.unix.nginx.php

Got stuck launching php for a while...

This site helped me get it running: https://www.cnblogs.com/my-blogs-for-everone/p/9983241.html

# PHP/HTML Writing Journey

Pages that helped me while writing php:
  - Code I used
    - https://www.simplilearn.com/tutorials/php-tutorial/php-login-form - the login form code
    - https://www.php.net/manual/en/function.exec.php - good for running scripts!

  - Errors I encountered
    - https://stackoverflow.com/questions/8028957/how-to-fix-headers-already-sent-error-in-php
    - https://stackoverflow.com/questions/67963371/load-a-env-file-with-php
    - Changed perms for setupVars file to 777 so that php could write to file (there may be a better solution?)

# Testing PHP locally

Run this command to run a local PHP server at the specified directory.
https://www.php.net/manual/en/features.commandline.webserver.php

> php.exe -S localhost:8000 -t C:\rootDir

# Using NGINX to handle AuthN and AuthZ

After doing some research I discovered that NGINX has the capability to handle our auth and lock down certain routes on the page as desired,
as well as to block outside IPs from accessing the page at all.

- https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/

# The wonderful world of Javascript

Using javascript makes charts a breeze!
https://www.chartjs.org/docs/latest/charts/line.html