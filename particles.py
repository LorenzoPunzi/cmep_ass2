'''
Assignment 2 of CMEP course : Particle parent and child classes
'''
import math


class EnergyTooLowError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particles energy must be >= its mass!')

class NegativeMassError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particles mass must be positive!')

class NegativeMomentumError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particles momentum must be positive or 0!')

class BetaError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particles beta must be between 0 and 1!')

class GammaTooLowError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particles gamma must be >= 1!')



class Particle:

    def __init__(self, mass, charge=0, name=None, momentum=0.):
        '''Class constructor'''
        self.mass = mass #in MeV/c^2
        self.charge = charge #in e
        self.name = name
        self.momentum = momentum #in MeV/c
        try:
            if mass<=0:
                raise NegativeMassError
        except ValueError as e:
            print(e)
        try:
            if momentum<0:
                raise NegativeMomentumError
        except ValueError as e:
            print(e)
    
    @property
    def energy(self):
        '''Return the energy of the particle in MeV'''
        return math.sqrt(self.momentum**2+self.mass**2)

    @energy.setter
    def energy(self, energy):
        try:
            if energy<self.mass:
                raise EnergyTooLowError
            self.momentum = math.sqrt(energy**2-self.mass**2)
        except ValueError as e:
            print(e)
        
    @property
    def beta(self):
        '''Return the beta of the particle'''
        return self.momentum/self.energy

    @beta.setter
    def beta(self, beta):
        self.momentum = self.mass*beta/math.sqrt(1-beta**2)
        try:
            if beta<0 or beta>=1 :
                raise BetaError
        except ValueError as e:
            print(e)

    @property
    def gamma(self):
        '''Return the gamma of the particle'''
        return self.energy/self.mass

    @gamma.setter
    def gamma(self, gamma):
        self.momentum = self.mass*gamma*math.sqrt(1-1/gamma**2)
        try:
            if gamma<1 :
                raise GammaError
        except ValueError as e:
            print(e)





