

#from _typeshed import Self
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import ui_main_projectgui7latest
from ui_main_projectgui7latest import *

# class TableModel(QtCore.QAbstractTableModel):
#     def __init__(self, data):
#         super(TableModel, self).__init__()
#         self._data = data
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             # See below for the nested-list data structure.
#             # .row() indexes into the outer list,
#             # .column() indexes into the sub-list
#             return self._data[index.row()]#[index.column()]

#     def rowCount(self, index):
#         # The length of the outer list.
        

#     # def columnCount(self, index):
#     #     # The following takes the first sub-list, and returns
#     #     # the length (only works if all rows are an equal length)
#     #     return len(self._data[0])

#         somclass_instance = ui_main_projectgui7latest.Ui_MainWindow() 
#         somclass_instance.search_clicked()
#         data = somclass_instance.listall
#         completer = QtWidgets.QCompleter(listall)
#         completer.setCaseSensitivity(Qt.CaseInsensitive)
#         self.ui.lineEdit_5.setCompleter(completer)
#         #return len(self._data)    
#         return TableModel(data)



import pyrebase

#Initialize Firebase
firebaseConfig={"apiKey": "AIzaSyD4qNlD_2M7_naDrZviRM2mJyCtpwctnqk",
    "authDomain": "projectgui-ovgu.firebaseapp.com",
    "databaseURL": "https://projectgui-ovgu-default-rtdb.europe-west1.firebasedatabase.app/",
    "projectId": "projectgui-ovgu",
    "storageBucket": "projectgui-ovgu.appspot.com",
    "messagingSenderId": "784430939100",
    "appId": "1:784430939100:web:1f4f21e01d122692e42d19",
    "measurementId": "G-3H7B56JCX4"}

   

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()





class TableModel(QtCore.QAbstractTableModel):

    

    

    def __init__(self, data):
        super(TableModel, self).__init__()
        
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.prd()]

    

    def prd(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


    # class_instance = ui_main_projectgui7latest.Ui_MainWindow() 
    # class_instance.search_clicked()
    
    # data = class_instance.listall    


#class MainWindow(QtWidgets.QMainWindow):

    def search_clicked(self):   


        #self.update()
        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database() 

        #abc = db.child("Allproducts").get().val()
        abc = db.get().val()
        #print(abc.val())
        global dabc
        dabc = dict(abc)
        #print(dabc.keys())
        #print(dabc["Allproducts"].keys())
        #dabc_l = len(dabc["Allproducts"]["ListAproducts"].items())
        
        ListAproducts = dabc["Allproducts"]["ListAproducts"]
        ListBproducts = dabc["Allproducts"]["ListBproducts"]
        ListCproducts = dabc["Allproducts"]["ListCproducts"]
        #print(dabc_l)
        global listall
        listall = []
        for i in ListAproducts.keys():
            ai=dabc["Allproducts"]["ListAproducts"][i].values()
            for j in ai:
                listall.append(j)
        #print(listall)
        for i in ListBproducts.keys():
            bi=dabc["Allproducts"]["ListBproducts"][i].values()
            for j in bi:
                listall.append(j)
        #print(listall)
        for i in ListCproducts.keys():
            ci=dabc["Allproducts"]["ListCproducts"][i].values()
            for j in ci:
                listall.append(j)

                
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        
        # completer = QtWidgets.QCompleter(TableModel.search_clicked(self).listall)
        # completer.setCaseSensitivity(Qt.CaseInsensitive)
        # self.ui.lineEdit_5.setCompleter(completer)
        data = TableModel.search_clicked(self).listall

        

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

 