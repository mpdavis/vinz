# Vinz

Vinz is a SSH key management system leveraging ansible to handle a company-wide deployment of keys.


## Dev Environment

Let's get everything setup.

### Pre-Requesites

You need to take care of a couple of things before getting started.

* [Install Vagrant](http://vagrantup.com)
* [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Install Git](http://git-scm.com/downloads)
* [Setup Github](https://help.github.com/articles/set-up-git)

### Checking out the code

Checking out the code pulls it down to your machine.  Remember where you check the code out to, as that is where you will be editing the code.  Exactly how you check out the code depends on what operating system you are using.  

If you are on Windows, I would reccomend [Github for Windows](http://windows.github.com/)

### Starting VM

Our dev environment takes place inside of a VM thanks to Vagrant.  You don't have to pay much attention to this, because the code on your system is automatically synced to the right place in the VM.  However, you do need to get the VM up and going before working. 

The first thing we need to do is pull down the base box image to your machine.  This is a VM image that vagrant can use in order to make VMs from.

    vagrant box add base http://files.vagrantup.com/precise64.box

Now, we can create the VM and get everything provisioned.  Make sure that you are in the directory where you checked out our source code.

    vagrant up
    
This will take about a minute and a half depending on your machine and network connection.  This creates the VM and installs everything needed in order to get it in a state that lets it run our code.

At this point, the VM should be up and running.  It already has a private network connection to your machine. You can see our application in a browser by going to `http://10.13.37.2`

If you edit the source code on the host machine, you can reload the webpage at see your changes.  

## Problems?

This is simply written from memory.  When (not if) you run into problems, let Michael know and he will update the README.
