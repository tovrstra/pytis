.. _ensembles:

Working with Ensembles
======================

Ensembles in PyTIS are currently limited to modifications of the state between
two MD simulations executed by a wrapper. It is assumed that the short MD
simulations are carried out in the NVE ensemble.


The NVE ensemble
~~~~~~~~~~~~~~~~

Reference documentation: :class:`NVE`

This ensemble never makes any changes to the state object. It is created as
follows::

    ensemble = NVE()


The Andersen thermostat
~~~~~~~~~~~~~~~~~~~~~~~

Reference documentation: :class:`NVTAndersen`

The Andersen thermostat resets the current atomic velocities with a given
probability per unit of time. The new velocities are samples from the
Maxwell-Boltzmann distribution. The ensemble is created as follows::

    ensemble = NVTAndersen(300, 0.01)

The first argument is the temperature. The second argument is the probability
that the velocities are updated before the wrapper is called.


Creating new ensembles
~~~~~~~~~~~~~~~~~~~~~~

One can easily create new ensemble classes. An ensemble class must have an
update method that has a state object as argument and returns either the same or
a new modified state object.
