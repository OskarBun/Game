'''
Created on 29 Nov 2013

@author: Oskar
'''
from oskar.interactable import Interactable

class Weapon(Interactable):
    '''
    Equipable weapon class
    '''


    def __init__(self, name, description, strength, dexterity, type_ = None):
        '''
        Constructor
        '''
        Interactable.__init__(self, name, description, packable = True)
        self.strength = strength
        self.dexterity = dexterity
        self.description = str(description) + "\nStrength: {}\nDexterity: {}".format(str(strength), str(dexterity)) 
        self.type = type_
        self.use = ("pick up", "inspect", "use", "combine", "equip")