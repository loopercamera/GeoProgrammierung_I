from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("uebung_8_gui.ui",self)
        self.show()
        self.pb_plot.clicked.connect(self.plot)


        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0,self.canvas) # 0 legt Reihenfolge fest

        self.slider_min.valueChanged.connect(self.updateslider_min)
        self.slider_max.valueChanged.connect(self.updateslider_max)
        self.cb_farbe.addItems(["b","g","r","c","m","y","k"])
        self.cb_farbe.currentIndexChanged.connect(self.plot)
        self.cb_darstellung.addItems(["o-","o--",".-",":",".","v","1","2","3"])
        self.cb_darstellung.currentIndexChanged.connect(self.plot)
        self.slider_anzahl_punkte.valueChanged.connect(self.updateslider_anzahl_punkte)


    def updateslider_anzahl_punkte (self,value):
        self.anzahl_punkte = value
        try:
            self.plot()
        except:
            pass

    def updateslider_min (self,value):
        self.min = value
        try:
            self.plot()
        except:
            pass
    def updateslider_max (self,value):
        self.max = value
        
        try:
            self.plot()
        except:
            pass
        


    def plot (self):     
        plt.clf()

        try:
            self.anzahl_punkte_def = self.anzahl_punkte
        except:
            self.anzahl_punkte_def = 30
                       
        try: 
            self.max_def = self.max
        except:
            self.max_def = -50
        
        try: 
            self.min_def = self.min
        except:
            self.min_def = 50
        
        self.farbe_darstellung = f"{self.cb_farbe.currentText()}{self.cb_darstellung.currentText()}"
        

        try:
            polynome = self.le_fkt.text()
            polynome_list = polynome.split(",")
            for i in range(len(polynome_list)):
                polynome_list[i] = float(polynome_list[i]) 
            f = np.poly1d(polynome_list)
            
            
            x = np.linspace(self.min_def,self.max_def,self.anzahl_punkte_def)
            y = f(x)
            
            plt.plot(x,y,self.farbe_darstellung)
            self.canvas.draw()


        except:
            QMessageBox.critical(self,"Fehler", "Bitte Polynme Kommagetrennt eingeben.")
            return

        



app = QApplication([])
win = Window()
app.exec()