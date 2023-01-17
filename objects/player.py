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
            ammunition=20
        )

    def _draw(self, surface, position):
        offset = self.rect.topleft - position
        # self.ray_tracing(offset, surface)

        surface.blit(self.image, position)

        position_turret = self.turret.rect.topleft - offset
        self.turret._custom_draw(surface, position_turret)

    def ray_tracing(self, offset, surface):
        radius = 300

        for sprite in self.obstacles:
            sprite_position = sprite.rect.center - offset
            tank_position = self.rect.center - offset
            diff = sprite_position - tank_position
            diff = (abs(diff[0]), abs(diff[1]))
            if diff[0] <= radius and diff[1] <= radius:
                pygame.draw.aaline(surface, (0, 0, 0), sprite_position, tank_position)


    def debug(self):
        w, h = pygame.display.get_surface().get_size()
        show(self.hp, x=w/2-100)
        show(self.ammunition, x=w/2-20)
        show(self.turret.reloading//100, x=w/2+40)

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