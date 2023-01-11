import pygame
from units.tank import Tank


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
            self.turret.rotate()
        elif keys[pygame.K_DOWN]:
            self.turret.rotate(self.vector_head)
        elif keys[pygame.K_LEFT]:
            self.turret.rotate(self.vector_head)
        elif keys[pygame.K_RIGHT]:
            self.turret.rotate(self.vector_head)
        
        if keys[pygame.K_SPACE]:
            self.shot()

    def update(self):
        self.input()
        self.move(self.speed)