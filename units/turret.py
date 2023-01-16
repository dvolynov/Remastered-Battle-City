import pygame
from debug import show



class Turret:
    
    def __init__(self, pos, image_origin, tank, visible_sprites):
        self.image_origin = image_origin
        self.image = image_origin
        self.rect = self.image.get_rect(topleft = pos)
        self.visible_sprites = visible_sprites
        self.vector = pygame.math.Vector2()
        self.vector.x, self.vector.y = (0, -1)
        self.tank = tank

    def rotate(self, vector):
        self.vector.x = vector.x
        self.vector.y = vector.y
        deg = 0
        if self.vector == (0, -1): deg = 0
        elif self.vector == (0, 1): deg = 180
        elif self.vector == (-1, 0): deg = 90
        elif self.vector == (1, 0): deg = -90
        self.image = pygame.transform.rotate(self.image_origin, deg)

    def move(self):
        if self.vector == (0, -1):
            self.rect.centerx = self.tank.rect.centerx
            self.rect.centery = self.tank.rect.centery - 24
        elif self.vector == (0, 1):
            self.rect.centerx = self.tank.rect.centerx
            self.rect.centery = self.tank.rect.centery + 23
        elif self.vector == (-1, 0):
            self.rect.centerx = self.tank.rect.centerx - 49
            self.rect.centery = self.tank.rect.centery + 25
        elif self.vector == (1, 0):
            self.rect.centerx = self.tank.rect.centerx - 2
            self.rect.centery = self.tank.rect.centery + 25

    def draw(self):
        player = self.visible_sprites.player
        display_surface = self.visible_sprites.display_surface
        half_width = self.visible_sprites.half_width
        half_height = self.visible_sprites.half_height
        offset = self.visible_sprites.offset

        offset.x = player.rect.centerx - half_width
        offset.y = player.rect.centery - half_height

        offset_pos = self.rect.topleft - offset
        display_surface.blit(self.image, offset_pos)

    def update(self):
        self.move()
        self.draw()