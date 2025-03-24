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

        self.music_files = {
            "menu": f"{SOUND_DIR}/bg_music_menu.mp3",
            "game": f"{SOUND_DIR}/bg_music_game.mp3"
        }
        self.current_music = None

    def play_jump(self):
        self.jump_sound.play()

    def play_hit(self):
        self.hit_sound.play()

    def play_score(self):
        self.score_sound.play()

    def play_music(self, music_type):
        """Phát nhạc nền dựa trên trạng thái menu hoặc game"""
        if music_type not in self.music_files:
            return

        if self.current_music == self.music_files[music_type]:
            return

        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.music_files[music_type])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.current_music = self.music_files[music_type]

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None