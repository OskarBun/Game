'''
Created on 25 Nov 2013

@author: Oskar
'''
import unittest
from oskar.player import Player
from oskar.room import Room
from oskar.console import Console
from oskar.interactable import Interactable

class Test_Console(Console):

    def parse_instruction(self, sentance):
        action = self.parse_action(sentance)
        if action.synonms[0] == "combine":
            arg1, arg2 = self.parse_2_arg(sentance, action)
        else:
            arg1, arg2 = self.parse_1_arg(sentance, action)
        if action is not None and arg1 is not None:    
            return action, arg1, arg2
        else:
            print("English, please!")
            return None, None, None
    
    
    def parse_action(self, sentance):
        result_action = None
        stripped = sentance.lower().split()
        for action in self.action.actions:
            x = action.check(stripped)
            if x:
                result_action = x
                break
        else:
            two_word_stripped = []
            for i in range(len(stripped)):
                for n in range(len(stripped)):
                    two_word_stripped.append(stripped[i] + " " + stripped[n])
            for action in self.action.actions:
                x = action.check(stripped)
                if x:
                    result_action = x
                    break
        return result_action
    
    
    def parse_1_arg(self, sentance, action):
        result_arg = None
        stripped = sentance.lower().split()
        for word in action.synonms:
            if word in stripped:
                stripped.remove(word)
        for arg in action.args:
            if arg in stripped:
                result_arg = arg
                break
        else:
            two_word_stripped = []
            for i in range(len(stripped)):
                for n in range(len(stripped)):
                    two_word_stripped.append(stripped[i] + " " + stripped[n])
            for arg in action.args:
                if arg in two_word_stripped:
                    result_arg = arg
                    break
        return result_arg, None
            

class Test(unittest.TestCase):

    def setUp(self):
        player = Player("Oskar")
        room1 = Room("room1")
        room2 = Room("room2")
        room1.add_connection(room2)
        chocolate = Interactable("chocolate")
        room1.add_interactable(chocolate)
        self.console = Test_Console(room1, player)
        

    def test_go_to(self):
        sentance = "go room2"
        print(self.console.parse_instruction(sentance))

    def test_equip(self):
        sentance = "pick up chocolate"
        print(self.console.parse_instruction(sentance))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInstructions']
    unittest.main()