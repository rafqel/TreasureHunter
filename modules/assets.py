import pygame
from .utils import get_resource_path
from .config import WIDTH, HEIGHT

# Carrega o fundo
def load_background():
    try:
        path = get_resource_path("assets/imgs/background.png")
        bg = pygame.image.load(path).convert()
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        print("Background loaded: background.png")
        return bg
    except Exception as e:
        print(f"Background not found: {e}")
        return None

# Carrega um som
def load_sound(filename):
    try:
        path = get_resource_path(f"assets/sounds/{filename}")
        sound = pygame.mixer.Sound(path)
        print(f"Sound loaded: {filename}")
        return sound
    except Exception as e:
        print(f"Sound not found: {filename} - {e}")
        return None

# Música de fundo
def load_music():
    try:
        path = get_resource_path("assets/sounds/music.wav")
        pygame.mixer.music.load(path)
        print("Music loaded: music.wav")
        return True
    except Exception as e:
        print(f"Music not found: {e}")
        return False