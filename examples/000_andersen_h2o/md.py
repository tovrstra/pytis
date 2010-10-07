#!/usr/bin/env python

from pytis import *

wrapper = CPMDWrapper("cpmd.x", "water.cpmd.inp", ["../cpmd/H_VDB_LDA.psp", "../cpmd/O_VDB_LDA.psp"])
ensemble = NVTAndersen(300, 0.01)
system = System.from_xyz("init.xyz", 300)
path = Path(system, wrapper, ensemble, "single")
path.run(2)
path.write_to_xyz("trajectory.xyz")
