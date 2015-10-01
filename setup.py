# Copyright (C) 2015 Okami, okami@fuzetsu.info

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

data = {
    'name': 'django-rrd',
    'version': '0.0.1',
    'author': 'Okami',
    'author_email': 'okami@fuzetsu.info',
    'description': 'Web frontend to RRDtool based on Django'
    'license': 'GPLv3',
    'keywords': 'django rrd rrdtool',
    'url': 'https://github.com/okami-1/django-rrd',
    'packages': [
        'django-rrd',
        'django-rrd.migrations',
        'django-rrd.management',
        'django-rrd.management.commands',
    ],
    'long_description': '',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Framework :: Django',
    ],
    'install_requires': [
        'Django >= 1.7',
        'python-rrdtool >= 1.4.7',
    ],
}

setup(**data)
