

import pygame
import os

# Khởi tạo pygame
pygame.init()
pygame.font.init()

# Kích thước màn hình
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (101, 67, 33)
ORANGE = (255, 140, 0)
DARK_ORANGE = (220, 80, 40)


# Đường dẫn tài nguyên
ASSETS_DIR = "Assets"
SOUND_DIR = os.path.join(ASSETS_DIR, "Sound")

# Nhạc nền
MENU_MUSIC = os.path.join(SOUND_DIR, "bg_music_menu.mp3")
GAME_MUSIC = os.path.join(SOUND_DIR, "bg_music_game.mp3")
