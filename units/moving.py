import pygame
from units.obstacle import Obstacle


class Moving(Obstacle):

    def __init__(self, position, path, groups, hp, speed, obstacles):
        super().__init__(position, path, groups, hp)
        self.obstacles = obstacles
        self.vector = pygame.math.Vector2(0, 0)
        self.speed = speed

    def _premove(self):
        pass

    def _move(self, speed):
        self._premove()
        
        self.rect.x += self.vector.x * speed
        self._collision('horisontal')
        self.rect.y += self.vector.y * speed
        self._collision('vertical')

    def _collision(self, direction):
        for sprite in self.obstacles:
            if sprite.rect.colliderect(self.rect) and self is not sprite:
                match direction:
                    case 'horisontal':
                        if self.vector.x > 0:
                            self.rect.right = sprite.rect.left
                        if self.vector.x < 0:
                            self.rect.left = sprite.rect.right
                    case 'vertical':
                        if self.vector.y > 0:
                            self.rect.bottom = sprite.rect.top
                        if self.vector.y < 0:
                            self.rect.top = sprite.rect.bottom

    def _set_vector(self, degree):
        match degree:
            case 0:   self.vector = pygame.math.Vector2(0, -1)
            case 180: self.vector = pygame.math.Vector2(0, 1)
            case 90:  self.vector = pygame.math.Vector2(-1, 0)
            case -90: self.vector = pygame.math.Vector2(1, 0)

    def _rotate_action(self, degree):
        self._set_vector(degree)