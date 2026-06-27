import pygame
from .player import get_resource_path


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        path = get_resource_path("assets/imgs/coin.png")
        try:
            self.image = pygame.image.load(path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((255, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)
