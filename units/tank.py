import pygame
from units.turret import Turret
from units.shell import Shell
from debug import show


class Tank(pygame.sprite.Sprite):
    
    def __init__(self, pos, speed, reloading, shot_speed, damage, hp, ammunition, path, sprites, groups):
        super().__init__(groups)
        self.groups = groups
        self.sprites = sprites

        self.image_origin = pygame.image.load(path[0]).convert_alpha()
        self.image_head_origin = pygame.image.load(path[1]).convert_alpha()
        self.image_shell_origin = pygame.image.load(path[2]).convert_alpha()

        self.shell_size = self.image_shell_origin.get_size()

        self.image = self.image_origin
        self.rect = self.image.get_rect(topleft = pos)
        self.vector = pygame.math.Vector2()

        self.speed = speed

        self.shot_speed = shot_speed
        self.damage = damage
        self.ammunition = ammunition
        self.reloading = reloading * 1000
        self.is_shot_ready = False
        self.cur_reloading = 0
        self.start_reloading = pygame.time.get_ticks()
        self.left_time_reloading = self.get_left_time_reloading()

        self.hp = hp

        self.turret = Turret(pos, self.image_head_origin, self, groups[0])

    def move(self, speed):
        self.rect.x += self.vector.x * speed
        self.collision('horisontal')
        self.rect.y += self.vector.y * speed
        self.collision('vertical')

    def collision(self, direction):
        for sprite in self.sprites['obstacle']:
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

        for sprite in self.sprites['boost']:
            if sprite.rect.colliderect(self.rect):
                match direction:
                    case 'horisontal':
                        if self.vector.x > 0:
                            sprite.add_boost(self)
                        if self.vector.x < 0:
                            sprite.add_boost(self)

                    case 'vertical':
                        if self.vector.y > 0:
                            sprite.add_boost(self)
                        if self.vector.y < 0:
                            sprite.add_boost(self)

    def rotate(self, vector):
        direction = (vector.x, vector.y)
        if direction == (0, -1): deg = 0
        elif direction == (0, 1): deg = 180
        elif direction == (-1, 0): deg = 90
        elif direction == (1, 0): deg = -90
        self.image = pygame.transform.rotate(self.image_origin, deg)
        self.rect = self.image.get_rect(center = self.rect.center)

    def shot(self):
        if self.is_shot_ready and self.ammunition:
            
            if self.turret.vector == (0, -1): pos = (self.rect.centerx, self.turret.rect.top - self.shell_size[1] * 3)
            elif self.turret.vector == (0, 1): pos = (self.rect.centerx, self.turret.rect.bottom + self.shell_size[1] * 3)
            elif self.turret.vector == (-1, 0): pos = (self.turret.rect.left - self.shell_size[0] * 3, self.rect.centery)
            elif self.turret.vector == (1, 0): pos = (self.turret.rect.right + self.shell_size[0] * 10, self.rect.centery)

            Shell(pos, self.turret.vector, self.shot_speed, self.damage, self.image_shell_origin, self.sprites)

            self.ammunition -= 1
            self.is_shot_ready = False
            self.start_reloading = pygame.time.get_ticks()

    def set_shot_ready(self):
        self.cur_reloading = pygame.time.get_ticks()
        self.left_time_reloading = self.get_left_time_reloading()

        if self.left_time_reloading <= 0:
            self.is_shot_ready = True

    def get_left_time_reloading(self):
        left_time_reloading = self.reloading - (self.cur_reloading - self.start_reloading)
        return left_time_reloading if left_time_reloading > 0 else 0

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.remove_self()

    def remove_self(self):
        for group in self.groups:
            group.remove(self)

    def input(self):
        self.vector.x = 0
        self.vector.y = 0

    def update(self):
        self.input()
        self.move(self.speed)
        self.turret.update()
        self.set_shot_ready()