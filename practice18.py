from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()
        # Loading the ui file with uic module
        uic.loadUi("practice18.ui", self)
        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.slider.valueChanged.connect(self.changed_slider)
        self.label = self.findChild(QLabel, "label")

        # self.slider =QSlider()
        # self.slider.setOrientation (Qt.Horizontal)
        # self.slider.setTickPosition (QSlider. TicksBelow) 
        # self.slider.setTickInterval(10)
        # self.slider.setMaximum(100)
        # self.slider.setMiniimum(100)

    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))
        


app = QApplication([])
window = UI()
window.show()
app.exec()
