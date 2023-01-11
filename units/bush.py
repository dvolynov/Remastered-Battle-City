import pygame
from units.tile import Tile


class Bush(Tile):

    def __init__(self, pos, size, groups):
        path = 'assets/bush.png'
        super().__init__(pos, size, path, groups)