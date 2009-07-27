#!/usr/bin/env python2.5
#
# Copyright (c) 2008 Daniel Truemper truemped@googlemail.com
#
# setup.py 27-Jul-2009
#
# All programs in this directory and
# subdirectories are published under the GNU General Public License as
# described below.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#
# Further information about the GNU GPL is available at:
# http://www.gnu.org/copyleft/gpl.html
#
#

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys

setup(
    name = 'loghouse',
    version = '0.1.0',

    description = 'LogHouse for Apache log file analysis using CouchDB',
    long_description = \
"""A simple django application based on CouchDB for analysis Apache log files.
""",
    author = 'Daniel Truemper',
    author_email = 'truemped@googlemail.com',
    license = 'GPL2',
    url = 'http://github.com/truemped/apache_loghouse/tree/master',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
        
    zip_safe = False,

    install_requires = [
        'couchdbkit>=0.1.8',
        'httpagentparser>=0.7'
    ],
    
    scripts = ['scripts/loader.py', ],

    test_suite='tests',

)
