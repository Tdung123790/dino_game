class PlayerData:
    """Lưu thông tin của một người chơi"""
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def to_dict(self):
        """Chuyển đổi thành dictionary để lưu vào JSON"""
        return {"name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, data):
        """Tạo đối tượng PlayerData từ dictionary"""
        return cls(data["name"], data["score"])
