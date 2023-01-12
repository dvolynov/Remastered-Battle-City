import pygame
from units.tile import Tile


class Stone(Tile):

    def __init__(self, pos, size, groups):
        path = 'assets/stone.png'
        super().__init__(pos, size, path, groups)
        self.inflate = 0