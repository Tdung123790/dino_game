from PyQt6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QFileDialog

from PyQt6.QtWidgets import QDialog, QMessageBox
from dino_game.data.leaderboard_manager import LeaderboardManager  # Quản lý bảng điểm
from dino_game.GUI.saving_data2 import Ui_Dialog  # UI của PyQt6

class DialogNhapTen(QDialog):
    def __init__(self, score):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.leaderboard_manager = LeaderboardManager()
        self.score = score  # Lưu điểm số

        # Hiển thị điểm số trong QLabel
        self.ui.label_score.setText(f"Score: {self.score}")

        # Gán sự kiện cho nút Save
        self.ui.pushButton.clicked.connect(self.save)

    def save(self):
        player_name = self.ui.inputname.text().strip()

        if not player_name:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên!")
            return

        if self.leaderboard_manager.is_name_taken(player_name):
            QMessageBox.warning(self, "Lỗi", "Tên đã tồn tại, hãy chọn tên khác!")
        else:
            self.leaderboard_manager.add_score(player_name, self.score)
            QMessageBox.information(self, "Thành công", "Lưu điểm thành công!")
            self.accept()  # Đóng dialog

