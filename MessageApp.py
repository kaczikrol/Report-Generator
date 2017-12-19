from PyQt4 import QtCore, QtGui
from Message import Ui_Message
import sys

class MessageBox(QtGui.QDialog,Ui_Message):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=None)
        self.msg = Ui_Message()
        self.msg.setupUi(self)
        self.confirmed=False
        self.declined=False
        QtCore.QObject.connect(self.msg.YesButton,QtCore.SIGNAL("clicked()"),self.Confirmed)
        QtCore.QObject.connect(self.msg.NoButton,QtCore.SIGNAL("clicked()"),self.Declined)

    def Confirmed(self):
        self.confirmed=True

    def Declined(self):
        self.declined=True



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    msg = MessageBox()
    msg.show()
    sys.exit(app.exec_())
