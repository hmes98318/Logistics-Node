# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\MSI GP65\Documents\GitHub\ftpy\src\gui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(100, 0))
        MainWindow.setStyleSheet("#MainWindow{background-color: rgba(255, 255, 255, 0);}")
        self.frame_Main = QtWidgets.QFrame(MainWindow)
        self.frame_Main.setGeometry(QtCore.QRect(-1, -1, 1000, 700))
        self.frame_Main.setStyleSheet("#frame_Main{background-color: rgba(36, 67, 124,250);\n"
"border-radius: 20px;}\n"
"\n"
"")
        self.frame_Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Main.setObjectName("frame_Main")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_Main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 202, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_SwitchPage = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_SwitchPage.setContentsMargins(0, 0, 0, 0)
        self.layout_SwitchPage.setObjectName("layout_SwitchPage")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_SwitchPage.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_SwitchPage.addItem(spacerItem1)
        self.button_Client = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.button_Client.setMinimumSize(QtCore.QSize(200, 70))
        self.button_Client.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.button_Client.setFont(font)
        self.button_Client.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_Client.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.button_Client.setCheckable(False)
        self.button_Client.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.button_Client.setObjectName("button_Client")
        self.layout_SwitchPage.addWidget(self.button_Client)
        spacerItem2 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_SwitchPage.addItem(spacerItem2)
        self.button_Server = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.button_Server.setMinimumSize(QtCore.QSize(200, 70))
        self.button_Server.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(18)
        self.button_Server.setFont(font)
        self.button_Server.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.button_Server.setObjectName("button_Server")
        self.layout_SwitchPage.addWidget(self.button_Server)
        spacerItem3 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_SwitchPage.addItem(spacerItem3)
        self.button_Setting = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.button_Setting.setMinimumSize(QtCore.QSize(200, 40))
        self.button_Setting.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(20)
        self.button_Setting.setFont(font)
        self.button_Setting.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.button_Setting.setObjectName("button_Setting")
        self.layout_SwitchPage.addWidget(self.button_Setting)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_SwitchPage.addItem(spacerItem4)
        self.button_User = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.button_User.setMinimumSize(QtCore.QSize(200, 50))
        self.button_User.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(20)
        self.button_User.setFont(font)
        self.button_User.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.button_User.setObjectName("button_User")
        self.layout_SwitchPage.addWidget(self.button_User)
        spacerItem5 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_SwitchPage.addItem(spacerItem5)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_Main)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 40, 771, 651))
        font = QtGui.QFont()
        font.setFamily("文鼎鬍子體")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("#stackedWidget{background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Client = QtWidgets.QWidget()
        self.Client.setObjectName("Client")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.Client)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 20, 731, 231))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.Layout_cRequireFile = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.Layout_cRequireFile.setContentsMargins(0, 0, 0, 0)
        self.Layout_cRequireFile.setSpacing(10)
        self.Layout_cRequireFile.setObjectName("Layout_cRequireFile")
        self.Layout_cFileInfo = QtWidgets.QHBoxLayout()
        self.Layout_cFileInfo.setSpacing(0)
        self.Layout_cFileInfo.setObjectName("Layout_cFileInfo")
        self.hint_cFilename = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.hint_cFilename.setMaximumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.hint_cFilename.setFont(font)
        self.hint_cFilename.setObjectName("hint_cFilename")
        self.Layout_cFileInfo.addWidget(self.hint_cFilename)
        self.label_cFilename = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_cFilename.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.label_cFilename.setFont(font)
        self.label_cFilename.setText("")
        self.label_cFilename.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cFilename.setWordWrap(False)
        self.label_cFilename.setObjectName("label_cFilename")
        self.Layout_cFileInfo.addWidget(self.label_cFilename)
        self.hint_cFileize = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.hint_cFileize.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.hint_cFileize.setFont(font)
        self.hint_cFileize.setObjectName("hint_cFileize")
        self.Layout_cFileInfo.addWidget(self.hint_cFileize)
        self.label_cFilesize = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_cFilesize.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.label_cFilesize.setFont(font)
        self.label_cFilesize.setText("")
        self.label_cFilesize.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cFilesize.setObjectName("label_cFilesize")
        self.Layout_cFileInfo.addWidget(self.label_cFilesize)
        self.Layout_cRequireFile.addLayout(self.Layout_cFileInfo)
        self.Layout_schedule = QtWidgets.QHBoxLayout()
        self.Layout_schedule.setSpacing(0)
        self.Layout_schedule.setObjectName("Layout_schedule")
        self.hint_schedule = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.hint_schedule.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.hint_schedule.setFont(font)
        self.hint_schedule.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.hint_schedule.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.hint_schedule.setObjectName("hint_schedule")
        self.Layout_schedule.addWidget(self.hint_schedule)
        self.progressBar_RecevieFile = QtWidgets.QProgressBar(self.verticalLayoutWidget_5)
        self.progressBar_RecevieFile.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.progressBar_RecevieFile.setFont(font)
        self.progressBar_RecevieFile.setStyleSheet("#progressBar_RecevieFile{\n"
"border: 2px solid #000;\n"
"border-radius: 10px;\n"
"text-align:center;\n"
"}\n"
"#progressBar_RecevieFile::chunk { \n"
"background-color: rgb(170, 170, 255);\n"
"border-radius: 8px;\n"
"}")
        self.progressBar_RecevieFile.setProperty("value", 24)
        self.progressBar_RecevieFile.setObjectName("progressBar_RecevieFile")
        self.Layout_schedule.addWidget(self.progressBar_RecevieFile)
        self.Layout_cRequireFile.addLayout(self.Layout_schedule)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_PickupNumber = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.input_PickupNumber.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.input_PickupNumber.setFont(font)
        self.input_PickupNumber.setStyleSheet("border-radius: 10px;\n"
"background-color: rgba(13, 95, 160, 100);")
        self.input_PickupNumber.setText("")
        self.input_PickupNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.input_PickupNumber.setObjectName("input_PickupNumber")
        self.horizontalLayout.addWidget(self.input_PickupNumber)
        self.button_RequireFile = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.button_RequireFile.setMinimumSize(QtCore.QSize(200, 50))
        self.button_RequireFile.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.button_RequireFile.setFont(font)
        self.button_RequireFile.setStyleSheet("border-radius: 10px;\n"
"color: rgb(170, 255, 255);\n"
"background-color: rgba(13, 95, 160, 200);")
        self.button_RequireFile.setObjectName("button_RequireFile")
        self.horizontalLayout.addWidget(self.button_RequireFile)
        self.Layout_cRequireFile.addLayout(self.horizontalLayout)
        self.label_spacer3_2 = QtWidgets.QLabel(self.Client)
        self.label_spacer3_2.setGeometry(QtCore.QRect(160, 190, 12, 45))
        self.label_spacer3_2.setMinimumSize(QtCore.QSize(12, 0))
        self.label_spacer3_2.setMaximumSize(QtCore.QSize(4, 16777215))
        self.label_spacer3_2.setText("")
        self.label_spacer3_2.setObjectName("label_spacer3_2")
        self.stackedWidget.addWidget(self.Client)
        self.Server = QtWidgets.QWidget()
        self.Server.setObjectName("Server")
        self.button_Startlistening = QtWidgets.QPushButton(self.Server)
        self.button_Startlistening.setGeometry(QtCore.QRect(650, 600, 101, 41))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button_Startlistening.setFont(font)
        self.button_Startlistening.setStyleSheet("background-color: rgb(192, 216, 251);\n"
"border-radius: 10px;")
        self.button_Startlistening.setObjectName("button_Startlistening")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Server)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 732, 531))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.Layout_SelectFile = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.Layout_SelectFile.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Layout_SelectFile.setContentsMargins(0, 0, 0, 0)
        self.Layout_SelectFile.setObjectName("Layout_SelectFile")
        self.Layout_FileInfo = QtWidgets.QVBoxLayout()
        self.Layout_FileInfo.setContentsMargins(-1, 0, 0, -1)
        self.Layout_FileInfo.setObjectName("Layout_FileInfo")
        self.Layout_Filename = QtWidgets.QHBoxLayout()
        self.Layout_Filename.setObjectName("Layout_Filename")
        self.hint_Filename = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.hint_Filename.setMinimumSize(QtCore.QSize(50, 0))
        self.hint_Filename.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.hint_Filename.setFont(font)
        self.hint_Filename.setObjectName("hint_Filename")
        self.Layout_Filename.addWidget(self.hint_Filename)
        self.label_Filename = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_Filename.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_Filename.setFont(font)
        self.label_Filename.setObjectName("label_Filename")
        self.Layout_Filename.addWidget(self.label_Filename)
        self.Layout_FileInfo.addLayout(self.Layout_Filename)
        self.Layout_Filesize = QtWidgets.QHBoxLayout()
        self.Layout_Filesize.setObjectName("Layout_Filesize")
        self.hint_Filesize = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.hint_Filesize.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.hint_Filesize.setFont(font)
        self.hint_Filesize.setObjectName("hint_Filesize")
        self.Layout_Filesize.addWidget(self.hint_Filesize)
        self.label_Filesize = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_Filesize.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_Filesize.setFont(font)
        self.label_Filesize.setObjectName("label_Filesize")
        self.Layout_Filesize.addWidget(self.label_Filesize)
        self.Layout_FileInfo.addLayout(self.Layout_Filesize)
        self.Layout_SelectFile.addLayout(self.Layout_FileInfo)
        self.Layout_Sendschedule = QtWidgets.QHBoxLayout()
        self.Layout_Sendschedule.setSpacing(0)
        self.Layout_Sendschedule.setObjectName("Layout_Sendschedule")
        self.hint_Sendschedule = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.hint_Sendschedule.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.hint_Sendschedule.setFont(font)
        self.hint_Sendschedule.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.hint_Sendschedule.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.hint_Sendschedule.setObjectName("hint_Sendschedule")
        self.Layout_Sendschedule.addWidget(self.hint_Sendschedule)
        self.progressBar_SendFile = QtWidgets.QProgressBar(self.verticalLayoutWidget_4)
        self.progressBar_SendFile.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.progressBar_SendFile.setFont(font)
        self.progressBar_SendFile.setStyleSheet("#progressBar_SendFile{\n"
"border: 2px solid #000;\n"
"border-radius: 10px;\n"
"text-align:center;\n"
"}\n"
"#progressBar_SendFile::chunk { \n"
"background-color: rgb(170, 170, 255);\n"
"border-radius: 8px;\n"
"}")
        self.progressBar_SendFile.setProperty("value", 24)
        self.progressBar_SendFile.setObjectName("progressBar_SendFile")
        self.Layout_Sendschedule.addWidget(self.progressBar_SendFile)
        self.Layout_SelectFile.addLayout(self.Layout_Sendschedule)
        self.button_SelectfFile = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.button_SelectfFile.setMinimumSize(QtCore.QSize(730, 100))
        self.button_SelectfFile.setMaximumSize(QtCore.QSize(730, 100))
        self.button_SelectfFile.setStyleSheet("background-image: url(./src/gui/image/button_SelectFile.png);\n"
"border-radius: 10px;")
        self.button_SelectfFile.setText("")
        self.button_SelectfFile.setObjectName("button_SelectfFile")
        self.Layout_SelectFile.addWidget(self.button_SelectfFile)
        self.listView_Sendpackage = QtWidgets.QListView(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(11)
        self.listView_Sendpackage.setFont(font)
        self.listView_Sendpackage.setStyleSheet("border-radius: 10px;\n"
"background-color: rgba(13, 95, 160, 200);")
        self.listView_Sendpackage.setObjectName("listView_Sendpackage")
        self.Layout_SelectFile.addWidget(self.listView_Sendpackage)
        self.stackedWidget.addWidget(self.Server)
        self.Setting = QtWidgets.QWidget()
        self.Setting.setObjectName("Setting")
        self.button_SettingSave = QtWidgets.QPushButton(self.Setting)
        self.button_SettingSave.setGeometry(QtCore.QRect(640, 600, 120, 40))
        font = QtGui.QFont()
        font.setFamily("文鼎粗魏碑")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.button_SettingSave.setFont(font)
        self.button_SettingSave.setMouseTracking(False)
        self.button_SettingSave.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_SettingSave.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_SettingSave.setStyleSheet("background-color: rgb(192, 216, 251);\n"
"border-radius: 10px;")
        self.button_SettingSave.setCheckable(False)
        self.button_SettingSave.setChecked(False)
        self.button_SettingSave.setAutoRepeat(False)
        self.button_SettingSave.setAutoExclusive(False)
        self.button_SettingSave.setObjectName("button_SettingSave")
        self.groupBox_client = QtWidgets.QGroupBox(self.Setting)
        self.groupBox_client.setGeometry(QtCore.QRect(30, 40, 651, 190))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_client.setFont(font)
        self.groupBox_client.setFlat(True)
        self.groupBox_client.setCheckable(False)
        self.groupBox_client.setChecked(False)
        self.groupBox_client.setObjectName("groupBox_client")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_client)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 601, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Layout_client1 = QtWidgets.QHBoxLayout()
        self.Layout_client1.setObjectName("Layout_client1")
        self.hint_clientIP = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        self.hint_clientIP.setFont(font)
        self.hint_clientIP.setStyleSheet("")
        self.hint_clientIP.setObjectName("hint_clientIP")
        self.Layout_client1.addWidget(self.hint_clientIP)
        self.input_clientIP = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_clientIP.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.input_clientIP.setFont(font)
        self.input_clientIP.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.input_clientIP.setStyleSheet("background-color: rgba(170, 170, 255, 70);\n"
"border-radius: 10px;")
        self.input_clientIP.setInputMask("")
        self.input_clientIP.setFrame(True)
        self.input_clientIP.setAlignment(QtCore.Qt.AlignCenter)
        self.input_clientIP.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_clientIP.setObjectName("input_clientIP")
        self.Layout_client1.addWidget(self.input_clientIP)
        spacerItem6 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_client1.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.Layout_client1)
        self.Layout_client2 = QtWidgets.QHBoxLayout()
        self.Layout_client2.setObjectName("Layout_client2")
        self.hint_clientPort = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.hint_clientPort.setFont(font)
        self.hint_clientPort.setObjectName("hint_clientPort")
        self.Layout_client2.addWidget(self.hint_clientPort)
        self.input_clientPort = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_clientPort.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.input_clientPort.setFont(font)
        self.input_clientPort.setStyleSheet("background-color: rgba(170, 170, 255, 70);\n"
"border-radius: 10px;")
        self.input_clientPort.setInputMask("")
        self.input_clientPort.setMaxLength(5)
        self.input_clientPort.setAlignment(QtCore.Qt.AlignCenter)
        self.input_clientPort.setObjectName("input_clientPort")
        self.Layout_client2.addWidget(self.input_clientPort)
        spacerItem7 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_client2.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.Layout_client2)
        self.Layout_client3 = QtWidgets.QHBoxLayout()
        self.Layout_client3.setObjectName("Layout_client3")
        self.hint_saveFolderPath = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.hint_saveFolderPath.setFont(font)
        self.hint_saveFolderPath.setObjectName("hint_saveFolderPath")
        self.Layout_client3.addWidget(self.hint_saveFolderPath)
        self.input_ShowSavepath = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_ShowSavepath.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.input_ShowSavepath.setFont(font)
        self.input_ShowSavepath.setStyleSheet("background-color: rgba(170, 170, 255, 70);\n"
"border-radius: 10px;")
        self.input_ShowSavepath.setAlignment(QtCore.Qt.AlignCenter)
        self.input_ShowSavepath.setReadOnly(True)
        self.input_ShowSavepath.setObjectName("input_ShowSavepath")
        self.Layout_client3.addWidget(self.input_ShowSavepath)
        self.button_OpenSaveFolder = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.button_OpenSaveFolder.setMinimumSize(QtCore.QSize(40, 40))
        self.button_OpenSaveFolder.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.button_OpenSaveFolder.setFont(font)
        self.button_OpenSaveFolder.setStyleSheet("background-image: url(./src/gui/image/button_openSaveFile.png);\n"
"border-radius: 10px;")
        self.button_OpenSaveFolder.setText("")
        self.button_OpenSaveFolder.setObjectName("button_OpenSaveFolder")
        self.Layout_client3.addWidget(self.button_OpenSaveFolder)
        self.verticalLayout_2.addLayout(self.Layout_client3)
        self.stackedWidget.addWidget(self.Setting)
        self.User = QtWidgets.QWidget()
        self.User.setObjectName("User")
        self.label_4 = QtWidgets.QLabel(self.User)
        self.label_4.setGeometry(QtCore.QRect(220, 280, 271, 261))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.User)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 1, 991, 42))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_MainControll = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_MainControll.setContentsMargins(0, 0, 0, 0)
        self.layout_MainControll.setSpacing(1)
        self.layout_MainControll.setObjectName("layout_MainControll")
        self.MainMove = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.MainMove.setMinimumSize(QtCore.QSize(930, 40))
        self.MainMove.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MainMove.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.MainMove.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.MainMove.setText("")
        self.MainMove.setIconSize(QtCore.QSize(20, 40))
        self.MainMove.setObjectName("MainMove")
        self.layout_MainControll.addWidget(self.MainMove)
        self.MainMin = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.MainMin.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MainMin.setFont(font)
        self.MainMin.setToolTip("")
        self.MainMin.setWhatsThis("")
        self.MainMin.setStyleSheet("border-image: url(./src/gui/image/WindowMin.jpg);")
        self.MainMin.setText("")
        self.MainMin.setIconSize(QtCore.QSize(30, 30))
        self.MainMin.setObjectName("MainMin")
        self.layout_MainControll.addWidget(self.MainMin)
        self.MainClose = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.MainClose.setMinimumSize(QtCore.QSize(0, 0))
        self.MainClose.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MainClose.setFont(font)
        self.MainClose.setToolTip("")
        self.MainClose.setStyleSheet("border-image: url(./src/gui/image/WindowClose.jpg);\n"
"")
        self.MainClose.setText("")
        self.MainClose.setIconSize(QtCore.QSize(30, 30))
        self.MainClose.setObjectName("MainClose")
        self.layout_MainControll.addWidget(self.MainClose)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.button_Client.setText(_translate("MainWindow", "Receive \n"
" package"))
        self.button_Server.setText(_translate("MainWindow", "Send \n"
" Package"))
        self.button_Setting.setText(_translate("MainWindow", "Setting"))
        self.button_User.setText(_translate("MainWindow", "User"))
        self.hint_cFilename.setText(_translate("MainWindow", "文件名:"))
        self.hint_cFileize.setText(_translate("MainWindow", "檔案大小:"))
        self.hint_schedule.setText(_translate("MainWindow", "進度  "))
        self.input_PickupNumber.setPlaceholderText(_translate("MainWindow", "請輸入取件碼"))
        self.button_RequireFile.setText(_translate("MainWindow", "取件✔"))
        self.button_Startlistening.setText(_translate("MainWindow", "發送包裹"))
        self.hint_Filename.setText(_translate("MainWindow", "檔案名稱:"))
        self.label_Filename.setText(_translate("MainWindow", "NOfile"))
        self.hint_Filesize.setText(_translate("MainWindow", "檔案大小:"))
        self.label_Filesize.setText(_translate("MainWindow", "0 mb"))
        self.hint_Sendschedule.setText(_translate("MainWindow", "進度  "))
        self.button_SettingSave.setText(_translate("MainWindow", "儲存設定"))
        self.groupBox_client.setTitle(_translate("MainWindow", "代理伺服器設定"))
        self.hint_clientIP.setText(_translate("MainWindow", "IP地址(IPv4) :"))
        self.hint_clientPort.setText(_translate("MainWindow", "Port(0~65535) :"))
        self.hint_saveFolderPath.setText(_translate("MainWindow", "存檔位置 :"))
        self.label_4.setText(_translate("MainWindow", "User"))
