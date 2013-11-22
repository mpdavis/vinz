.. _development-environment:

Development Environment
=======================

Let's get everything set up.

Prerequisites
-------------

You need to take care of a couple of things before getting started.

* Install Vagrant_
* Install VirutalBox_
* Install Git_
* Setup GitHub_

Checking out the code
---------------------

We need to check out the code and get it on your machine locally.  Make sure you keep track of where you check out the code so that you can make changes to it.

Windows
-------

If you are on Windows, I would recommend [GitHub for Windows](http://windows.github.com/)

OS X
----
::

    git clone git@github.com:mpdavis/vinz.git

Starting VM
-----------

Our dev environment takes place inside of a VM thanks to Vagrant.  You don't have to pay much attention to this, because the code on your system is automatically synced to the right place in the VM.  However, you do need to get the VM up and going before working. 

The first thing we need to do is pull down the base box image to your machine.  This is a VM image that vagrant can use in order to make VMs from.::

    vagrant box add base http://files.vagrantup.com/precise64.box

Windows
-------

On Windows, simply double-click `run_vagrant.bat`

This will take about a minute and a half depending on your machine and network connection.  This creates the VM and installs everything needed in order to get it in a state that lets it run our code.

OS X
----
::

    .run_vagrant.sh

Developing on Vinz
------------------

At this point, the VM should be up and running.  It already has a private network connection to your machine. You can see our application in a browser by going to `http://10.13.37.2`
The dev console will begin spitting out information related to the requests coming in.

If you edit the source code on the host machine, you can reload the webpage and see your changes.

Problems?
---------

This is simply written from memory.  When (not if) you run into problems, let Michael know and he will update the README.


.. _Vagrant: http://vagrantup.com
.. _VirutalBox: https://www.virtualbox.org/wiki/Downloads
.. _Git: http://git-scm.com/downloads
.. _GitHub: https://help.github.com/articles/set-up-git