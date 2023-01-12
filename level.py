import pygame

import random
import os
import csv

from settings import *

from units import *
from player import Player



class Level(pygame.sprite.Sprite):

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.sprites = {
            'visible': YSortCameraGroup(),
            'obstacle': pygame.sprite.Group(),
            'boost': pygame.sprite.Group()
        }

        self.create_map()

    def create_map(self):
        maps_amount = len(os.listdir('maps'))
        map_id = random.randint(0, maps_amount - 1)
        map_path = "maps/" + os.listdir('maps')[map_id]

        map = []
        for row in csv.reader(open(map_path), delimiter=','):
            map.append(list(row))

        player = (0, 0)
        bushes = []

        for i, row in enumerate(map):
            for j, tile_id in enumerate(row):

                x = j * TILE_SIZE
                y = i * TILE_SIZE
                pos = (x, y)

                Ground(pos, TILE_SIZE, self.sprites)

                match tile_id:
                    case '1':
                        Stone(pos, TILE_SIZE, self.sprites)
                        # Tank((x, y), SPEED, RELOADING, SHOT_SPEED, DAMAGE, 150, 1000, self.sprites)
                    case '2':
                        Box1(pos, TILE_SIZE, self.sprites)
                    case '3':
                        Box2(pos, TILE_SIZE, self.sprites)
                    case '4':
                        player_pos = pos
                    case '5':
                        bushes.append(pos)
                    case '6':
                        Ammunition(pos, TILE_SIZE, self.sprites)

        self.player = Player(player_pos, SPEED, RELOADING, SHOT_SPEED, DAMAGE, self.sprites)

        for pos in bushes:
            Bush(pos, TILE_SIZE, self.sprites)

    def run(self):
        self.sprites['visible'].custom_draw(self.player)
        self.sprites['visible'].update()
 

class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)