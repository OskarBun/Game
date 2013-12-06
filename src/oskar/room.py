'''
Created on 25 Nov 2013

@author: Oskar
'''
from oskar.door import Door
from oskar.inventory import Inventory

class Room(Inventory):
    '''
    A room
    '''


    def __init__(self, name, description=None):
        '''
        Create a Named room
        '''
        Inventory.__init__(self)
        self.name = name
        self.description_ = description
        self.exits = []
        self.use = ["inspect"]
    
    @property
    def description(self):
        result = "{} - {}".format(self.name, self.description_)
        if len(self.inventory) > 1:
            result += "\nthere are items: {}".format(", ".join([str(x) for x in self.inventory]))
        elif len(self.inventory) > 0:
            result += "\nthere is an item: {}".format(self.inventory[0])
        exits = "\nExits:"
        for exit_ in self.exits:
            exits += " " + str(exit_.i_go(self))
        result += exits
        return result
    
    def __str__(self):
        return self.name

    def add_connection(self, room, lock = False):
        d1 = Door(self, room, lock)
        self.exits.append(d1)
        room.exits.append(d1)
        return d1
    
    def remove_connection(self, room):
        self.remove_exit(room)
        room.remove_exit(self)
        
    def add_interactable(self, interactable):
        self.add_inventory(interactable)
    
    def remove_interactable(self, interactable):
        self.remove_inventory(interactable)
    
    def get_exit_by_name(self, name):
        for door in self.exits:
            if door.i_go(self).name == name:
                return door
    
    