'''
Created on 25 Nov 2013

@author: Oskar
'''

class Interactable(object):
    '''
    Creates an Interactable Item
    '''


    def __init__(self, name, description = None, packable = False):
        '''
        Constructor
        '''
        self.name = name
        self.description = description
        self.packable = packable
        self.combination = {}
        self.wittyremark = None
        if self.packable:
            self.use = ("pick up", "inspect", "use")
        else:
            self.use = ("inspect", "use")
        
    def __str__(self):
        return self.name
    
    def add_combination(self, item, result):
        self.combination[item] = result
        item.combination[self] = result
    
    def remove_combination(self, item):
        self.combination.remove(item)
        item.combination.remove(self)