# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0dSLNoz.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PySide2.QtWidgets import *
import datetime
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



# #Stats for Type A
#data={"Total Produced":30, "Total Stored":12,"Total Dispatched":8}
#db.child("Product Type").child("Product A").set(data)
# add do a variable

# tap is total number of A products produced

tap = db.child('Product Type').child('Product A').child('Total Produced').get()
# tbp is total number of B products produced
tbp = db.child('Product Type').child('Product B').child('Total Produced').get()
# tcp is total number of C products produced
tcp = db.child('Product Type').child('Product C').child('Total Produced').get()
# tallp is total number of All products produced
tallp = tap.val() + tbp.val() + tcp.val()
# tas is total number of A products Stored
tas = db.child('Product Type').child('Product A').child('Total Stored').get()
# tbs is total number of B products Stored
tbs = db.child('Product Type').child('Product B').child('Total Stored').get()
# tad is total number of A products Dispatched
tad = db.child('Product Type').child('Product A').child('Total Dispatched').get()
# tbd is total number of B products Dispatched
tbd = db.child('Product Type').child('Product B').child('Total Dispatched').get()
# tcd is total number of C products Dispatched
tcd = db.child('Product Type').child('Product C').child('Total Dispatched').get()
# tsc is total storage capacity
tsc = (tas.val() + tbs.val()) * 100 / 24
tsc = str(round(tsc, 2))
# toc is total number of Orders created
toc = db.child('ID').child('Ordercount').get()
tpid = db.child('ProductID').get()
orderid = 00000000

#print(values.val())




