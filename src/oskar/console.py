'''
Created on 25 Nov 2013

@author: Oskar
'''
from oskar.console_actions.actions import Actions

class Console(object):
    '''
    Basic functions
    '''


    def __init__(self, start_room ,start_player):
        '''
        Constructor
        '''
        self.current_player = start_player
        self.current_room = start_room
        self.action = Actions(self)
        self.args = {
                     self.current_player : ["player", "skill sheet", "me"],
                     self.current_room: ["room", "current room", self.current_room.name.lower()],
                    "inventory" : ["inventory", "backpack", "pocket", "pockets"]
                    }
        
        
    def parse_instructions(self, sentance):
        action = self.parse_action(sentance)
        if action == "combine":
            arg1, arg2 = self.parse_2_arg(sentance)
        else:
            arg1 = self.parse_1_arg(sentance)
            arg2 = None
        if action is not None and arg1 is not None:    
            return action, arg1, arg2
        else:
            print("English, please!")
            return None, None, None
        
        
    def parse_action(self, sentance):
            result_action = None
            stripped = sentance.lower().split()     
            for verb in self.actions_synonms:
                for action in self.actions_synonms[verb]:
                    if action in stripped:
                        result_action = verb
                        break
                    else:
                        two_word_action = []
                        for i in range(len(stripped)):
                            for n in range(len(stripped)):
                                two_word_action.append(stripped[i] + " " + stripped[n])
                    if action in two_word_action:
                        result_action = verb
                        break
            return result_action
            
    def parse_1_arg(self, sentance):
        result_arg = None
        stripped = sentance.lower().split()    
        args = [str(item) for item in ([exit_.i_go(self.current_room) for exit_ in self.current_room.exits] + self.current_room.inventory + self.current_player.inventory + self.args[self.current_player] + self.args["inventory"] + self.args[self.current_room])]
        for arg in args:
            if arg.lower() in stripped:
                result_arg = arg
                break
            else:
                two_word_arg = []
                for i in range(len(stripped)):
                    for n in range(len(stripped)):
                        two_word_arg.append(stripped[i] + " " + stripped[n])
            if arg.lower() in two_word_arg:
                result_arg = arg
                break
        return result_arg
    
    
    def parse_2_arg(self, sentance):
        result_arg1 = None
        result_arg2 = None
        stripped = sentance.lower().split()    
        args = [str(item) for item in ([exit_.i_go(self.current_room) for exit_ in self.current_room.exits] + self.current_room.inventory + self.current_player.inventory)]
        for arg in args:
            if arg.lower() in stripped:
                result_arg1 = arg
                stripped.remove(arg.lower())
                break
            else:
                two_word_arg = []
                for i in range(len(stripped)):
                    for n in range(len(stripped)):
                        two_word_arg.append(stripped[i] + " " + stripped[n])
            if arg.lower() in two_word_arg:
                result_arg1 = arg
                stripped.remove(result_arg1.lower().split()[0])
                stripped.remove(result_arg1.lower().split()[1])
                break
        for arg in args:
            if arg.lower() in stripped:
                result_arg2 = arg
                break
            else:
                two_word_arg = []
                for i in range(len(stripped)):
                    for n in range(len(stripped)):
                        two_word_arg.append(stripped[i] + " " + stripped[n])
            if arg.lower() in two_word_arg:
                result_arg2 = arg
                break
        return result_arg1, result_arg2
    
    
    def change_room(self, room):
        self.current_room = room
        self.update_args()
    
    
    def change_player_name(self, name):
        self.current_player.change_name(name)
        self.update_args()
    
    
    def get_interactable_by_name(self, arg):
        result = self.current_room.get_inventory_item_by_name(arg)
        if result is None:
            result = self.current_player.get_inventory_item_by_name(arg)
        return result
    
    
    def get_item_by_name(self, name):
        result = self.get_interactable_by_name(name)
        if result is None:
            result = self.current_room.get_exit_by_name(name)
        return result
    
    def get_every_item_by_name(self, name):
        result = self.get_item_by_name(name)
        if result is None:
            for item in self.actions.args:
                for x in self.actions.args[item]:
                    if x == name.lower():
                        result = item
                        break
        return result
    
    def update_args(self):
        self.args = {
                     self.current_player : ["player", "skill sheet", "me", self.current_player.name.lower()],
                     self.current_room: ["room", "current room", self.current_room.name.lower()],
                     "inventory" : ["inventory", "backpack", "pocket", "pockets"]
                     }
    
    def new_input(self):
        action, arg1, arg2 = self.parse_instructions(input())
        if action is not None:
            self.which_action(action, arg1, arg2)
    