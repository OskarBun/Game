'''
Created on 27 Nov 2013

@author: Oskar
'''
import unittest
from oskar.player import Player
from oskar.room import Room
from oskar.console import Console
from oskar.interactable import Interactable

class Test_Console(Console):
    
    def __init__(self, start_room, start_player):
        Console.__init__(self, start_room, start_player)

    def parse_instructions_test(self, sentance):
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
        args = [str(item) for item in ([exit_.i_go(self.current_room) for exit_ in self.current_room.exits] + self.current_room.inventory + self.current_player.inventory)]
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
    

class Test(unittest.TestCase):
    
    def test2(self):
        sentance = "combine plank and nail"
        room1 = Room("Room 1")
        room2 = Room("Room 2")
        room1.add_connection(room2)
        plank = Interactable("Plank", None, True)
        nail = Interactable("Nail", None, True)
        player1 = Player()
        player1.inventory.append(plank)
        player1.inventory.append(nail)
        console1 = Test_Console(room1, player1)
        action, arg1, arg2 = console1.parse_instructions_test(sentance)
        print(action)
        print(arg1)
        print(arg2)
        self.assertEqual(action, "combine")
        self.assertEqual(arg1, "Plank")
        self.assertEqual(arg2, "Nail")
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()