class Ui_MainWindow(object):
    # adding action to the spin box

    def show_resultA(self):
        # getting current value
        valueA = self.ProductA.value()
        return valueA

    def show_resultB(self):
        # getting current value
        valueB = self.ProductB.value()
        return valueB

    def show_resultC(self):
        # getting current value
        valueC = self.ProductC.value()
        return valueC


    def button_clicked(self):
        #self.label.setText("you pressed the button")

        self.update()
        firebase = pyrebase.initialize_app(firebaseConfig)

        db = firebase.database()



        db.child("Product Type").child("Product A").update({"Total Produced": tap.val() + self.show_resultA()})
        db.child("Product Type").child("Product B").update({"Total Produced": tbp.val() + self.show_resultB()})
        db.child("Product Type").child("Product C").update({"Total Produced": tcp.val() + self.show_resultC()})
        db.child("ID").update({"Ordercount": toc.val()+1})
        #print(tpid.val())
        #orderid+=1
        #print(self.show_resultA())

       
        now = datetime.datetime.now()
        timenow=int(now.strftime("%Y%m%d%H%M%S%f")[:-4])
        #print(type(timenow))

        listA=[]
        for i in range(self.show_resultA()):
            #i++
            listA.append(i)
        #print(listA)
        #print(list[0])
        #for i in range(len(listA)):
        #    print(listA[i])
        
        #length=len(list)
        for i in range(len(listA)):
            #for j in len(i):
            aid = str(timenow+i) + "A" + str(i)
            oid = db.child("Allproducts").child("ListAproducts").child(timenow).child(timenow+i).set(aid)
            #db.child("Allproducts").child("ListAproducts").child(timenow).child(timenow+i).update({"i": aid})
            i+=1
            
            #print(i)

        listB=[]
        for i in range(self.show_resultB()):
            #i++
            listB.append(i)
        #print(listB)
        #print(list[0])
        # for i in range(len(listB)):
        #     print(listB[i])
        
        #length=len(list)
        for i in range(len(listB)):
            #for j in len(i):
            bid = str(timenow+i) + "B" + str(i)
            oid = db.child("Allproducts").child("ListBproducts").child(timenow).child(timenow+i).set(bid)
            #db.child("Allproducts").child("ListBproducts").child(timenow).child(timenow+i).update({"i": bid})
            i+=1
            #print(bns)
            
            #print(i)    
        
        listC=[]
        for i in range(self.show_resultC()):
            #i++
            listC.append(i)
        #print(listC)
        #print(list[0])
        #for i in range(len(listC)):
            #print(listC[i])
        
        #length=len(list)
        for i in range(len(listC)):
            #for j in len(i):
            cid = str(timenow+i) + "C" + str(i)
            oid = db.child("Allproducts").child("ListCproducts").child(timenow).child(timenow+i).set(cid)
            #db.child("Allproducts").child("ListCproducts").child(timenow).child(timenow+i).update({"i": cid})
            i+=1
            
            #print(i)       

        # productida_final = productida
        # productida_final.insert(-1,productida)
        # print(productida_final)
             

       


    def update(self):
        self.label.adjustSize()



    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(191, 194, 200);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(68, 496))
        self.frame_top_menus.setMaximumSize(QSize(68, 496))
        self.frame_top_menus.setAutoFillBackground(True)
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Plain)
        self.frame_top_menus.setLineWidth(0)
        self.frame_top_menus.setMidLineWidth(2)
        self.home = QPushButton(self.frame_top_menus)
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        self.home.setGeometry(QRect(0, 51, 68, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setMinimumSize(QSize(0, 40))
        self.home.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.storage = QPushButton(self.frame_top_menus)
        self.storage.setObjectName(u"storage")
        self.storage.setGeometry(QRect(0, 227, 68, 40))
        self.storage.setMinimumSize(QSize(0, 40))
        self.storage.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.dispatch = QPushButton(self.frame_top_menus)
        self.dispatch.setObjectName(u"dispatch")
        self.dispatch.setGeometry(QRect(0, 315, 68, 40))
        self.dispatch.setMinimumSize(QSize(0, 40))
        self.dispatch.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Stats = QPushButton(self.frame_top_menus)
        self.Stats.setObjectName(u"Stats")
        self.Stats.setGeometry(QRect(0, 388, 68, 40))
        self.Stats.setMinimumSize(QSize(0, 40))
        self.Stats.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.production = QPushButton(self.frame_top_menus)
        self.production.setObjectName(u"production")
        self.production.setGeometry(QRect(0, 139, 68, 40))
        sizePolicy.setHeightForWidth(self.production.sizePolicy().hasHeightForWidth())
        self.production.setSizePolicy(sizePolicy)
        self.production.setMinimumSize(QSize(0, 40))
        self.production.setMaximumSize(QSize(16777215, 16777215))
        self.production.setMouseTracking(True)
        self.production.setAutoFillBackground(True)
        self.production.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.production.setAutoDefault(False)
        self.production.setFlat(False)

        self.verticalLayout_3.addWidget(self.frame_top_menus)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"palette.setColor(QtGui.QPalette.Background, QColor(\"rgb(191, 194, 200)\"))")
        self.stackedWidget.setInputMethodHints(Qt.ImhNone)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.ProductC = QSpinBox(self.Home)
        self.ProductC.setObjectName(u"ProductC")
        self.ProductC.setGeometry(QRect(800, 260, 78, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.ProductC.sizePolicy().hasHeightForWidth())
        self.ProductC.setSizePolicy(sizePolicy1)
        self.ProductC.setMaximum(12)
        self.ProductC.valueChanged.connect(self.show_resultC)


        self.ProductA = QSpinBox(self.Home)
        self.ProductA.setObjectName(u"ProductA")
        self.ProductA.setEnabled(True)
        self.ProductA.setGeometry(QRect(800, 140, 78, 40))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(32)
        sizePolicy2.setVerticalStretch(23)
        sizePolicy2.setHeightForWidth(self.ProductA.sizePolicy().hasHeightForWidth())
        self.ProductA.setSizePolicy(sizePolicy2)
        self.ProductA.setLayoutDirection(Qt.LeftToRight)
        self.ProductA.setMaximum(12)
        self.ProductA.valueChanged.connect(self.show_resultA)

        self.ProductB = QSpinBox(self.Home)
        self.ProductB.setObjectName(u"ProductB")
        self.ProductB.setGeometry(QRect(800, 200, 78, 40))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ProductB.sizePolicy().hasHeightForWidth())
        self.ProductB.setSizePolicy(sizePolicy3)
        self.ProductB.setMaximum(12)
        self.ProductB.valueChanged.connect(self.show_resultB)
        self.pushButton = QPushButton(self.Home)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 330, 93, 28))
        self.lineEdit = QLineEdit(self.Home)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(670, 150, 113, 22))
        self.lineEdit_2 = QLineEdit(self.Home)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(670, 210, 113, 22))
        self.lineEdit_3 = QLineEdit(self.Home)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(670, 270, 113, 22))
        self.lineEdit_4 = QLineEdit(self.Home)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(140, 30, 631, 22))
        self.tableWidget = QTableWidget(self.Home)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(200, 180, 351, 192))
        self.lineEdit_5 = QLineEdit(self.Home)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(150, 130, 113, 22))
        self.label = QLabel(self.Home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 130, 111, 16))
        self.label_2 = QLabel(self.Home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 130, 111, 16))
        self.lineEdit_6 = QLineEdit(self.Home)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(420, 130, 113, 22))
        self.pushButton_2 = QPushButton(self.Home)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 180, 93, 28))
        self.label_3 = QLabel(self.Home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 100, 91, 16))
        self.label_4 = QLabel(self.Home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(810, 100, 55, 16))
        self.stackedWidget.addWidget(self.Home)
        self.Production = QWidget()
        self.Production.setObjectName(u"Production")
        self.Production_2 = QLabel(self.Production)
        self.Production_2.setObjectName(u"Production_2")
        self.Production_2.setGeometry(QRect(460, 110, 151, 16))
        self.lineEdit_8 = QLineEdit(self.Production)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(130, 20, 631, 22))
        self.label_5 = QLabel(self.Production)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 330, 221, 16))
        self.lineEdit_10 = QLineEdit(self.Production)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(540, 190, 113, 22))
        self.lineEdit_10.setText(str(tap.val()))
        self.label_6 = QLabel(self.Production)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 270, 201, 16))
        self.label_7 = QLabel(self.Production)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 190, 201, 16))
        self.label_8 = QLabel(self.Production)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 230, 201, 16))
        self.lineEdit_11 = QLineEdit(self.Production)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(540, 230, 113, 22))
        self.lineEdit_11.setText(str(tbp.val()))
        self.lineEdit_12 = QLineEdit(self.Production)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(540, 270, 113, 22))
        self.lineEdit_12.setText(str(tcp.val()))
        self.lineEdit_13 = QLineEdit(self.Production)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(540, 330, 113, 22))
        self.lineEdit_13.setText(str(tallp))
        self.stackedWidget.addWidget(self.Production)
        self.Storage = QWidget()
        self.Storage.setObjectName(u"Storage")
        self.lineEdit_7 = QLineEdit(self.Storage)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(140, 30, 631, 22))
        self.label_9 = QLabel(self.Storage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(350, 120, 241, 16))
        self.label_10 = QLabel(self.Storage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(370, 250, 121, 16))
        self.label_11 = QLabel(self.Storage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(370, 300, 191, 16))
        self.label_12 = QLabel(self.Storage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(370, 350, 191, 16))
        self.lineEdit_14 = QLineEdit(self.Storage)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(560, 300, 113, 22))
        self.lineEdit_14.setText(str(tas.val()))
        self.lineEdit_15 = QLineEdit(self.Storage)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(560, 350, 113, 22))
        self.lineEdit_15.setText(str(tbs.val()))
        self.lineEdit_16 = QLineEdit(self.Storage)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(560, 250, 113, 22))
        self.lineEdit_16.setText(str(tsc))
        self.stackedWidget.addWidget(self.Storage)
        self.Dispatch = QWidget()
        self.Dispatch.setObjectName(u"Dispatch")
        self.lineEdit_9 = QLineEdit(self.Dispatch)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(140, 20, 631, 22))
        self.label_13 = QLabel(self.Dispatch)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(410, 70, 111, 16))
        self.label_14 = QLabel(self.Dispatch)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(430, 160, 91, 16))
        self.label_15 = QLabel(self.Dispatch)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(300, 210, 241, 16))
        self.label_16 = QLabel(self.Dispatch)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(300, 270, 241, 16))
        self.label_17 = QLabel(self.Dispatch)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(300, 240, 241, 16))
        self.lineEdit_17 = QLineEdit(self.Dispatch)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(540, 160, 113, 22))
        self.lineEdit_18 = QLineEdit(self.Dispatch)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(540, 210, 113, 22))
        self.lineEdit_18.setText(str(tad.val()))
        self.lineEdit_19 = QLineEdit(self.Dispatch)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(540, 240, 113, 22))
        self.lineEdit_19.setText(str(tbd.val()))
        self.lineEdit_20 = QLineEdit(self.Dispatch)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(540, 270, 113, 22))
        self.lineEdit_20.setText(str(tcd.val()))
        self.stackedWidget.addWidget(self.Dispatch)
        self.Statistics = QWidget()
        self.Statistics.setObjectName(u"Statistics")
        self.lineEdit_21 = QLineEdit(self.Statistics)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(180, 20, 631, 22))
        self.lineEdit_22 = QLineEdit(self.Statistics)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(400, 70, 161, 22))
        self.listWidget = QListWidget(self.Statistics)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 130, 371, 271))
        self.stackedWidget.addWidget(self.Statistics)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)


        #self.b1 = QtWidgets.QPushButton(self)
       # self.b1.setText("click me!")
        self.pushButton.clicked.connect(self.button_clicked)
        
         

        self.retranslateUi(MainWindow)


        self.production.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)




        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.storage.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.dispatch.setText(QCoreApplication.translate("MainWindow", u"Dispatch", None))
        self.Stats.setText(QCoreApplication.translate("MainWindow", u"KPI", None))
        self.production.setText(QCoreApplication.translate("MainWindow", u"Production", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Order", None))




        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Product A", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Product B", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Product C", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"                                                        INDUSTRY 4.0 FACTORY LAYOUT", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Order ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Product Type", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search Product ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search Order ID", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Product Type", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.Production_2.setText(QCoreApplication.translate("MainWindow", u"PRODUCTION DATA", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"                                                        INDUSTRY 4.0 FACTORY LAYOUT", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total number of products produced", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Number of C products produced", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Number of A products produced", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Number of B products produced", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"                                                        INDUSTRY 4.0 FACTORY LAYOUT", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"HIGH BAY SHELF STORAGE DATA", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Storage capacity", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Number of A products stored", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Number of B products stored", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"                                                        INDUSTRY 4.0 FACTORY LAYOUT", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"DISPATCH DATA", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DISPATCH ID", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total number of product A dispatched", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Total number of product C dispatched", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Total number of product B dispatched", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"                                                        INDUSTRY 4.0 FACTORY LAYOUT", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"TOTAL STATISTICS", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Total A products produced            "+"     "+ str(tap.val()), None));
        
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Total B products produced            "+"     "+ str(tbp.val()), None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total C products produced            "+"     "+ str(tcp.val()), None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total number of products produced"+"  "+ str(tallp), None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Number of A products stored         "+"    "+ str(tas.val()), None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Number of B products stored         "+"    "+ str(tbs.val()), None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Number of A products dispatched   "+"   "+ str(tad.val()), None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Number of B products dispatched   "+"   "+ str(tbd.val()), None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Number of C products dispatched   "+"   "+ str(tcd.val()), None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Storage capacity                    "+"   "+ str(tsc), None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Number of orders created        "+"  "+ str(toc.val()), None));
        self.listWidget.setSortingEnabled(__sortingEnabled)
        



    # retranslateUi
    

    