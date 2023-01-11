import pygame

import random
import os
import csv

from settings import *
from config import *

from units import Tile
from player import Player


class Level(pygame.sprite.Sprite):

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visile_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        maps_amount = len(os.listdir('maps'))
        map_id = random.randint(0, maps_amount - 1)
        map_path = "maps/" + os.listdir('maps')[map_id]

        map = []
        for row in csv.reader(open(map_path), delimiter=','):
            map.append(list(row))

        player = (0, 0)
        grass = []

        for i, row in enumerate(map):
            for j, tile_id in enumerate(row):

                x = j * TILE_SIZE
                y = i * TILE_SIZE

                if tile_id == '0':
                    continue
                elif tile_id == '4':
                    player_pos = (x, y)
                elif tile_id == '5':
                    grass.append((x, y))
                else:
                    Tile((x, y), TILE_SIZE, images[tile_id], [self.visile_sprites, self.obstacle_sprites])

        self.player = Player(player_pos, SPEED, RELOADING, SHOT_SPEED, images['4'], [self.visile_sprites], self.obstacle_sprites)

        for x, y in grass:
            Tile((x, y), TILE_SIZE, images['5'], [self.visile_sprites])

    def run(self):
        self.visile_sprites.custom_draw(self.player)
        self.visile_sprites.update()
 

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