import pygame
import random
from .config import (
    WIDTH, HEIGHT, WHITE, BLACK, GREEN, YELLOW, RED,
    MENU, PLAYING, GAME_OVER,
    GAME_AREA_LEFT, GAME_AREA_TOP, GAME_AREA_RIGHT, GAME_AREA_BOTTOM,
    FORBIDDEN_ZONE, DEBUG
)
from classes.player import Player
from classes.enemy import Enemy
from classes.coin import Coin


def render_menu(screen):
    font_title = pygame.font.Font(None, 72)
    font_text = pygame.font.Font(None, 36)
    title = font_title.render("TREASURE HUNTER", True, WHITE)
    start = font_text.render("Press SPACE to play", True, GREEN)
    commands1 = font_text.render("ARROWS: Move the character", True, YELLOW)
    commands2 = font_text.render("Goal: Collect 10 coins and dodge enemies", True, YELLOW)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 250))
    screen.blit(commands1, (WIDTH // 2 - commands1.get_width() // 2, 350))
    screen.blit(commands2, (WIDTH // 2 - commands2.get_width() // 2, 400))


def render_game_over(screen, end_message):
    font = pygame.font.Font(None, 48)
    font_small = pygame.font.Font(None, 36)
    end_text = font.render(end_message, True, WHITE)
    restart_text = font_small.render("Press SPACE to return to Menu", True, GREEN)
    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, 200))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 300))


def run_game(screen, player, coins, enemies, coin_sound, victory_sound, defeat_sound,
             defeat_sound_played, victory_sound_played, music_playing):
    if player is None:
        player = Player()

    # Gera 10 moedas (garantido)
    if coins is None:
        coins = pygame.sprite.Group()
        tentativas = 0
        max_tentativas = 1000
        while len(coins) < 10 and tentativas < max_tentativas:
            x = random.randint(GAME_AREA_LEFT, GAME_AREA_RIGHT - 30)
            y = random.randint(GAME_AREA_TOP, GAME_AREA_BOTTOM - 30)
            coins.add(Coin(x, y))
            tentativas += 1
        if len(coins) < 10:
            print(f"⚠️ Apenas {len(coins)} moedas geradas! Ajuste a área de jogo.")

    # Gera inimigos
    if enemies is None:
        enemies = pygame.sprite.Group()
        positions = [
            (GAME_AREA_LEFT + 60, GAME_AREA_TOP + 60),
            (GAME_AREA_RIGHT - 100, GAME_AREA_TOP + 100),
            (WIDTH // 2, GAME_AREA_BOTTOM - 80),
        ]
        for x, y in positions:
            enemies.add(Enemy(x, y))
        # Complementa com aleatórios se necessário
        while len(enemies) < 3:
            x = random.randint(GAME_AREA_LEFT, GAME_AREA_RIGHT - 40)
            y = random.randint(GAME_AREA_TOP, GAME_AREA_BOTTOM - 40)
            enemies.add(Enemy(x, y))

    # Atualiza jogador
    player.update()
    # Limites da tela
    if player.rect.left < 0: player.rect.left = 0
    if player.rect.right > WIDTH: player.rect.right = WIDTH
    if player.rect.top < 0: player.rect.top = 0
    if player.rect.bottom > HEIGHT: player.rect.bottom = HEIGHT

    # Atualiza inimigos
    for enemy in enemies:
        enemy.update(WIDTH)

    # --- Colisões ---
    new_state = PLAYING
    end_message = ""
    new_defeat_played = defeat_sound_played
    new_victory_played = victory_sound_played
    new_music_playing = music_playing

    # Derrota
    if pygame.sprite.spritecollide(player, enemies, False):
        if not defeat_sound_played and defeat_sound:
            defeat_sound.play()
            new_defeat_played = True
        new_state = GAME_OVER
        end_message = "DEFEAT! You touched an enemy."
        if music_playing:
            pygame.mixer.music.stop()
            new_music_playing = False

    # Coleta de moedas
    collected = pygame.sprite.spritecollide(player, coins, True)
    if collected and coin_sound:
        coin_sound.play()

    # Vitória
    if len(coins) == 0:
        if not victory_sound_played and victory_sound:
            victory_sound.play()
            new_victory_played = True
        new_state = GAME_OVER
        end_message = "VICTORY! You collected all coins!"
        if music_playing:
            pygame.mixer.music.stop()
            new_music_playing = False

    # --- Desenho ---
    screen.blit(player.image, player.rect)
    coins.draw(screen)
    enemies.draw(screen)

    # Modo de depuração (desenha a zona proibida)
    if DEBUG:
        pygame.draw.rect(screen, RED, FORBIDDEN_ZONE, 2)

    # Contador
    font = pygame.font.Font(None, 36)
    coin_text = font.render(f"Coins remaining: {len(coins)}", True, WHITE)
    screen.blit(coin_text, (10, 10))

    return new_state, end_message, player, coins, enemies, new_defeat_played, new_victory_played, new_music_playing