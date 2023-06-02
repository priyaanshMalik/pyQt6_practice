from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout
import sys
from PyQt6 import QtCore, uic


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 VBoxLayout")
        # self.setWindowIcon(QIcon("python.png"))
        uic.loadUi("practice3.ui", self)
        self.show()

app = QApplication(sys.argv)
ui = Window()
app.exec()
