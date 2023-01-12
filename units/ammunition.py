import pygame
from units.tile import Tile


class Ammunition(Tile):
    
    def __init__(self, pos, size, groups):
        path = 'assets/ammunition.png'
        super().__init__(pos, size, path, groups)

        self.radius = 10