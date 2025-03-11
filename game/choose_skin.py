import sys
from constants import *
from game.game_loop import game_loop
from game.SkinManager import skin_manager
from game.sound_manager import SoundManager
from game.effects import *
from game.image_manager import assets
def choose_skin():
    current_skin_index = skin_manager.get_skin()  # Lấy skin hiện tại  # Lưu trạng thái skin hiện tại
    sound_manager = SoundManager()
    sound_manager.play_music("bg_music_menu.mp3")  # Phát nhạc menu khi vào giao diện chọn skin

    running = True
    while running:
        SCREEN.blit(assets.backgroundsmenu, (0, 0))

        # Hiển thị tiêu đề
        title_text = font.render("Select Your Skin", True, BLACK)
        SCREEN.blit(title_text, (SCREEN.get_width() // 2 - title_text.get_width() // 2, 100))

        # Hiển thị hình ảnh skin hiện tại
        selected_skin = assets.running_skins[current_skin_index][0]
        skin_rect = selected_skin.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 20))
        SCREEN.blit(selected_skin, skin_rect.topleft)

        btn_left = pygame.Rect(300, SCREEN_HEIGHT // 2 - 25, 50, 50)  # Nút trái
        btn_right = pygame.Rect(750, SCREEN_HEIGHT // 2 - 25, 50, 50)  # Nút phải
        btn_select = pygame.Rect(450, SCREEN_HEIGHT // 2 + 75, 200, 50)
        draw_button(SCREEN, btn_left, "←", font, btn_left.collidepoint(pygame.mouse.get_pos()))
        draw_button(SCREEN, btn_right, "→", font, btn_right.collidepoint(pygame.mouse.get_pos()))
        draw_button(SCREEN, btn_select, "Select", font, btn_select.collidepoint(pygame.mouse.get_pos()))
        # Hiển thị hướng dẫn
        instruction_text = font.render("← / → to change, ESC to return", True, BLACK)
        SCREEN.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT - 100))


        pygame.display.update()

        # Xử lý sự kiện chọn skin
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Trở về menu nếu nhấn ESC
                    running = False
                    from game.menu import menu
                    menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_left.collidepoint(event.pos):  # Chọn skin trước
                    current_skin_index = (current_skin_index - 1) % len(assets.running_skins)
                if btn_right.collidepoint(event.pos):  # Chọn skin tiếp theo
                    current_skin_index = (current_skin_index + 1) % len(assets.running_skins)
                if btn_select.collidepoint(event.pos):  # Xác nhận skin
                    skin_manager.set_skin(current_skin_index)
                    running = False
                    game_loop()  # Chạy lại game với skin mới
