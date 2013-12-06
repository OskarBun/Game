'''
Created on 27 Nov 2013

@author: Oskar
'''
import unittest
from oskar.room import Room





def door_name(room1, room2):
    exits = ""
    for exit_ in room1.exits:
        exits += str(exit_.i_go(room1))
    return exits

class Test(unittest.TestCase):


    def testName(self):
        room1 = Room("Room 1")
        room2 = Room("Room 2")
        room1.add_connection(room2) 
        self.assertEqual(door_name(room1, room2), room2.name)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()