import pygame
from units.tile import Tile


class Stone(Tile):

    def __init__(self, pos, size, sprites):
        path = 'assets/stone.png'

        groups = [sprites['visible'], sprites['obstacle']]
        super().__init__(pos, size, path, groups)