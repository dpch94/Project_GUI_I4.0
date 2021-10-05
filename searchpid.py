

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import ui_main_projectgui7latest
from ui_main_projectgui7latest import Ui_MainWindow

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        somclass_instance = ui_main_projectgui7latest.Ui_MainWindow() # we make a new instance of the class. this runs the code in __init__
        somclass_instance.search_clicked()
        data = somclass_instance.listall

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

        
        print(somclass_instance.listall)

    

        


# app=QtWidgets.QApplication(sys.argv)
# window=MainWindow2()
# window.show()
# app.exec_()