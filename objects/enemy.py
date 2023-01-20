import pygame
import sprites
import random


class Enemy(sprites.Tank):
    
    def __init__(self, position, sprites, player):
        super().__init__(
            position, 
            paths = {
                "hull": "assets/body_brown.png", 
                "turret": "assets/head_brown.png", 
                "shell": "assets/bullet.png",
                "destroyed": "assets/body_brown_destroyed.png",
            }, 
            groups = [sprites['visible'], sprites['obstacle'], sprites['object']],
            hp = 200, 
            speed = 3, 
            obstacles = sprites['obstacle'], 
            visibles = sprites['visible'], 
            ammunition = 20,
            objects = sprites['object']
        )

        self.player = player

    def _input(self): 
        to_add = 80
        dirs = [0, 180, 90, -90]

        for _ in range(to_add):
            dirs.append(self.rotation)

        dir_id = random.randint(0, len(dirs) - 1)

        self._rotate(dirs[dir_id])
        self._move(self.speed)

    def _focus_enemy(self):
        x_distance = abs(self.view_point[0] - self.player.view_point[0])
        y_distance = abs(self.view_point[1] - self.player.view_point[1])

        if x_distance > y_distance:
            if x_distance <= self.view_range:
                if self.view_point[0] < self.player.view_point[0]:
                    self.turret._rotate(-90)
                    if self.player.rect.topleft[1] <= self.view_point[1] <= self.player.rect.bottomleft[1]:
                        self.turret._shot()
                else:
                    self.turret._rotate(90)
                    if self.player.rect.topright[1] <= self.view_point[1] <= self.player.rect.bottomright[1]:
                        self.turret._shot()
        else:
            if y_distance <= self.view_range:
                if self.view_point[1] < self.player.view_point[1]:
                    self.turret._rotate(180)
                    if self.player.rect.topleft[0] <= self.view_point[0] <= self.player.rect.topright[0]:
                        self.turret._shot()
                else:
                    self.turret._rotate(0)
                    if self.player.rect.bottomleft[0] <= self.view_point[0] <= self.player.rect.bottomright[0]:
                        self.turret._shot()


    def _additional_update(self):
        self._focus_enemy()