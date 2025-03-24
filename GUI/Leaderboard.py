import pygame
import sys

from dino_game.config.constants import SCREEN, SCREEN_WIDTH, BLACK, SCREEN_HEIGHT, DARK_ORANGE, fontldb

from dino_game.game.effects import EffectManager
from dino_game.game.image_manager import assets
from dino_game.data.leaderboard_manager import LeaderboardManager

def show_leaderboard():
    background = pygame.transform.scale(assets.backgroundsmenu, (1100, 600))
    leaderboard_manager = LeaderboardManager()

    running = True
    while running:
        SCREEN.blit(background, (0, 0))

        title_text = fontldb.render("Leaderboard", True, DARK_ORANGE)
        SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

        top_scores = leaderboard_manager.get_leaderboard()

        y_offset = 120
        for i, entry in enumerate(top_scores[:10]):
            score_text = fontldb.render(f"{i+1}. {entry['name']} - {entry['score']}", True, BLACK)
            SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, y_offset))
            y_offset += 40

        btn_back = pygame.Rect(450, SCREEN_HEIGHT - 100, 200, 50)
        EffectManager.draw_button(SCREEN, btn_back, "Back", fontldb, btn_back.collidepoint(pygame.mouse.get_pos()))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_back.collidepoint(event.pos):
                    running = False


