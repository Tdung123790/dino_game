import pygame
import sys
from dino_game.game.leaderboard_manager import LeaderboardManager
from dino_game.constants import SCREEN, ORANGE, DARK_ORANGE, WHITE, BLACK,font
from dino_game.game.effects import EffectManager
from dino_game.game.image_manager import assets
pygame.init()


def saving_screen(score):
    """Hiển thị màn hình khi chọn lưu"""
    leaderboard_manager = LeaderboardManager()
    player_name = ""
    save_button = pygame.Rect(475, 400, 200, 50)  # Nút "Save"
    input_box = pygame.Rect(425, 300, 300, 50)  # Ô nhập tên
    color_inactive = pygame.Color(ORANGE)
    color_active = pygame.Color(DARK_ORANGE)
    color = color_inactive
    input_active = False
    error_message = ""  # 🔹 Chỉ lưu dưới dạng `str`, không render ngay
    running = True
    while running:
        SCREEN.blit(assets.backgroundsmenu, (0, 0))
        # Hiển thị điểm
        score_text = font.render(f"Score: {score}", True, BLACK)
        SCREEN.blit(score_text, (475, 150))

        # Hiển thị hướng dẫn nhập tên
        title_text = font.render("Enter Your Name", True, BLACK)
        SCREEN.blit(title_text, (410, 225))

        # Ô nhập tên
        pygame.draw.rect(SCREEN, color, input_box, 2)
        text_surface = font.render(player_name, True, WHITE)
        SCREEN.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        # Hiển thị nút Save
        EffectManager.draw_button(SCREEN,save_button,"Save",font,save_button.collidepoint(pygame.mouse.get_pos()))
        # Hiển thị lỗi
        if error_message:
            error_text = font.render(error_message, True, WHITE)
            SCREEN.blit(error_text, (200, 350))

        pygame.display.flip()

        # Xử lý sự kiện nhập tên
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):  # Nhấp vào ô nhập
                    input_active = True
                    color = color_active
                else:
                    input_active = False
                    color = color_inactive

                if save_button.collidepoint(event.pos) and player_name.strip():  # Nhấn Save
                    if leaderboard_manager.is_name_taken(player_name):  # Kiểm tra tên trùng
                        error_message = "Name already taken! Choose another."
                    else:
                        leaderboard_manager.add_score(player_name, score)  # Lưu điểm
                        running = False  # Thoát về menu sau khi lưu
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:  # Nhấn Enter để lưu
                        if player_name.strip():
                            if leaderboard_manager.is_name_taken(player_name):  # Kiểm tra tên trùng
                                error_message = "Name already taken! Choose another."
                            else:
                                leaderboard_manager.add_score(player_name, score)
                                running = False
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]  # Xóa ký tự cuối
                    else:
                        player_name += event.unicode  # Nhập ký tự mới
                if event.key==pygame.K_ESCAPE:
                    running=False