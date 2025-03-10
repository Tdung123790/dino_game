import json

class PlayerData:
    DATA_FILE = "player_data.json"

    def __init__(self, name="Player"):
        """Khởi tạo dữ liệu người chơi"""
        self.name = name
        self.score = 0
        self.death_count = 0
        self.load_data()

    def load_data(self):
        """Đọc dữ liệu từ file nếu tồn tại"""
        try:
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)
                if self.name in data:
                    self.score = data[self.name]["score"]
                    self.death_count = data[self.name]["death_count"]
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Nếu chưa có file, giữ nguyên dữ liệu mặc định

    def save_data(self):
        """Lưu dữ liệu người chơi vào file"""
        try:
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data[self.name] = {"score": self.score, "death_count": self.death_count}

        with open(self.DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
