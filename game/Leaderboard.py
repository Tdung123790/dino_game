import pygame
import sys

from dino_game.constants import SCREEN, SCREEN_WIDTH, BLACK, SCREEN_HEIGHT, DARK_ORANGE, fontldb

from dino_game.game.effects import EffectManager
from dino_game.game.image_manager import assets
from dino_game.game.leaderboard_manager import LeaderboardManager  # Lớp trung gian quản lý điểm số

def show_leaderboard():
    """ Hiển thị bảng xếp hạng """
    background = pygame.transform.scale(assets.backgroundsmenu, (1100, 600))
    leaderboard_manager = LeaderboardManager()  # Dùng lớp trung gian để lấy dữ liệu

    running = True
    while running:
        SCREEN.blit(background, (0, 0))

        # Hiển thị tiêu đề
        title_text = fontldb.render("Leaderboard", True, DARK_ORANGE)
        SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

        # Lấy dữ liệu bảng xếp hạng
        top_scores = leaderboard_manager.get_leaderboard()

        # Hiển thị danh sách điểm số
        y_offset = 120
        for i, entry in enumerate(top_scores[:10]):  # Chỉ hiển thị top 10
            score_text = fontldb.render(f"{i+1}. {entry['name']} - {entry['score']}", True, BLACK)
            SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, y_offset))
            y_offset += 40

        # Nút "Back" để quay lại menu
        btn_back = pygame.Rect(450, SCREEN_HEIGHT - 100, 200, 50)
        EffectManager.draw_button(SCREEN, btn_back, "Back", fontldb, btn_back.collidepoint(pygame.mouse.get_pos()))
        pygame.display.update()

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_back.collidepoint(event.pos):
                    running = False


