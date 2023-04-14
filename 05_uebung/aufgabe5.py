from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse
from datetime import datetime





class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Programmierung II")

        #layout erzeugen
        #layout = ... # QVBoxLayout, QHBoxLayout, QGridlayout, ...

        layout = QFormLayout()

        #gui Elemente erstellen

        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QDateEdit()
        self.adresse = QLineEdit()
        self.postleitzahl = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz","Deutschland","Österreich"])
        self.auf_karte_anzeigen = QPushButton("Auf Karte anzeigen")
        self.laden = QPushButton("Laden")              
        self.button_save = QPushButton("Speichern")
     
        #gui Elemente dem Layout hinzufügen

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        
        #connect
        save = QAction("Laden", self)
        save.triggered.connect(self.load)        
        laden = QAction("Save", self)
        laden.triggered.connect(self.file_save)        
        quit= QAction("Quit", self)
        quit.triggered.connect(self.file_quit)

        filemenu.addAction(laden)    
        filemenu.addAction(save)
        filemenu.addAction(quit)

        self.button_save.clicked.connect(self.file_save)
        self.auf_karte_anzeigen.clicked.connect(self.karte_anzeigen)
        self.laden.clicked.connect(self.load)
        
        
        

        
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag", self.geburtstag)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Postleit:", self.postleitzahl)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.auf_karte_anzeigen)    
        layout.addRow(self.laden)
        layout.addRow(self.button_save) 
        
        

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def file_save(self):

        speicherpfad, filter = QFileDialog.getSaveFileName(self,"Datei speichern" , "" , "Text Dateien (*.txt)")
        if speicherpfad != "":
            output_file = open(speicherpfad, "w", encoding="utf-8")
            data = f"{self.vorname.text()},{self.name.text()},{self.geburtstag.text()},{self.adresse.text()},{self.postleitzahl.text()},{self.ort.text()},{self.land.currentText()}"
            output_file.write(str(data))
            output_file.close()
        

        

    def load (self):
        speicherpfad, filter =QFileDialog.getOpenFileName(self,"Datei öffen","" ,"Text Files(*.txt)")
        
        if speicherpfad != "":
            
            input_file = open(speicherpfad,"r",encoding="utf-8")
            for zeile in input_file:
                 zeile = zeile.rstrip()
                 daten = zeile.split(",")
                 self.vorname.setText(daten[0])
                 self.name.setText(daten[1])
                 datum_convertet = datetime.strptime(daten[2], '%d/%m/%Y').date()
                 self.geburtstag.setDate(datum_convertet)
                 self.adresse.setText(daten[3])
                 self.postleitzahl.setText(daten[4])
                 self.ort.setText(daten[5])
                 self.land.setCurrentText(daten[6])
            input_file.close()

    def file_quit(self):
        self.close ()

    def karte_anzeigen (self):
        
        adresse = self.adresse.text()
        adresse = adresse.replace(" ","+")
        adresse = urllib.parse.quote(adresse)
        postleitzahl = urllib.parse.quote(self.postleitzahl.text())
        ort = urllib.parse.quote(self.ort.text()) 
        land = urllib.parse.quote(self.land.currentText())       
        
        link = f"https://www.google.ch/maps/place/{adresse}+{postleitzahl}+{ort}+{land}"
        
        QDesktopServices.openUrl(QUrl(link))   # benötigt QtCore & QtGui





app = QApplication([])
win = Fenster()
app.exec()