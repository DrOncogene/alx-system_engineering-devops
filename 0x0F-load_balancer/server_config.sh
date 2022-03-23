#!/usr/bin/env bash
# configures a url redirect at /redirect_me
# ignore SC2154
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
ufw enable
service apache2 stop
service nginx start
sed -i -r 's/^(\s+)(# SSL configuration)/\1rewrite \^\/redirect_me\[\/\]*\$ https:\/\/google.com permanent\;\n\1\2/g' /etc/nginx/sites-available/default
sed -i -r "s|^(\s+)(location / \{)|\1\2\n\1\1add_header X-Served-By $HOSTNAME always\;\n|g" /etc/nginx/sites-available/default
service nginx reload
