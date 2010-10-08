PyTIS examples
==============

A Simple Andersen NVT simulation on top of CPMD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Location: ``examples/000_andersen_h2o``

This example demonstrates the basic usage of the ``CPMDWrapper`` and how one
works with ``Path`` objects to run and Andersen NVT molecular dynamics
simulation, using conventional NVE Born-Oppenheimer MD simulations in CPMD.

The PyTIS script: ``examples/000_andersen_h2o/md.py``

.. literalinclude:: ../examples/000_andersen_h2o/md.py
   :lines: 24-
   :linenos:

The meaning of each line is explained below:

    **Line 1** -- Import everything from the PyTIS library.

    **Line 3** -- Define the CPMD wrapper. One must specify a binary, a template
    file and a list of other files needed in the input directory. (See
    :ref:`cpmd_wrapper` for more details.)

    **Line 4** -- Define the NVT Andersen ensemble at a temperature of 300K and
    an update probability of 1%.

    **Line 5** -- Create a system and an initial state from a simple XYZ file
    and a temperature for the initial velocities.

    **Line 6** -- Create a path object. It needs a definition of the system and
    the initial state. It needs a wrapper to perform moves through the phase
    space, and an ensemble.

    **Line 7** -- Add two moves to the path, starting from the initial state.
    All states, including the initial state, are stored in ``path.frames``.

    **Line 8** -- Write an XYZ trajectory file.
