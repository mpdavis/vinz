#!/bin/bash

echo "Running apt-get"
sudo apt-get update
sudo apt-get install nginx build-essential psmisc python-dev python-pip mongodb -y

echo "Installing python requirements with pip"
sudo pip install -r /vagrant/app/requirements.txt
sudo pip install gunicorn

echo "Setting up nginx configuration"
sudo cp /vagrant/provision/files/vinz_nginx /etc/nginx/sites-enabled/default

echo "Moving SSH key file"
cp /vagrant/provision/files/id_rsa /home/vagrant/.ssh/id_rsa
cp /vagrant/provision/files/known_hosts /home/vagrant/.ssh/known_hosts
cp /vagrant/provision/files/config /home/vagrant/.ssh/config

chown -R vagrant:vagrant /home/vagrant/.ssh

echo "Restarting nginx"
sudo service nginx restart

echo "Done provisioning!"
