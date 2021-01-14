import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import random

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(800,300,621,351)
        self.setWindowTitle("FiestaBot")
        self.setFixedSize(621,351)
        self.setWindowIcon(QIcon("Image//fiest.ico"))
        tab = QTabWidget()
        tab.addTab(Shop(), "Shop")

        vbox = QVBoxLayout()
        vbox.addWidget(tab)
        self.setLayout(vbox)
        self.show()

#Shop tab
class Shop(QWidget):
    def __init__(self):
        super().__init__()
        self.charselect()
        self.rowselect()
        self.tableprice()
    

    def charselect(self):
        label1 = QLabel("Charakterauswahl", self)
        label1.setGeometry(30,20,230,16)
        label1.setFont(QFont("Ravie", 12))
        scroll = QListWidget(self)
        scroll.setGeometry(30,50,211,87)
        csv_file = open("VerkaufInfo.csv", "r")
        objekt = csv.reader(csv_file, delimiter=";")
        csvl = list(objekt)
        charcount = int(csvl[0][2])
        for i in range(charcount):
            scroll.addItem(csvl[i*5][0])
        button = QPushButton("Preise anzeigen",self)
        button.setGeometry(30,140,101,28)
        check = QCheckBox("Preis OK",self)
        check.setGeometry(140,145,95,20)

    def rowselect(self):
        label1 = QLabel("Verfügbare Shopzeilen",self)
        label1.setGeometry(40,180,131,16)
        label1.setFont(QFont("Ravie", 8))
        radio1 = QRadioButton("1 (Standard)",self)
        radio2 = QRadioButton("2 (CS-Haus)",self)
        radio3 = QRadioButton("3 (GH-Lizenz)",self)
        radio4 = QRadioButton("4 (CS-Haus + GH-Lizenz)",self)
        radio1.setGeometry(40,200,101,20)
        radio2.setGeometry(40,220,101,20)
        radio3.setGeometry(40,240,101,20)
        radio4.setGeometry(40,260,141,20)
        radio1.toggled.connect(self.lineone)
        radio2.toggled.connect(self.linetwo)
        radio3.toggled.connect(self.linethree)
        radio4.toggled.connect(self.linefour)
    def tableprice(self):
        self.list=[]
        self.backlist = []
        x = 0
        for i in range(4):
            for j in range(5):
                self.backlist.append(QLabel("",self))
                self.backlist[x].setStyleSheet("background-color : rgb(200,200,200)")          
                self.backlist[x].setGeometry(320+(j * 50),80+(i*50),41,41)
                self.list.append(QLabel("",self))
                self.list[x].setStyleSheet("background-color : rgb(105,105,105)")          
                self.list[x].setGeometry(320+(j * 50),80+(i*50),41,41)
                self.list[x].installEventFilter(self)
                x += 1
       
        gem = QLabel(self)
        gem.setGeometry(330,30,16,16)
        gem.setStyleSheet("background-image : url(Image//gem.jpg)")
        self.gemc = QLabel("",self)
        self.gemc.setGeometry(355,30,25,16)
        self.gemc.setFont(QFont("Dubai Medium", 10))

        gold = QLabel(self)
        gold.setGeometry(390,30,16,16)
        gold.setStyleSheet("background-image : url(Image//gold.jpg)")
        self.goldc = QLabel("",self)
        self.goldc.setGeometry(415,30,25,16)
        self.goldc.setFont(QFont("Dubai Medium", 10))

        silver = QLabel(self)
        silver.setGeometry(450,30,16,16)
        silver.setStyleSheet("background-image : url(Image//silver.jpg)")
        self.silverc = QLabel("",self)
        self.silverc.setGeometry(475,30,25,16)
        self.silverc.setFont(QFont("Dubai Medium", 10))
        
        copper = QLabel(self)
        copper.setGeometry(510,30,16,16)
        copper.hide
        copper.setStyleSheet("background-image : url(Image//kupfer.jpg)")
        self.copperc = QLabel("",self)
        self.copperc.setGeometry(535,30,25,16)
        self.copperc.setFont(QFont("Dubai Medium", 10))
            
        
    def eventFilter(self,object, event):
        if event.type() == QEvent.Enter:
            object.setStyleSheet("background-color : rgb(150,150,150)")
            #Test
            self.gemc.setText(str(random.randint(1,99)))
            self.goldc.setText(str(random.randint(1,99)))
            self.silverc.setText(str(random.randint(1,99)))
            self.copperc.setText(str(random.randint(1,99)))
            
            return True
        elif event.type() == QEvent.Leave:
            object.setStyleSheet("background-color : rgb(105,105,105)")
            self.gemc.setText("")
            self.goldc.setText("")
            self.silverc.setText("")
            self.copperc.setText("")
        return False

    def lineone(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
            for i in range(5,20):
                self.list[i].setHidden(True)
    def linetwo(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
            for i in range(10,20):
                self.list[i].setHidden(True)
    def linethree(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
            for i in range(15,20):
                self.list[i].setHidden(True)
    def linefour(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
app = QApplication(sys.argv)
win = Mainwindow()
sys.exit(app.exec_())