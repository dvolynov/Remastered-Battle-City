import pygame
from units.turret import Turret
from units.shell import Shell


class Tank(pygame.sprite.Sprite):
    
    def __init__(self, pos, speed, reloading, shot_speed, damage, path, groups, obstacle_sprites):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites
        self.visible_sprites = groups[0]

        self.image_origin = pygame.image.load(path[0]).convert_alpha()
        self.image_head_origin = pygame.image.load(path[1]).convert_alpha()
        self.image_shell_origin = pygame.image.load(path[2]).convert_alpha()

        self.shell_size = self.image_shell_origin.get_size()

        self.image = self.image_origin
        self.rect = self.image.get_rect(topleft = pos)
        self.vector = pygame.math.Vector2()

        self.speed = speed
        self.reloading = reloading
        self.cur_reloading = reloading
        self.shot_speed = shot_speed
        self.damage = damage

        self.turret = Turret(pos, self.image_head_origin, self.rect, groups[0])

    def move(self, speed):
        self.rect.x += self.vector.x * speed
        self.collision('horisontal')
        self.rect.y += self.vector.y * speed
        self.collision('vertical')

    def collision(self, direction):
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
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

    def rotate(self, vector):
        direction = (vector.x, vector.y)
        if direction == (0, -1): deg = 0
        elif direction == (0, 1): deg = 180
        elif direction == (-1, 0): deg = 90
        elif direction == (1, 0): deg = -90
        self.image = pygame.transform.rotate(self.image_origin, deg)
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        self.turret.draw()

    def shot(self):
        if self.cur_reloading >= self.reloading:
            
            if self.turret.vector == (0, -1): pos = (self.rect.centerx, self.turret.rect.top - self.shell_size[1] * 3)
            elif self.turret.vector == (0, 1): pos = (self.rect.centerx, self.turret.rect.bottom + self.shell_size[1] * 3)
            elif self.turret.vector == (-1, 0): pos = (self.turret.rect.left - self.shell_size[0] * 3, self.rect.centery)
            elif self.turret.vector == (1, 0): pos = (self.turret.rect.right + self.shell_size[0] * 10, self.rect.centery)

            Shell(pos, self.turret.vector, self.shot_speed, self.damage, self.image_shell_origin, [self.visible_sprites], self.obstacle_sprites)
            self.cur_reloading = 0
        else:
            self.cur_reloading += 0.09