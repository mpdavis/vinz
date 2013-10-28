#!/bin/bash

echo "Running apt-get"
sudo apt-get update
sudo apt-get install nginx build-essential psmisc python-dev python-pip mongodb -y

echo "Installing python requirements with pip"
sudo pip install -r /vagrant/app/requirements.txt
sudo pip install gunicorn

echo "Setting up nginx configuration"
sudo cp /vagrant/provision/files/vinz_nginx /etc/nginx/sites-enabled/default

echo "Restarting nginx"
sudo service nginx restart

echo "Done provisioning!"
