

import sys,random
import platform
import PyQt5.QtWidgets as qp
from PySide2 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt










# GUI FILE

from ui_main_projectgui7latest import Ui_MainWindow
from chhart import ChWindow



# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    


    def __init__(self):

        super().__init__()

        #QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
      
        #self.show()





    




    


        ## TOGGLE/BURGUER MENU
        ########################################################################
        #self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################


        # PAGE 1
        self.ui.home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        
        # PAGE 2
        self.ui.production.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Production))

        # PAGE 3
        self.ui.storage.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Storage))

        # PAGE 4
        self.ui.dispatch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Dispatch))

        # PAGE 5
        self.ui.Stats.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Statistics))

        self.ui.pushButton.clicked.connect(restart)

        

        # ## SHOW ==> MAIN WINDOW
        # ########################################################################
        # self.show()
        ## ==> END ##


        


      
def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window1 = ChWindow()
    window.show()
    window1.show()

    sys.exit(app.exec_())


# def main():
#     app = QtWidgets.QApplication(sys.argv)
    
    

#     window = MainWindow()
#     window.show()
    

    

#     sys.exit(app.exec_())




# if __name__ == '__main__':
#     main()


   

         


   










#################################################################################################

# class MainWindow(QMainWindow):
#     singleton: 'MainWindow' = None

#     def __init__(self):
#         super().__init__()
        
#         # self.ui.pushButton.clicked.connect(MainWindow.restart)
        
#         # self.show()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
        
#         self.show()



#         # PAGE 1
#         self.ui.home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        
# #         # PAGE 2
#         self.ui.production.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Production))

# #         # PAGE 3
#         self.ui.storage.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Storage))

# #         # PAGE 4
#         self.ui.dispatch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Dispatch))

# #         # PAGE 5
#         self.ui.Stats.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Statistics))

#         #self.ui.pushButton.clicked.connect(restart)

#         self.ui.pushButton.clicked.connect(MainWindow.restart)

# #         ## SHOW ==> MAIN WINDOW
# #         ########################################################################
#         MainWindow.show(self)
# #         ## ==> END ##


#     @staticmethod
#     def restart():
#         #status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
#         MainWindow.singleton = MainWindow()
#         #QtCore.QCoreApplication.quit()
#         #MainWindow()


# def main():
#     app = QApplication([])
#     #app = QtWidgets.QApplication(sys.argv)
    
    
#     #MainWindow.show()
#     MainWindow().restart()
    
   
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
