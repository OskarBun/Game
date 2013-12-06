'''
Created on 29 Nov 2013

@author: Oskar
'''

class Use(object):
    '''
    Uses an Item
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.synonms = ["use"]
    
    @property
    def args(self):
        return self.console.current_player.inventory
    
    def action(self, arg):
        if "equip" in arg.use:
            self.console.actions.args["equip"].actions(arg)
        else:
            for exit_ in self.console.current_room.exits:
                if arg in exit_.keys:
                    self.console.actions.args["unlock"].actions(exit_)
                    break
            else:
                print("can't find a use for %s in this room" %arg)
    
    def check(self, string):
            for word in self.synonms:
                if word in string:
                    return self
                    break
            else:
                return False