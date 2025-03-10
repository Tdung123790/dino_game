import sys
import pygame
from constants import SCREEN, GAME_MUSIC, WHITE
from game.sound_manager import SoundManager
from game.game_manager import GameManager
from game.menu import menu
from game.SkinManager import skin_manager
#from game.gamestat import
def game_loop():

    sound_manager = SoundManager()
    sound_manager.play_music(GAME_MUSIC)

    game_manager = GameManager()
    game_manager.player.update_skin(skin_manager.get_skin())

    clock = pygame.time.Clock()
    font = pygame.font.Font("Assets/Other/PressStart2P-Regular.ttf", 25)

    running = True
    while running:
        SCREEN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Nhấn ESCAPE thì quay lại menu ban đầu
                menu()
                return

        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_SPACE] or userInput[pygame.K_UP]:
            if not game_manager.player.dino_jump:  # Chỉ phát âm thanh nếu chưa nhảy
                sound_manager.play_jump()

        running = game_manager.update(userInput)

        if not running:
            sound_manager.play_hit()
            pygame.time.wait(500)
            menu(game_manager.death_count, game_manager.points)  # Gọi menu với số lần chết và điểm

        game_manager.points += 1  # Tăng điểm mỗi frame
        if game_manager.points % 100 == 0:
            sound_manager.play_score()  # Phát âm thanh khi đạt mốc điểm ngay lập tức
            game_manager.game_speed+=1

        game_manager.draw()

        # Hiển thị điểm
        score_text = font.render(f"Points: {game_manager.points}", True, (0, 0, 0))
        SCREEN.blit(score_text, (750, 40))

        pygame.display.update()
        clock.tick(30)  # Giữ tốc độ khung hình ổn định


