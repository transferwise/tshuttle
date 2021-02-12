tshuttle: where transparent proxy meets VPN meets ssh
=====================================================

As far as I know, tshuttle is the only program that solves the following
common case:

- Your client machine (or router) is Linux, FreeBSD, or MacOS.

- You have access to a remote network via teleport.

- You don't want to create an ssh port forward for every
  single host/port on the remote network.

## NOTE THAT THIS IS A FORK OF SSHUTTLE TO ENABLE IT TO WORK WITH TELEPORT. WE ARE RENAMING IT TO TSHUTTLE
the "real" repo is here: https://github.com/sshuttle/sshuttle

Obtaining sshuttle
------------------

- Homebrew::

      brew install transferwise/private/tshuttle

It is possible to install into a virtualenv as a non-root user.

- Clone::

      virtualenv -p python3 /tmp/tshuttle
      . /tmp/sshuttle/bin/activate
      git clone git@github.com:transferwise/tshuttle.git
      cd sshuttle
      ./setup.py install

- Homebrew::

      brew install sshuttle


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
