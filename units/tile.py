import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, path, groups):
        super().__init__(groups)
        self.groups = groups
        
        self.size = size
        self.pos  = pos
        self.set_new_image(path)
        self.path_broken = 'assets/ground.png'

    def hit(self, damage):
        if hasattr(self, 'hp'):
            self.hp -= damage
            
            if self.hp <= 0:
                self.set_new_image(self.path_broken)
                self.remove_self()

            for i, path in enumerate(self.paths_hit):
                if self.hp <= damage * (len(self.paths_hit) - i):
                    self.set_new_image(path)

    def set_new_image(self, path):
        image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft = self.pos)

    def remove_self(self):
        for group in self.groups:
            group.remove(self)