import sys
import traceback

from PyQt6.QtWidgets import QApplication
from menu import MainWindow


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)



if __name__ == "__main__":  # Запуск
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
