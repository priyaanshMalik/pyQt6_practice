from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QLabel,
    QLCDNumber,
)
import sys
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTime, QTimer, QDate, Qt


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 300)
        self.setWindowTitle("PyQt6 Timer")
        self.vl = QVBoxLayout()
        self.setLayout(self.vl)
        self.lcd_number()
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.show)

    def lcd_number(self):
        self.lcd = QLCDNumber()
        self.vl.addWidget(self.lcd)

        time = QTime.currentTime()
        text = time.toString("hh:mm:ss")
        self.lcd.setDigitCount(8)
        self.lcd.display(text)

        self.date = QDate()
        print(self.date.currentDate().toString())
        self.dt = QLabel(self.date.currentDate().toString())
        self.dt.setFont(QFont("Courier", 23))
        self.dt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vl.addWidget(self.dt)

    def show(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm:ss")
        print(text)
        self.lcd.setDigitCount(8)
        self.lcd.display(text)

        self.date = QDate()
        print(self.date.currentDate().toString())
        self.dt.setText(self.date.currentDate().toString('dddd, MMMM dd, yyyy'))


app = QApplication(sys.argv)
win = Window()
win.show()
win.exec()
