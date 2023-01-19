import pygame
import random
import os
import csv

import settings
import groups
import objects
import sprites

from debug import show


class Level(pygame.sprite.Sprite):

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.sprites = {
            'visible': groups.YSortCameraGroup(),
            'obstacle': pygame.sprite.Group(),
            'boost': pygame.sprite.Group(),
            'object': pygame.sprite.Group()
        }

        self._create_map()

    def _get_map_from_csv(self):
        maps_amount = len(os.listdir('maps'))
        map_id = random.randint(0, maps_amount - 1)
        map_path = "maps/" + os.listdir('maps')[map_id]

        map = []
        for row in csv.reader(open(map_path), delimiter=','):
            map.append(list(row))

        return map

    def _create_map(self):
        map = self._get_map_from_csv()

        bush_positions = []
        enemy_positions = []

        for i, row in enumerate(map):
            for j, tile_id in enumerate(row):

                x = j * settings.TILE_SIZE
                y = i * settings.TILE_SIZE
                position = pygame.math.Vector2(x, y)
            
                sprites.Ground(position, self.sprites)

                match tile_id:
                    case '1': sprites.Stone(position, self.sprites)
                    case '2': sprites.Box1(position, self.sprites)
                    case '3': sprites.Box2(position, self.sprites)
                    case '4': player_position = position
                    case '5': bush_positions.append(position)
                    case '6': sprites.Ammunition(position, self.sprites)
                    case '7': enemy_positions.append(position)
                    case '8': sprites.Heal(position, self.sprites)

        self.player = objects.Player(player_position, self.sprites)

        for position in enemy_positions:
            objects.Enemy(position, self.sprites, self.player)

        for position in bush_positions:
            sprites.Bush(position, self.sprites)

    def run(self):
        self.sprites['visible'].set_player(self.player)
        self.sprites['visible'].custom_draw()

        self.hood()

    def hood(self):
        w, h = pygame.display.get_surface().get_size()
        
        if self.player.alive:
            show(self.player.hp, x=w/2-100)
            show(self.player.ammunition, x=w/2-20)
            show(self.player.turret.reloading//100, x=w/2+40)
            show(self.player.rect.center, x=w-200, y=h-50)
        else:
            show('Died', x=w/2-80, y=h/2-200, size=100)