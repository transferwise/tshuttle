tshuttle: where transparent proxy meets VPN meets ssh
=====================================================

tshuttle is the only program that solves the following
common case:

- Your client machine (or router) is Linux, FreeBSD, or MacOS.

- You have access to a remote network via teleport.

- You don't want to create an ssh port forward for every
  single host/port on the remote network.

**Note that this is a fork of sshuttle to enable it to work with teleport. we are renaming it to tshuttle.
The real repo is here: https://github.com/sshuttle/sshuttle**

Obtaining tshuttle
------------------

Simplest way is to just install using pip:
- pip3::

      git clone git@github.com:transferwise/tshuttle.git
      cd tshuttle
      pip3 install .

It is possible to install into a virtualenv as a non-root user.

- Clone::

      virtualenv -p python3 /tmp/tshuttle
      . /tmp/tshuttle/bin/activate
      git clone git@github.com:transferwise/tshuttle.git
      cd tshuttle
      ./setup.py install

Using tshuttle with Teleport
----------------------------

Example to connect to 192.168.0.0/24 using Teleport JumpHost 1.2.3.4

::
   tshuttle   -e 'tsh ssh'    -r joe.bloggs@1.2.3.4 192.168.0.0/24
   < in a new terminal >
   ssh 192.1689.0.10 # some host in the destination subnet


Documentation
-------------
The documentation for the stable version is available at:
https://sshuttle.readthedocs.org/

The documentation for the latest development version is available at:
https://sshuttle.readthedocs.org/en/latest/


Running as a service
--------------------
Sshuttle can also be run as a service and configured using a config management system: 
https://medium.com/@mike.reider/using-sshuttle-as-a-service-bec2684a65fe
