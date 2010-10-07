#!/usr/bin/env python
# PyTIS is a Python implementation of transition interface sampling.
# Copyright (C) 2010 Titus Van Erp <Titus.VanErp@biw.kuleuven.be>,
# Toon Verstraelen <Toon.Verstraelen@UGent.be>
#
# This file is part of PyTIS.
#
# PyTIS is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# PyTIS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --

from distutils.core import setup

setup(
    name='PyTIS',
    version='0.0-git',
    description='PyTIS is a Python implementation of transition interface sampling.',
    author='Titus van Erp, Toon Verstraelen',
    author_email='Titus.VanErp@biw.kuleuven.be, Toon.Verstraelen@UGent.be',
    url='',
    package_dir = {'pytis': 'pytis'},
    packages = ['pytis'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License version 3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
)
