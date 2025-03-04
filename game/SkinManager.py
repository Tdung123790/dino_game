class SkinManager:
    def __init__(self):
        self.selected_skin_index = 0  # Skin mặc định

    def set_skin(self, index):
        """Cập nhật skin mới"""
        self.selected_skin_index = index

    def get_skin(self):
        """Trả về skin hiện tại"""
        return self.selected_skin_index


skin_manager=SkinManager()