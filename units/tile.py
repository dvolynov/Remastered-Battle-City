import pygame
from units.obstacle import Obstacle


class Tile(Obstacle):
    def __init__(self, position, path, groups, hp):
        super().__init__(position, path, groups, hp)

    def _hit_action(self): pass
        # path = self.paths_hit[self.hit_counter - 1]
        # self.set_new_image(path)