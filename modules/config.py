import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

MENU = 0
PLAYING = 1
GAME_OVER = 2

# ------------------------------------------------------------
# ZONA PROIBIDA (faixa superior com árvores)
# ------------------------------------------------------------
FORBIDDEN_ZONE = pygame.Rect(0, 30, WIDTH, 150)

# ------------------------------------------------------------
# ÁREA DE JOGO (moedas e inimigos nascem aqui)
# ------------------------------------------------------------
MARGEM = 60
GAME_AREA_LEFT = MARGEM + 50
GAME_AREA_TOP = FORBIDDEN_ZONE.bottom + 20
GAME_AREA_RIGHT = WIDTH - MARGEM - 50
GAME_AREA_BOTTOM = HEIGHT - MARGEM - 30

DEBUG = False   # True apenas para testes