import pygame
import os

CURRENT_DIR = os.path.dirname(__file__)

ASSETS_DIR = os.path.relpath(os.path.join(CURRENT_DIR, "..", "Assets"))
IMAGE_DIR = os.path.join(ASSETS_DIR, "Other")

class AssetManager:
    def __init__(self):
        self.bird_skins = None
        self.large_cactus_skins = None
        self.small_cactus_skins = None
        self.skins = None
        self.ducking_skins = None
        self.jumping_skins = None
        self.running_skins = None
        self.track_skins = None
        self.load_skins()
        self.load_obstacles()
        self.load_backgrounds()
        self.load_tracks()
    def load_images_from_folder(self, folder_path):
        images = []
        for file_name in sorted(os.listdir(folder_path)):
            if file_name.endswith(".png"):
                img_path = os.path.join(folder_path, file_name)
                images.append(pygame.image.load(img_path))
        return images

    def load_skins(self):
        self.running_skins = []
        self.jumping_skins = []
        self.ducking_skins = []
        self.skins = {}

        for folder in sorted(os.listdir(ASSETS_DIR)):
            folder_path = os.path.join(ASSETS_DIR, folder)
            if os.path.isdir(folder_path) and folder.startswith("Dino_"):
                self.running_skins.append(self.load_images_from_folder(os.path.join(folder_path, "Run")))
                self.jumping_skins.append(pygame.image.load(os.path.join(folder_path, "DinoJump.png")))
                self.ducking_skins.append(self.load_images_from_folder(os.path.join(folder_path, "Duck")))

                skin_name = folder.replace("Dino_", "Skin ")
                self.skins[skin_name] = self.running_skins[-1][0]

    def load_obstacles(self):
        self.small_cactus_skins = []
        self.large_cactus_skins = []
        self.bird_skins = []

        for folder in sorted(os.listdir(ASSETS_DIR)):
            folder_path = os.path.join(ASSETS_DIR, folder)
            if os.path.isdir(folder_path) and folder.startswith("Cactus_"):
                self.small_cactus_skins.append(self.load_images_from_folder(os.path.join(folder_path, "Small")))
                self.large_cactus_skins.append(self.load_images_from_folder(os.path.join(folder_path, "Large")))
            elif os.path.isdir(folder_path) and folder.startswith("Bird_"):
                self.bird_skins.append(self.load_images_from_folder(folder_path))

    def load_tracks(self):
        self.track_skins = []
        for folder in sorted(os.listdir(ASSETS_DIR)):
            folder_path = os.path.join(ASSETS_DIR, folder)
            if os.path.isdir(folder_path) and folder.startswith("Track"):
                for file_name in sorted(os.listdir(folder_path)):
                    if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                        file_path = os.path.join(folder_path, file_name)
                        self.track_skins.append(pygame.image.load(file_path))
    def load_backgrounds(self):
        self.cloud = pygame.image.load(os.path.join(IMAGE_DIR, "Cloud.png"))
        self.backgroundsmenu=pygame.image.load(os.path.join(IMAGE_DIR, "background.jpg"))

assets = AssetManager()