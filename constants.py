

import pygame
import os

# Screen Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
WHITE=(255,255,255)
BLACK=(0,0,0)
BROWN=(101,67,33)
ORANGE=(255,140,0)
DARK_ORANGE=(220,80,40)
angle = 0  # Góc xoay
scale_factor = 1  # Hệ số phóng to thu nhỏ
scale_direction = 1  # Hướng phóng to thu nhỏ
selected_skin_index = 0
# Assets
RUNNING_1 = [pygame.image.load(os.path.join("Assets/Dino_1", "DinoRun1.png")),
             pygame.image.load(os.path.join("Assets/Dino_1", "DinoRun2.png"))]
JUMPING_1 = pygame.image.load(os.path.join("Assets/Dino_1", "DinoJump.png"))
DUCKING_1 = [pygame.image.load(os.path.join("Assets/Dino_1", "DinoDuck1.png")),
             pygame.image.load(os.path.join("Assets/Dino_1", "DinoDuck2.png"))]

RUNNING_2 = [pygame.image.load(os.path.join("Assets/Dino_2", "DinoRun1.png")),
             pygame.image.load(os.path.join("Assets/Dino_2", "DinoRun2.png"))]
JUMPING_2 = pygame.image.load(os.path.join("Assets/Dino_2", "DinoJump.png"))
DUCKING_2 = [pygame.image.load(os.path.join("Assets/Dino_2", "DinoDuck1.png")),
             pygame.image.load(os.path.join("Assets/Dino_2", "DinoDuck2.png"))]

#load hình ảnh skin
skins = {
        "Classic": pygame.image.load(os.path.join("Assets/Dino_1", "DinoRun1.png")),
        "Minecraft": pygame.image.load(os.path.join("Assets/Dino_2", "DinoRun1.png"))
    }
SMALL_CACTUS_1 = [pygame.image.load(os.path.join("Assets/Cactus_1", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus_1", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus_1", "SmallCactus3.png"))]
LARGE_CACTUS_1 = [pygame.image.load(os.path.join("Assets/Cactus_1", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus_1", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus_1", "LargeCactus3.png"))]

BIRD_1 = [pygame.image.load(os.path.join("Assets/Bird_1", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird_1", "Bird2.png"))]

SMALL_CACTUS_2 = [pygame.image.load(os.path.join("Assets/Cactus_2", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus_2", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus_2", "SmallCactus3.png"))]
LARGE_CACTUS_2 = [pygame.image.load(os.path.join("Assets/Cactus_2", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus_2", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus_2", "LargeCactus3.png"))]

BIRD_2 = [pygame.image.load(os.path.join("Assets/Bird_2", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird_2", "Bird2.png"))]



CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
BG_1 = pygame.image.load(os.path.join("Assets/Other", "Track1.png"))
BG_2 = pygame.image.load(os.path.join("Assets/Other", "Track2.png"))

BGMENU= pygame.image.load(os.path.join("Assets/Other", "background.jpg"))




# Danh sách tổng hợp tất cả skin
RUNNING_SKINS = [RUNNING_1, RUNNING_2]
JUMPING_SKINS = [JUMPING_1, JUMPING_2]
DUCKING_SKINS = [DUCKING_1, DUCKING_2]
SMALL_SKINS= [SMALL_CACTUS_1,SMALL_CACTUS_2]
LARGE_SKINS=[LARGE_CACTUS_1,LARGE_CACTUS_2]
BIRD_SKINS=[BIRD_1,BIRD_2]
BG_SKINS=[BG_1,BG_2]



# Định nghĩa đường dẫn tới âm thanh
SOUND_DIR = "Assets/Sound"
