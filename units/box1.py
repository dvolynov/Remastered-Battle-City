import pygame
from units.tile import Tile


class Box1(Tile):

    def __init__(self, pos, size, sprites):
        self.hp = 100
        self.paths_hit = ['assets/box1_hit1.png']

        path = 'assets/box1.png'
        groups = [sprites['visible'], sprites['obstacle']]
        super().__init__(pos, size, path, groups)