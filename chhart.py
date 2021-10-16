import sys, random
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter


from ui_main_projectgui7latest import Ui_MainWindow

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

class ChWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		#self.setWindowTitle("PyQt BarChart")
		self.setGeometry(100,60,1000,800)
		self.show()
		self.create_bar()
		

		

	def create_bar(self):

		set0 = QBarSet('Prod A')
		set1 = QBarSet('Prod B')
		set2 = QBarSet('Prod C')
		set3 = QBarSet('Stor A')
		set4 = QBarSet('Stor B')
		set5 = QBarSet('Disp A')
		set6 = QBarSet('Disp B')
		set7 = QBarSet('Disp C')
		set8 = QBarSet('Range')

		set0.append([tap.val()])
		set1.append([tbp.val()])
		set2.append([tcp.val()])
		set3.append([tas.val()])
		set4.append([tbs.val()])
		set5.append([tad.val()])
		set6.append([tbd.val()])
		set7.append([tcd.val()])
		set8.append(400)
		#set8.setTheme

		series = QBarSeries()
		series.append(set0)
		series.append(set1)
		series.append(set2)
		series.append(set3)
		series.append(set4)
		series.append(set5)
		series.append(set6)
		series.append(set7)
		series.append(set8)
		series.setBarWidth(1);
		series.setLabelsVisible(True)  #displays values of bars

		chart = QChart()
		chart.addSeries(series)
		chart.setTitle('Statistics of Industry 4.0')
		chart.setAnimationOptions(QChart.SeriesAnimations)
		#chart.setTheme(QChart.)

		#kpi = ['Production', 'Storage', 'Dispatch C']

		axis = QBarCategoryAxis()
		#axis.append(series)

		chart.createDefaultAxes()
		chart.setAxisX(axis, series)

		#chart.addAxis(axis, Qt.AlignBottom)
		#chart.addAxis(axisY, Qt.AlignLeft)

		

		chart.legend().setVisible(True)
		chart.legend().setAlignment(Qt.AlignBottom)

		chartView = QChartView(chart)
		chartView.setRenderHint(QPainter.Antialiasing)

		self.setCentralWidget(chartView)


	

