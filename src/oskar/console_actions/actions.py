'''
Created on 29 Nov 2013

@author: Oskar
'''
from oskar.console_actions.go import Go
from oskar.console_actions.pick_up import Pick_Up
from oskar.console_actions.inspect import Inspect
from oskar.console_actions.unlock import Unlock
from oskar.console_actions.combine import Combine
from oskar.console_actions.equip import Equip
from oskar.console_actions.use import Use

class Actions(object):
    '''
    Decides which action to call
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.actions = [
                        Go(self.console),
                        Pick_Up(self.console),
                        Inspect(self.console),
                        Use(self.console),
                        Unlock(self.console),
                        Combine(self.console),
                        Equip(self.console)
                        ]
        
    def which_action(self, action, arg1, arg2):
        arg = self.console.get_every_item_by_name(arg1)
        if arg:
            if action in arg.use:
                if arg2:
                    self.actions[action].action(arg, arg2)
                else:
                    self.actions[action].action(arg)
            else:
                print("I can't %s {}".format("%s or %s"%(arg, arg2) if arg2 else arg) %(action))
        