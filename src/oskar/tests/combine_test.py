'''
Created on 27 Nov 2013

@author: Oskar
'''
import unittest
from oskar.interactable import Interactable
from oskar.player import Player




class Test(unittest.TestCase):


    def test1(self):
        plank = Interactable("Plank", None, True)
        nail = Interactable("Nail", None, True)
        nail_plank = Interactable("Nail plank", None, True)
        player = Player()
        plank.add_combination(nail, nail_plank)
        player.inventory.append(plank)
        player.inventory.append(nail)
        combine2(nail, plank, player)
        self.assertEqual(nail_plank, player.inventory[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()