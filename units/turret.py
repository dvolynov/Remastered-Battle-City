import pygame
from debug import show



class Turret:
    
    def __init__(self, pos, image_origin, tank_rect, visible_sprites):
        self.image_origin = image_origin
        self.image = image_origin
        self.rect = self.image.get_rect(topleft = pos)
        self.visible_sprites = visible_sprites
        self.tank_rect = tank_rect
        self.vector = pygame.math.Vector2()
        self.vector.x, self.vector.y = (0, -1)

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
            self.rect.centerx = self.tank_rect.centerx
            self.rect.centery = self.tank_rect.centery - 24
        elif self.vector == (0, 1):
            self.rect.centerx = self.tank_rect.centerx
            self.rect.centery = self.tank_rect.centery + 23
        elif self.vector == (-1, 0):
            self.rect.centerx = self.tank_rect.centerx - 49
            self.rect.centery = self.tank_rect.centery + 25
        elif self.vector == (1, 0):
            self.rect.centerx = self.tank_rect.centerx - 2
            self.rect.centery = self.tank_rect.centery + 25

    def draw(self):
        display_surface = self.visible_sprites.display_surface
        
        half_width = self.visible_sprites.half_width
        half_height = self.visible_sprites.half_height

        offset = self.visible_sprites.offset

        offset.x = self.tank_rect.centerx - half_width
        offset.y = self.tank_rect.centery - half_height

        offset_pos = self.rect.topleft - offset
        display_surface.blit(self.image, offset_pos)

    def update(self, tank_rect):
        self.tank_rect = tank_rect
        self.move()
        self.draw()