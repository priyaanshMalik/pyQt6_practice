from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
    QLabel,
    QLineEdit,
)

# label and lineEdit:
import sys
from PyQt6 import QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()
        verticalLayout = QVBoxLayout()
        self.setLayout(verticalLayout)
        self.lbl = QLabel("Your Name", parent=self)
        self.txt = QLineEdit(parent=self)
        horizontalLayout1 = QHBoxLayout()
        horizontalLayout1.addWidget(self.lbl)
        horizontalLayout1.addWidget(self.txt)
        verticalLayout.addLayout(horizontalLayout1)
        horizontalLayout2 = QHBoxLayout()
        self.btn = QPushButton("Click me")
        horizontalLayout2.addWidget(self.btn)
        verticalLayout.addLayout(horizontalLayout2)
        self.btn.clicked.connect(self.click_btn)

    def click_btn(self):
        name = self.txt.text()
        self.lbl.setText(name)  # change label
        self.txt.clear()
        print(name)


app = QApplication(sys.argv)
win = Window()
win.show()
app.exec()
