from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("karte_zeigen.ui",self)
        self.show()


        self.pushButton.clicked.connect(self.buttonclick)
    

    def buttonclick(self):
        try: 
            lNgeLineEdit_text = self.lNgeLineEdit.text()
            laenge = float(lNgeLineEdit_text)
            breiteLineEdit_text = self.breiteLineEdit.text()
            breite = float(breiteLineEdit_text)
            self.webEngineView.load(QUrl(f"https://www.google.ch/maps/place/{breite},{laenge}"))

        except:
            QMessageBox.critical(self,"Warnung", "Bitte Koordinaten eigneben")       
            
app = QApplication([])
win = UIFenster()
app.exec()
