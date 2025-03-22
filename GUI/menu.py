import sys
from dino_game.config.constants import *
from dino_game.game.effects import EffectManager
from dino_game.GUI.gdsaving_data import DialogNhapTen
from dino_game.game.sound_manager import SoundManager
from dino_game.game.image_manager import assets

def menu(death_count=0, points=0):
    background = pygame.transform.scale(assets.backgroundsmenu, (1100, 600))
    effects = EffectManager()
    sound_manager = SoundManager()
    sound_manager.play_music("menu")


    while True:
        SCREEN.blit(background, (0, 0))

        if death_count == 0:
            scale_factor = effects.update_scale()
            effects.draw_text_with_outline(SCREEN, "Dinosaur Game", "Assets/Other/PressStart2P-Regular.ttf",
                                   550, 300, WHITE, BLACK, scale_factor, 4)

            btn_1 = pygame.Rect(400, 350, 280, 50)  # Play
            btn_2 = pygame.Rect(400, 425, 280, 50)  # Options
            btn_3 = pygame.Rect(400, 500, 280, 50)  # Quit
            btn_ldb=pygame.Rect(800, 500, 280, 50)
            effects.draw_button(SCREEN, btn_1, "Play", font, btn_1.collidepoint(pygame.mouse.get_pos()))
            effects.draw_button(SCREEN, btn_2, "Choose skin", font, btn_2.collidepoint(pygame.mouse.get_pos()))
            effects.draw_button(SCREEN, btn_3, "Quit Game", font, btn_3.collidepoint(pygame.mouse.get_pos()))
            effects.draw_button(SCREEN,btn_ldb,"Leaderboard", font,btn_ldb.collidepoint(pygame.mouse.get_pos()))
        else:
            # Hiển thị thông báo thất bại
            text = font.render("You failed!", True, (0, 0, 0))
            score_text = font.render(f"Your Score: {points}", True, (0, 0, 0))
            SCREEN.blit(score_text,
                        (SCREEN.get_width() // 2 - score_text.get_width() // 2, SCREEN.get_height() // 2 + 50))
            SCREEN.blit(text, (SCREEN.get_width() // 2 - text.get_width() // 2, SCREEN.get_height() // 2))

            btn_1 = pygame.Rect(425, 400, 280, 50)  # Restart
            btn_3 = pygame.Rect(425, 475, 280, 50)  # Quit
            btn_save=pygame.Rect(800, 475, 280, 50)
            effects.draw_button(SCREEN, btn_1, "Restart", font, btn_1.collidepoint(pygame.mouse.get_pos()))
            effects.draw_button(SCREEN, btn_3, "Quit Game", font, btn_3.collidepoint(pygame.mouse.get_pos()))
            effects.draw_button(SCREEN, btn_save, "Save", font, btn_save.collidepoint(pygame.mouse.get_pos()))

        # Khủng long xoay
        dino_rect = assets.running_skins[0][0].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        rotated_dino = pygame.transform.rotate(assets.running_skins[0][0], effects.update_rotation())
        new_rect = rotated_dino.get_rect(center=dino_rect.center)
        SCREEN.blit(rotated_dino, new_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Nhấn ESCAPE thì quay lại menu ban đầu
                menu(death_count=0, points=0)
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_1.collidepoint(event.pos):
                    from dino_game.GUI.game_loop import game_loop
                    game_loop()
                if death_count == 0 and btn_2.collidepoint(event.pos):
                    from dino_game.GUI.choose_skin import choose_skin
                    choose_skin()
                if btn_3.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if death_count==0 and btn_ldb.collidepoint(event.pos):
                    from dino_game.GUI.Leaderboard import show_leaderboard
                    show_leaderboard()
                if death_count>0 and btn_save.collidepoint(event.pos):
                    from PyQt6.QtWidgets import QApplication
                    app = QApplication([])
                    dialog = DialogNhapTen(points)
                    dialog.exec()  # PyQt6
                    # from dino_game.game.saving_data import saving_screen
                    #saving_screen(points) #dùng pygame
        pygame.display.update()
        clock.tick(60)
