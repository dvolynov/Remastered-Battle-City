import pygame


class Enemy():
    
    def __init__(self, pos, speed, reloading, shot_speed, damage, sprites):
        path = ["assets/body_brown.png", "assets/head_brown.png", 'assets/bullet.png']
        hp = 200
        ammunition = 20
        groups = [sprites['visible'], sprites['obstacle']]
        super().__init__(pos, speed, reloading, shot_speed, damage, hp, ammunition, path, sprites, groups)

    def input(self):
        self.vector.x = 0
        self.vector.y = 0