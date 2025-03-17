import pygame
import random
from dino_game.game.player import Dinosaur
from dino_game.game.obstacles import SmallCactus, LargeCactus, Bird
from dino_game.game.cloud import Cloud
from dino_game.config.constants import SCREEN
from dino_game.game.SkinManager import skin_manager
from dino_game.game.image_manager import assets
from dino_game.game.sound_manager import SoundManager


class GameManager:
    def __init__(self):
        self.game_speed = 20
        self.death_count = 0
        self.obstacles = []
        self.points=0
        self.player = Dinosaur(skin_manager.get_skin())
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.cloud = Cloud(assets.cloud)
        self.sound_manager=SoundManager()
        self.sound_manager.play_music("game")
    def update(self, userInput):
        if userInput[pygame.K_SPACE] or userInput[pygame.K_UP]:
            if  not self.player.dino_jump:
                self.sound_manager.play_jump()

        self.player.update(userInput)
        self.update_obstacles()
        self.increase_score()
        if self.check_collision():
            pygame.time.delay(1000)
            self.sound_manager.play_hit()
            self.death_count += 1
            return False  # Trò chơi kết thúc
        return True

    def update_obstacles(self):
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

    def check_collision(self):
        """Kiểm tra va chạm thủ công"""
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            obs_rect = obstacle.get_rect()

            if (player_rect.right > obs_rect.left and player_rect.left < obs_rect.right and
                    player_rect.bottom > obs_rect.top and player_rect.top < obs_rect.bottom):
                return True  # Có va chạm
        return False

    def increase_score(self):
        """Tăng điểm số và tăng tốc độ game"""
        self.points += 1  # Cộng 1 điểm mỗi frame
        if self.points % 100 == 0:  # Khi đạt mốc 100 điểm
            self.sound_manager.play_score()  # Phát âm thanh
            self.game_speed += 1  # Tăng tốc độ game

    def get_score(self):
        """Trả về điểm số hiện tại"""
        return self.points

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
