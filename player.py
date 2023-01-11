import pygame
from units.tank import Tank
from debug import show
from settings import FPS


class Player(Tank):
    
    def __init__(self, pos, speed, reloading, shot_speed, path, groups, obstacle_sprites):
        super().__init__(pos, speed, reloading, shot_speed, path, groups, obstacle_sprites)

    def input(self):
        keys = pygame.key.get_pressed()

        self.vector.x = 0
        self.vector.y = 0
        
        if keys[pygame.K_w]:
            self.vector.y = -1
            self.rotate(self.vector)
        elif keys[pygame.K_s]:
            self.vector.y = 1
            self.rotate(self.vector)
        elif keys[pygame.K_a]:
            self.vector.x = -1
            self.rotate(self.vector)
        elif keys[pygame.K_d]:
            self.vector.x = 1 
            self.rotate(self.vector)

        if keys[pygame.K_UP]:
            self.turret.vector.x = 0
            self.turret.vector.y = -1
            self.turret.rotate(self.turret.vector)
        elif keys[pygame.K_DOWN]:
            self.turret.vector.x = 0
            self.turret.vector.y = 1
            self.turret.rotate(self.turret.vector)
        elif keys[pygame.K_LEFT]:
            self.turret.vector.x = -1
            self.turret.vector.y = 0
            self.turret.rotate(self.turret.vector)
        elif keys[pygame.K_RIGHT]:
            self.turret.vector.x = 1
            self.turret.vector.y = 0
            self.turret.rotate(self.turret.vector)
        
        if keys[pygame.K_SPACE]:
            self.shot()

        # Debug --------------------
        if keys[pygame.K_f]:
            show(FPS)
        if keys[pygame.K_v]:
            show(self.vector)
        if keys[pygame.K_h]:
            show(self.turret.vector)
        # Debug --------------------

    def update(self):
        self.input()
        self.move(self.speed)
        self.turret.update(self.rect)