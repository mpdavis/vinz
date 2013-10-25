#!/bin/bash

echo "Running apt-get"
sudo apt-get update
sudo apt-get install nginx build-essential python-dev python-pip supervisor mongodb -y

echo "Installing python requirements with pip"
sudo pip install -r /vagrant/app/requirements.txt
sudo pip install gunicorn

echo "Setting up nginx configuration"
sudo cp /vagrant/provision/files/vinz_nginx /etc/nginx/sites-enabled/default

echo "Restarting nginx"
sudo service nginx restart

echo "Setting up supervisor configuration"
sudo cp /vagrant/provision/files/vinz_supervisor.conf /etc/supervisor/conf.d/vinz.conf

echo "Restarting supervisor"
sudo supervisorctl reload

echo "Done provisioning!"
