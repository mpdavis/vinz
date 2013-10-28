@ECHO OFF
vagrant up
vagrant ssh -c "/vagrant/provision/run_dev.sh"
