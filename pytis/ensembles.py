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
"""Collection of thermodynamic ensembles implemented at the PyTIS level."""


import numpy

from molmod import boltzmann


__all__ = ["get_temperature", "set_boltzmann_velocities", "NVTAndersen", "NVE"]


def get_temperature(system, state):
    """Return the instantaneous temperature for a given state of the system.

       Arguments:
        | ``system`` -- An object of the type ``System``.
        | ``state`` -- A corresponding ``State`` object.
    """
    kinetic = 0.5*((state.vel**2).sum(axis=1)*system.masses).mean()
    return kinetic/boltzmann


def set_boltzmann_velocities(temp, system, state):
    """Assign random velocities based on the Boltzmann distribution.

       Arguments:
        | ``temp`` -- The temperature in Kelvin.
        | ``system`` -- An object of the type ``System``.
        | ``state`` -- A corresponding ``State`` object.
    """
    for i, m in enumerate(system.masses):
        state.vel[i] = numpy.random.normal(0, numpy.sqrt(2*boltzmann*temp/m), 3)


class NVTAndersen(object):
    """The Andersen thermostat for the NVT ensemble."""
    def __init__(self, temp, rate):
        """
           Arguments:
            | ``temp`` -- The temperature in Kelvin.
            | ``rate`` -- The probability per unit of time slices that the
                          Andersen thermostat updates the velocities.
        """
        self.temp = temp
        self.rate = rate

    def update(self, system, state):
        """Update the velocities (with a certain probability)

           Arguments:
            | ``system`` -- An object of the type ``System``.
            | ``state`` -- A corresponding ``State`` object.

           This should be called before every time move.
        """
        if numpy.random.uniform(0, 1) < self.rate:
            # Reset all velocities
            set_boltzmann_velocities(self.temp, masses, state)


class NVE(object):
    """The NVE ensemble.

       This ensemble does not update velocities.
    """

    def update(self, system, state):
        """Stub that does nothing."""
        pass
