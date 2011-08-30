#/usr/bin/env/python

import sys
import ConfigParser
import os.path
from paste.script.templates import Template, var
from IPy import IP

_dir, _f = os.path.split(os.path.abspath(__file__))
DEFAULT_CONFIG_FILE = os.path.join(_dir, 'etc', 'defaults.cfg')
BOOLEANS = ['False', 'True', '1', '0']


def getdefaults(section, cfg=DEFAULT_CONFIG_FILE):
    """Get default values for template vars."""
    Config = ConfigParser.ConfigParser()
    Config.read(cfg)
    options = Config.items(section)
    settings = dict(options)

    # sets real bool values in settings
    for option in options:
        if option[1] in BOOLEANS:
            settings[option[0]] = Config.getboolean(section, option[0])
    return settings


class BaseIface(Template):
    """Base interface template."""
    use_cheetah = True

    vars = [var('cidr_ip', 'A CIDR IP address : 192.168.0.1/24', default=''),
            ]

    def is_a_network_address(self, address):
        """Check if address is a network address."""
        try:
            net = IP(address)
            return True
        except:
            return False

    def compute_net(self, vars):
        """Compute net, netmask and broadcast."""
        if vars['cidr_ip'].count('/') != 1:
            print '%s is not a CIDR IP address :/' % vars['cidr_ip']
            sys.exit(True)
        else:
            vars['ip'], cidr_netmask = vars['cidr_ip'].split('/')
            if cidr_netmask != '32':
                if self.is_a_network_address(vars['cidr_ip']):
                    msg = "Need cofee? you provided "\
                          "a network address : %s" % vars['cidr_ip']
                    print msg
                    sys.exit(True)

            net = IP(vars['cidr_ip'], make_net=True)
            vars['netmask'] = net.netmask()
            vars['broadcast'] = str(net.broadcast())

            if cidr_netmask != '32':
                if vars['ip'] == vars['broadcast']:
                    msg = "Need cofee? you provided "\
                          "the broadcast address %s of your network %s/%s" \
                           % (vars['ip'], net.net(), cidr_netmask)
                    print msg
                    sys.exit(True)

# vim:set et sts=4 ts=4 tw=80:
