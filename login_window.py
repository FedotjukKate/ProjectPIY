# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 389, 18))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 80, 320, 64))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(110, 150, 352, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.login_text_browser = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.login_text_browser.setMinimumSize(QtCore.QSize(350, 20))
        self.login_text_browser.setMaximumSize(QtCore.QSize(350, 20))
        self.login_text_browser.setObjectName("login_text_browser")
        self.verticalLayout_2.addWidget(self.login_text_browser)
        self.login_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_push_button.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.login_push_button.setObjectName("login_push_button")
        self.registration_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.registration_push_button.setGeometry(QtCore.QRect(180, 330, 201, 21))
        self.registration_push_button.setObjectName("registration_push_button")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(110, 210, 352, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.password_push_button = QtWidgets.QTextBrowser(self.layoutWidget3)
        self.password_push_button.setMinimumSize(QtCore.QSize(350, 20))
        self.password_push_button.setMaximumSize(QtCore.QSize(350, 20))
        self.password_push_button.setObjectName("password_push_button")
        self.verticalLayout_3.addWidget(self.password_push_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "*?????????? ?????????? ?????????????? (????????????????)*"))
        self.label_2.setText(_translate("MainWindow", "*?????????? ?????????? ??????????????(??????????)*"))
        self.label_3.setText(_translate("MainWindow", "                *?????????? ?????????? ???????????????? ??????????????*"))
        self.label_4.setText(_translate("MainWindow", "?????????? ????????????????????! ???????? ???????????? ?????? ??????????!"))
        self.label_5.setText(_translate("MainWindow", "Login"))
        self.login_push_button.setText(_translate("MainWindow", "????????"))
        self.registration_push_button.setText(_translate("MainWindow", "????????????????????????????????????"))
        self.label_6.setText(_translate("MainWindow", "Password"))
