import pygame
import sprites
from debug import show


class Player(sprites.Tank):
    
    def __init__(self, position, sprites):
        paths = {
            "hull": "assets/body_green.png", 
            "turret": "assets/head_green.png", 
            "shell": "assets/bullet.png"
        }
        hp = 500
        speed = 3
        groups = [sprites['visible'], sprites['obstacle']]
        obstacles = sprites['obstacle']
        visibles = sprites['visible']
        super().__init__(position, paths, groups, hp, speed, obstacles, visibles)

    def debug(self):
        w, h = pygame.display.get_surface().get_size()
        show(self.turret.ammunition, x=w / 2 - 40)
        show(self.turret.reloading // 100, x=w / 2 + 20)

    def _input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self._rotate(0)
            self._move(self.speed)
        elif keys[pygame.K_s]:
            self._rotate(180)
            self._move(self.speed)
        elif keys[pygame.K_a]:
            self._rotate(90)
            self._move(self.speed)
        elif keys[pygame.K_d]:
            self._rotate(-90)
            self._move(self.speed)

        if keys[pygame.K_UP]:
            self.turret._rotate(0)
            self.turret._move()
        elif keys[pygame.K_DOWN]:
            self.turret._rotate(180)
            self.turret._move()
        elif keys[pygame.K_LEFT]:
            self.turret._rotate(90)
            self.turret._move()
        elif keys[pygame.K_RIGHT]:
            self.turret._rotate(-90)
            self.turret._move()
        
        if keys[pygame.K_SPACE]:
            self._shot()