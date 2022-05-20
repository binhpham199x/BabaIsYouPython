import sys
import os
current_dir = os.path.dirname(__file__) 
sys.path.append(os.path.join(current_dir,".."))

from gameplay import Gameplay, Tile
from graphics.objects_graphic import *
import numpy as np
import pandas as pd

import pygame

current_dir = os.path.dirname(__file__) 

class GameplayGraphic(Gameplay):
    def load_map_level(self, level_file, info_file):
        self.level = level_file
        self.info = info_file 
        with open(info_file) as f:
            # resize 
            info = f.readline().split(',')

            self.rows = int(info[0])
            self.columns = int(info[1])

            self.rules = []
            self.tiles = np.zeros((self.rows, self.columns), dtype=object)
            for i in range(self.rows):
                for j in range(self.columns):
                    self.tiles[i,j] = Tile()

        map_data_array = np.array(pd.read_csv(level_file, header=None), dtype=str)
        for row in range(self.rows):
            for col in range(self.columns):
                # '/' chia cac obj trong cung 1 tile
                tile_value = map_data_array[row,col].split('/')    
                for value in tile_value:
                    if value == '':
                        continue
                    elif value == 'rock':
                        self.tiles[row,col].add_object(RockGraphic())
                    elif value == 'wall':
                        self.tiles[row,col].add_object(WallGraphic())    
                    elif value == 'flag':
                        self.tiles[row,col].add_object(FlagGraphic())    
                    elif value == 'baba':
                        self.tiles[row,col].add_object(BabaGraphic()) 
                    elif value == 'water':
                        self.tiles[row,col].add_object(WaterGraphic())
                    elif value == 'skull':
                        self.tiles[row,col].add_object(SkullGraphic()) 
                    elif value.isupper():
                        self.tiles[row,col].add_object(WordGraphic(value.lower()))

    def render(self, window):
        for row in range(self.rows):
            for col in range(self.columns):
                t = self.tiles[row,col]
                for obj in t.objects:
                    obj.render(window,1+40*col,1+40*row)



if __name__ == '__main__':
    pygame.init()

    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
    running = True
    
    graphic_map_test = GameplayGraphic(6,9)
    graphic_map_test.load_map_level(os.path.join(current_dir,'../../resources/maps/level_1.csv'),os.path.join(current_dir,'../../resources/maps/level_1.info'))

    while running:
        # graphic_map_test.render(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        graphic_map_test.render(screen)
        pygame.display.update()
    