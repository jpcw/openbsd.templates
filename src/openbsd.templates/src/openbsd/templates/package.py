#/usr/bin/env/python
#
from paste.script.templates import var
from base import MyTemplate, getdefaults


class OpenbsdCarpIfaceTemplate(MyTemplate):
    """."""
    _template_dir = 'tmpl/carp/iface'
    defaults = getdefaults('iface')
    summary = "An Openbsd carp interface."

    vars = MyTemplate.vars + \
           [var('desc', 'description (max 48 bytes)',
                default=defaults['desc']),
            var('vhid', 'Virtual Hostname ID', default=''),
            var('carp_group', 'Add this iface to another carpgroup',
                 default=defaults['carp_group']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'carpdev' in vars.keys():
            vars['carpdev'] = self.defaults['carpdev']
        if not 'advskew' in vars.keys():
            vars['advskew'] = self.defaults['advskew']
        if not 'password' in vars.keys():
            vars['password'] = self.defaults['password']
        self.boolify(vars)
        self.compute_net(vars)


class OpenbsdCarpVlanTemplate(OpenbsdCarpIfaceTemplate):
    """."""
    _template_dir = 'tmpl/carp/vlan'
    defaults = getdefaults('iface')
    summary = "An Openbsd vlan carp interface."

    vars = OpenbsdCarpIfaceTemplate.vars + \
           [var('vlandev', 'Physical interface',
                default=defaults['vlandev']),
           ]


# vim:set et sts=4 ts=4 tw=80:
