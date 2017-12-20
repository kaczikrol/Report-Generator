# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Message.ui'
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

class Ui_Message(object):
    def setupUi(self, Message):
        Message.setObjectName(_fromUtf8("Message"))
        Message.resize(376, 159)
        self.horizontalLayoutWidget = QtGui.QWidget(Message)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 80, 160, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.YesButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.YesButton.setObjectName(_fromUtf8("YesButton"))
        self.horizontalLayout.addWidget(self.YesButton)
        self.NoButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.NoButton.setObjectName(_fromUtf8("NoButton"))
        self.horizontalLayout.addWidget(self.NoButton)
        self.MessageText = QtGui.QTextBrowser(Message)
        self.MessageText.setGeometry(QtCore.QRect(20, 20, 331, 51))
        self.MessageText.setObjectName(_fromUtf8("MessageText"))

        self.retranslateUi(Message)
        QtCore.QMetaObject.connectSlotsByName(Message)

    def retranslateUi(self, Message):
        Message.setWindowTitle(_translate("Message", "Form", None))
        self.YesButton.setText(_translate("Message", "Yes", None))
        self.NoButton.setText(_translate("Message", "No", None))


