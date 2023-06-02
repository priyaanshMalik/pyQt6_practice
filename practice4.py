from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
)
import sys
from PyQt6 import QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt6 Layout")

        # hboxLayout = QHBoxLayout()
        gridLayout = QGridLayout()
        btn1 = QPushButton("click one")
        btn2 = QPushButton("click one")
        btn3 = QPushButton("click one")

        # hboxLayout.addWidget(btn1)
        # hboxLayout.addWidget(btn2)
        # hboxLayout.addWidget(btn3)
        # self.setLayout(hboxLayout)

        gridLayout.addWidget(btn1, 0,0)
        gridLayout.addWidget(btn2, 1,0)
        gridLayout.addWidget(btn3, 2,0, 2, 2)
        self.setLayout(gridLayout)


app = QApplication(sys.argv)
win = Window()
win.show()
app.exec()
