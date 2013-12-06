'''
Created on 29 Nov 2013

@author: Oskar
'''

class Equip(object):
    '''
    Equip an item
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.synonms = ["equip"]
    
    @property
    def args(self):
        self.console.current_player.inventory
    
    def action(self, item):
        if item in self.console.current_player.inventory:
            self.console.current_player.equip_weapon(item)
            print("Now equiped: %s" %item)
        else:
            print("%s is not in your inventory" %item)
    
    def check(self, string):
        for word in self.synonms:
            if word in string:
                return self
                break
        else:
            return False
        