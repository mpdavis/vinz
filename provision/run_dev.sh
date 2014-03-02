#!/bin/bash
/usr/bin/killall python

/bin/echo -e "\n"
cd /vagrant
grunt dev-app > /dev/null 2>&1 &
echo "Running development server at 10.13.37.2 on port 80"
python /vagrant/server/main.py
