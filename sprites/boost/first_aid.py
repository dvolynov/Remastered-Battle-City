import pygame
from units.boost import Boost



class FirstAid(Boost):
    
    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            path = 'assets/first_aid.png', 
            groups = [sprites['visible'], sprites['boost']], 
            objects = sprites['object'],
            attribute = 'hp', 
            amount = 50
        )