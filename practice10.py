from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QGroupBox,
    QHBoxLayout,
    QRadioButton,
    QVBoxLayout,
    QLabel,
    QCheckBox,
    QSpinBox,
    QLineEdit,
    QCalendarWidget
)
import sys
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QDate 


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt6")
        vLayout = QVBoxLayout()
        self.setLayout(vLayout)
        calendar = QCalendarWidget()
        # calendar.setStyleSheet("QToolButton{border:3px solid red;")
        vLayout.addWidget(calendar)
        lbl = QLabel("TODAY: ")
        lbl2 = QLabel(QDate().currentDate().toString())
        hl = QHBoxLayout()
        hl.addWidget(lbl)
        hl.addWidget(lbl2)
        vLayout.addLayout(hl)
app = QApplication(sys.argv)
win = Window()
win.show()
win.exec()
