import sys
from PyQt5.QtGui import QPixmap, QTextBlock
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
from tkinter import *
import tkinter.ttk as ttk

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("노래 리스트 var.2")
        self.setresize = (100,500,300,500)

        self.rjatorLabel=QLabel("검색",self)
        self.rjatorText=QTextBlock()

        # btn_rjatorframe=QHBoxLayout()

        # btn_rjatorframe.addWidget(self.rjatorLabel)

        # btn_rjatorframe_layout=QWidget()
        # btn_rjatorframe_layout.setLayout(self.rjatorLabel)

        





if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()

    win.show()
    app.exec_()