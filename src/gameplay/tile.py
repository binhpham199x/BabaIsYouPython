import numpy as np
import pandas as pd
from .object import *
class Tile:
    def __init__(self):
        self.objects = np.array([], dtype=object)

    def add_object(self, obj : Object):        
        has_interacted = False
        objects_after_interaction = []
        for old_obj in self.objects:
            if has_interacted or obj.interact(old_obj) == None:
                objects_after_interaction = np.append(objects_after_interaction, [old_obj])
            else:
                objects_after_interaction = np.append(objects_after_interaction, obj.interact(old_obj))
                has_interacted = True
                
        self.objects = objects_after_interaction

        if not has_interacted:
            self.objects = np.append(self.objects, [obj])


    def find_word(self):
        for obj in self.objects:
            if isinstance(obj, Word):
                return obj.value
            return ''

    def has_property(self, property):
        for obj in self.objects:
            if obj.property == property:
                return True

    # delete a 'push' object in the list
    # return that 'push' object to a variable
    
    def pop_push_or_you(self):
        position = -1
        for i in range(len(self.objects)):
            if self.objects[i].property == 'push' or self.objects[i].property == 'you' :
                position = i
                # print(position)

        temp_obj = self.objects[position]
        self.objects = np.delete(self.objects, position)

        return temp_obj

    def __repr__(self):
        s = ''
        for obj in self.objects:
            s += '/'+ obj.name + ',' + obj.property            
        return s
