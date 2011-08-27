from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='openbsd.templates',
      version=version,
      description="Templates to deploy a Openbsd project",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords="pastescript templates to deploy Openbsd's project",
      author='Jean-Philippe Camguilhem',
      author_email='jpc_at_makina-corpus.com',
      url='https://github.com/jpcw/openbsd.templates',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['openbsd'],
      include_package_data=True,
      data_files = [('etc', ['src/templates/etc/defaults.cfg'])],
      zip_safe=False,
      install_requires=['setuptools', 'PasteScript', 'Cheetah'],
      entry_points=""" # -*- Entry points: -*-
      [paste.paster_create_template]
      openbsd_carp_iface = openbsd.templates.package:OpenbsdCarpIfaceTemplate
      openbsd_carp_vlan = openbsd.templates.package:OpenbsdCarpVlanTemplate
      """,
      )
