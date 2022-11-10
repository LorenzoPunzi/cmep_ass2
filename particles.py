'''
Assignment 2 of CMEP course : Particle parent and child classes. Could be improved because child particles are not very DRY
'''
import math

class EnergyTooLowError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particle\'s energy must be >= its mass!')

class NegativeMassError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particle\'s mass must be positive!')

class NegativeMomentumError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particle\'s momentum must be positive or 0!')

class BetaError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particle\'s beta must be between 0 and 1!')

class GammaTooLowError(ValueError):
    def __init__(self): 
        super().__init__(f'{self.__class__.__name__} : the particle\'s gamma must be >= 1!')


class Particle:
    '''Class describing a particle in general'''
    def __init__(self, mass, charge=0, name=None, momentum=0.):
        '''Class constructor'''
        self.__mass = mass #in MeV/c^2
        self.__momentum = momentum #in MeV/c
        self.__charge = charge #in e
        self.__name = name

    @property
    def momentum(self):
        return self.__momentum

    @momentum.setter
    def momentum(self, new_momentum):
        try:
            if new_momentum<0:
                raise NegativeMomentumError
            self.__momentum = new_momentum
        except ValueError as e:
            print(e)

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, new_mass):
        try:
            if new_mass<=0:
                raise NegativeMassError
            self.__mass = new_mass
        except ValueError as e:
            print(e)

    @property
    def energy(self):
        '''Return the energy of the particle in MeV'''
        return math.sqrt(self.__momentum**2+self.__mass**2)

    @energy.setter
    def energy(self, new_energy):
        try:
            if new_energy<self.__mass:
                raise EnergyTooLowError
            self.__momentum = math.sqrt(new_energy**2-self.__mass**2)
        except ValueError as e:
            print(e)
        
    @property
    def beta(self):
        '''Return the beta of the particle'''
        return self.__momentum/self.energy

    @beta.setter
    def beta(self, new_beta):
        try:
            if new_beta<0 or new_beta>=1 :
                raise BetaError
            self.__momentum = self.__mass*new_beta/math.sqrt(1-new_beta**2)
        except ValueError as e:
            print(e)

    @property
    def gamma(self):
        '''Return the gamma of the particle'''
        return self.energy/self.__mass

    @gamma.setter
    def gamma(self, new_gamma):
        try:
            if new_gamma<1 :
                raise GammaTooLowError
            self.__momentum = self.__mass*new_gamma*math.sqrt(1-1/new_gamma**2)
        except ValueError as e:
            print(e)

    def printstats(self):
        print(f'The particle {self.__name} has charge {self.__charge} [e] and mass {self.__mass} [MeV]. Its momentum is {self.__momentum} [MeV].')


class Alpha(Particle):
    '''Class describing an Alpha particle'''
    def __init__(self,momentum=0):
        self.__mass = 3727
        self.__charge = 2
        self.__name = 'Alpha'
        Particle.__init__(self, self.__mass, self.__charge, self.__name, momentum)

    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, new_charge):
        print(f'You cannot change the alpha particles\'s charge. It is {self.__charge} [e] and stays so')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print(f'You cannot change the alpha particles\'s name. It is {self.__name} and stays so')

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        print(f'You cannot change the alpha particles\'s mass. It is {self.__mass} [MeV] and stays so')

class Proton(Particle):
    '''Class describing a Proton'''
    def __init__(self,momentum=0):
        self.__mass = 938
        self.__charge = 1
        self.__name = 'Proton'
        Particle.__init__(self, self.__mass, self.__charge, self.__name, momentum)

    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, new_charge):
        print(f'You cannot change the proton\'s charge. It is {self.__charge} [e] and stays so')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print(f'You cannot change the proton\'s name. It is {self.__name} and stays so')

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        print(f'You cannot change the proton\'s mass. It is {self.__mass} [MeV] and stays so')