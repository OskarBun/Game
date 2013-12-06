'''
Created on 29 Nov 2013

@author: Oskar
'''

class Combine(object):
    '''
    Combine command
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.synonms = ["combine"]
    
    def args(self):
        return self.console.current_player.inventory + self.console.current_room.inventory
    
    
    def action(self, arg1, arg2 = None):
        if arg1 in self.console.current_player.inventory:
            if arg2 is None:
                temp_arg2 = input("What will you combine %s with?\n" %arg1)
                arg2 = self.console.get_interactable_by_name(temp_arg2)
            else:
                arg2 = self.console.get_interactable_by_name(arg2)
            if arg2 in self.console.current_player.inventory:
                for item in arg1.combination:
                    if item == arg2:
                        if arg1 == self.console.current_player.weapon:
                            self.console.current_player.unequip_weapon()
                        elif arg2 == self.console.current_player.weapon:
                            self.console.current_player.unequip.weapon()
                        self.console.current_player.remove_inventory(arg1)
                        self.console.current_player.remove_inventory(arg2)
                        self.console.current_player.add_inventory(arg1.combination[arg2])
                    else:
                        print("Can not combine %s with %s" %(arg1, arg2))
            else:
                print("%s is not in your inventory" %(arg2 if arg2 else temp_arg2))
        else:
            print("%s is not in your inventory" %arg1)
        
    def check(self, string):
            for word in self.synonms:
                if word in string:
                    return self
                    break
            else:
                return False