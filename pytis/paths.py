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


import numpy, os

from molmod.io import XYZWriter
from molmod import Molecule

from pytis.ensembles import set_boltzmann_velocities


__all__ = ["System", "State", "Path"]


class State(object):
    def __init__(self, pos, vel, dirname=None):
        self.pos = pos
        self.vel = vel
        self.dirname = dirname
        # a few sanity checks
        if self.pos.shape[1] != 3:
            raise TypeError("The array with atom positions must have three columns.")
        if self.vel.shape != self.pos.shape:
            raise TypeError("The arrays with positions and velocities must have the same shape.")


class System(object):
    @classmethod
    def from_xyz(self, fn_xyz, temp, masses=None):
        molecule = Molecule.from_file(fn_xyz)
        if masses is None:
            molecule.set_default_masses()
        else:
            molecule.masses = masses
        vel = numpy.zeros(molecule.coordinates.shape, float)
        set_boltzmann_velocities(temp, molecule.masses, vel)
        return System(molecule.coordinates, vel, molecule.symbols, molecule.masses, molecule.numbers)

    size = property(lambda self: len(self.symbols))

    def __init__(self, pos, vel, symbols, masses, numbers=None, dirname=None):
        self.state = State(pos, vel, dirname)
        self.symbols = symbols
        self.masses = masses
        self.numbers = numbers
        # a few sanity checks
        if len(self.masses) != self.size:
            raise TypeError("The number of masses and symbols must be the same.")
        if self.numbers is not None and len(self.numbers) != self.size:
            raise TypeError("The number of atom numbers and symbols must be the same.")
        if len(self.state.pos) != self.size:
            raise TypeError("The number of symbols and coordinates must be the same.")


class Path(object):
    def __init__(self, system, wrapper, ensemble, dirname):
        self.system = system
        self.wrapper = wrapper
        self.ensemble = ensemble
        self.dirname = dirname
        #
        if os.path.isdir(self.dirname):
            raise IOError("The directory %s already exists." % dirname)
        os.mkdir(self.dirname)
        self.frames = [self.system.state]


    def run(self, num_iter):
        current = self.frames[-1]
        for i in xrange(num_iter):
            self.ensemble.update(self.system, current)
            dirname = os.path.join(self.dirname, "frame%07i" % len(self.frames))
            current = self.wrapper.move(self.system, current, dirname)
            self.frames.append(current)

    def write_to_xyz(self, fn_xyz):
        w = XYZWriter(fn_xyz, self.system.symbols)
        for i, frame in enumerate(self.frames):
            w.dump("Frame %i" % i, frame.pos)
