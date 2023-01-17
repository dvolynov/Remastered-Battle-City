import pygame
from units.sprite import Sprite


class Boost(Sprite):

    def __init__(self, position, path, groups, objects, attribute, amount):
        super().__init__(position, path, groups)
        self.objects = objects
        self.attribute = attribute
        self.amount = amount

    def collision(self):
        for object in self.objects:
            if object.rect.colliderect(self.rect):
                self._add_boost(object)
                self._remove()
                
    def _add_boost(self, object):
        amount = getattr(object, self.attribute)
        setattr(object, self.attribute, amount + self.amount)