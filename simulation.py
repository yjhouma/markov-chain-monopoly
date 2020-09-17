# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:30:58 2020

@author: Yohanes Jhouma
"""
import random
list_of_block_monopoly = [
        "Go",
        "Mediterranean Avenue",
        "Community Chest 1",
        "Baltic Avenue",
        "Income Tax",
        "Reading Railroad",
        "Oriental Avenue",
        "Chance 1",
        "Vermont Avenue",
        "Connecticut Avenue",
        "Jail Visiting",
        "St. Charles Place",
        "Electric Company",
        "States Avenue",
        "Virginia Avenue",
        "Pennsylvania Railroad",
        "St. James Palace",
        "Community Chest 2",
        "Tennessee Avenue",
        "New York Avenue",
        "Free Parking",
        "Kentucky Avenue",
        "Chance 2",
        "Indiana Avenue",
        "Illinois Avenue",
        "B. & O. Railroad",
        "Atlantic Avenue",
        "Ventnor Avenue",
        "Water Works",
        "Marvin Gardens",
        "Go To Jail",
        "Pacific Avenue",
        "North Carolina Avenue",
        "Comunity Chest 3",
        "Pennsylvania Avenue",
        "Short Line",
        "Chance 3",
        "Park Place",
        "Luxury Tax",
        "Boardwalk"
]




class Monopoly:
    def __init__(self):
        self.position = 0
        self.block = list_of_block_monopoly[self.position]
        
    def dice_roll(self):
        return random.randint(1,6) + random.randint(1,6)
        
    def move(self):
        how_far = self.dice_roll()
        #print(how_far)
        self.position = (self.position + how_far) % 40
        self.block = list_of_block_monopoly[self.position]
        
    def move_to(self,target_index):
        self.position = target_index
        self.block = list_of_block_monopoly[self.position]
    
    def chance_draw(self, chance_number):
        #print("CHANCE")
        x = random.randint(1,16)
        if x == 1:
            self.move_to(0)
        elif x == 2:
            self.move_to(24)
        elif x == 3:
            self.move_to(11)
        elif x == 4:
            self.move_to(30)
        elif x == 5:
            self.move_to(5)
        elif x == 6:
            self.move_to(39)
        elif x == 7:
            if chance_number == 1 or chance_number == 3:
                self.move_to(12)
            elif chance_number == 2:
                self.move_to(28)
        elif x == 8:
            if chance_number == 1:
                self.move_to(15)
            elif chance_number == 2:
                self.move_to(25)
            else:
                self.move_to(5)
        elif x == 9:
            if chance_number == 1:
                self.move_to(4)
            elif chance_number == 2:
                self.move_to(19)
            else:
                self.move_to(33)
                
    def community_chest(self):
        #"COMMUNITY"
        x  = random.randint(1,17)
        if x == 1:
            self.move_to(0)
        elif x == 2:
            self.move_to(30)
            
    def simulate_game(self):
        if self.position == 30:
            self.move_to(10)
    
        self.move()
        
        if self.position == 7:
            self.chance_draw(1)
        elif self.position == 22:
            self.chance_draw(2)
        elif self.position == 36:
            self.chance_draw(3)
        elif self.position == 2 or self.position == 17 or self.position == 33:
            self.community_chest()
        
        return self.block


dict_prob = {}

for i in list_of_block_monopoly:
    dict_prob[i] = 0

positions = [0] * 40
game = Monopoly()
for i in range(100000):
    a = game.simulate_game()
    dict_prob[a] += 1/100000
            

        
    