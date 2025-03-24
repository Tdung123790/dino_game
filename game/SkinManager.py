
class SkinManager:
    def __init__(self):
        self.selected_skin_index = 0

    def set_skin(self, index):
        self.selected_skin_index = index

    def get_skin(self):
        return self.selected_skin_index


skin_manager=SkinManager()

