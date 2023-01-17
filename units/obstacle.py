import pygame
from units.sprite import Sprite


class Obstacle(Sprite):

    def __init__(self, position, path, groups, hp):
        super().__init__(position, path, groups)
        self.hp = hp
        self.hit_counter = 0

    def hit(self, damage):
        self.hit_counter += 1
        self.hp -= damage

        if self.hp <= 0:
            self.remove()

        self._hit_action()

    def _hit_action(self):
        pass