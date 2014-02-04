#!/bin/bash
/usr/bin/killall python

/bin/echo -e "\n"
echo "Running development server at 10.13.37.2 on port 80"
python /vagrant/app/main.py
