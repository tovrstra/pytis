#!/usr/bin/env python
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


from pytis import *

wrapper = CPMDWrapper("cpmd.x", "water.cpmd.inp", ["../cpmd/H_VDB_LDA.psp", "../cpmd/O_VDB_LDA.psp"])
ensemble = NVTAndersen(300, 0.01)
system = System.from_xyz("init.xyz", 300)
path = Path(system, wrapper, ensemble, "single")
path.run(2)
path.write_to_xyz("trajectory.xyz")
