import pygame
from units.turret import Turret


class Tank(pygame.sprite.Sprite):
    
    def __init__(self, pos, speed, reloading, shot_speed, path, groups, obstacle_sprites):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites

        self.image_origin = pygame.image.load(path[0]).convert_alpha()
        self.image_head_origin = pygame.image.load(path[1]).convert_alpha()
        self.image_shell_origin = pygame.image.load(path[2]).convert_alpha()

        self.image = self.image_origin
        self.rect = self.image.get_rect(topleft = pos)
        self.vector = pygame.math.Vector2()

        self.speed = speed
        self.reloading = reloading
        self.cur_reloading = reloading
        self.shot_speed = shot_speed

        self.turret = Turret(pos, self.image_head_origin, self.rect)

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
        match direction:
            case (0, -1):
                deg = 0
            case (0, 1):
                deg = 180
            case (-1, 0):
                deg = 90
            case (1, 0):
                deg = -90
        self.image = pygame.transform.rotate(self.image_origin, deg)
        self.rect = self.image.get_rect(center = self.rect.center)

    def shot(self):
        pass

        # if self.cur_reload >= self.reload:
        #     pos = (self.rect_head.centerx, self.rect_head.centery)
        #     Shell(pos, self.vector_head, self.image_shell_origin, self.groups, self.obstacle_sprites)
        #     self.cur_reload = 0
        # else:
        #     self.cur_reload += 0.09