import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, path, groups):
        super().__init__(groups)
        image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)