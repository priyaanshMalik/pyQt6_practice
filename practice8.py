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
)
import sys
from PyQt6.QtGui import QIcon, QFont


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt6 QRadioButton")
        self._create_spinkbox()

    def _create_spinkbox(self):
        hbox = QHBoxLayout()
        label = QLabel("Laptop Price:")
        self.lineEdit = QLineEdit("100")
        self.spinbox = QSpinBox()
        self.totalResult = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.totalResult)

        self.setLayout(hbox)
        self.spinbox.valueChanged.connect(self._spin_selected)

    def _spin_selected(self):
        if self.lineEdit.text() != 0:
            price = int(self.lineEdit.text())
            totalPrice = self.spinbox.value() * price
            self.totalResult.setText(str(totalPrice))
        else:
            print("Wrong value")


app = QApplication(sys.argv)
win = Window()
win.show()
win.exec()
