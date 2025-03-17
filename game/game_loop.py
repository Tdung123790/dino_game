import sys
import pygame
from dino_game.config.constants import SCREEN, WHITE, font
from dino_game.game.sound_manager import SoundManager
from dino_game.game.game_manager import GameManager
from dino_game.GUI.menu import menu
from dino_game.game.SkinManager import skin_manager
def game_loop():

    sound_manager = SoundManager()
    game_manager = GameManager()
    game_manager.player.update_skin(skin_manager.get_skin())

    clock = pygame.time.Clock()

    running = True
    while running:
        SCREEN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sound_manager.stop_music()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Nhấn ESCAPE thì quay lại menu ban đầu
                sound_manager.stop_music()
                menu()
                return

        userInput = pygame.key.get_pressed()
        running = game_manager.update(userInput)
        if not running:
            menu(game_manager.death_count, game_manager.get_score())  # Gọi menu với số lần chết và điểm


        game_manager.draw()

        # Hiển thị điểm
        score_text = font.render(f"Points: {game_manager.get_score()}", True, (0, 0, 0))
        SCREEN.blit(score_text, (750, 40))

        pygame.display.update()
        clock.tick(30)  # Giữ tốc độ khung hình ổn định


