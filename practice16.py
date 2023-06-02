from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QDial, QLabel
import sys
from PyQt6.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 QDial Application")
        self.setWindowIcon(QIcon("python.png"))
        self.create_dial()

    def create_dial(self):
        vbox = QVBoxLayout()
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.setStyleSheet("background:red")
        self.dial.valueChanged.connect(self.dial_changed)

        self.label = QLabel("Value: 0")
        self.label.setFont(QFont("Sanserif", 15))
        self.label.setStyleSheet("color:red")

        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def dial_changed(self):
        getValue = self.dial.value()
        self.label.setText("Value: " + str(getValue))


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
