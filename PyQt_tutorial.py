# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:28:59 2020

@author: rodri
"""

#https://build-system.fman.io/pyqt5-tutorial
# https://doc.qt.io/qt-5/stylesheet-syntax.html

# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMessageBox
# app= QApplication([]) #every GUI needs this, and brackets are the command line arguments passes to the application
# app.setStyleSheet("QPushButton:hover {margin: 10ex; color: green}") #added hover for psuedostate
# # app.setStyleSheet("QMessageBox {color:green}")
# button= QPushButton("is that a frog?")
# # label= QLabel('Hello World <3') #make the label
# # label.show() #show the label
# def on_button_click():
#     alert= QMessageBox()
#     alert.setText("It is! ribbit ribbit")
#     alert.setStyleSheet("QLabel{ color: green}")
#     alert.exec()

# button.clicked.connect(on_button_click)
# #button.clicked is a signal
# #.connect is a slot, which is a function that gets called when signal occurs 
# button.show()
# app.exec_()  #run the application

#within every app, everything is a widget
####################################################
# http://zetcode.com/gui/pyqt5/firstprograms/
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QFont

class Example(QWidget): #inherits from the Qwidget class

    def __init__(self):
        super().__init__()  #returns the parent object, and init is the constructor
        self.initUI() #creation of the GUI
    
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("hiiiii")
        
        btn= QPushButton("Quit", self) #the button is the instance of the QpushButton class, second paramete is the parent widget
        #self will be the Example widget from this class (Example(QWidget))
        btn.clicked.connect(QApplication.instance().quit) #quits the app
        btn.setToolTip("<3")
        btn.resize(btn.sizeHint()) #sets recommended size
        btn.move(50,50)
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.show()
        
    def closeEvent(self, event):
        #if we close the Qwidget, this is raised
        #widgets without parents are the toplevel windows
        reply= QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def center(self):
        qr=self.frameGeometry() #specifies the geometry of the main window and resolution of the monitor
        cp= QDesktopWidget().availableGeometry().center() #set the center of the rectangle to the center of the screen
        qr.moveCenter(cp) #set the center of the rectangle to the center of the screen
        self.move(qr.topLeft()) #move the top left of the app window to the top left of the qr rectangle 
            
def main():
    app= QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()