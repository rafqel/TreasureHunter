import pygame
import sys
from modules.config import WIDTH, HEIGHT, FPS, MENU, PLAYING, GAME_OVER, BLACK
from modules.assets import load_background, load_sound, load_music
from modules.states import render_menu, render_game_over, run_game
from modules.utils import get_resource_path

# Inicialização
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunter")
clock = pygame.time.Clock()

# Carrega assets
background = load_background()
coin_sound = load_sound("coin.wav")
victory_sound = load_sound("victory.wav")
defeat_sound = load_sound("defeat.wav")
music_loaded = load_music()

# Estado inicial
current_state = MENU
end_message = ""
music_playing = False

# Variáveis do jogo
player = None
coins = None
enemies = None
victory_sound_played = False
defeat_sound_played = False

# Loop principal
running = True
while running:
    clock.tick(FPS)

    if current_state == MENU and music_playing:
        pygame.mixer.music.stop()
        music_playing = False

    # --- Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if current_state == MENU and event.key == pygame.K_SPACE:
                current_state = PLAYING
                # Reseta o jogo
                player = None
                coins = None
                enemies = None
                victory_sound_played = False
                defeat_sound_played = False
                if music_loaded:
                    pygame.mixer.music.play(-1)
                    music_playing = True

            elif current_state == GAME_OVER and event.key == pygame.K_SPACE:
                current_state = MENU
                if music_playing:
                    pygame.mixer.music.stop()
                    music_playing = False

    # --- Desenha o fundo ---
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(BLACK)

    # --- Estados ---
    if current_state == MENU:
        render_menu(screen)

    elif current_state == PLAYING:
        new_state, end_message, player, coins, enemies, defeat_sound_played, victory_sound_played, music_playing = run_game(
            screen, player, coins, enemies, coin_sound, victory_sound, defeat_sound,
            defeat_sound_played, victory_sound_played, music_playing
        )
        current_state = new_state

    elif current_state == GAME_OVER:
        render_game_over(screen, end_message)

    pygame.display.flip()

pygame.quit()
sys.exit()
