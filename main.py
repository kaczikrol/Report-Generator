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
        self.expensevalue=float(self.ui.ValueEdit.text())
        self.tagdescription=str(self.ui.TagEdit.toPlainText())
        self.dateopertaion=self.ui.CalendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.expense=ORM_Module.Operation(self.dateopertaion,'C',self.expensevalue,self.tagdescription)
        ORM_Module.session.add(self.expense)
        ORM_Module.session.commit()

    def addIncome(self):
        self.incomevalue=float(self.ui.ValueEdit.text())
        self.tagdescription=str(self.ui.TagEdit.toPlainText())
        self.dateopertaion=self.ui.CalendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.income=ORM_Module.Operation(self.dateopertaion,'D',self.incomevalue,self.tagdescription)
        ORM_Module.session.add(self.income)
        ORM_Module.session.commit()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Ui_MainWindow()
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())