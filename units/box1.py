import pygame
from units.tile import Tile


class Box1(Tile):

    def __init__(self, pos, size, groups):
        path = 'assets/box_1.png'
        super().__init__(pos, size, path, groups)
        self.hp = 100