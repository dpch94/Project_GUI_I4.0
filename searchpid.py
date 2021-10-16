import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow,QLineEdit,QCompleter)
from PyQt5.QtCore import Qt, QStringListModel
# from PyQt5.QtWidgets import (QApplication, QMainWindow,QLineEdit,QCompleter)
# from PyQt5.QtWidgets import QWidget, QVBoxLayout
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QStringListModel
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
#         self.ui.lineEdit_5#.setCompleter(completer)
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

class TableWindow(QMainWindow):

	def __init__(self):
		super().__init__()
		#self.setGeometry(100,60,1000,800)
		self.show()
		self.dabc = dict( db.get().val())
		self.search_clicked()
        #self.click_method()
        
        
 
       
	def search_clicked(self):
		ListAproducts = self.dabc["Allproducts"]["ListAproducts"]
		ListBproducts = self.dabc["Allproducts"]["ListBproducts"]
		ListCproducts = self.dabc["Allproducts"]["ListCproducts"]
		self.orders_list = []

		for i in ListAproducts.keys():
			ai=self.dabc["Allproducts"]["ListAproducts"][i].values()
			self.orders_list.append(i)

		# for j in ai:
		#     self.listall.append(j)
		# #print(listall)
		# for i in ListBproducts.keys():
		# 	bi=self.dabc["Allproducts"]["ListBproducts"][i].values()
		# for j in bi:
		#     self.listall.append(j)
		# #print(listall)
		# for i in ListCproducts.keys():
		# 	ci=self.dabc["Allproducts"]["ListCproducts"][i].values()
		# for j in ci:
		#     self.listall.append(j)	

		#print(self.orders_list)
        
		self.model = QStringListModel()
		#self.model.setStringList(['some', 'words', 'in', 'my', 'dictionary'])
		self.model.setStringList(self.orders_list)

		self.completer = QtWidgets.QCompleter()
		self.completer.setModel(self.model)

		self.lineedit = QtWidgets.QLineEdit()
		self.lineedit.setCompleter(self.completer)
		self.lineedit.show()
        # obutton = QtWidgets.QPushButton()
        # obutton.clicked.connect(self.click_method)
        # obutton.show()
        # # obutton.resize(200,32)
        # # obutton.move(80,60)
        # def click_method(self,check):
        #     if self.lineedit.text() in self.orders_list:
        #         print('Order found ' + self.lineedit.text())
        #     else:
        #         print('Order not found')
# class TableModel(QtCore.QAbstractTableModel):

    # def __init__(self):
    #     super(TableModel, self).__init__()
        
    #     self.dabc = dict( db.get().val())
    #     self._data = self.search_clicked()
        
       
    # def data(self, index, role):
    #     if role == Qt.DisplayRole:
    #         # See below for the nested-list data structure.
    #         # .row() indexes into the outer list,
    #         # .column() indexes into the sub-list
    #         return self._data[index.prd()]

    # def prd(self, index):
    #     # The following takes the first sub-list, and returns
    #     # the length (only works if all rows are an equal length)
    #     return len(self._data[0])

    # def search_clicked(self):          
    #     ListAproducts = self.dabc["Allproducts"]["ListAproducts"]
    #     ListBproducts = self.dabc["Allproducts"]["ListBproducts"]
    #     ListCproducts = self.dabc["Allproducts"]["ListCproducts"]
    #     listall = []
    #     for i in ListAproducts.keys():
    #         ai=self.dabc["Allproducts"]["ListAproducts"][i].values()
            
    #         for j in ai:
    #             listall.append(j)
    #     #print(listall)
    #     for i in ListBproducts.keys():
    #         bi=self.dabc["Allproducts"]["ListBproducts"][i].values()
    #         for j in bi:
    #             listall.append(j)
    #     #print(listall)
    #     for i in ListCproducts.keys():
    #         ci=self.dabc["Allproducts"]["ListCproducts"][i].values()
    #         for j in ci:
    #             listall.append(j)
        
        # completer = QtWidgets.QCompleter(TableModel.search_clicked(self).listall)
        # completer.setCaseSensitivity(Qt.CaseInsensitive)
        # self.ui.lineEdit_5.setCompleter(completer)
        #data = TableModel.search_clicked(self).listall

    



 