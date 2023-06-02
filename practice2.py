# use of some basic pyQt6 tools

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6 import QtCore, uic
import sys


# practice2.ui is the corresponding file designed by pyQt designer
#       it is saved as xml file; like this:
# ``.\.venv\Scripts\qt6-tools.exe designer```
# you can use pyuic6.exe file to convert the xml
#       code created from designer into python code, like this:
# ````.\.venv\Scripts\pyuic6.exe  ..\..\practice2.ui -o ..\..\practice3.py -x```
# if useing virtual environment you can find the above two
#       in scripts under virtual env folder. run the files as
#           scripts with appropriate arguments


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("practice2.ui", self)

        self.show()

        button = self.findChild(QPushButton, "pushButton_2")
        button.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        print("butttton clicked")


app = QApplication(sys.argv)
ui = UI()
app.exec()
