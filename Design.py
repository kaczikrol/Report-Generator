# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 406)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        MainWindow.setProperty("toolTipDuration", 2)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 391, 191))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ExpenseButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.ExpenseButton.setObjectName(_fromUtf8("ExpenseButton"))
        self.gridLayout.addWidget(self.ExpenseButton, 2, 0, 1, 1)
        self.CloseButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.gridLayout.addWidget(self.CloseButton, 6, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 0, 0, 1, 1)
        self.IncomeButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.IncomeButton.setObjectName(_fromUtf8("IncomeButton"))
        self.gridLayout.addWidget(self.IncomeButton, 5, 0, 1, 1)
        self.dateEdit_2 = QtGui.QDateEdit(self.gridLayoutWidget)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.gridLayout.addWidget(self.dateEdit_2, 3, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.gridLayout.addWidget(self.plainTextEdit_2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.CloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Report Generator", None))
        self.ExpenseButton.setText(_translate("MainWindow", "Add Expense", None))
        self.CloseButton.setText(_translate("MainWindow", "Close", None))
        self.IncomeButton.setText(_translate("MainWindow", "Add Income", None))

