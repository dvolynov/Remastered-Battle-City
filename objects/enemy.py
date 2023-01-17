import pygame
import sprites


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
            ammunition=20
        )