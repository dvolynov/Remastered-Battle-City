import pygame
from units.tile import Tile


class Ammunition(Tile):
    
    def __init__(self, pos, size, sprites):
        self.amount = 3
        path = 'assets/ammunition.png'

        groups = [sprites['visible'], sprites['boost']]
        super().__init__(pos, size, path, groups)

    def add_boost(self, tank):
        tank.ammunition += self.amount
        self.remove_self()
    
    def remove_self(self):
        for group in self.groups:
            group.remove(self)