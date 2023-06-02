from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QGroupBox,
    QHBoxLayout,
    QRadioButton,
    QVBoxLayout,
    QLabel,
    QCheckBox
)
import sys
from PyQt6.QtGui import QIcon, QFont


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt6 QRadioButton")
        vlay = QVBoxLayout()
        self.setLayout(vlay)
        # layout of window is set

        topLbl = QLabel("LabelTop")
        vlay.addWidget(topLbl)

        hl = QHBoxLayout()
        vlay.addLayout(hl)
        self.midLbl = QLabel("label middle")
        hl.addWidget(self.midLbl)
        self.gb = QGroupBox("Select one")
        hl.addWidget(self.gb)
        self.btmLbl = QLabel("LabelBottom")
        vlay.addWidget(self.btmLbl)

        self.set_gb()

    def set_gb(self):
        vLay = QVBoxLayout()
        self.gb.setLayout(vLay)
        self.chk1=QCheckBox('apple')
        self.chk2=QCheckBox('beer')
        self.chk3=QCheckBox('cake')
        vLay.addWidget(self.chk1)
        vLay.addWidget(self.chk2)
        vLay.addWidget(self.chk3)

        self.chk1.stateChanged.connect(self.gbCheck)
        self.chk2.stateChanged.connect(self.gbCheck)
        self.chk3.stateChanged.connect(self.gbCheck)

    def gbCheck(self):
        price = 0
        if self.chk1.isChecked():
            price+=3
        if self.chk2.isChecked():
            price+=6
        if self.chk3.isChecked():
            price+=8
        self.btmLbl.setText('total: Rs'+ str(price))


app = QApplication(sys.argv)
win = Window()
win.show()
win.exec()
