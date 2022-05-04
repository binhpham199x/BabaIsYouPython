import numpy as np
import pandas as pd
from .object import *
from .rule import *
from .tile import *
class Gameplay:
    def __init__(self, n_rows, n_cols):
        self.columns = n_cols
        self.rows = n_rows
        self.rules = []
        self.tiles = np.zeros((n_rows, n_cols), dtype=object)
        for i in range(n_rows):
            for j in range(n_cols):
                self.tiles[i,j] = Tile()

        self.prefixes = ['baba', 'rock', 'water', 'skull', 'wall', 'flag']
        self.suffixes = ['you', 'push', 'sink', 'defeat', 'stop', 'win']
            

    # def __repr__(self):
    #     ret_val = ""
    #     for row in range(self.rows):
    #         for col in range(self.columns):
    #             if len(self.tiles[row,col].objects) == 0:
    #                 ret_val += 'null'
    #             else:
    #                 for obj in self.tiles[row,col].objects:
    #                     if isinstance(obj, Word):
    #                         ret_val += obj.value
    #                     else:
    #                         ret_val += obj.property if obj.property != '' else 'null'
    #                     ret_val += ', '
    #             ret_val += '\\ '
    #         ret_val += '\n'
    #     return ret_val
    
    def __repr__(self):
        ret_val = ''
        for i in range(self.rows):
            for j in range(self.columns):
                tile_string = ''
                if len(self.tiles[i,j].objects) == 0:
                    tile_string += '/'
                    # tile_string += 'null'
                else:
                    for obj in self.tiles[i,j].objects:
                        if isinstance(obj, Word):
                            tile_string += obj.value.upper()
                        else:
                            tile_string += obj.property if obj.property !='' else 'null'
                        tile_string += ','
                ret_val += '{:10}'.format(tile_string)
                # ret_val += tile_string
            ret_val += '\n'
        return ret_val



    def get_rules(self):
        self.rules = []
    
        for i in range(self.rows):
            for j in range(self.columns):
                if self.tiles[i,j].find_word() == "is":
                    print("yes")
                    
                    #left -> right
                    if j-1 >= 0 and j+1 <=self.columns-1:
                        if self.tiles[i,j-1].find_word() in self.prefixes and self.tiles[i,j+1].find_word() in self.suffixes:
                            rule = Rule(self.tiles[i,j-1].find_word(), self.tiles[i,j+1].find_word())
                            self.rules += [rule]

                    #up -> down
                    if i-1 >= 0 and i+1 <=self.rows-1:
                        if self.tiles[i-1,j].find_word() in self.prefixes and self.tiles[i+1,j].find_word() in self.suffixes:
                            rule = Rule(self.tiles[i-1,j].find_word(), self.tiles[i+1,j].find_word())
                            self.rules += [rule]
                #ko can return bi self.rules luu trong __init__

    def apply_rules(self):
        for row in range(self.rows):
            for col in range(self.columns):
                temp = self.tiles[row,col]
                for obj in temp.objects:
                    for rule in self.rules:
                        if obj.name == rule.first:
                            obj.property = rule.second



    def find_block_upward(self,row,col):        
        if not self.tiles[row,col].has_property('you'):
            return 0
        count = 1
        current_row = row - 1
        # current_row < 0 : out of map -> no need to check anymore
        if current_row < 0:
            return -1
        # current_row >= 0 check again, so the checked tile is still in the map
        while current_row >= 0 and self.tiles[current_row,col].has_property('push'):     
            current_row -= 1
            count += 1
        #   out of map                 check stop tile                       
        if current_row < 0 or self.tiles[current_row,col].has_property('stop') or self.tiles[current_row,col].has_property('you'):
            return -1
            
        else:
            return count
            
    def move_up(self):        
        for row in range(self.rows):
            for col in range(self.columns):
                size = self.find_block_upward(row,col)
                if size > 0:
                    for current_row in range(row+1-size,row+1):
                        temp = self.tiles[current_row,col].pop_push_or_you()
                        # self.tiles[current_row-1,col].objects = np.append(self.tiles[current_row-1,col].objects, [temp])
                        self.tiles[current_row-1,col].add_object(temp)
                                   


    def find_block_downward(self,row,col):        
        if not self.tiles[row,col].has_property('you'):
            return 0
        count = 1
        current_row = row + 1
        # current_row >= self.rows : out of map -> no need to check anymore
        if current_row >= self.rows:
            return -1
        # current_row < self.rows check again, so the checked tile is still in the map
        while current_row < self.rows and self.tiles[current_row,col].has_property('push'):     
            current_row += 1
            count += 1
        #     out of map                    check stop tile                     
        if current_row >= self.rows or self.tiles[current_row,col].has_property('stop') or self.tiles[current_row,col].has_property('you'):
            return -1 
        else:
            return count
    
    def move_down(self):
        for row in range(self.rows-1, -1, -1):
            for col in range(self.columns):
                size = self.find_block_downward(row, col)
                if size > 0:
                    for current_row in range(row+size-1,row-1,-1):
                        temp = self.tiles[current_row,col].pop_push_or_you()
                        # self.tiles[current_row+1,col].objects = np.append(self.tiles[current_row+1,col].objects, [temp])
                        self.tiles[current_row+1,col].add_object(temp)


    def find_block_left(self,row,col):        
        if not self.tiles[row,col].has_property('you'):
            return 0
        count = 1
        current_col = col - 1
        # current_col >= self.columns : out of map -> no need to check anymore
        if current_col < 0:
            return -1
        # current_col < self.columns check again, so the checked tile is still in the map
        while current_col >= 0 and self.tiles[row,current_col].has_property('push'):     
            current_col -= 1
            count += 1
        #     out of map                    check stop tile                     
        if current_col < 0 or self.tiles[row,current_col].has_property('stop') or self.tiles[row,current_col].has_property('you'):
            return -1
        else:
            return count

    def move_left(self):
        for col in range(self.columns):
            for row in range(self.rows):
                size = self.find_block_left(row,col)
                if size > 0:
                    for current_col in range(col+1-size,col+1):
                        temp = self.tiles[row,current_col].pop_push_or_you()
                        # self.tiles[row,current_col-1].objects = np.append(self.tiles[row,current_col-1].objects, [temp])
                        self.tiles[row,current_col-1].add_object(temp)



    def find_block_right(self,row,col):        
        if not self.tiles[row,col].has_property('you'):
            return 0
        count = 1
        current_col = col + 1
        # current_col >= self.columns : out of map -> no need to check anymore
        if current_col >= self.columns:
            return -1
        # current_row < self.rows check again, so the checked tile is still in the map
        while current_col < self.columns and self.tiles[row,current_col].has_property('push'):     
            current_col += 1
            count += 1
        #     out of map                    check stop tile                     
        if current_col >= self.columns or self.tiles[row,current_col].has_property('stop') or self.tiles[row,current_col].has_property('you'):
            return -1
        else:
            return count
            
    def move_right(self):
        for col in range(self.columns-1, -1,-1):
            for row in range(self.rows):            
                size = self.find_block_right(row,col)
                if size > 0:
                    for current_col in range(col+size-1,col-1,-1):
                        temp = self.tiles[row,current_col].pop_push_or_you()
                        # self.tiles[row,current_col+1].objects = np.append(self.tiles[row,current_col+1].objects, [temp])
                        self.tiles[row,current_col+1].add_object(temp)



    def check_win(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.tiles[row,col].has_property('you') and self.tiles[row,col].has_property('win'):
                    return True
        return False

    def check_lose(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.tiles[row,col].has_property('you'):
                    return False
        return True

    
    def reset_game(self):
        self.load_map_level(self.level, self.info)

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
                        self.tiles[row,col].add_object(Rock())
                    elif value == 'wall':
                        self.tiles[row,col].add_object(Wall())    
                    elif value == 'flag':
                        self.tiles[row,col].add_object(Flag())    
                    elif value == 'baba':
                        self.tiles[row,col].add_object(Baba()) 
                    elif value == 'water':
                        self.tiles[row,col].add_object(Water()) 
                    elif value == 'skull':
                        self.tiles[row,col].add_object(Skull()) 
                    elif value.isupper():
                        self.tiles[row,col].add_object(Word(value.lower()))


    # self.prefixes = ['baba', 'rock', 'water', 'skull', 'wall', 'flag']
    # self.suffixes = ['you', 'push', 'sink', 'defeat', 'stop', 'win']
          