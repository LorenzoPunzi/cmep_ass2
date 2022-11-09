'''
Assignment 2 of CMEP course : Particle parent and child classes
'''
import math

class Particle:

    def __init__(self, mass, charge=0, name=None, momentum=0.):
        '''Class constructor'''
        self.mass = mass #in MeV/c^2
        self.charge = charge #in e
        self.name = name
        self.momentum = momentum #in MeV/c
    
    @property
    def energy(self):
        '''Return the energy of the particle in MeV'''
        return math.sqrt(self.momentum**2+self.mass**2)

    @property
    def beta(self):
        '''Return the beta of the particle'''
        return self.energy/self.momentum

    @property
    def gamma(self):
        '''Return the gamma of the particle'''
        return self.energy/self.mass