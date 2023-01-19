import pygame
import sprites
from debug import show


class Player(sprites.Tank):
    
    def __init__(self, position, sprites):
        super().__init__(
            position, 
            paths = {
                "hull": "assets/body_green.png", 
                "turret": "assets/head_green.png", 
                "shell": "assets/bullet.png"
            }, 
            groups = [sprites['visible'], sprites['obstacle'], sprites['object']],
            hp = 200, 
            speed = 3, 
            obstacles = sprites['obstacle'], 
            visibles = sprites['visible'], 
            ammunition = 20,
            objects = sprites['object']
        )

    def debug(self):
        w, h = pygame.display.get_surface().get_size()
        show(self.hp, x=w/2-100)
        show(self.ammunition, x=w/2-20)
        show(self.turret.reloading//100, x=w/2+40)
        show(self.rect.center, x=w-200)

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
        elif keys[pygame.K_DOWN]:
            self.turret._rotate(180)
        elif keys[pygame.K_LEFT]:
            self.turret._rotate(90)
        elif keys[pygame.K_RIGHT]:
            self.turret._rotate(-90)
        
        if keys[pygame.K_SPACE]:
            self._shot()