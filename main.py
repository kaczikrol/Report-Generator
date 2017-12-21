from PyQt4 import QtCore, QtGui
from Design import Ui_MainWindow
import MessageApp
import sys
import ORM_Module

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.msg=MessageApp.MessageBox()

        QtCore.QObject.connect(self.ui.ExpenseButton,QtCore.SIGNAL("clicked()"),self.addExpense)
        QtCore.QObject.connect(self.ui.IncomeButton,QtCore.SIGNAL("clicked()"),self.addIncome)
        QtCore.QObject.connect(self.ui.ActionAddUser,QtCore.SIGNAL("triggered()"),self.addUser)
        QtCore.QObject.connect(self.ui.ActionChangeUser,QtCore.SIGNAL("triggered()"),self.changeUser)
        QtCore.QObject.connect(self.ui.ActionDeleteUser,QtCore.SIGNAL("triggered()"),self.deleteUser)
        QtCore.QObject.connect(self.ui.ActionShowUsers,QtCore.SIGNAL("triggered()"),self.showUsers)
        QtCore.QObject.connect(self.ui.ActionAverage,QtCore.SIGNAL("triggered()"),self.ui.ActionAverage.isChecked)
        QtCore.QObject.connect(self.ui.ActionMedian,QtCore.SIGNAL("triggered()"),self.ui.ActionMedian.isChecked)
        QtCore.QObject.connect(self.ui.ActionModa,QtCore.SIGNAL("triggered()"),self.ui.ActionModa.isChecked)
        QtCore.QObject.connect(self.ui.ActionStDev,QtCore.SIGNAL("triggered()"),self.ui.ActionStDev.isChecked)
        QtCore.QObject.connect(self.ui.ActionShowStats,QtCore.SIGNAL("triggered()"),self.showStats)



    def getChoice(self):
        self.msg.exec()
        self.msg.close()
        return self.msg.getChoice()

#Z poniższych dwoch funkcji spróbuj zrobić jedna za pomoca functools partial

    def addExpense(self):
        self.expensevalue=float(self.ui.ValueEdit.text())
        self.tagdescription=str(self.ui.TagEdit.toPlainText())
        self.dateopertaion=self.ui.CalendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.msg.setTextMessage('Do you want add following expense?\n','Value: ',str(self.expensevalue),'\n',
                                'Description: ',self.tagdescription,'\n',
                                'Date operation: ',self.dateopertaion)
        if self.getChoice() == True:
            self.expense=ORM_Module.Operation(self.dateopertaion,'C',self.expensevalue,self.tagdescription)
            ORM_Module.session.add(self.expense)
            ORM_Module.session.commit()
        else:
            pass


    def addIncome(self):
        self.incomevalue=float(self.ui.ValueEdit.text())
        self.tagdescription=str(self.ui.TagEdit.toPlainText())
        self.dateopertaion=self.ui.CalendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.msg.setTextMessage('Do you want add following income?\n','Value: ',str(self.incomevalue),'\n',
                                'Description: ',self.tagdescription,'\n',
                                'Date operation: ',self.dateopertaion)
        if self.getChoice() == True:
            self.income=ORM_Module.Operation(self.dateopertaion,'D',self.incomevalue,self.tagdescription)
            ORM_Module.session.add(self.income)
            ORM_Module.session.commit()
        else:
            pass

    def addUser(self):
        print("Add user!")

    def changeUser(self):
        print("Change user!")

    def deleteUser(self):
        print("Delete user!")

    def showUsers(self):
        print("Show users!")

    def showStats(self):
        print('Statistics of:',self.ui.ActionAverage.isChecked())



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Ui_MainWindow()
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())