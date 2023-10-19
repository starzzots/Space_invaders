import pygame
from settings import *

class LevelMaker:
    #want to create a func that can generate a list 15x20 same size as screen and then fill with 0's to start then after figure out how it should generate the enemies and player
    def __init__(self,level):
        #I should generate the list on init so make the loop here
        self.level = level
        
        
    def generate_sprite_cords(self):
        enemy_list_1 = []
        enemy_list_2 = []
        enemy_list_3 = []
        for i,row in enumerate(self.level):
            #print(i)
            for j,col in enumerate(row):
                if col == 2:
                    height= i*32 + 32
                    width = j*32 + 32
                    enemy_list_1.append((width, height))
                if col == 3:
                    height= i*32 + 32
                    width = j*32 + 32
                    enemy_list_2.append((width, height))
                if col == 4:
                    height= i*32 + 32
                    width = j*32 + 32
                    enemy_list_3.append((width, height))
        return enemy_list_1, enemy_list_2,enemy_list_3
    
level = LevelMaker(level_1)
print(level.generate_sprite_cords())