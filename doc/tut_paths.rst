.. _paths:

Working with Systems, States and Paths
======================================

Systems
~~~~~~~

Reference documentation :class:`pytis.paths.System`

A ``System`` object contains all the time-independent information of a molecular
system. One must construct system object for the preparation of simulations with
PyTIS. ``System`` objects have the following attributes, which are also
arguments to the constructor:

* Mandatory:
    * ``symbols`` -- A list of symbols for the atoms.
    * ``masses`` -- A numpy array corresponding masses of the atoms in atomic
      units.

* Optional:
    * ``numbers`` -- A numpy array with atom numbers.

States
~~~~~~

Reference documentation :class:`pytis.paths.State`

A ``State`` object contains all the time-dependent information of a system at
a certain time step. The following attributes are also the arguments of the
constructor.

* Mandatory:
    * ``pos`` -- A numpy array with N rows and 3 columns containing all the
      Cartesian positions of the atoms.
    * ``vel`` -- A numpy array with N rows and 3 columns containing all the
      Cartesian velocities of the atoms.

* Optional:
    * ``dirname`` -- A directory containing the computation that leads to this
      state.



Setting up a system and an initial state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference documentation :func:`pytis.paths.load_xyz`

The function ``load_xyz`` is a convenient way to construct a system and an
initial state based on a conventional XYZ file. It is used as follows::

    system, init_state = load_xyz("start.xyz", temp=300)


Paths
~~~~~

Reference documentation :class:`pytis.paths.Path`

A ``Path`` object keeps track of subsequent states of a system at regular time
steps. One creates a Path object as follows::

    path = Path(system, init_state, wrapper, ensemble, dirname)

The ``system`` and ``init_state`` object have to be created as discussed above.
The three other arguments have the following meaning.

* ``wrapper`` -- A Wrapper object that knows how to run short MD or MC
  simulations using an external program. A wrapper has a fixed API, independent
  of the underlying program. Wrappers are discussed in the chapter
  :ref:`wrappers`.

* ``ensemble`` -- An ensemble at the PyTIS level. These are discussed in the
  chapter :ref:`ensembles`. The Path object calls the ``update`` method of the
  ensemble object to modify the state prior to running

* ``dirname`` -- A directory in which a subdirectory will be created for every
  MD simulation performed by the wrapper. It may not exist yet when the Path
  object is created.
