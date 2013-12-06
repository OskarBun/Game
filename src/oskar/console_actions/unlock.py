'''
Created on 29 Nov 2013

@author: Oskar
'''

class Unlock(object):
    '''
    Unlocks doors
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.synonms = ["unlock"]
    
    @property
    def args(self):
        return [str(exit_.i_go(self.current_room)) for exit_ in self.current_room.exits]
    
    def action(self, door):
        for item in self.console.current_player.inventory:
            if item in door.keys:
                door.open_me()
                print(door.is_open)
                break
        else:
            print("You don't have the key to %s" %door.i_go(self.console.current_room))
    
    def check(self, string):
            for word in self.synonms:
                if word in string:
                    return self
                    break
            else:
                return False