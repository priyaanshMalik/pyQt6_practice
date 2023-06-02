from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QTextDocument
from PyQt6.QtCore import Qt, QRectF 


class UI(QWidget):
    def __init__(self):
        super().__init__()
        # self.setGeometry(200,200,700,300)
        self.setWindowTitle("PyQt6 Drawing")

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        brush = QBrush(Qt.BrushStyle.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(100, 150, 90, 60)
        document = QTextDocument()
        rect2 = QRectF(50,50,250,250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>Python</b> <h1>hihihihih</h1>")
        document.drawContents(qp)
        qp.end()


app = QApplication([])
window = UI()
window.show()
app.exec()
