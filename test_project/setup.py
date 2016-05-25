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

from setuptools import setup


setup(**{
    'name': 'django-rrd',
    'version': '0.0.10',
    'author': 'Okami',
    'author_email': 'okami@fuzetsu.info',
    'description': 'Web frontend to RRDtool based on Django',
    'license': 'GPLv3',
    'keywords': 'django rrd rrdtool',
    'url': 'https://sourceforge.net/p/django-rrd/wiki/',
    'packages': [
        'djangorrd',
        'djangorrd.migrations',
        'djangorrd.management',
        'djangorrd.management.commands',
        'djangorrd.tests',
    ],
    'long_description': '',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Framework :: Django',
    ],
    'install_requires': [
        'Django >= 1.9.2',
        'python-rrdtool >= 1.4.7',
    ],
})
