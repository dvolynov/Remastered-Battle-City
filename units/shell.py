import pygame


class Shell(pygame.sprite.Sprite):
    def __init__(self, pos, vector, shot_speed, damage, image, groups, obstacle_sprites):
        super().__init__(groups)
        self.visible_sprites = groups[0]
        self.obstacle_sprites = obstacle_sprites
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
        self.vector = self.vector = pygame.math.Vector2()
        self.vector.x = vector.x
        self.vector.y = vector.y
        self.shot_speed = shot_speed
        self.damage = damage

    def fly(self):
        self.rect.centerx += self.shot_speed * self.vector.x
        self.rect.centery += self.shot_speed * self.vector.y 

    def ishit(self): 
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):

                if self.vector.x != 0:
                    if self.vector.x > 0 or self.vector.x < 0:
                        return True
                elif self.vector.y != 0:
                    if self.vector.y > 0 or self.vector.y < 0:
                        return True
        return False

    def update(self):
        self.fly()
        if self.ishit():
            self.visible_sprites.remove(self)