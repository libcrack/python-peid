#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: borja@libcrack.so
# Date: Mon Oct 19 20:21:53 CEST 2015

import re
import os

from setuptools import find_packages, setup


def read(relpath):
    '''
    Return string containing the contents of the file at *relpath* relative to
    this file.
    '''
    cwd = os.path.dirname(__file__)
    abspath = os.path.join(cwd, os.path.normpath(relpath))
    with open(abspath) as f:
        return f.read()

NAME = 'peid'
VERSION = re.search('__version__ = "(.+?)"', read('peid.py')).group(1)
DESCRIPTION = 'PEiD like python script.'
KEYWORDS = 'packer malware peid'
AUTHOR = 'Borja Ruiz'
AUTHOR_EMAIL = 'borja@libcrack.so'
URL = 'https://www.github.com/borjiviri/peid'
LICENSE = read('LICENSE')
PACKAGES = [NAME]
PACKAGE_DATA = {NAME: ['data/*'],}
PACKAGE_DIR = {NAME: '.'}
INSTALL_REQUIRES = [x.replace('-','_') for x in
        read('requirements.txt').split('\n') if x != '']
LONG_DESC = read('README.md') + '\n\n'
PLATFORMS = ['Linux']
PROVIDES = [NAME]
CLASSIFIERS = [
    'Development Status :: 3 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: Other/Propietary License',
    'Operating System :: OS Independent',
    'Operating System :: POSIX :: Linux',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
]

PARAMS = {
    'platforms': PLATFORMS,
    'name': NAME,
    'version': VERSION,
    'description': DESCRIPTION,
    'keywords': KEYWORDS,
    'long_description': LONG_DESC,
    'author': AUTHOR,
    'author_email': AUTHOR_EMAIL,
    'url': URL,
    'license': LICENSE,
    'packages': PACKAGES,
    'package_dir': PACKAGE_DIR,
    'package_data': PACKAGE_DATA,
    'provides': PROVIDES,
    'requires': INSTALL_REQUIRES,
    'install_requires': INSTALL_REQUIRES,
    'classifiers': CLASSIFIERS,
}

setup(**PARAMS)

# vim:ts=4 sts=4 tw=79 expandtab:
