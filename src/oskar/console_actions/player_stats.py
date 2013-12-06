'''
Created on 29 Nov 2013

@author: Oskar
'''

class Player_Stats(object):
    '''
    Things that change the players stats
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        
    
    def increase_strength(self, value = None):
        x = None
        if value is None:
            value = input("How many points would you like in Strength?\n")
        try:
            x = int(value)
        except:
            print("Don't be silly")
        if x == None:
            self.increase_strength(value = None)
        elif x > self.console.current_player.skill_points or x<0:
            print("You only have %s skill points" %self.skill_points)
            self.increase_strength(value = None)
        else:
            self.console.current_player.increase_strength(x)
            self.console.current_player.decrease_skill_points(x) 
    
    def increase_dexterity(self, value = None):
        x = None
        if value is None:
            value = input("How many points would you like in Dexterity?\n")
        try:
            x = int(value)
        except:
            print("Don't be silly")
        if x == None:
            self.increase_dexterity(value = None)
        elif x > self.console.current_player.skill_points:
            print("You only have %s skill points" %self.skill_points)
            self.increase_dexterity(value = None)
        else:
            self.console.current_player.increase_dexterity(x)
            self.console.current_player.decrease_skill_points(x) 
        
    
    
    
    
    
    
        