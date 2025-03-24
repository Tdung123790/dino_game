import json
from dino_game.data.player_data import PlayerData

class LeaderboardManager:

    def __init__(self):
        self.players = []
        self.DATA_FILE = "leaderboard.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)
                self.players = [PlayerData.from_dict(entry) for entry in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.players = []

    def save_data(self):
        with open(self.DATA_FILE, "w") as file:
            json.dump([player.to_dict() for player in self.players], file, indent=4)

    def add_score(self, name, score):
        new_player = PlayerData(name, score)
        self.players.append(new_player)
        self.players = sorted(self.players, key=lambda x: x.score, reverse=True)[:10]  # Giữ Top 10
        self.save_data()

    def get_leaderboard(self, top_n=10):
        return [player.to_dict() for player in self.players[:top_n]]

    def is_name_taken(self, name):
        return any(player.name.lower() == name.lower() for player in self.players)

