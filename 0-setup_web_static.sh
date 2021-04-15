#!/usr/bin/env bash
# sets up your servers for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "File to test Nginx config" | sudo tee /data/web_static/releases/test/index.html
sudo rm /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -ie "s|^\tlocation / {|\tlocation /hbnb_static/ {\n\t\talias /data/web_staic/current/;\n\t}\n\n\tlocation / {|" /etc/nginx/sites-available/default
sudo service nginx restart
