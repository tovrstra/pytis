
import os, shutil, tempfile

from pytis import *


def test_nvt_andersen_md():
    # Create a temporary directory for the output.
    workdir = tempfile.mkdtemp("pytis")
    # Run a PyTIS example.
    wrapper = CPMDWrapper("cpmd.x", "test/input/cpmd/water.cpmd.inp",
        ["test/input/cpmd/H_VDB_LDA.psp", "test/input/cpmd/O_VDB_LDA.psp"])
    ensemble = NVTAndersen(300, 0.01)
    system = System.from_xyz("test/input/xyz/water.xyz", 300)
    path = Path(system, wrapper, ensemble, os.path.join(workdir, "single"))
    path.run(2)
    path.write_to_xyz(os.path.join(workdir, "trajectory.xyz"))
    # Clean up the workdir.
    shutil.rmtree(workdir)
    # Check the contents of the path object. (TODO: Add more assertions)
    assert len(path.frames) == 3
