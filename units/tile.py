import pygame
from settings import DAMAGE
from debug import show


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, path, groups):
        super().__init__(groups)
        self.groups = groups
        self.size = size
        self.pos  = pos
        self.set_new_image(path)
        self.path_broken = 'assets/ground.png'

    def hit(self):
        if hasattr(self, 'hp'):
            self.hp -= DAMAGE
            
            if self.hp <= 0:
                self.set_new_image(self.path_broken)
                for group in self.groups:
                    group.remove(self)
            elif self.hp <= DAMAGE:
                print('hit')
                self.set_new_image(self.path_hit)

    def set_new_image(self, path):
        image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft = self.pos)