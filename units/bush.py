import pygame
from units.tile import Tile


class Bush(Tile):

    def __init__(self, pos, size, sprites):
        path = 'assets/bush.png'

        groups = [sprites['visible']]
        super().__init__(pos, size, path, groups)