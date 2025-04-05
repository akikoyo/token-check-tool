import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from discord_utils import check_token_validity, get_user_info

class TokenManager(QWidget):
    def load_tokens_from_file(self):
        if os.path.exists("TOKEN.txt"):
            with open("TOKEN.txt", "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        return []
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Discord Token Manager & Watcher')
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.tokens = self.load_tokens_from_file()
        layout.addWidget(QLabel('Loaded Tokens from TOKEN.txt'))

        self.check_button = QPushButton('Check Tokens', self)
        self.check_button.clicked.connect(self.check_tokens)
        layout.addWidget(self.check_button)

        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)
        layout.addWidget(QLabel('Token Status:'))
        layout.addWidget(self.result_area)

        self.setLayout(layout)

    def check_tokens(self):
        results = []
        valid_tokens = []
        for token in self.tokens:
            if check_token_validity(token.strip()):
                user_info = get_user_info(token.strip())
                results.append(f"✅ Valid: {user_info['username']}#{user_info['discriminator']}")
                valid_tokens.append(token.strip())
            else:
                results.append("❌ Invalid token")

        # 表示を更新
        self.result_area.setText(os.linesep.join(results))

        # 有効なトークンを valid_tokens.txt に保存
        with open("valid_tokens.txt", "w", encoding="utf-8") as f:
            for token in valid_tokens:
                f.write(token + os.linesep)

if __name__ == '__main__':
    app = QApplication([])
    window = TokenManager()
    window.show()
    app.exec()