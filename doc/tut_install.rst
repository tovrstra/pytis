Installation
============


Preparing your Linux system
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some software packages should be installed before PyTIS can be installed or
used. It is recommended to use the software package management of your Linux
distribution to install these dependencies.

The following software must be installed for PyTIS:

* Python 2.5, 2.6 or 2.7 (including the header files): http://www.python.org/doc/
* Numpy 1.0 or later: http://numpy.scipy.org/
* A Fortran and a C compiler supported by the F2PY module in Numpy, e.g.
  gfortran and gcc: http://gcc.gnu.org/
* Git: http://git-scm.com/

Most Linux distributions can install this software with just a single command
on the command line by the administrator. They are listed below for several
popular Linux distributions:

* Ubuntu 10.4::

    sudo apt-get install python python-dev python-numpy gfortran gcc git-core

* Debian 5. You first have to become root because the sudo program is not
  configured by default. ::

    su -
    apt-get install python python-dev python-numpy gfortran gcc git-core
    exit

* Fedora 12 and 13. You first have to become root because the sudo program is
  not configured by default. ::

    su -
    pkcon install python-devel numpy numpy-f2py gcc-gfortran gcc git
    exit

* Suse 11.2::

    sudo zypper install python-devel python-numpy gcc gcc-fortran git

  There seems to be something odd going on with the default Python configuration
  on Suse installations. You have to edit the file
  ``/usr/lib64/python2.4/distutils/distutils.cfg`` or
  ``/usr/lib32/python2.4/distutils/distutils.cfg``, depending on the CPU
  architecture, to comment out the line ``prefix=/usr/local`` with a ``#``
  symbol. Otherwise it is impossible to install Python packages in the home
  directory, as we will do below.

In order to enable the installation and usage of Python packages in the home
directory, as we will do in the next section, one must configure a few
environment variables:

* Bash users: add the following two lines to your ``~/.bashrc`` file::

    export PYTHONPATH=$HOME/lib/python:$HOME/lib64/python:$PYTHONPATH
    export PATH=$HOME/bin:$PATH

* TC Shell users: add the lines to your ``~/.tcshrc`` file::

    setenv PYTHONPATH $HOME/lib/python:$HOME/lib64/python:$PYTHONPATH
    setenv PATH $HOME/bin:$PATH

If you don't know which shell you are using, you are probably using Bash. Note
that some of these lines may already be present. **These settings are only
loaded in new terminal sessions, so close your terminal and open a new one
before proceeding.**


Installing the bleeding edge version of PyTIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following series of commands will download the latest versions of the
MolMod package (required) and PyTIS, and will then install them into your
home directory. Make sure you execute these commands in some sort of temporary
directory. ::

    git clone git://molmod.ugent.be/git/molmod.git
    git clone git://github.com/tovrstra/pytis.git
    (cd molmod; ./setup.py install --home=~)
    (cd pytis; ./setup.py install --home=~)

You are now ready to start using PyTIS!

A few quick checks
~~~~~~~~~~~~~~~~~~

It may be interesting to double check your installation before proceeding,
unless you `feel lucky`. The PyTIS and MolMod files are installed in the
following directories:

* Modules: ``~/lib/python`` or ``~/lib64/python``
* Data: ``~/share``

There should be at least some files present in these directories.

The Python modules should be accessible from any Python session. This can be
checked by starting Python interactively and loading the modules manually. There
should be no errors when importing the modules::

    toon@poony ~> python
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import molmod
    >>> import pytis
    >>> quit()
    toon@poony ~>


Upgrading to the bleeding edge version of PyTIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you want to upgrade PyTIS to the latests development version after a
previous install, then execute the following commands (in the same directory)::

    (cd molmod; git pull; rm -r ~/lib*/python/molmod*; ./setup.py install --home=~)
    (cd pytis; git pull; rm -r ~/lib*/python/pytis*; ./setup.py install --home=~)


Testing your installation
~~~~~~~~~~~~~~~~~~~~~~~~~

For the development and testing one needs to install three additional packages:

 * Nosetests: http://somethingaboutorange.com/mrl/projects/nose/0.11.2/
 * Sphinx: http://sphinx.pocoo.org/

Most Linux distributions can install this software with just a single command on
the command line by the administrator. The other packages are installed as
follows:

* Ubuntu 10.4::

    sudo apt-get install python-nose python-sphinx

* Debian 5::

    su -
    apt-get install python-nose python-sphinx
    exit

* Fedora 12 and 13. You first have to become root because the sudo program is
  not configured by default. ::

    su -
    pkcon install python-nose sphinx
    exit

* Suse 11.2::

    sudo zypper install python-nose python-sphinx

    cd pytis
    ./setup.py build_ext -i
    nosetests -v

This will run a series of tests to check the validity of the outcomes generated
by PyTIS.
