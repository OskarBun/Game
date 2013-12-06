'''
Created on 25 Nov 2013

@author: Oskar
'''
from oskar.room import Room
from oskar.console import Console
from oskar.player import Player
from oskar.weapon import Weapon

def load():
    cell_a = Room("Cell A")
    prison_hall = Room("Prison Hall")
    d1 = cell_a.add_connection(prison_hall)
    d1.cut_key("Cell Key", "Rusty", cell_a)
    plank = Weapon("Plank", "Standard 2x4", 3, 1)
    nail = Weapon("Nail", "A HUGE nail", 1, 3)
    nail_plank = Weapon("Nail Plank", "2x4 with a HUGE nail sticking through, looks deadly", 5, 1)
    plank.add_combination(nail, nail_plank)
    cell_a.add_interactable(plank)
    cell_a.add_interactable(nail)
    player_1 = Player()
    primary_console = Console(cell_a, player_1)
    print("Welcome, enter name:")
    primary_console.change_player_name(input().capitalize())
    if player_1.name.lower() == "oskar":
        print("Hello Master")
    else:
        print("%s what a silly name" % player_1.name)
    player_1.assign_skill_points()
    primary_console.new_room()
    
    while player_1.alive:
        primary_console.new_input()
        