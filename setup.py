# -*- coding: utf-8 -*-
"""
This module contains the tool of senaite.labmedik
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('README.rst')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('senaite', 'labmedik', 'README.rst')
    + '\n' +
    read('senaite', 'labmedik', 'browser', 'images', 'README.rst')
    + '\n' +
    read('senaite', 'labmedik', 'browser', 'javascripts', 'README.rst')
    + '\n' +
    read('senaite', 'labmedik', 'browser', 'stylesheets', 'README.rst')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.rst')
    + '\n' +
    'Download\n'
    '********\n')

tests_require = ['zope.testing']

setup(name='senaite.labmedik',
      version=version,
      description="SENAITE LIMS extension for LabMedik Solution",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='lims lis senaite opensource health labmedik',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/collective/senaite.labmedik',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['senaite', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='senaite.labmedik.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
