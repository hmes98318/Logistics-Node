# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame{background-image:url(./src/gui/image/LoginBackground.jpg);\n"
"border-radius: 20px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 1, 1001, 42))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_LoginControll = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_LoginControll.setContentsMargins(0, 0, 0, 0)
        self.layout_LoginControll.setSpacing(0)
        self.layout_LoginControll.setObjectName("layout_LoginControll")
        self.LoginMove = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.LoginMove.setMinimumSize(QtCore.QSize(924, 40))
        self.LoginMove.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.LoginMove.setText("")
        self.LoginMove.setObjectName("LoginMove")
        self.layout_LoginControll.addWidget(self.LoginMove)
        self.LoginMin = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.LoginMin.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.LoginMin.setFont(font)
        self.LoginMin.setWhatsThis("")
        self.LoginMin.setStyleSheet("border-image: url(./src/gui/image/WindowMin.jpg);")
        self.LoginMin.setText("")
        self.LoginMin.setIconSize(QtCore.QSize(30, 30))
        self.LoginMin.setObjectName("LoginMin")
        self.layout_LoginControll.addWidget(self.LoginMin)
        self.LoginClose = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.LoginClose.setMinimumSize(QtCore.QSize(1, 0))
        self.LoginClose.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.LoginClose.setFont(font)
        self.LoginClose.setToolTip("")
        self.LoginClose.setStyleSheet("border-image: url(./src/gui/image/WindowClose.jpg);")
        self.LoginClose.setText("")
        self.LoginClose.setIconSize(QtCore.QSize(30, 30))
        self.LoginClose.setObjectName("LoginClose")
        self.layout_LoginControll.addWidget(self.LoginClose)
        self.button_LogicIn = QtWidgets.QPushButton(self.frame)
        self.button_LogicIn.setGeometry(QtCore.QRect(10, 380, 311, 41))
        font = QtGui.QFont()
        font.setFamily("華康粗明體(P)")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.button_LogicIn.setFont(font)
        self.button_LogicIn.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 15px;")
        self.button_LogicIn.setObjectName("button_LogicIn")
        self.ForgetPW = QtWidgets.QLabel(self.frame)
        self.ForgetPW.setGeometry(QtCore.QRect(10, 670, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.ForgetPW.setFont(font)
        self.ForgetPW.setObjectName("ForgetPW")
        self.CreateID = QtWidgets.QLabel(self.frame)
        self.CreateID.setGeometry(QtCore.QRect(10, 650, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        self.CreateID.setFont(font)
        self.CreateID.setObjectName("CreateID")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 250, 311, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.layout_ID = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.layout_ID.setContentsMargins(0, 0, 0, 0)
        self.layout_ID.setSpacing(1)
        self.layout_ID.setObjectName("layout_ID")
        self.frame_ID = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.frame_ID.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.frame_ID.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ID.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ID.setObjectName("frame_ID")
        self.icon_ID = QtWidgets.QLabel(self.frame_ID)
        self.icon_ID.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.icon_ID.setMinimumSize(QtCore.QSize(30, 0))
        self.icon_ID.setMaximumSize(QtCore.QSize(16777215, 30))
        self.icon_ID.setStyleSheet("border-image: url(./src/gui/image/Account_Icon.jpg);")
        self.icon_ID.setText("")
        self.icon_ID.setTextFormat(QtCore.Qt.PlainText)
        self.icon_ID.setObjectName("icon_ID")
        self.input_ID = QtWidgets.QLineEdit(self.frame_ID)
        self.input_ID.setGeometry(QtCore.QRect(40, 10, 261, 27))
        self.input_ID.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.input_ID.setFont(font)
        self.input_ID.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.input_ID.setText("")
        self.input_ID.setMaxLength(100)
        self.input_ID.setFrame(False)
        self.input_ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_ID.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.input_ID.setObjectName("input_ID")
        self.layout_ID.addWidget(self.frame_ID)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 310, 311, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.layout_PW = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.layout_PW.setContentsMargins(0, 0, 0, 0)
        self.layout_PW.setSpacing(1)
        self.layout_PW.setObjectName("layout_PW")
        self.frame_PW = QtWidgets.QFrame(self.horizontalLayoutWidget_5)
        self.frame_PW.setStyleSheet("#frame_PW{background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;}")
        self.frame_PW.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_PW.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_PW.setObjectName("frame_PW")
        self.icon_PW = QtWidgets.QLabel(self.frame_PW)
        self.icon_PW.setGeometry(QtCore.QRect(10, 10, 31, 30))
        self.icon_PW.setMinimumSize(QtCore.QSize(30, 0))
        self.icon_PW.setMaximumSize(QtCore.QSize(16777215, 30))
        self.icon_PW.setStyleSheet("border-image: url(./src/gui/image/Password_Icon.jpg);")
        self.icon_PW.setText("")
        self.icon_PW.setTextFormat(QtCore.Qt.PlainText)
        self.icon_PW.setObjectName("icon_PW")
        self.input_PW = QtWidgets.QLineEdit(self.frame_PW)
        self.input_PW.setGeometry(QtCore.QRect(40, 10, 261, 27))
        self.input_PW.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.input_PW.setFont(font)
        self.input_PW.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.input_PW.setText("")
        self.input_PW.setMaxLength(100)
        self.input_PW.setFrame(False)
        self.input_PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_PW.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.input_PW.setObjectName("input_PW")
        self.layout_PW.addWidget(self.frame_PW)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.button_LogicIn.setText(_translate("LoginWindow", "Login"))
        self.ForgetPW.setText(_translate("LoginWindow", "忘記密碼"))
        self.CreateID.setText(_translate("LoginWindow", "註冊帳號"))
        self.input_ID.setPlaceholderText(_translate("LoginWindow", "帳號"))
        self.input_PW.setPlaceholderText(_translate("LoginWindow", "密碼"))
