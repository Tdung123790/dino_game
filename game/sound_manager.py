import pygame
import os
from constants import SOUND_DIR, MENU_MUSIC, GAME_MUSIC
pygame.mixer.pre_init(44100, -16, 2, 512)  # Giảm buffer để giảm delay
pygame.init()
pygame.mixer.init()


class SoundManager:
    def __init__(self):
        self.jump_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "jump_sound.wav"))
        self.hit_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "dead_sound.wav"))
        self.score_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "point_get_sound.wav"))

    def play_music(self, music_file):
        pygame.mixer.music.stop()

        # Nếu `music_file` đã chứa `SOUND_DIR`, không nối thêm
        if not music_file.startswith(SOUND_DIR):
            music_file = os.path.join(SOUND_DIR, music_file)

        if os.path.exists(music_file):  # Kiểm tra file tồn tại
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        else:
            print(f"⚠ Lỗi: Không tìm thấy file nhạc {music_file}")

    def play_jump(self):
        self.jump_sound.play()

    def play_hit(self):
        self.hit_sound.play()

    def play_score(self):
        self.score_sound.play()

