from player_data import PlayerData

class GameStats:
    def __init__(self, player_name):
        """Quản lý thống kê của người chơi"""
        self.player_data = PlayerData(player_name)  # PlayerData chỉ lưu trữ dữ liệu
        self.current_score = 0
        self.game_speed = 1

    def update(self):
        """Cập nhật điểm số và tốc độ game"""
        self.current_score += 1
        if self.current_score % 100 == 0:
            self.game_speed += 1
            return True  # Để phát âm thanh khi đạt mốc điểm
        return False

    def game_over(self):
        """Xử lý khi game kết thúc"""
        if self.current_score > self.player_data.score:
            self.player_data.score = self.current_score  # Cập nhật điểm cao
        self.player_data.death_count += 1  # Tăng số lần chết

        self.player_data.save_data()  # Lưu dữ liệu mới vào file
        self.current_score = 0  # Reset điểm số
        self.game_speed = 1  # Reset tốc độ

    def reset_stats(self):
        """Reset toàn bộ dữ liệu người chơi"""
        self.player_data.score = 0
        self.player_data.death_count = 0
        self.player_data.save_data()
        self.current_score = 0
        self.game_speed = 1

    def __str__(self):
        return f"Player: {self.player_data.name}, Score: {self.current_score}, High Score: {self.player_data.score}, Deaths: {self.player_data.death_count}, Speed: {self.game_speed}"
