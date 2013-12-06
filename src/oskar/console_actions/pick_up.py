'''
Created on 29 Nov 2013

@author: Oskar
'''

class Pick_Up(object):
    '''
    Puts objects into players inventory
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.synonms = ["pick up", "grab", "take", "get"]
    
    @property
    def args(self):
        return self.console.current_room.inventory
    
    def action(self, arg):
        if arg in self.console.current_player.inventory:
            print("%s is already in your inventory")%str(arg)
        elif arg in self.console.current_room.inventory:
            self.console.current_player.add_inventory(arg)
            self.console.current_room.remove_interactable(arg)
        else:
            raise Exception("where was this item?")
    
    def check(self, string):
            for word in self.synonms:
                if word in string:
                    return self
                    break
            else:
                return False
        