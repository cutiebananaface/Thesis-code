from PyQt5.uic import loadUiType

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

import sys
from PyQt5.QtWidgets import QApplication
import numpy as np
Ui_MainWindow, QMainWindow = loadUiType('window.ui')
#http://blog.rcnelson.com/building-a-matplotlib-gui-with-qt-designer-part-1/
        
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig_dict = {}

        self.mplfigs.itemClicked.connect(self.changefig)

        fig = Figure()
        self.addmpl(fig)

    def changefig(self, item): #signal for changing the figure, itemclicked is connected to this
        text = item.text() #to get info and text of the item
        self.rmmpl() #remove the old fig
        self.addmpl(self.fig_dict[text]) #add new fig based on the list item that was clicked

    def addfig(self, name, fig):
        self.fig_dict[name] = fig
        self.mplfigs.addItem(name) #add fig to fig dictionary?

    def addmpl(self, fig): #add plot 
        self.canvas = FigureCanvas(fig)  
        self.mplvl.addWidget(self.canvas) #create the figure canvas widget 
        self.canvas.draw() #draw canvas on app window
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True) #set toolbar
        self.mplvl.addWidget(self.toolbar) #add toolbar to layout
# This is the alternate toolbar placement. Susbstitute the three lines above
# for these lines to see the different look.
#        self.toolbar = NavigationToolbar(self.canvas,
#                self, coordinates=True)
#        self.addToolBar(self.toolbar)

    def rmmpl(self,): #changing plots- removes plot
        self.mplvl.removeWidget(self.canvas) #remove canvas and toolbar from vertical layout
        self.canvas.close() #removes their display from the application window 
        self.mplvl.removeWidget(self.toolbar) #remove the toolbar
        self.toolbar.close() #remove toolbar from window

# if __name__ == '__main__':
    # import sys
    # from PyQt5.QtWidgets import QApplication
    # import numpy as np
# def customplot(xdata, ydata):
def customplot(nameoffig,figureobj):
    fig1 = Figure() #figure instance
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(np.random.rand(5))

    fig2 = Figure() #figure instance
    ax1f2 = fig2.add_subplot(121)
    ax1f2.plot(np.random.rand(5))
    ax2f2 = fig2.add_subplot(122)
    ax2f2.plot(np.random.rand(10))

    fig3 = Figure() #figure instance
    ax1f3 = fig3.add_subplot(111)
    ax1f3.pcolormesh(np.random.rand(20,20))
    
    #place holder for what i want to do later
    fig4= Figure()
    ax1f4= fig4.add_subplot(311)
    ax1f4.plot(np.random.rand(5))
    ax2f4= fig4.add_subplot(312)
    ax2f4.plot(np.random.rand(5))
    ax3f4= fig4.add_subplot(313)
    ax3f4.plot(np.random.rand(5), '*-', label="label for legend") #make markers and plot
    ax3f4.set_xlabel("X axis label") #make label
    ax3f4.set_ylabel("Y axis label") # make label
    ax3f4.set_title("Title of subplot") #make title
    ax3f4.annotate("annotate string", (1,0.5)) #make string on plot
    ax3f4.legend() #display legend
    
    # fig5= Figure()
    # ax1f5= fig5.add_subplot(311)
    # ax1f5.plot(xdata,ydata)
    # ax2f5= fig5.add_subplot(312)
    # ax2f5.plot(xdata)

    app = QApplication(sys.argv)
    main = Main()
    main.addfig('One plot', fig1)
    main.addfig('Two plots', fig2)
    main.addfig('Pcolormesh', fig3)
    main.addfig("Testfig", fig4)
    main.addfig(nameoffig, figureobj)
    # main.addfig("from saveAshape", fig5)
    main.show()
    sys.exit(app.exec_())

