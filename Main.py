import os.path
import random
import sys

from constants import *
from ClassPlayer import Dinosaur
from ClassObstacle import SmallCactus, LargeCactus, Bird
from effects import EffectManager, draw_text_with_outline, draw_button


pygame.init()

def menu(death_count, points):
    font = pygame.font.Font(os.path.join("Assets/Other", "PressStart2P-Regular.ttf"), 25)
    background = pygame.transform.scale(BGMENU, (1100, 600))
    effects = EffectManager()

    while True:
        SCREEN.blit(background, (0, 0))

        if death_count == 0:
            scale_factor = effects.update_scale()
            draw_text_with_outline(SCREEN, "Dinosaur Game", os.path.join("Assets/Other", "PressStart2P-Regular.ttf"), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE, BLACK, scale_factor, 4)

            # Tạo nút Play - Options - Quit
            btn_1 = pygame.Rect(425, 350, 280, 50)  # Play
            btn_2 = pygame.Rect(425, 425, 280, 50)  # Options
            btn_3 = pygame.Rect(425, 500, 280, 50)  # Quit

            draw_button(SCREEN, btn_1, "Play", font, btn_1.collidepoint(pygame.mouse.get_pos()))
            draw_button(SCREEN, btn_2, "Choose skin", font, btn_2.collidepoint(pygame.mouse.get_pos()))
            draw_button(SCREEN, btn_3, "Quit Game", font, btn_3.collidepoint(pygame.mouse.get_pos()))

        else:
            # Hiển thị thông báo thất bại
            text = font.render("You failed!", True, (0, 0, 0))
            score_text = font.render(f"Your Score: {points}", True, (0, 0, 0))
            SCREEN.blit(score_text, (SCREEN.get_width() // 2 - score_text.get_width() // 2, SCREEN.get_height() // 2 + 50))
            SCREEN.blit(text, (SCREEN.get_width() // 2 - text.get_width() // 2, SCREEN.get_height() // 2))

            # Tạo nút Restart - Quit (Không có Options)
            btn_1 = pygame.Rect(425, 400, 280, 50)  # Restart (thay thế Play)
            btn_3 = pygame.Rect(425, 475, 280, 50)  # Quit

            draw_button(SCREEN, btn_1, "Restart", font, btn_1.collidepoint(pygame.mouse.get_pos()))
            draw_button(SCREEN, btn_3, "Quit Game", font, btn_3.collidepoint(pygame.mouse.get_pos()))

        #Khủng long xoay
        dino_rect = RUNNING[0].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        rotated_dino = pygame.transform.rotate(RUNNING[0], effects.update_rotation())
        new_rect = rotated_dino.get_rect(center=dino_rect.center)
        SCREEN.blit(rotated_dino, new_rect.topleft)
        # Lấy vị trí chuột
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Nhấn ESCAPE thì quay lại menu ban đầu
                menu(death_count=0, points=0)
                return

        # Xử lý khi click vào nút
        if btn_1.collidepoint(mx, my) and click:
            main()  # Nếu death_count > 0, đây sẽ là "Restart"
        if death_count == 0 and btn_2.collidepoint(mx, my) and click:
            choose_skin()  # Chỉ xuất hiện khi death_count == 0
        if btn_3.collidepoint(mx, my) and click:
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(60)

# Hàm chính
def main():
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    death_count = 0
    obstacles = []
    player = Dinosaur()
    running= True
    font = pygame.font.Font(os.path.join("Assets/Other", "PressStart2P-Regular.ttf"), 25)
    def draw_background():
        nonlocal x_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (x_pos_bg + image_width, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed


    def draw_score():
        nonlocal points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        score_text = font.render(f"Points: {points}", True, (0, 0, 0))
        SCREEN.blit(score_text, (750, 40))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        draw_background()
        draw_score()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            obstacle_choice = random.randint(0, 2)
            if obstacle_choice == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_choice == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_choice == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles)

            # Kiểm tra va chạm
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                menu(death_count, points)
                return  # Thoát game loop và quay về menu

        clock.tick(30)
        pygame.display.update()
#Hàm chọn skin
def choose_skin():
    running=True
    SKIN_1 = None
    SKIN_2 = None
    SKIN_3=None
    background = pygame.transform.scale(BGMENU, (1100, 600))
    current_skin_index = 0  # Chỉ mục skin hiện tại
    skins = [SKIN_1, SKIN_2, SKIN_3]  # Danh sách các skin nhân vật
    selected_skin = skins[current_skin_index]  # Skin được chọn

    font = pygame.font.Font(os.path.join("Assets/Other", "PressStart2P-Regular.ttf"), 25)
    while running:
        SCREEN.blit(background, (0, 0))
        # Hiển thị tiêu đề
        title_text = font.render("Select Your Skin", True, BLACK)
        SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

        # Hiển thị skin hiện tại
        #skin_rect = selected_skin.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        #SCREEN.blit(selected_skin, skin_rect.topleft)
        # Tạo nút bấm sử dụng lại draw_button()
        btn_left = pygame.Rect(300, SCREEN_HEIGHT // 2 - 25, 50, 50)  # Nút trái
        btn_right = pygame.Rect(750, SCREEN_HEIGHT // 2 - 25, 50, 50)  # Nút phải

        draw_button(SCREEN, btn_left, "←", font, btn_left.collidepoint(pygame.mouse.get_pos()))
        draw_button(SCREEN, btn_right, "→", font, btn_right.collidepoint(pygame.mouse.get_pos()))
        # Hiển thị hướng dẫn
        instruction_text = font.render("← / → to change, ESC to return", True, BLACK)
        SCREEN.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT - 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=  False
        clock.tick(30)
        pygame.display.update()
# Hiển thị menu khởi động
menu(death_count=0, points=0)