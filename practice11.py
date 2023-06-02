from PyQt6.QtWidgets import QApplication, QDialog, QCalendarWidget, QLabel
from PyQt6 import uic
from PyQt6.QtCore import QDate


class UI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("practice11.ui", self)

        # finding the widgets
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.date_today = self.findChild(QLabel, "label_2")
        date = QDate().currentDate().toString()
        self.date_today.setText(date)
        self.label = self.findChild(QLabel, "label")
        self.label.setText(date)
        self.calendar.selectionChanged.connect(self._calendar_date)

    def _calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_str = str(dateselected.toString())
        self.label.setText("Selected: " + date_in_str)


app = QApplication([])
window = UI()
window.show()
app.exec()
