

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
