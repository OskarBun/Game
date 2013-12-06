'''
Created on 29 Nov 2013

@author: Oskar
'''
import unittest
import random
from oskar.player import Player
import math

def start_fight(player, monster):
    if player.weapon:
        player_strength = player.strength + player.weapon.strength
    else:
        player_strength = player.strength
    print("You enter a battle with %s"%monster.name)
    while player.hp >0 and monster.hp >0:
        print("{} health: {}".format(player.name, player.hp))
        print("{} health: {}".format(monster.name, monster.hp))
        print("You can:\n1 Melee Attack")
        if int(input("What will you do?")) == 1:
            x = (player_strength)*(10-random.random()*2)
            x = math.floor(x/monster.dexterity)
            monster.hp -= x
            print("You deal %s damage" %str(x))
        if monster.hp <=0:
            break
        print("The monster attacks")
        y = (monster.strength)*(10-random.random()*2)
        y = math.floor(y/player.dexterity)
        player.hp -= math.floor(y)
        print("it deals %s damage"%str(y))
    if player.hp>0:
        print("You defeated %s"%monster.name)
    else:
        print("You were defeated")

class Test(unittest.TestCase):


    def test1(self):
        player1 = Player("Oskar")
        monster1 = Player("Monster")
        player1.strength = 10
        player1.dexterity = 2
        monster1.strength = 5
        monster1.dexterity = 1
        start_fight(player1, monster1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()