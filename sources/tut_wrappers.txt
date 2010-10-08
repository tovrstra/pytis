.. _wrappers:

Working with Wrappers
=====================


.. _cpmd_wrapper:

The CPMD wrapper
~~~~~~~~~~~~~~~~

Reference documentation :class:`pytis.wrappers.CPMDWrapper`

The ``CPMDWrapper`` can be used to run Car-Parrinello or Born-Oppenheimer MD
simulations to move through the phase space. The constructor requires three
arguments:

    ``binary``
        A string with the CPMD binary. If the binary is in the system path, one
        does not have to specify the full path. The examples (in the
        ``examples`` directory assume that a single-cpu binary ``cpmd.x``
        resides in the system path. One may also refer to a script that contains
        the parameters for a parallel run.

    ``fn_template``
        The file containing the template for the input of the MD simulation. The
        following keywords must be present in the template file:

        * ``${restart}`` in the ``CPMD`` section of the input file
        * ``${temp}`` right on the line after the ``TEMPERATURE`` keyword in the
          ``CPMD`` section. This is also required in the case of NVE
          simulations.
        * ``${x_atoms}`` where x is some element or atom type in the ``ATOMS``
          section.
        * ``${velocities}`` on the line between ``VELOCITIES`` and ``END
          VELOCITIES`` in the ``ATOMS`` section.
        * ``${isotopes}`` after the ``ISOTOPES`` line in the ``ATOMS`` section.

        The following template file is used in the example ``000_andersen_h2o``:

        .. literalinclude:: ../examples/000_andersen_h2o/water.cpmd.inp

    ``fns_other``
        The filenames of other files that must be included in the directory
        where a CMPD simulation is executed, e.g. pseudopotential files.

It is mandatory for the CPMD wrapper that the atom symbols in the system are
in alphabetical order, and that the same order is used in the specification of
the pseudopotentials.


Creating new wrappers
~~~~~~~~~~~~~~~~~~~~~

One can create new wrapper classes that can be used instead of the CPMD wrapper.
Wrappers must have a ``move`` method that takes the following arguments:

* ``system``: an instance of the ``System`` class
* ``init_state``: an instance of the ``State`` class. It is the initial state of
  the system that used as the starting point of a short simulation.
* ``dirname``: a directory where the input, output and restart files are
  stored.

The function must return a new ``State`` object with the final positions and
velocities of the short MD simulation.
