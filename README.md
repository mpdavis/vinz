# Vinz

Vinz is a SSH key management system leveraging ansible to handle a company-wide deployment of keys.


## Dev Environment

Let's get everything set up.

### Prerequisites

You need to take care of a couple of things before getting started.

* [Install Vagrant](http://vagrantup.com)
* [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads) NOTE: There is a bug in VirtualBox 4.3, [use 4.2 for now](https://www.virtualbox.org/wiki/Download_Old_Builds_4_2).
* [Install Git](http://git-scm.com/downloads)
* [Set up GitHub](https://help.github.com/articles/set-up-git)

### Checking out the code

Checking out the code pulls it down to your machine.  Remember where you check the code out to, as that is where you will be editing the code.  Exactly how you check out the code depends on what operating system you are using.  

If you are on Windows, I would recommend [GitHub for Windows](http://windows.github.com/)

### Starting VM

Our dev environment takes place inside of a VM thanks to Vagrant.  You don't have to pay much attention to this, because the code on your system is automatically synced to the right place in the VM.  However, you do need to get the VM up and going before working. 

The first thing we need to do is pull down the base box image to your machine.  This is a VM image that vagrant can use in order to make VMs from.

    vagrant box add base http://files.vagrantup.com/precise64.box

Now we can start the VM and open the dev console. On Windows simply double-click **run_vagrant.bat**. On Mac/Linux:

    ./run_vagrant.sh
    

This will take about a minute and a half depending on your machine and network connection.  This creates the VM and installs everything needed in order to get it in a state that lets it run our code.

At this point, the VM should be up and running.  It already has a private network connection to your machine. You can see our application in a browser by going to `http://10.13.37.2`
The dev console will begin spitting out information related to the requests coming in.

If you edit the source code on the host machine, you can reload the webpage and see your changes.  

## Problems?

This is simply written from memory.  When (not if) you run into problems, let Michael know and he will update the README.
