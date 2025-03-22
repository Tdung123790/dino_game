import pygame
import os
from dino_game.config.constants import SOUND_DIR
pygame.mixer.pre_init(44100, -16, 2, 512)  # Giảm buffer để giảm delay
pygame.init()
pygame.mixer.init()


class SoundManager:
    def __init__(self):
        self.jump_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "jump_sound.wav"))

        self.hit_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "dead_sound.wav"))
        self.score_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "point_get_sound.wav"))
        # Nhạc nền cho menu & game
        self.music_files = {
            "menu": f"{SOUND_DIR}/bg_music_menu.mp3",
            "game": f"{SOUND_DIR}/bg_music_game.mp3"
        }
        self.current_music = None  # Lưu trạng thái nhạc hiện tại

    def play_jump(self):
        self.jump_sound.play()

    def play_hit(self):
        self.hit_sound.play()

    def play_score(self):
        self.score_sound.play()

    def play_music(self, music_type):
        """Phát nhạc nền dựa trên trạng thái menu hoặc game"""
        if music_type not in self.music_files:
            return  # Nếu loại nhạc không hợp lệ thì không làm gì cả

        if self.current_music == self.music_files[music_type]:
            return  # Không đổi nhạc nếu đang phát đúng loại nhạc

        pygame.mixer.music.stop()  # Dừng nhạc hiện tại
        pygame.mixer.music.load(self.music_files[music_type])
        pygame.mixer.music.set_volume(0.5)  # Điều chỉnh âm lượng (0.0 - 1.0)
        pygame.mixer.music.play(-1)  # Lặp vô hạn
        self.current_music = self.music_files[music_type]  # Cập nhật trạng thái nhạc

    def stop_music(self):
        """Dừng nhạc nền"""
        pygame.mixer.music.stop()
        self.current_music = None