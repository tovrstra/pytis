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


import numpy

from molmod import boltzmann


__all__ = ["get_temperature", "set_boltzmann_velocities", "NVTAndersen"]


def get_temperature(system, state):
    kinetic = 0.5*((state.vel**2).sum(axis=1)*system.masses).mean()
    return kinetic/boltzmann


def set_boltzmann_velocities(temp, masses, vel):
    for i, m in enumerate(masses):
        vel[i] = numpy.random.normal(0, numpy.sqrt(2*boltzmann*temp/m), 3)


class NVTAndersen(object):
    def __init__(self, temp, rate):
        self.temp = temp
        self.rate = rate

    def update(self, system, state):
        if numpy.random.uniform(0, 1) < self.rate:
            # Reset all velocities
            set_boltzmann_velocities(self.temp, system.masses, state.vel)
