

import pygame


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
ASSETS_DIR = "./Assets"
SOUND_DIR = f"{ASSETS_DIR}/Sound"


#Font
font = pygame.font.Font(f"{ASSETS_DIR}/Other/PressStart2P-Regular.ttf", 25)
fontldb = pygame.font.Font(f"{ASSETS_DIR}/Other/PressStart2P-Regular.ttf", 30)
