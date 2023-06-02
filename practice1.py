# pyQt basics

import sys
from PyQt6 import QtCore

# all classes for making application window:
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow

from PyQt6.QtGui import QIcon

# other widgets:
from PyQt6.QtWidgets import QPushButton, QLabel


class Window(QMainWindow):  # extends from Qwidget or Qdialog or QMainWindow
    def __init__(self):
        self.i = 0
        super(Window, self).__init__()
        self.setGeometry(200, 200, 400, 400)  # Change  this position argument
        self.setWindowTitle("")
        # self.setFixedHeight(400)
        # self.setFixedWidth(300)
        # self.setWindowOpacity(0.9)
        # self.setWindowIcon(QIcon('abc.png'))
        self.setStyleSheet("background:#000000")
        self._create_button("one", 100)
        self._create_button("two", 200)
        self.show()

    def _create_button(self, txt, pos):
        btn = QPushButton(parent=self)
        btn.setText(txt)
        btn.setStyleSheet("background:yellow; color:red;")
        btn.setGeometry(pos, 50, 100, 100)
        btn.setIcon(QIcon("abc.png"))
        btn.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        print("button click")
        print(self.i)
        self.i += 1


def main():
    app = QApplication(sys.argv)
    window = Window()
    app.exec()


main()
