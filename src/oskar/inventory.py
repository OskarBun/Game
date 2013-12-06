'''
Created on 26 Nov 2013

@author: Oskar
'''

class Inventory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.inventory = []
    
    def get_inventory_item_by_name(self, name):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item
    
    def add_inventory(self, item):
        self.inventory.append(item)
    
    def remove_inventory(self, item):
        self.inventory.remove(item)