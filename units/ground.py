import pygame
from units.tile import Tile


class Ground(Tile):

    def __init__(self, pos, size, groups):
        path = 'assets/ground.png'
        super().__init__(pos, size, path, groups)