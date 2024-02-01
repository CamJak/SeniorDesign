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

  - Errors I encountered
    - https://stackoverflow.com/questions/8028957/how-to-fix-headers-already-sent-error-in-php
    - https://stackoverflow.com/questions/67963371/load-a-env-file-with-php