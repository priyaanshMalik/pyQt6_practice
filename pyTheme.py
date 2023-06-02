from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Window.resize(934, 739)
        Window.setStyleSheet(
            "QMenuBar, QStatusBar{\n"
            "background-color:#30A2FF;\n"
            "color:white;\n"
            "border:2px solid white;\n"
            "}\n"
            "\n"
            ""
        )
        Window.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=Window)
        self.centralwidget.setStyleSheet("background-color:rgb(173, 216, 230);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet(
            "*{\n"
            "    background-color:  #DDE6ED\n"
            "\n"
            "}\n"
            "/*VERTICAL SCROLLBAR */ \n"
            "QScrollBar:vertical { \n"
            "    border: none;\n"
            "    background-color: rgb(255,255,255);\n"
            "    width: 14px;\n"
            "    margin: 15px 0 15px 0;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "/*HANDLE BAR VERTICAL */\n"
            " QScrollBar::handle:vertical {\n"
            "    background-color: #005ef4; \n"
            "    min-height: 30px;\n"
            "    border-radius: 7px;\n"
            "}\n"
            "QScrollBar::handle:vertical:hover{ \n"
            "    background-color: #394867;\n"
            "}\n"
            "\n"
            "/*BTN TOP-SCROLLBAR */ \n"
            "QScrollBar::sub-line:vertical { \n"
            "    border: none;\n"
            "    background-color: #005ef4; \n"
            "    height: 15px;\n"
            "    border-top-left-radius: 7px; \n"
            "    border-top-right-radius: 7px; \n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "/*BTN BOTTOM-SCROLLBAR */\n"
            "QScrollBar::add-line:vertical { \n"
            "    border: none;\n"
            "    background-color: #005ef4; \n"
            "    height: 15px;\n"
            "    border-bottom-left-radius: 7px; \n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:pressed, QScrollBar::add-line:vertical:pressed { \n"
            "    background-color: rgb(59, 59, 90);\n"
            "}\n"
            "\n"
            "/*reset arrows*/\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { \n"
            "    background: none;\n"
            "}"
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -575, 900, 1218))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtWidgets.QFrame(parent=self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)
        self.reply_1 = QtWidgets.QLabel(parent=self.frame)
        self.reply_1.setMinimumSize(QtCore.QSize(600, 100))
        self.reply_1.setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reply_1.setFont(font)
        self.reply_1.setStyleSheet(
            "QLabel{background-color:#005ef4;\n"
            "color:white;\n"
            "border-top-left-radius :20px;\n"
            "border-top-right-radius : 30px; \n"
            "border-bottom-right-radius : 30px; \n"
            "margin:10px;\n"
            "}\n"
            "QLabel:hover{\n"
            "background-color: #0087f4;\n"
            "border:1px solid white;\n"
            "}"
        )
        self.reply_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.reply_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.reply_1.setLineWidth(3)
        self.reply_1.setMidLineWidth(3)
        self.reply_1.setObjectName("reply_1")
        self.gridLayout.addWidget(self.reply_1, 4, 0, 1, 1)
        self.query_1 = QtWidgets.QLabel(parent=self.frame)
        self.query_1.setMinimumSize(QtCore.QSize(600, 100))
        self.query_1.setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.query_1.setFont(font)
        self.query_1.setStyleSheet(
            "QLabel{\n"
            "background-color: #eff2f9;\n"
            "border-top-left-radius :30px;\n"
            "border-top-right-radius : 20px; \n"
            "border-bottom-left-radius : 30px; \n"
            "margin:10px;\n"
            "}\n"
            "QLabel:hover{\n"
            "background-color: rgb(217, 229, 240);\n"
            "border:1px solid white;\n"
            "}"
        )
        self.query_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.query_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.query_1.setLineWidth(3)
        self.query_1.setMidLineWidth(3)
        self.query_1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.query_1.setWordWrap(False)
        self.query_1.setObjectName("query_1")
        self.gridLayout.addWidget(self.query_1, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setStyleSheet(
            "background-color:white;\n" "border-radius:10px;\n" "padding:10px;\n" ""
        )
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(parent=self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:blue;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(parent=self.horizontalWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "QLineEdit{\n"
            "    background-color:#DDE6ED;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid #005ef4;\n"
            "\n"
            "}"
        )
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.line_2 = QtWidgets.QFrame(parent=self.horizontalWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.pushButton.setStyleSheet(
            "QPushButton{\n"
            "    color: #132d52;\n"
            "    background-color:#DDE6ED;\n"
            "    border:none;\n"
            "    border-radius:5%;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    border:2px solid #005ef4;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    border:4px solid black;\n"
            "}\n"
            "\n"
            ""
        )
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self._send_query)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.horizontalWidget)
        Window.setCentralWidget(self.centralwidget)
        self.actionRestart = QtGui.QAction(parent=Window)
        self.actionRestart.setObjectName("actionRestart")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        # list for queries
        self.query = [self.query_1]
        self.queryNumber = 0
        self.reply = [self.reply_1]
        self.replyNumber = 0
        self.gridCount = 4

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.reply_1.setText(_translate("Window", "HI!!! How can I help you?"))
        self.query_1.setText(_translate("Window", "HI!!!"))
        self.label.setText(_translate("Window", "Ask Here"))
        self.lineEdit.setToolTip(
            _translate(
                "Window",
                '<html><head/><body><p><span style=" font-size:11pt; font-weight:700;">Enter Your Query...</span></p></body></html>',
            )
        )
        self.pushButton.setToolTip(
            _translate(
                "Window",
                '<html><head/><body><p align="center"><span style=" font-size:11pt; font-weight:700;">Ask the ChatBot</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("Window", "SEND"))
        self.actionRestart.setText(_translate("Window", "Restart"))
        QTimer.singleShot(100, self._handle_scrlbar)

    def _handle_scrlbar(self):
        x = self.scrollArea.verticalScrollBar().maximum()
        self.scrollArea.verticalScrollBar().setValue(x)

    def _send_query(self):
        queryStr = self.lineEdit.text()
        print(queryStr)
        self.queryFunc(queryStr)
        self._handle_scrlbar()

    def queryFunc(self, queryTxt):
        self.query.append(QtWidgets.QLabel(text=queryTxt,parent=self.frame))
        self.queryNumber += 1
        self.gridCount += 1
        self.query[self.queryNumber].setMinimumSize(QtCore.QSize(600, 100))
        self.query[self.queryNumber].setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.query[self.queryNumber].setFont(font)
        self.query[self.queryNumber].setStyleSheet(
            "QLabel{\n"
            "background-color: #eff2f9;\n"
            "border-top-left-radius :30px;\n"
            "border-top-right-radius : 20px; \n"
            "border-bottom-left-radius : 30px; \n"
            "margin:10px;\n"
            "}\n"
            "QLabel:hover{\n"
            "background-color: rgb(217, 229, 240);\n"
            "border:1px solid white;\n"
            "}"
        )
        self.query[self.queryNumber].setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.query[self.queryNumber].setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.query[self.queryNumber].setLineWidth(3)
        self.query[self.queryNumber].setMidLineWidth(3)
        self.query[self.queryNumber].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.query[self.queryNumber].setWordWrap(False)
        self.query[self.queryNumber].setObjectName("query_" + str(self.queryNumber + 1))
        self.gridLayout.addWidget(self.query[self.queryNumber], self.gridCount, 0, 1, 1)

    def replyFunc(self):
        self.reply.append(QtWidgets.QLabel(parent=self.frame))
        self.replyNumber += 1
        self.reply[self.replyNumber].setMinimumSize(QtCore.QSize(600, 100))
        self.reply[self.replyNumber].setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reply[self.replyNumber].setFont(font)
        self.reply[self.replyNumber].setStyleSheet(
            "QLabel{background-color:#005ef4;\n"
            "color:white;\n"
            "border-top-left-radius :20px;\n"
            "border-top-right-radius : 30px; \n"
            "border-bottom-right-radius : 30px; \n"
            "margin:10px;\n"
            "}\n"
            "QLabel:hover{\n"
            "background-color: #0087f4;\n"
            "border:1px solid white;\n"
            "}"
        )
        self.reply[self.replyNumber].setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.reply[self.replyNumber].setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.reply[self.replyNumber].setLineWidth(3)
        self.reply[self.replyNumber].setMidLineWidth(3)
        self.reply[self.replyNumber].setObjectName("reply_" + str(self.queryNumber + 1))
        self.gridLayout.addWidget(self.reply[self.replyNumber], self.gridCount, 0, 1, 1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
