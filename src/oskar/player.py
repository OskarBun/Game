'''
Created on 25 Nov 2013

@author: Oskar
'''
from oskar.inventory import Inventory



class Player(Inventory):
    '''
    Creates a character
    '''


    def __init__(self, name=None):
        '''
        Constructor
        '''
        Inventory.__init__(self)
        self.name = name
        self.alive = True
        self.level = 1
        self.skill_points = 10
        self.xp = 0
        self.hp = 100
        self.strength = 0
        self.dexterity = 0
        self.use = "inspect"
        self.weapon = None
    
    @property
    def description(self):
        return self.show_skill_sheet()
    
    @property
    def health(self):
        if self.hp == 100:
            return"Perfectly Healthy"
        elif self.hp >= 80:
            return "\Barely a scratch"
        elif self.hp >= 50:
            return "Only missing an arm, no biggie"
        elif self.hp >= 20:
            return "Criticaly wounded"
        else:
            return "May only be a head, but will still bite your ankles"
    
    def add_inventory(self, item):
        if item.packable:
            print("%s added to inventory" %item.name)
            Inventory.add_inventory(self, item)         
        else:
            print(item.wittyremark)
    
    def remove_inventory(self, item):
        print("%s removed from inventory" %item.name)
        Inventory.remove_inventory(self, item)
    
    def assign_skill_points(self):
        print(self.description)
        print("You have %s skill points" %self.skill_points)
        self.increase_strength()
        self.increase_dexterity()
    
    def show_skill_sheet(self):
        skill_sheet = ""
        skill_sheet += self.name
        skill_sheet += "\nHp: %s" %self.hp
        skill_sheet += "\nLevel: %s" %self.level
        skill_sheet += "\nXp: %s" %self.xp
        skill_sheet += "\nStrength: {}".format(self.strength+self.weapon.strength if self.weapon else self.strength)
        skill_sheet += "\nDexterity: {}".format(self.dexterity+self.weapon.dexterity if self.weapon else self.dexterity) 
        if self.hp == 100:
            skill_sheet += "\nPerfectly Healthy"
        elif self.hp >= 80:
            skill_sheet += "\nBarely a scratch"
        elif self.hp >= 50:
            skill_sheet += "\nOnly missing an arm, no biggie"
        elif self.hp >= 20:
            skill_sheet += "\nCriticaly wounded"
        else:
            skill_sheet += "\nMay only be a head, but will still bite your ankles"
        return skill_sheet
            
    def change_name(self, name):
        self.name = name
            
    def equip_weapon(self, item):
        self.weapon = item
    
    def unequip_weapon(self):
        self.weapon = None
    
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
        elif x > self.skill_points or x<0:
            print("You only have %s skill points" %self.skill_points)
            self.increase_strength(value = None)
        else:
            self.strength += x
            self.skill_points -= x 
            
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
        elif x > self.skill_points:
            print("You only have %s skill points" %self.skill_points)
            self.increase_dexterity(value = None)
        else:
            self.dexterity += x
            self.skill_points -= x 
            
        
    
    
    
    
    
    
    
    
        