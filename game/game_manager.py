import pygame
import random
from game.player import Dinosaur
from game.obstacles import SmallCactus, LargeCactus, Bird
from game.cloud import Cloud
from constants import SCREEN
from game.SkinManager import skin_manager
from game.image_manager import assets
class GameManager:
    def __init__(self):
        self.game_speed = 20
        self.death_count = 0
        self.obstacles = []
        self.points=0
        self.player = Dinosaur(skin_manager.get_skin())
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        cloud_image = assets.cloud
        self.cloud = Cloud(cloud_image)
    def update(self, userInput):
        self.player.update(userInput)

        # Sinh chướng ngại vật ngẫu nhiên
        if len(self.obstacles) == 0:
            obstacle_choice = random.randint(0, 2)

            if obstacle_choice == 0:
                self.obstacles.append(SmallCactus(assets.small_cactus_skins[skin_manager.get_skin()]))
            elif obstacle_choice == 1:
                self.obstacles.append(LargeCactus(assets.large_cactus_skins[skin_manager.get_skin()]))
            elif obstacle_choice == 2:
                self.obstacles.append(Bird(assets.bird_skins[skin_manager.get_skin()]))

        for obstacle in self.obstacles:
            obstacle.update(self.game_speed, self.obstacles)

            if self.player.dino_rect.colliderect(obstacle.rect):

                pygame.time.delay(1000)
                self.death_count += 1
                return False  # Chết thì quay lại menu
        return True

    def draw(self):
        self.draw_background()
        self.cloud.draw(SCREEN)
        self.cloud.update(self.game_speed)
        self.player.draw(SCREEN)
        for obstacle in self.obstacles:
            obstacle.draw(SCREEN)

    def draw_background(self):
        """Vẽ background chạy liên tục"""
        image_width =assets.track_skins[skin_manager.get_skin()].get_width()
        SCREEN.blit(assets.track_skins[skin_manager.get_skin()], (self.x_pos_bg, self.y_pos_bg))
        SCREEN.blit(assets.track_skins[skin_manager.get_skin()], (self.x_pos_bg + image_width, self.y_pos_bg))
        self.x_pos_bg -= self.game_speed

        # Reset vị trí để tạo hiệu ứng cuộn liên tục
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0
