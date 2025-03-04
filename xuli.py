def draw_background(x_pos_bg):
    image_width = BG_SKINS[selected_skin_index].get_width()

    SCREEN.blit(BG_SKINS[selected_skin_index], (x_pos_bg, y_pos_bg))
    SCREEN.blit(BG_SKINS[selected_skin_index], (x_pos_bg + image_width, y_pos_bg))

    x_pos_bg -= game_speed
    x_pos_bg %= -image_width

    return x_pos_bg  # Trả về giá trị mới để cập nhật


# Trong vòng lặp game:
x_pos_bg = draw_background(x_pos_bg)