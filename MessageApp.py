from PyQt4 import QtCore, QtGui
from Message import Ui_Message
from functools import partial
import sys

class MessageBox(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=None)
        self.msg = Ui_Message()
        self.msg.setupUi(self)
        self.confirmed=None

        QtCore.QObject.connect(self.msg.NoButton, QtCore.SIGNAL(("clicked()")),partial(self.Confirmed,False))
        QtCore.QObject.connect(self.msg.YesButton, QtCore.SIGNAL(("clicked()")),partial(self.Confirmed,True))

    def Confirmed(self,bool):
        self.confirmed = bool
        MessageBox.close(self)

    def getChoice(self):
        return self.confirmed


"""
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    msg = MessageBox()
    msg.show()
    sys.exit(app.exec_())
"""