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
"""Wrappers around programs that make moves through the phase space."""


import os, shutil, string, numpy

from molmod import amu

from pytis.paths import State
from pytis.ensembles import get_temperature


__all__ = ["CPMDWrapper"]


class CPMDWrapper(object):
    """A wrapper that uses CPMD program to move trough the phase space."""
    def __init__(self, binary, fn_template, fns_other):
        """
           Arguments:
            | ``binary`` -- The CPMD binary.
            | ``fn_template`` -- A template for the CPMD input.
            | ``fns_other`` -- A list of files that must also be present in
                               the directory where the move is computed, e.g.
                               pseudopotential files.
        """
        self.binary = binary
        f = open(fn_template)
        self.template = string.Template(f.read())
        f.close()
        self.fns_other = fns_other

    def move(self, system, init_state, dirname):
        """Perform a move trough the phase space.

           Arguments:
            | ``system`` -- A ``System`` instance.
            | ``init_state`` -- A state object with the initial state to put
                                into CPMD.
            | ``dirname`` -- The directory where the CPMD job has to be carried
                             out.
        """
        self.create_input(system, init_state, dirname)
        self.run_cpmd(dirname, "slice")
        return self.get_final_state(system, dirname)

    def create_input(self, system, init_state, dirname):
        """Create an input file for CPMD.

           Arguments:
            | ``system`` -- A ``System`` instance.
            | ``init_state`` -- A state object with the initial state to put
                                into CPMD.
            | ``dirname`` -- The directory where the CPMD job has to be carried
                             out.
        """
        # check the atom order, symbols should be in alphabetical order
        for s1, s2 in zip(system.symbols, sorted(system.symbols)):
            if s1 != s2:
                raise ValueError("Symbols should be in alphabetical order.")
        # prepare environment
        if os.path.isdir(dirname):
            raise IOError("Directory %s already exists." % dirname)
        os.mkdir(dirname)
        for fn_other in self.fns_other:
            shutil.copy(fn_other, dirname)
        if init_state.dirname is not None:
            shutil.copy(
                os.path.join(init_state.dirname, "RESTART.1"),
                os.path.join(dirname, "RESTART")
            )
        # prepare text fragments that will be substituted in template
        subs = {}
        ## restart
        if init_state.dirname is not None:
            subs["restart"] = "  RESTART WAVEFUNCTION"
        else:
            subs["restart"] = ""
        ## positions
        pos_lines = {}
        for i in xrange(system.size):
            l = pos_lines.setdefault(system.symbols[i], [])
            l.append("    %.7f %.7f %.7f" % tuple(init_state.pos[i]))
        for symbol, lines in pos_lines.iteritems():
            lines.insert(0, "  %i" % len(lines))
            key = "%s_atoms" % (symbol.lower())
            subs[key] = "\n".join(lines)
        ## velocities
        vel_lines = [("  %i " % len(init_state.vel)) + " ".join(str(i+1) for i in xrange(system.size))]
        for row in init_state.vel:
            vel_lines.append("    %.7f %.7f %.7f" % tuple(row))
        subs["velocities"] = "\n".join(vel_lines)
        ## masses (isotopes)
        massmap = {}
        for i in xrange(system.size):
            mass = massmap.setdefault(system.symbols[i], system.masses[i])
            if mass != system.masses[i]:
                raise ValueError("Atoms with the same symbol must have the same mass.")
        mass_lines = []
        for symbol, mass in sorted(massmap.iteritems()):
            mass_lines.append("    %.7f" % (mass/amu))
        subs["isotopes"] = "\n".join(mass_lines)
        ## temperature
        subs["temp"] = "  %.7f" % (get_temperature(system, init_state))
        # write input file
        f = open(os.path.join(dirname, "slice.inp"), "w")
        f.write(self.template.substitute(subs))
        f.close()

    def run_cpmd(self, dirname, prefix):
        """Execute the CPMD binary on in input file with the given prefix.

           Arguments:
            | ``dirname`` -- The directory with the input.
            | ``prefix`` -- The prefix for the input (.inp) and output (.out)
        """
        # run cpmd, very simple for now
        os.system("cd %s; %s %s.inp > %s.out" % (dirname, self.binary, prefix, prefix))
        # get back the final pos and vel

    def get_final_state(self, system, dirname):
        """Get the last state from the CPMD output

           Arguments:
            | ``system`` -- A ``System`` instance.
            | ``dirname`` -- The directory where the CPMD job has to be carried
                             out.
        """
        # read the final positions and velocities from the file TRAJECTORY.
        f = file(os.path.join(dirname, "TRAJECTORY"), "r")
        ## read the last time step
        last_lines = []
        last_index = 0
        for line in f:
            words = line.split()
            index = int(words[0])
            if index != last_index:
                last_lines = []
                last_index = index
            last_lines.append(words[1:])
        f.close()
        ## convert it to numpy arrays
        if len(last_lines) != system.size:
            raise IOError("Could not read the correct number of atoms from the last time step.")
        final_pos = numpy.zeros((system.size, 3), float)
        final_vel = numpy.zeros((system.size, 3), float)
        for i in xrange(system.size):
            final_pos[i][0] = float(last_lines[i][0])
            final_pos[i][1] = float(last_lines[i][1])
            final_pos[i][2] = float(last_lines[i][2])
            final_vel[i][0] = float(last_lines[i][3])
            final_vel[i][1] = float(last_lines[i][4])
            final_vel[i][2] = float(last_lines[i][5])
        return State(final_pos, final_vel, dirname)
