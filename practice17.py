from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()
        # Loading the ui file with uic module
        uic.loadUi("practice17.ui", self)
        self.combo = self.findChild(QComboBox, "comboBox")
        self.label = self.findChild(QLabel, "label")
        self.combo.currentTextChanged.connect(self.combo_selected)

    def combo_selected(self):
        item = self.combo.currentText()
        self.label.setText("YOu selected: " + item)


app = QApplication([])
window = UI()
window.show()
app.exec()
