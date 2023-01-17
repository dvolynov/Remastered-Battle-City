import pygame
import sprites


class Enemy(sprites.Tank):
    
    def __init__(self, position, sprites):
        paths = {
            "hull": "assets/body_brown.png", 
            "turret": "assets/head_brown.png", 
            "shell": "assets/brown.png"
        }
        hp = 200
        speed = 3
        groups = [sprites['visible'], sprites['obstacle']]
        obstacles = sprites['obstacle']
        visibles = sprites['visible']
        super().__init__(position, paths, groups, hp, speed, obstacles, visibles)