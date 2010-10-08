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


import os, shutil, tempfile

from pytis import *


def test_nvt_andersen_md():
    # Create a temporary directory for the output.
    workdir = tempfile.mkdtemp("pytis")
    # Run a PyTIS example.
    wrapper = CPMDWrapper("cpmd.x", "test/input/cpmd/water.cpmd.inp",
        ["test/input/cpmd/H_VDB_LDA.psp", "test/input/cpmd/O_VDB_LDA.psp"])
    ensemble = NVTAndersen(300, 0.01)
    system, init_state = load_xyz("test/input/xyz/water.xyz", 300)
    path = Path(system, init_state, wrapper, ensemble, os.path.join(workdir, "single"))
    path.run(2)
    path.write_to_xyz(os.path.join(workdir, "trajectory.xyz"))
    # Clean up the workdir.
    shutil.rmtree(workdir)
    # Check the contents of the path object. (TODO: Add more assertions)
    assert len(path.frames) == 3


def test_nve_md():
    # Create a temporary directory for the output.
    workdir = tempfile.mkdtemp("pytis")
    # Run a PyTIS example.
    wrapper = CPMDWrapper("cpmd.x", "test/input/cpmd/water.cpmd.inp",
        ["test/input/cpmd/H_VDB_LDA.psp", "test/input/cpmd/O_VDB_LDA.psp"])
    ensemble = NVE()
    system, init_state = load_xyz("test/input/xyz/water.xyz", 300)
    path = Path(system, init_state, wrapper, ensemble, os.path.join(workdir, "single"))
    path.run(2)
    path.write_to_xyz(os.path.join(workdir, "trajectory.xyz"))
    # Clean up the workdir.
    shutil.rmtree(workdir)
    # Check the contents of the path object. (TODO: Add more assertions)
    assert len(path.frames) == 3
