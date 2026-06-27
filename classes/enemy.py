import pygame
from .player import get_resource_path


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        path = get_resource_path("assets/imgs/enemy.png")
        try:
            self.image = pygame.image.load(path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10, -10)
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = 3

    def update(self, screen_width):
        self.rect.x += self.speed * self.direction
        if self.rect.right > screen_width or self.rect.left < 0:
            self.direction *= -1
