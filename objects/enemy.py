import pygame
import sprites
from debug import show


class Enemy(sprites.Tank):
    
    def __init__(self, position, sprites):
        super().__init__(
            position, 
            paths = {
                "hull": "assets/body_brown.png", 
                "turret": "assets/head_brown.png", 
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

    def _focus_enemy(self):
        for object in self.objects:
            if object.__class__.__name__ == 'Player':
                x_distance = abs(self.view_point[0] - object.view_point[0])
                y_distance = abs(self.view_point[1] - object.view_point[1])

                if x_distance > y_distance:
                    if x_distance <= self.view_range:
                        if self.view_point[0] < object.view_point[0]:
                            self.turret._rotate(-90)
                        else:
                            self.turret._rotate(90)

                        if self.view_point[0] - object.view_point[0] < 50:
                            self.turret._shot()
                else:
                    if y_distance <= self.view_range:
                        if self.view_point[1] < object.view_point[1]:
                            self.turret._rotate(180)
                        else:
                            self.turret._rotate(0)

                        if self.view_point[1] - object.view_point[1] < 50:
                            self.turret._shot()


    def _additional_update(self):
        self._focus_enemy()