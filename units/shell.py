import pygame


class Shell(pygame.sprite.Sprite):
    def __init__(self, pos, vector, shot_speed, damage, image, sprites):
        self.groups = [sprites['visible']]
        super().__init__(self.groups)
        self.sprites = sprites
        
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
        for sprite in self.sprites['obstacle']:
            if sprite.rect.colliderect(self.rect):

                if self.vector.x != 0:
                    if self.vector.x > 0 or self.vector.x < 0:
                        return sprite
                elif self.vector.y != 0:
                    if self.vector.y > 0 or self.vector.y < 0:
                        return sprite
        return False

    def remove_self(self):
        for group in self.groups:
            group.remove(self)

    def update(self):
        self.fly()
        hited = self.ishit()
        if hited:
            self.remove_self()
            hited.hit()