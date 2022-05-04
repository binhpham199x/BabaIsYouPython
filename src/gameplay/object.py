import numpy as np
import pandas as pd

class Object:
    # static variable: common variable for all the instances of the class Object.
    
    interaction_table = {'you':{'you':None, 'push':None, 'sink':'', 'defeat':'defeat', 'stop':None, 'win':None},\
                         'push':{'you':None, 'push':None, 'sink':'', 'defeat':None, 'stop':None, 'win':None},\
                         'sink':{'you':'', 'push':'', 'sink':None, 'defeat':None, 'stop':None, 'win':None},\
                         'defeat':{'you':'defeat', 'push':None, 'sink':None, 'defeat':None, 'stop':None, 'win':None},\
                         'stop':{'you':None, 'push':None, 'sink':None, 'defeat':None, 'stop':None, 'win':None},\
                         'win':{'you':None, 'push':None, 'sink':None, 'defeat':None, 'stop':None, 'win':None}}

    def __init__(self, property='', name=''):
        self.property = property
        self.name = name

    def interact(self, another_object:object):
        if self.property =='' or another_object.property == '':
            return None

        if Object.interaction_table[self.property][another_object.property] == None:
            return None
        
        elif Object.interaction_table[self.property][another_object.property] == 'defeat':
            if self.property == 'defeat':
                return [self]
            else:
                return [another_object]

        elif Object.interaction_table[self.property][another_object.property] == '':
            return []

class Baba(Object): 
    def __init__(self,property=''):        
        super().__init__(property, 'baba')

class Rock(Object):
    def __init__(self,property=''):
        super().__init__(property, 'rock')

class Wall(Object):
    def __init__(self,property=''):
        super().__init__(property, 'wall')

class Water(Object):
    def __init__(self,property=''):
        super().__init__(property, 'water')

class Skull(Object):
    def __init__(self,property=''):
        super().__init__(property, 'skull')

class Flag(Object):
    def __init__(self,property=''):
        super().__init__(property, 'flag')

class Word(Object):
    def __init__(self, value):        
        super().__init__('push', 'word')
        self.value = value