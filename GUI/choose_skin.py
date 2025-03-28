import sys
from dino_game.config.constants import *
from dino_game.GUI.game_loop import game_loop
from dino_game.game.SkinManager import skin_manager
from dino_game.game.effects import EffectManager
from dino_game.game.image_manager import assets
def choose_skin():
    current_skin_index = skin_manager.get_skin()

    running = True
    while running:
        SCREEN.blit(assets.backgroundsmenu, (0, 0))

        title_text = font.render("Select Your Skin", True, BLACK)
        SCREEN.blit(title_text, (SCREEN.get_width() // 2 - title_text.get_width() // 2, 100))

        selected_skin = assets.running_skins[current_skin_index][0]
        skin_rect = selected_skin.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 20))
        SCREEN.blit(selected_skin, skin_rect.topleft)

        btn_left = pygame.Rect(300, SCREEN_HEIGHT // 2 - 25, 50, 50)
        btn_right = pygame.Rect(750, SCREEN_HEIGHT // 2 - 25, 50, 50)
        btn_select = pygame.Rect(450, SCREEN_HEIGHT // 2 + 75, 200, 50)
        EffectManager.draw_button(SCREEN, btn_left, "←", font, btn_left.collidepoint(pygame.mouse.get_pos()))
        EffectManager.draw_button(SCREEN, btn_right, "→", font, btn_right.collidepoint(pygame.mouse.get_pos()))
        EffectManager.draw_button(SCREEN, btn_select, "Select", font, btn_select.collidepoint(pygame.mouse.get_pos()))
        instruction_text = font.render("← / → to change, ESC to return", True, BLACK)
        SCREEN.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT - 100))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_left.collidepoint(event.pos):
                    current_skin_index = (current_skin_index - 1) % len(assets.running_skins)
                if btn_right.collidepoint(event.pos):
                    current_skin_index = (current_skin_index + 1) % len(assets.running_skins)
                if btn_select.collidepoint(event.pos):
                    skin_manager.set_skin(current_skin_index)
                    running = False
                    game_loop()
