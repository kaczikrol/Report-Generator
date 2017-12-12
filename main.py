from PyQt4 import QtCore, QtGui
from Design import Ui_MainWindow
import sys
import ORM_Module

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.ExpenseButton,QtCore.SIGNAL("clicked()"),self.addExpense)
        QtCore.QObject.connect(self.ui.IncomeButton,QtCore.SIGNAL("clicked()"),self.addIncome)


    def addExpense(self):
        self.expense=ORM_Module.Operation('2017-12-12','C',124.12)
        ORM_Module.session.add(self.expense)
        ORM_Module.session.commit()

    def addIncome(self):
        self.income=ORM_Module.Operation('2017-12-12','D',112.23)
        ORM_Module.session.add(self.income)
        ORM_Module.session.commit()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())