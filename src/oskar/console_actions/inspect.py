'''
Created on 29 Nov 2013

@author: Oskar
'''

class Inspect(object):
    '''
    Looks at objects
    '''


    def __init__(self, console):
        '''
        Constructor
        '''
        self.console = console
        self.synonms = ["inspect", "look", "show", "view"]
        self.player_template = """
        {name}
        {hp}
        {level}
        {xp}
        {strength}
        {dexterity}
        {health}
        """
    
    @property
    def args(self):
        return [exit_.i_go(self.console.current_room) for exit_ in self.console.current_room.exits] + self.console.current_room.inventory + self.console.current_player.inventory + self.console.args[self.console.current_player] + self.console.args["inventory"] + self.console.args[self.console.current_room]
    
    def skill_sheet(self):
        values = {
                  "name":self.console.current_player.name,
                  "hp":self.console.current_player.hp,
                  "level":self.console.current_player.level,
                  "xp":self.console.current_player.xp,
                  "strength":self.console.current_player.strength,
                  "dexterity":self.console.current_player.dexterity,
                  "health": self.console.current_player.health
                  }
        print(self.player_template.format(**values))
    
    def check(self, string):
            for word in self.synonms:
                if word in string:
                    return self
                    break
            else:
                return False