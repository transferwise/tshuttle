Usage
=====

.. note::

    For information on usage with Windows, see the :doc:`windows` section.
    For information on using the TProxy method, see the :doc:`tproxy` section.

Forward all traffic::

    tshuttle -r username@sshserver 0.0.0.0/0

- Use the :option:`tshuttle -r` parameter to specify a remote server.

- By default tshuttle will automatically choose a method to use. Override with
  the :option:`tshuttle --method` parameter.

- There is a shortcut for 0.0.0.0/0 for those that value
  their wrists::

      tshuttle -r username@sshserver 0/0


- For 'My VPN broke and need a temporary solution FAST to access local IPv4 addresses'::

      tshuttle --dns -NHr username@sshserver 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16

If you would also like your DNS queries to be proxied
through the DNS server of the server you are connect to::

  tshuttle --dns -r username@sshserver 0/0

The above is probably what you want to use to prevent
local network attacks such as Firesheep and friends.
See the documentation for the :option:`tshuttle --dns` parameter.

(You may be prompted for one or more passwords; first, the local password to
become root using sudo, and then the remote ssh password.  Or you might have
sudo and ssh set up to not require passwords, in which case you won't be
prompted at all.)


Usage Notes
-----------
That's it!  Now your local machine can access the remote network as if you
were right there.  And if your "client" machine is a router, everyone on
your local network can make connections to your remote network.

You don't need to install tshuttle on the remote server;
the remote server just needs to have python available. 
tshuttle will automatically upload and run its source code
to the remote python interpreter.

This creates a transparent proxy server on your local machine for all IP
addresses that match 0.0.0.0/0.  (You can use more specific IP addresses if
you want; use any number of IP addresses or subnets to change which
addresses get proxied.  Using 0.0.0.0/0 proxies *everything*, which is
interesting if you don't trust the people on your local network.)

Any TCP session you initiate to one of the proxied IP addresses will be
captured by tshuttle and sent over an ssh session to the remote copy of
tshuttle, which will then regenerate the connection on that end, and funnel
the data back and forth through ssh.

Fun, right?  A poor man's instant VPN, and you don't even have to have
admin access on the server.

Sudoers File
------------
tshuttle can auto-generate the proper sudoers.d file using the current user 
for Linux and OSX. Doing this will allow tshuttle to run without asking for
the local sudo password and to give users who do not have sudo access
ability to run tshuttle::

  tshuttle --sudoers

DO NOT run this command with sudo, it will ask for your sudo password when
it is needed.

A costume user or group can be set with the :
option:`tshuttle --sudoers --sudoers-username {user_descriptor}` option. Valid
values for this vary based on how your system is configured. Values such as 
usernames, groups pre-pended with `%` and sudoers user aliases will work. See
the sudoers manual for more information on valid user specif actions.
The options must be used with `--sudoers`::

  tshuttle --sudoers --sudoers-user mike
  tshuttle --sudoers --sudoers-user %sudo

The name of the file to be added to sudoers.d can be configured as well. This
is mostly not necessary but can be useful for giving more than one user
access to tshuttle. The default is `tshuttle_auto`::

  tshuttle --sudoer --sudoers-filename tshuttle_auto_mike
  tshuttle --sudoer --sudoers-filename tshuttle_auto_tommy

You can also see what configuration will be added to your system without
modifying anything. This can be helpfull is the auto feature does not work, or
you want more control. This option also works with `--sudoers-username`.
`--sudoers-filename` has no effect with this option::

  tshuttle --sudoers-no-modify

This will simply sprint the generated configuration to STDOUT. Example::

  08:40 PM william$ tshuttle --sudoers-no-modify

  Cmnd_Alias SSHUTTLE304 = /usr/bin/env PYTHONPATH=/usr/local/lib/python2.7/dist-packages/tshuttle-0.78.5.dev30+gba5e6b5.d20180909-py2.7.egg /usr/bin/python /usr/local/bin/tshuttle --method auto --firewall

  william ALL=NOPASSWD: SSHUTTLE304
