# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_window_univ.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(900, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(900, 1000))
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
" border-image: url(C:/PyQt/pythonProject/site_page/background4.jpg)\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"     font: 8pt \"Segoe Script\";\n"
"     color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton\n"
"{    \n"
"     font: 8pt \"Segoe Script\";\n"
"     background-color: rgb(255, 255, 255);\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-color: rgb(235, 235, 235);\n"
"     color: black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(247, 214, 239);\n"
"    border-width: 2px;\n"
"    border-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(231, 200, 225);\n"
"    border-width: 2px;\n"
"    border-color: rgb(235, 235, 235);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton__query_window_univ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__query_window_univ.setGeometry(QtCore.QRect(800, 935, 80, 40))
        self.pushButton__query_window_univ.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton__query_window_univ.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton__query_window_univ.setObjectName("pushButton__query_window_univ")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Найденные по запросу ВУЗы"))
        self.pushButton__query_window_univ.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Найденные по запросу ВУЗы"))