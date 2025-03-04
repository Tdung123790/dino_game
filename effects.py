import random
import pygame

class EffectManager:
    def __init__(self):
        self.angle = 0
        self.scale_factor = 1
        self.scale_direction = 1
        self.rotation_direction = random.choice([-3, 3])
        self.change_time = pygame.time.get_ticks() + random.randint(1000, 1500)

    def update_scale(self):
        self.scale_factor += self.scale_direction * 0.005
        if self.scale_factor >= 1.2 or self.scale_factor <= 0.8:
            self.scale_direction *= -1
        return self.scale_factor

    def update_rotation(self):
        if pygame.time.get_ticks() >= self.change_time:
            self.rotation_direction = random.choice([-3, 3])
            self.change_time = pygame.time.get_ticks() + random.randint(1000, 3000)
        self.angle += self.rotation_direction
        return self.angle

def draw_text_with_outline(surface, text, font_path, x, y, text_color, outline_color, scale_factor, outline_size=3):
    dynamic_font = pygame.font.Font(font_path, int(36 * scale_factor))
    text_surface = dynamic_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x, y))

    for dx, dy in [(-outline_size, 0), (outline_size, 0), (0, -outline_size), (0, outline_size),
                   (-outline_size, -outline_size), (-outline_size, outline_size),
                   (outline_size, -outline_size), (outline_size, outline_size)]:
        outline_surface = dynamic_font.render(text, True, outline_color)
        outline_rect = outline_surface.get_rect(center=(x + dx, y + dy))
        surface.blit(outline_surface, outline_rect.topleft)

    surface.blit(text_surface, text_rect.topleft)

def draw_button(surface, rect, text, font, hover=False):
    main_color = (255, 165, 0) if not hover else (255, 140, 0)  # Màu cam, sáng hơn khi hover
    border_color = (139, 69, 19)  # Viền nâu
    white = (255, 255, 255)

    pygame.draw.rect(surface, border_color, (rect.x - 8, rect.y - 8, rect.width + 16, rect.height + 16))
    pygame.draw.rect(surface, white, (rect.x - 4, rect.y - 4, rect.width + 8, rect.height + 8))
    pygame.draw.rect(surface, main_color, rect)

    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)