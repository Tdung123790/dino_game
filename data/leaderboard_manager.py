import json
from dino_game.data.player_data import PlayerData

class LeaderboardManager:
    DATA_FILE = "leaderboard.json"

    def __init__(self):
        """Khởi tạo bảng xếp hạng, tự động load dữ liệu"""
        self.players = []  # Danh sách PlayerData
        self.load_data()

    def load_data(self):
        """Tải dữ liệu từ file JSON và chuyển thành danh sách PlayerData"""
        try:
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)
                self.players = [PlayerData.from_dict(entry) for entry in data]  # Chuyển dict thành PlayerData
        except (FileNotFoundError, json.JSONDecodeError):
            self.players = []

    def save_data(self):
        """Lưu danh sách PlayerData vào file JSON"""
        with open(self.DATA_FILE, "w") as file:
            json.dump([player.to_dict() for player in self.players], file, indent=4)

    def add_score(self, name, score):
        """Thêm người chơi vào bảng xếp hạng"""
        new_player = PlayerData(name, score)
        self.players.append(new_player)
        self.players = sorted(self.players, key=lambda x: x.score, reverse=True)[:10]  # Giữ Top 10
        self.save_data()

    def get_leaderboard(self, top_n=10):
        """Lấy danh sách Top N dưới dạng dictionary"""
        return [player.to_dict() for player in self.players[:top_n]]

    def is_name_taken(self, name):
        """Kiểm tra xem tên đã tồn tại trong bảng xếp hạng chưa"""
        return any(player.name.lower() == name.lower() for player in self.players)

