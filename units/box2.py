import pygame
from units.tile import Tile


class Box2(Tile):

    def __init__(self, pos, size, groups):
        path = 'assets/box_2.png'
        super().__init__(pos, size, path, groups)
        self.hp = 150