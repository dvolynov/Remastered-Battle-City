import pygame
from units.tile import Tile


class Ammunition(Tile):
    
    def __init__(self, pos, size, groups):
        path = 'assets/amm6.png'
        super().__init__(pos, size, path, groups)