import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
from tkinter import *
import tkinter.ttk as ttk
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("계산기다")
        self.setGeometry = (200,500,500,600)

        rPtksrl_box=QVBoxLayout()

        self.label=QLabel("0",self)
        self.btn1=QPushButton("1",self)
        self.btn2=QPushButton("2",self)
        self.btn3=QPushButton("3",self)
        self.btn4=QPushButton("4",self)
        self.btn5=QPushButton("5",self)
        self.btn6=QPushButton("6",self)
        self.btn7=QPushButton("7",self)
        self.btn8=QPushButton("8",self)
        self.btn9=QPushButton("9",self)
        self.btn0=QPushButton("0",self)

        self.btnplus=QPushButton("+",self)
        self.btnminus=QPushButton("-",self)
        self.btnmult=QPushButton("*",self)
        self.btndiv=QPushButton("/",self)
        self.btnresult=QPushButton("=",self)
        self.btndhswja=QPushButton(".",self)

        self.btn1.clicked.connect(self.numpuls1)
        self.btn2.clicked.connect(self.numpuls2)
        self.btn3.clicked.connect(self.numpuls3)
        self.btn4.clicked.connect(self.numpuls4)
        self.btn5.clicked.connect(self.numpuls5)
        self.btn6.clicked.connect(self.numpuls6)
        self.btn7.clicked.connect(self.numpuls7)
        self.btn8.clicked.connect(self.numpuls8)
        self.btn9.clicked.connect(self.numpuls9)
        self.btn0.clicked.connect(self.numpuls0)

        self.btnplus.clicked.connect(self.plus)
        self.btnminus.clicked.connect(self.minus)
        self.btnmult.clicked.connect(self.mult)
        self.btndiv.clicked.connect(self.div)
        self.btnresult.clicked.connect(self.result)
        self.btndhswja.clicked.connect(self.dhswja)
        

        btn_frame1=QHBoxLayout()
        btn_frame1.addWidget(self.btn7)
        btn_frame1.addWidget(self.btn8)
        btn_frame1.addWidget(self.btn9)
        btn_frame1.addWidget(self.btnplus)

        btn_frame2=QHBoxLayout()
        btn_frame2.addWidget(self.btn4)
        btn_frame2.addWidget(self.btn5)
        btn_frame2.addWidget(self.btn6)
        btn_frame2.addWidget(self.btnminus)

        btn_frame3=QHBoxLayout()
        btn_frame3.addWidget(self.btn1)
        btn_frame3.addWidget(self.btn2)
        btn_frame3.addWidget(self.btn3)
        btn_frame3.addWidget(self.btnmult)

        btn_frame0=QHBoxLayout()
        btn_frame0.addWidget(self.btndhswja)
        btn_frame0.addWidget(self.btn0)
        btn_frame0.addWidget(self.btnresult)
        btn_frame0.addWidget(self.btndiv)

        label_box=QHBoxLayout()
        label_box.addWidget(self.label)

        btn_frame1_layout=QWidget()
        btn_frame1_layout.setLayout(btn_frame1)

        btn_frame2_layout=QWidget()
        btn_frame2_layout.setLayout(btn_frame2)

        btn_frame3_layout=QWidget()
        btn_frame3_layout.setLayout(btn_frame3)

        btn_frame0_layout=QWidget()
        btn_frame0_layout.setLayout(btn_frame0)

        label_frame=QWidget()
        label_frame.setLayout(label_box)


        rPtksrl_box.addWidget(label_frame)
        rPtksrl_box.addWidget(btn_frame1_layout)
        rPtksrl_box.addWidget(btn_frame2_layout)
        rPtksrl_box.addWidget(btn_frame3_layout)
        rPtksrl_box.addWidget(btn_frame0_layout)


        self.setLayout(rPtksrl_box)
    def labelset(self, num):

        guswolabel=self.label.text()
        if guswolabel=="0":
            if "0"<=num<="9":
                self.label.setText(num)

        elif "0"<=num<="9":
            self.label.setText(guswolabel+num)

        elif guswolabel[len(guswolabel)-1:]!="+" and guswolabel[len(guswolabel)-1:]!="-" and guswolabel[len(guswolabel)-1:]!="*" and guswolabel[len(guswolabel)-1:]!="/"and guswolabel[len(guswolabel)-1:]!=".":
            self.label.setText(guswolabel+num)

    def result(self):
        guswolabel=eval(self.label.text())
        if guswolabel%1==0:
            self.label.setText(str(int(guswolabel)))
        else:
            self.label.setText(str(float(guswolabel)))

    def numpuls1(self):
        self.labelset("1")

    def numpuls2(self):
        self.labelset("2")

    def numpuls3(self):
        self.labelset("3")

    def numpuls4(self):
        self.labelset("4")

    def numpuls5(self):
        self.labelset("5")

    def numpuls6(self):
        self.labelset("6")

    def numpuls7(self):
        self.labelset("7")

    def numpuls8(self):
        self.labelset("8")

    def numpuls9(self):
        self.labelset("9")

    def numpuls0(self):
        self.labelset("0")

    def plus(self):
        self.labelset("+")
        
    def minus(self):
        self.labelset("-")

    def mult(self):
        self.labelset("*")

    def div(self):
        self.labelset("/")

    def dhswja(self):
        self.labelset(".")




if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()

    win.show()
    app.exec_()