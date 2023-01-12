import pygame
from units.tile import Tile


class Box2(Tile):

    def __init__(self, pos, size, sprites):
        self.hp = 150
        self.paths_hit = [
            'assets/box2_hit1.png',
            'assets/box2_hit2.png'
        ]

        path = 'assets/box2.png'
        groups = [sprites['visible'], sprites['obstacle']]
        super().__init__(pos, size, path, groups)