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
        #Create label and ListWidget
        self.charid = 0
        label1 = QLabel("Charakterauswahl", self)
        label1.setGeometry(30,20,230,16)
        label1.setFont(QFont("Ravie", 12))
        self.scroll = QListWidget(self)
        self.scroll.setGeometry(30,50,211,87)

        #Read csv-file for creating charlist
        self.scroll.currentRow()
        csvfile = open("VerkaufInfo.csv", "r")
        objekt = csv.reader(csvfile, delimiter=";")
        csvl = list(objekt)
        charcount = int(csvl[0][2])
        for i in range(charcount):
            self.scroll.addItem(csvl[i*5][0])
        self.charid = 0
        csvfile.close()
        self.scroll.clicked.connect(self.click_on_item)

        #Create button and checkbox
        button = QPushButton("Preise anzeigen",self)
        button.setGeometry(30,140,101,28)
        check = QCheckBox("Preis OK",self)
        check.setGeometry(140,145,95,20)

    #Click on charName
    def click_on_item(self):
        self.charid = self.scroll.currentRow()
        csvfile = open("VerkaufInfo.csv", "r")
        file = csv.reader(csvfile, delimiter=";")
        csvl = list(file)
        x = int(csvl[5*self.charid][1])
        if x == 1:
            self.radio1.setChecked(True)
            self.lineone(self.radio1.isChecked())
            print(self.radio1.isChecked())
        if x == 2:
            self.radio2.setChecked(True)
            self.linetwo(self.radio2.isChecked())
            #print(self.radio2.isChecked())
        if x == 3:
            self.radio3.setChecked(True)
            self.linethree(self.radio3.isChecked())
        if x == 4:
            self.radio4.setChecked(True)
            self.linefour(self.radio4.isChecked())
    
    #Create radiobuttons
    def rowselect(self):
        label1 = QLabel("Verfügbare Shopzeilen",self)
        label1.setGeometry(40,180,131,16)
        label1.setFont(QFont("Ravie", 8))
        self.radio1 = QRadioButton("1 (Standard)",self)
        self.radio2 = QRadioButton("2 (CS-Haus)",self)
        self.radio3 = QRadioButton("3 (GH-Lizenz)",self)
        self.radio4 = QRadioButton("4 (CS-Haus + GH-Lizenz)",self)
        self.radio1.setGeometry(40,200,101,20)
        self.radio2.setGeometry(40,220,101,20)
        self.radio3.setGeometry(40,240,101,20)
        self.radio4.setGeometry(40,260,141,20)
        self.radio1.toggled.connect(self.lineone)
        self.radio2.toggled.connect(self.linetwo)
        self.radio3.toggled.connect(self.linethree)
        self.radio4.toggled.connect(self.linefour)

    #Create inventory
    def tableprice(self):
        #Create the inventory
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
        #Create gem icon 
        gem = QLabel(self)
        gem.setGeometry(330,30,16,16)
        gem.setStyleSheet("background-image : url(Image//gem.jpg)")
        self.gemc = QLabel("",self)
        self.gemc.setGeometry(355,30,25,16)
        self.gemc.setFont(QFont("Dubai Medium", 10))

        #Create gold icon
        gold = QLabel(self)
        gold.setGeometry(390,30,16,16)
        gold.setStyleSheet("background-image : url(Image//gold.jpg)")
        self.goldc = QLabel("",self)
        self.goldc.setGeometry(415,30,25,16)
        self.goldc.setFont(QFont("Dubai Medium", 10))

        #Create silver icon
        silver = QLabel(self)
        silver.setGeometry(450,30,16,16)
        silver.setStyleSheet("background-image : url(Image//silver.jpg)")
        self.silverc = QLabel("",self)
        self.silverc.setGeometry(475,30,25,16)
        self.silverc.setFont(QFont("Dubai Medium", 10))
        
        #Create copper icon
        copper = QLabel(self)
        copper.setGeometry(510,30,16,16)
        copper.hide
        copper.setStyleSheet("background-image : url(Image//kupfer.jpg)")
        self.copperc = QLabel("",self)
        self.copperc.setGeometry(535,30,25,16)
        self.copperc.setFont(QFont("Dubai Medium", 10))

    
    #Function to select the price 
    def itemselect(self,x,charid):
        csvfile = open("VerkaufInfo.csv", "r")
        file = csv.reader(csvfile, delimiter=";")
        csvl = list(file)
        charid = charid * 5
        ge, g,s,k = 0,0,0,0
        if x <= 4:
            ge, g,s,k = csvl[1+charid][x].split(",")
        if 4 < x <=9:
            ge, g,s,k =csvl[2+charid][x-5].split(",")
        if 9 < x <=14:
            ge, g,s,k =csvl[3+charid][x-10].split(",")
        if 14 < x <=19:
            ge, g,s,k =csvl[4+charid][x-15].split(",")
        csvfile.close()
        return ge,g,s,k

    #Hover-function for inventory  
    def eventFilter(self,object, event):
        if event.type() == QEvent.Enter:
            object.setStyleSheet("background-color : rgb(150,150,150)")
            x = self.list.index(object)
            gem,gold,silver,copper = self.itemselect(x,self.charid)
            self.gemc.setText(gem)
            self.goldc.setText(gold)
            self.silverc.setText(silver)
            self.copperc.setText(copper)
            return True
        elif event.type() == QEvent.Leave:
            object.setStyleSheet("background-color : rgb(105,105,105)")
            self.gemc.setText("")
            self.goldc.setText("")
            self.silverc.setText("")
            self.copperc.setText("")
        return False
    #Enable only first row of inventory
    def lineone(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
            for i in range(5,20):
                self.list[i].setHidden(True)

    #Enable only first two rows of inventory
    def linetwo(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
            for i in range(10,20):
                self.list[i].setHidden(True)

    #Enable only first three rows of inventory
    def linethree(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
            for i in range(15,20):
                self.list[i].setHidden(True)

    #Enable all rows of inventory
    def linefour(self, selected):
        if selected:
            for i in self.list:
                i.setHidden(False)
                
app = QApplication(sys.argv)
win = Mainwindow()
sys.exit(app.exec_())