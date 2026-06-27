import pygame
from modules.utils import get_resource_path
from modules.config import FORBIDDEN_ZONE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        path = get_resource_path("assets/imgs/player.png")
        try:
            self.image = pygame.image.load(path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 70))
        except:
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10, -10)
        self.rect.x = 375
        self.rect.y = 500
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]: dx = -self.speed
        if keys[pygame.K_RIGHT]: dx = self.speed
        if keys[pygame.K_UP]: dy = -self.speed
        if keys[pygame.K_DOWN]: dy = self.speed

        if dx != 0:
            self.rect.x += dx
            if self.rect.colliderect(FORBIDDEN_ZONE):
                self.rect.x -= dx

        if dy != 0:
            self.rect.y += dy
            if self.rect.colliderect(FORBIDDEN_ZONE):
                self.rect.y -= dy
