import pygame
from units.tile import Tile


class Ground(Tile):

    def __init__(self, pos, size, sprites):
        path = 'assets/ground.png'

        groups = [sprites['visible']]
        super().__init__(pos, size, path, groups)