from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem, QTableWidget, QVBoxLayout
from PyQt6 import uic


class UI(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("creating Table")
        self._create_table()
        self.setLayout(self.vbox)

    def _create_table(self):
        self.vbox = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        table_widget.setItem(0,0, QTableWidgetItem('Name'))
        table_widget.setItem(0,1, QTableWidgetItem('Email'))
        table_widget.setItem(0,2, QTableWidgetItem('Phone'))

        #adding Items
        table_widget.setItem(1,0, QTableWidgetItem('aplle'))
        table_widget.setItem(1,1, QTableWidgetItem('Email.em@e.com'))
        table_widget.setItem(1,2, QTableWidgetItem('9080980928345'))
        table_widget.setItem(2,0, QTableWidgetItem('bally'))
        table_widget.setItem(2,1, QTableWidgetItem('ballE@gmail.com'))
        table_widget.setItem(2,2, QTableWidgetItem('1232112312'))
        
        self.vbox.addWidget(table_widget)

app = QApplication([])
window = UI()
window.show()
app.exec()
