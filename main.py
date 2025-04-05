from gui import TokenManager
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    window = TokenManager()
    window.show()
    app.exec()