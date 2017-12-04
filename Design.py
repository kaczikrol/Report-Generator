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
        #MainWindow.setToolTipDuration(2)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 180, 471, 171))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.AddUser = QtGui.QPushButton(self.verticalLayoutWidget)
        self.AddUser.setEnabled(True)
        self.AddUser.setCheckable(True)
        self.AddUser.setAutoDefault(True)
        self.AddUser.setDefault(False)
        self.AddUser.setFlat(False)
        self.AddUser.setObjectName(_fromUtf8("AddUser"))
        self.verticalLayout.addWidget(self.AddUser)
        self.AddOperations = QtGui.QPushButton(self.verticalLayoutWidget)
        self.AddOperations.setObjectName(_fromUtf8("AddOperations"))
        self.verticalLayout.addWidget(self.AddOperations)
        self.CheckIncomes = QtGui.QPushButton(self.verticalLayoutWidget)
        self.CheckIncomes.setFocusPolicy(QtCore.Qt.StrongFocus)
        #self.CheckIncomes.setToolTipDuration(4)
        self.CheckIncomes.setObjectName(_fromUtf8("CheckIncomes"))
        self.verticalLayout.addWidget(self.CheckIncomes)
        self.CheckExpenses = QtGui.QPushButton(self.verticalLayoutWidget)
        self.CheckExpenses.setObjectName(_fromUtf8("CheckExpenses"))
        self.verticalLayout.addWidget(self.CheckExpenses)
        self.showPlots = QtGui.QPushButton(self.verticalLayoutWidget)
        self.showPlots.setObjectName(_fromUtf8("showPlots"))
        self.verticalLayout.addWidget(self.showPlots)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 60, 351, 51))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Report Generator", None))
        self.AddUser.setText(_translate("MainWindow", "Dodaj użytkownika", None))
        self.AddOperations.setText(_translate("MainWindow", "Dodaj wydatek", None))
        self.CheckIncomes.setText(_translate("MainWindow", "Sprawdź wydatki", None))
        self.CheckExpenses.setText(_translate("MainWindow", "Sprawdź wpływy", None))
        self.showPlots.setText(_translate("MainWindow", "Pokaż zestawienia", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">Witaj w Raport Generatorze!</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

