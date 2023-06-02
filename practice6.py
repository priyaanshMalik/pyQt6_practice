from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QGroupBox,
    QHBoxLayout,
    QRadioButton,
    QVBoxLayout,
    QLabel,
)
import sys
from PyQt6.QtGui import QIcon, QFont


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt6 QRadioButton")
        # self.setWindowIcon(QIcon("python.png"))
        self.create_radiobutton()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)
        self.label = QLabel("you have selected: Football")
        vbox.addWidget(self.label)

    def create_radiobutton(self):
        self.groupbox = QGroupBox("WHat is your favourite sport")
        self.groupbox.setFont(QFont("Sanserif", 15))

        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("Footbal")
        self.rad1.setChecked(True)
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("Cricket")
        self.rad2.setFont(QFont("Sanserif", 14))
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("volley")
        self.rad3.setFont(QFont("Sanserif", 14))
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)

        self.groupbox.setLayout(hbox)

    def on_selected(self):
        radio_button=self.sender()

        if radio_button.isChecked():
            self.label.setText("you have selected: "+ radio_button.text())

app = QApplication(sys.argv)
win = Window()
win.show()
win.exec()
