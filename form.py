# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product_table2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setObjectName("buttonClear")
        self.gridLayout.addWidget(self.buttonClear, 0, 6, 1, 1)
        self.buttonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSearch.setObjectName("buttonSearch")
        self.gridLayout.addWidget(self.buttonSearch, 0, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 5)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 7)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 2, 0, 1, 3)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 2, 4, 1, 3)
        self.buttonUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUpdate.setObjectName("buttonUpdate")
        self.gridLayout.addWidget(self.buttonUpdate, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonClear.setText(_translate("MainWindow", "Сброс"))
        self.buttonSearch.setText(_translate("MainWindow", "Поиск"))
        self.button1.setText(_translate("MainWindow", "Сохранить данные"))
        self.button2.setText(_translate("MainWindow", "Очистить таблицу"))
        self.buttonUpdate.setText(_translate("MainWindow", "Обновить"))
