import pygame
import os

# Lấy thư mục hiện tại của file này
CURRENT_DIR = os.path.dirname(__file__)

# Định nghĩa đường dẫn tương đối
ASSETS_DIR = os.path.relpath(os.path.join(CURRENT_DIR, "..", "Assets"))
IMAGE_DIR = os.path.join(ASSETS_DIR, "Other")

class AssetManager:
    def __init__(self):
        """Load tất cả tài nguyên game"""
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
        """Tự động load tất cả hình ảnh trong thư mục"""
        images = []
        for file_name in sorted(os.listdir(folder_path)):  # Sắp xếp theo tên file để đúng thứ tự
            if file_name.endswith(".png"):  # Chỉ load file PNG
                img_path = os.path.join(folder_path, file_name)
                images.append(pygame.image.load(img_path))
        return images

    def load_skins(self):
        """Tự động load tất cả skin nhân vật từ thư mục"""
        self.running_skins = []
        self.jumping_skins = []
        self.ducking_skins = []
        self.skins = {}

        for folder in sorted(os.listdir(ASSETS_DIR)):  # Duyệt qua các thư mục trong Assets
            folder_path = os.path.join(ASSETS_DIR, folder)
            if os.path.isdir(folder_path) and folder.startswith("Dino_"):  # Chỉ lấy thư mục Dino_
                self.running_skins.append(self.load_images_from_folder(os.path.join(folder_path, "Run")))
                self.jumping_skins.append(pygame.image.load(os.path.join(folder_path, "DinoJump.png")))
                self.ducking_skins.append(self.load_images_from_folder(os.path.join(folder_path, "Duck")))

                # Đặt tên skin theo thư mục (VD: "Dino_1" -> "Classic", "Dino_2" -> "Minecraft")
                skin_name = folder.replace("Dino_", "Skin ")
                self.skins[skin_name] = self.running_skins[-1][0]

    def load_obstacles(self):
        """Tự động load hình ảnh chướng ngại vật"""
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
        """Tự động load tất cả skin đường đi từ thư mục IMAGE_DIR"""
        self.track_skins = []
        for folder in sorted(os.listdir(ASSETS_DIR)):
            folder_path = os.path.join(ASSETS_DIR, folder)
            if os.path.isdir(folder_path) and folder.startswith("Track"):
                for file_name in sorted(os.listdir(folder_path)):  # Duyệt toàn bộ file
                    if file_name.lower().endswith((".png", ".jpg", ".jpeg")):  # Chỉ load ảnh
                        file_path = os.path.join(folder_path, file_name)
                        self.track_skins.append(pygame.image.load(file_path))
    def load_backgrounds(self):
        """Load hình nền"""
        self.cloud = pygame.image.load(os.path.join(IMAGE_DIR, "Cloud.png"))
        self.backgroundsmenu=pygame.image.load(os.path.join(IMAGE_DIR, "background.jpg"))

assets = AssetManager()