'''
Created on 26 Nov 2013

@author: Oskar
'''
from oskar.interactable import Interactable

class Door(object):
    '''
    creates a door
    '''


    def __init__(self, room1, room2, lock):
        '''
        Constructor
        '''
        self.lock = lock
        self.keys = []
        self.connection = {
                           room1 : room2,
                           room2 : room1
                           }
        self.use = ["go", "inspect"]
    
    @property
    def description(self):
        return "I am a {} door".format("closed" if self.lock else "open")
    @property
    def is_open(self):
        return "The way is {}".format("locked" if self.lock else "now open")
    
    def cut_key(self, name, description = None, room = None):
        key = Interactable(name, description, True)
        self.keys.append(key)
        self.lock = True
        self.use.append("unlock")
        if room:
            room.add_interactable(key)
        return key
    
    def open_me(self):
        self.lock = False
        self.use.remove("unlock")
    
    def go(self, room):
        pass
    
    def i_go(self, current_room):
        return self.connection[current_room]