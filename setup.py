# -*- coding: utf-8 -*-
"""
This module contains the tool of senaite.labmedikdemos
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
    read('senaite', 'labmedikdemos', 'README.rst')
    + '\n' +
    read('senaite', 'labmedikdemos', 'browser', 'images', 'README.rst')
    + '\n' +
    read('senaite', 'labmedikdemos', 'browser', 'javascripts', 'README.rst')
    + '\n' +
    read('senaite', 'labmedikdemos', 'browser', 'stylesheets', 'README.rst')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.rst')
    + '\n' +
    'Download\n'
    '********\n')

tests_require = ['zope.testing']

setup(name='senaite.labmedikdemos',
      version=version,
      description="Custom demostration extension that adapts SENAITE LIMS for LabMedik Solution.",
      long_description=long_description,
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
      keywords='lims lis senaite opensource health labmedik plone4 zope2',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/macagua/senaite.labmedikdemos',
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
      test_suite='senaite.labmedikdemos.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
