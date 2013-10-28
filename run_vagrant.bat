@ECHO OFF
call vagrant up
call vagrant ssh -c "/vagrant/provision/run_dev.sh"
