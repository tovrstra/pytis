#!/usr/bin/env python

from distutils.core import setup

setup(
    name='PyTIS',
    version='0.0-git',
    description='PyTIS is a Python implementation of transition interface sampling.',
    author='Titus van Erp, Toon Verstraelen',
    author_email='Titus.VanErp@KULeuven.be, Toon.Verstraelen@UGent.be',
    url='',
    package_dir = {'pytis': 'pytis'},
    packages = ['pytis'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        #'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
)
