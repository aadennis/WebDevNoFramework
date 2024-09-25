Snippets for configuration

stty cols 120
export PS1="> "

Let's call the ip address version of the file consistently ip_ver
And the domain version domain_ver

Which would give say for ip_ver…(note - do not use http://, just the ip address followed by a ;

server {
    listen 80;
    server_name 20.90.164.19;

    root /var/www/app;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

/etc/nginx/sites-available/ip_ver

cd /etc/nginx/sites-available

ls -ld

sudo chown azureuser /etc/nginx/sites-available
sudo chown azureuser /etc/nginx/sites-enabled

sudo chown azureuser /etc/nginx/sites-available/*

export PS1="> "

cp default ip_ver


azureuser@ajax-vm:/etc/nginx/sites-available$ history
    1  pwd
    2  cd /
    3  ls -l
    4  mkdir /app
    5  mkdir /var/www
    6  sudo mkdir /var/www
    7  mkdir /var/www
    8  sudo chown azureuser:azureuser /var/www
    9  asdf
   10  sudo apt update
   11  sudo apt install nginx
   12  clear
   13  history
   14  sudo apt update
   15  apt list --upgradable
   16  sudo apt install nginx
   17  sudo nano /etc/nginx/sites-available/mywebsite
   18  sudo vi /etc/nginx/sites-available/mywebsite
   19  sudo nano /etc/nginx/sites-available/mywebsite
   20  ls
   21  cd /etc/nginx/sites-available/
   22  > mywebsite
   23  sudo nano /etc/nginx/sites-available/mywebsite
   24  cat mywebsite 
   25  ls -l mywebsite 
   26  chmod +w mywebsite 
   27  sudo chown azureuser mywebsite
   28  ls -l mywebsite 
   29  cat mywebsite 
   30  sudo ln -s /etc/nginx/sites-available/mywebsite /etc/nginx/sites-enabled/
   
   sudo ln -s /etc/nginx/sites-available/ip_ver /etc/nginx/sites-enabled/

ls -l /etc/nginx/sites-enabled/


sudo nginx -t

sudo systemctl reload nginx

ls -l /etc/nginx/sites-available

cat /etc/nginx/sites-available/default

/var/www/app 
