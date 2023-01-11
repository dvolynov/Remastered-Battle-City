import pygame


class Turret:
    
    def __init__(self, pos, image_origin, tank_rect):
        self.image_origin = image_origin
        self.image = self.image_origin
        self.rect = self.image.get_rect(topleft = pos)
        self.tank_rect = tank_rect
        self.vector = pygame.math.Vector2()
        self.vector.x, self.vector.y = (0, -1)

    def rotate(self, vector):
        direction = (int(vector.x), int(vector.y))
        match direction: 
            case (0, -1):
                deg = 0
                self.rect.centerx = self.tank_rect.centerx
                self.rect.centery = self.tank_rect.centery - 24
            case (0, 1):
                deg = 180
                self.rect.centerx = self.tank_rect.centerx
                self.rect.centery = self.tank_rect.centery + 23
            case (-1, 0):
                deg = 90
                self.rect.centerx = self.tank_rect.centerx - 49
                self.rect.centery = self.tank_rect.centery + 25
            case (1, 0):
                deg = -90
                self.rect.centerx = self.tank_rect.centerx - 2
                self.rect.centery = self.tank_rect.centery + 25
            case _:
                deg = 0
        self.image = pygame.transform.rotate(self.image_origin, deg)

    def draw(self):
        pass