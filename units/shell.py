import pygame
from settings import *


class Shell(pygame.sprite.Sprite):
    def __init__(self, pos, vector, image, groups, obstacle_sprites):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites    

        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
        
        self.vector = pygame.math.Vector2()
        self.direction = self.turret.direction

        self.vector.x = vector[0]
        self.vector.y = vector[1]

    def fly(self):
        self.rect.centerx += SHOT_SPEED * self.vector.x
        self.rect.centery += SHOT_SPEED * self.vector.y 

    def ishit(self): 
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):

                if self.vector.x != 0:
                    if self.vector.x > 0 or self.vector.x < 0:
                        return True
                elif self.vector.y != 0:
                    if self.vector.y > 0 or self.vector.y < 0:
                        return True
        return False

    def update(self):
        self.fly()
        if self.ishit():
            self.vector.x, self.vector.y = 0, 0