

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
IMAGE_DIR = os.path.join(ASSETS_DIR, "Other")

# Nhạc nền
MENU_MUSIC = os.path.join(SOUND_DIR, "bg_music_menu.mp3")
GAME_MUSIC = os.path.join(SOUND_DIR, "bg_music_game.mp3")
'''
# Hình ảnh nhân vật
RUNNING_1 = [pygame.image.load(os.path.join(ASSETS_DIR, "Dino_1/DinoRun1.png")),
             pygame.image.load(os.path.join(ASSETS_DIR, "Dino_1/DinoRun2.png"))]
JUMPING_1 = pygame.image.load(os.path.join(ASSETS_DIR, "Dino_1/DinoJump.png"))
DUCKING_1 = [pygame.image.load(os.path.join(ASSETS_DIR, "Dino_1/DinoDuck1.png")),
             pygame.image.load(os.path.join(ASSETS_DIR, "Dino_1/DinoDuck2.png"))]

RUNNING_2 = [pygame.image.load(os.path.join(ASSETS_DIR, "Dino_2/DinoRun1.png")),
             pygame.image.load(os.path.join(ASSETS_DIR, "Dino_2/DinoRun2.png"))]
JUMPING_2 = pygame.image.load(os.path.join(ASSETS_DIR, "Dino_2/DinoJump.png"))
DUCKING_2 = [pygame.image.load(os.path.join(ASSETS_DIR, "Dino_2/DinoDuck1.png")),
             pygame.image.load(os.path.join(ASSETS_DIR, "Dino_2/DinoDuck2.png"))]
#to chuc lai skin, tao list quuan li=> quan li doi tuong, class chi la lop

# Hình ảnh chướng ngại vật
SMALL_CACTUS_1 = [pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_1/SmallCactus1.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_1/SmallCactus2.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_1/SmallCactus3.png"))]
LARGE_CACTUS_1 = [pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_1/LargeCactus1.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_1/LargeCactus2.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_1/LargeCactus3.png"))]
BIRD_1 = [pygame.image.load(os.path.join(ASSETS_DIR, "Bird_1/Bird1.png")),
          pygame.image.load(os.path.join(ASSETS_DIR, "Bird_1/Bird2.png"))]

SMALL_CACTUS_2 = [pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_2/SmallCactus1.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_2/SmallCactus2.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_2/SmallCactus3.png"))]
LARGE_CACTUS_2 = [pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_2/LargeCactus1.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_2/LargeCactus2.png")),
                   pygame.image.load(os.path.join(ASSETS_DIR, "Cactus_2/LargeCactus3.png"))]
BIRD_2 = [pygame.image.load(os.path.join(ASSETS_DIR, "Bird_2/Bird1.png")),
          pygame.image.load(os.path.join(ASSETS_DIR, "Bird_2/Bird2.png"))]

# Hình ảnh background
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
BG_1 = pygame.image.load(os.path.join(IMAGE_DIR, "Track1.png"))
BG_2 = pygame.image.load(os.path.join(IMAGE_DIR, "Track2.png"))
BGMENU = pygame.image.load(os.path.join(IMAGE_DIR, "background.jpg"))

#load hình ảnh skin
skins = {
        "Classic": pygame.image.load(os.path.join("Assets/Dino_1", "DinoRun1.png")),
        "Minecraft": pygame.image.load(os.path.join("Assets/Dino_2", "DinoRun1.png"))
    }

# Danh sách tổng hợp tất cả skin
RUNNING_SKINS = [RUNNING_1, RUNNING_2]
JUMPING_SKINS = [JUMPING_1, JUMPING_2]
DUCKING_SKINS = [DUCKING_1, DUCKING_2]
SMALL_SKINS = [SMALL_CACTUS_1, SMALL_CACTUS_2]
LARGE_SKINS = [LARGE_CACTUS_1, LARGE_CACTUS_2]
BIRD_SKINS = [BIRD_1, BIRD_2]
BG_SKINS = [BG_1, BG_2]

'''
