import pygame
import units


class Tank(units.Moving):

    def __init__(self, position, paths, groups, hp, speed, obstacles, visibles):
        super().__init__(position, paths['hull'], groups, hp, speed, obstacles)

        self.turret = Turret(
            position = position, 
            path = paths['turret'],     
            groups = visibles,
            vector = pygame.math.Vector2(0, -1),
            tank = self
        )

    def _move_action(self):
        self.turret._move()

    def _draw(self, surface, position):
        surface.blit(self.image, position)

        offset = self.rect.topleft - position
        position_turret = self.turret.rect.topleft - offset
        self.turret._custom_draw(surface, position_turret)


class Turret(units.Sprite):

    def __init__(self, position, path, groups, vector, tank):
        super().__init__(position, path, groups)
        self.position = position
        self.vector = vector
        self.tank = tank

        self._move()

    def _move(self):
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

    def _set_vector(self, degree):
        match degree:
            case 0:   self.vector = pygame.math.Vector2(0, -1)
            case 180: self.vector = pygame.math.Vector2(0, 1)
            case 90:  self.vector = pygame.math.Vector2(-1, 0)
            case -90: self.vector = pygame.math.Vector2(1, 0)

    def _rotate_action(self, degree):
        self._set_vector(degree)

    def _draw(self, surface, position):
        pass

    def _custom_draw(self, surface, position):
        surface.blit(self.image, position)