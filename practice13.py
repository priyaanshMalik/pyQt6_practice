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
    QCalendarWidget,
    QMessageBox,
    QPushButton,
)
import sys
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QDate


class Window(QDialog):
    def __init__(self):
        super().__init__()
        # self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt6")
        self._create_messageBox()

    def _create_messageBox(self):
        hbox = QHBoxLayout()

        btn1 = QPushButton("Warning")
        btn1.clicked.connect(self.warning_msg)

        btn2 = QPushButton("Information")
        btn2.clicked.connect(self.info_msg)

        btn3 = QPushButton("About")
        btn3.clicked.connect(self.about_msg)

        btn4 = QPushButton("Yes/No")
        btn4.clicked.connect(self.multiChoiceMSg)

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        vbox = QVBoxLayout()
        self.label = QLabel("...")
        self.label.setFont(QFont("Courier", 16))

        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def warning_msg(self):
        QMessageBox.warning(self, "Warning", "This is  a warning test")

    def info_msg(self):
        QMessageBox.information(self, "Info", "This is  a info msgBOx")

    def about_msg(self):
        QMessageBox.about(self, "About", "about this msg box....lol.")

    def multiChoiceMSg(self):
        message = QMessageBox.question(
            self,
            "abcd",
            "IS PYTHON GOOD? YES/NO",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if message == QMessageBox.StandardButton.Yes:
            self.label.setText("Yes I Like Python")
        else:
            self.label.setText("No I Dont Like Python")


app = QApplication(sys.argv)
win = Window()
win.show()
win.exec()
