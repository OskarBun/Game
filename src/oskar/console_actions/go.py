'''
Created on 29 Nov 2013

@author: Oskar
'''

class Go(object):
    '''
    Moves to a new room
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.synonms = ["go", "head for", "enter", "pass into", "walk", "forward"]
    
    @property
    def args(self):
        return [(str(exit_.i_go(self.console.current_room))) for exit_ in self.console.current_room.exits]
        
    def action(self, door):
        if door.lock is not True:
            self.console.change_room(door.connection[self.current_room])
            print("now entering %s" %self.current_room)
            self.new_room()
        else:
            print(door.is_open)
    
    def new_room(self):
        print("you are here...")
        #inspect(self.console.current_room)
        print("What will you do?")
    
    def check(self, string):
            for word in self.synonms:
                if word in string:
                    return self
                    break
            else:
                return False