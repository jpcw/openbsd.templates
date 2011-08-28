########################
openbsd.templates
########################

PasteScript templates to generate OpenBSD configuration's files.

This project uses Python tools to automate some tasks and produce some configuration's file

Interfaces
===============

    * carped interface
    * carped vlan interface 

How to play with me
======================

 :: 
    
    python bootstrap.py -d
    bin/buildout

Now you have new entries in bin/ ::
    
    bin/paster create --list-templates
    (thd)athena:OPENBSD jpcw$ bin/paster create --list-templates
    Available templates:
      ...
      openbsd_carp_iface:  An Openbsd carp interface.
      openbsd_carp_vlan:   An Openbsd vlan carp interface.
      ...


We can now play with templates ::
    
    (thd)athena:OPENBSD jpcw$ bin/paster create -t openbsd_carp_iface foo
    Selected and implied templates:
      openbsd.templates#openbsd_carp_iface  An Openbsd carp interface.

    Variables:
      egg:      foo
      package:  foo
      project:  foo
    Enter cidr_ip (A CIDR IP address : 192.168.0.1/24) ['']: 192.168.1.15/24
    Enter desc (description (max 48 bytes)) ['a default description']: Lan interface
    Enter vhid (Virtual Hostname ID) ['']: 1
    Enter carp_group (Add this iface to another carpgroup) ['']: 
    Creating template openbsd_carp_iface
    Creating directory ./foo
      Recursing into master
        Creating ./foo/master/
        Copying hostname.carp+vhid+_tmpl to ./foo/master/hostname.carp1
      Recursing into slave
        Creating ./foo/slave/
        Copying hostname.carp+vhid+_tmpl to ./foo/slave/hostname.carp1
    

Let we check::
    
    (thd)athena:OPENBSD jpcw$ cat foo/master/hostname.carp1 
    inet 192.168.1.15 255.255.255.0 192.168.1.255 vhid 1 carpdev em1 pass secure description "Lan interface"
    (thd)athena:OPENBSD jpcw$ cat foo/slave/hostname.carp1 
    inet 192.168.1.15 255.255.255.0 192.168.1.255 vhid 1 carpdev em1 advskew 100 pass secure description "Lan interface"


templates are intercative for a minimum variables, others came from default values in src/openbsd/templates/etc/defaults.cfg

but you could set thems like this ::
    
     bin/paster create -t openbsd_carp_iface foo advskew=80

Availables vars are :

+ iface

 + cidr_ip
 + vhid
 + desc
 + carp_group
 + advskew
 + password

+ vlan

 + sames as above
 + vlandev 

Please note that for carp vlan interface we assume you want the same id on vhid and vlan_id to be consistent

Then if you play with vhid = 8 the carpdev will be vlan8, and template will create hostname.vlan8

Enjoy
