from PyQt5.QtWidgets import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Programmierung I")

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

        self.button_save = QPushButton("Save")
     
        #gui Elemente dem Layout hinzufügen

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        
        #connect
        save = QAction("Save", self)
        save.triggered.connect(self.file_save)

        quit= QAction("Quit", self)
        quit.triggered.connect(self.file_quit)

        filemenu.addAction(save)
        filemenu.addAction(quit)

        self.button_save.clicked.connect(self.file_save)
        
        
        

        
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag", self.geburtstag)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Postleit:", self.postleitzahl)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.button_save)      


        

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def file_save(self):
        file = open("output.txt","w",encoding="utf-8")

        data = f"{self.vorname.text()},{self.name.text()},{self.geburtstag.text()},{self.adresse.text()},{self.postleitzahl.text()},{self.ort.text()},{self.land.currentText()}"

        file.write(str(data))
        print(data)

        file.close()

        

    def file_quit(self):
        self.close ()


app = QApplication([])
win = Fenster()
app.exec()