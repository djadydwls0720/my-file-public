# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Temp\musiclist.var.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 9, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(6, 39, 41, 21))
        self.label_2.setObjectName("label_2")
        self.search_text = QtWidgets.QLineEdit(self.centralwidget)
        self.search_text.setGeometry(QtCore.QRect(50, 10, 113, 20))
        self.search_text.setObjectName("search_text")
        self.search_text_yotude = QtWidgets.QLineEdit(self.centralwidget)
        self.search_text_yotude.setGeometry(QtCore.QRect(50, 40, 113, 20))
        self.search_text_yotude.setObjectName("search_text_yotude")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(172, 10, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(172, 40, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(690, 410, 81, 31))
        self.next_btn.setObjectName("next_btn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 561, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 250, 75, 23))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 300, 75, 23))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 150, 75, 23))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_29 = QtWidgets.QPushButton(self.frame)
        self.pushButton_29.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 100, 75, 23))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame)
        self.pushButton_27.setGeometry(QtCore.QRect(360, 50, 75, 23))
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame)
        self.pushButton_37.setGeometry(QtCore.QRect(480, 150, 75, 23))
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame)
        self.pushButton_28.setGeometry(QtCore.QRect(360, 300, 75, 23))
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 200, 75, 23))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame)
        self.pushButton_35.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(240, 100, 75, 23))
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame)
        self.pushButton_36.setGeometry(QtCore.QRect(480, 100, 75, 23))
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame)
        self.pushButton_24.setGeometry(QtCore.QRect(360, 250, 75, 23))
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame)
        self.pushButton_31.setGeometry(QtCore.QRect(480, 0, 75, 23))
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame)
        self.pushButton_30.setGeometry(QtCore.QRect(360, 0, 75, 23))
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame)
        self.pushButton_33.setGeometry(QtCore.QRect(480, 200, 75, 23))
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame)
        self.pushButton_25.setGeometry(QtCore.QRect(360, 100, 75, 23))
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(120, 250, 75, 23))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame)
        self.pushButton_34.setGeometry(QtCore.QRect(480, 300, 75, 23))
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 50, 75, 23))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 300, 75, 23))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(240, 0, 75, 23))
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame)
        self.pushButton_26.setGeometry(QtCore.QRect(360, 150, 75, 23))
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame)
        self.pushButton_32.setGeometry(QtCore.QRect(480, 250, 75, 23))
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(120, 0, 75, 23))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame)
        self.pushButton_23.setGeometry(QtCore.QRect(240, 250, 75, 23))
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame)
        self.pushButton_22.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame)
        self.pushButton_21.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.remocon_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remocon_btn.setGeometry(QtCore.QRect(593, 80, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.remocon_btn.setFont(font)
        self.remocon_btn.setObjectName("remocon_btn")
        self.corona_btn = QtWidgets.QPushButton(self.centralwidget)
        self.corona_btn.setGeometry(QtCore.QRect(593, 170, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.corona_btn.setFont(font)
        self.corona_btn.setObjectName("corona_btn")
        self.wether_btn = QtWidgets.QPushButton(self.centralwidget)
        self.wether_btn.setGeometry(QtCore.QRect(593, 260, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.wether_btn.setFont(font)
        self.wether_btn.setObjectName("wether_btn")
        self.the_btn = QtWidgets.QPushButton(self.centralwidget)
        self.the_btn.setGeometry(QtCore.QRect(593, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.the_btn.setFont(font)
        self.the_btn.setObjectName("the_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(593, 410, 81, 31))
        self.back_btn.setObjectName("back_btn")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(240, 14, 90, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(304, 14, 90, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 80, 561, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_38.setGeometry(QtCore.QRect(0, 250, 75, 23))
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_39.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_40.setGeometry(QtCore.QRect(120, 300, 75, 23))
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_41.setGeometry(QtCore.QRect(0, 150, 75, 23))
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_42.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_43.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_43.setText("")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_44.setGeometry(QtCore.QRect(0, 100, 75, 23))
        self.pushButton_44.setText("")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_45.setGeometry(QtCore.QRect(360, 50, 75, 23))
        self.pushButton_45.setText("")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_46.setGeometry(QtCore.QRect(480, 150, 75, 23))
        self.pushButton_46.setText("")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_47.setGeometry(QtCore.QRect(360, 300, 75, 23))
        self.pushButton_47.setText("")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_48.setGeometry(QtCore.QRect(0, 200, 75, 23))
        self.pushButton_48.setText("")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_49.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton_49.setText("")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_50.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.pushButton_50.setText("")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_51.setGeometry(QtCore.QRect(240, 100, 75, 23))
        self.pushButton_51.setText("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_52.setGeometry(QtCore.QRect(480, 100, 75, 23))
        self.pushButton_52.setText("")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_53.setGeometry(QtCore.QRect(360, 250, 75, 23))
        self.pushButton_53.setText("")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_54.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.pushButton_54.setText("")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_55.setGeometry(QtCore.QRect(480, 0, 75, 23))
        self.pushButton_55.setText("")
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_56.setGeometry(QtCore.QRect(360, 0, 75, 23))
        self.pushButton_56.setText("")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_57.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.pushButton_57.setText("")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_58.setGeometry(QtCore.QRect(480, 200, 75, 23))
        self.pushButton_58.setText("")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_59.setGeometry(QtCore.QRect(360, 100, 75, 23))
        self.pushButton_59.setText("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_60.setGeometry(QtCore.QRect(120, 250, 75, 23))
        self.pushButton_60.setText("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_61.setGeometry(QtCore.QRect(480, 300, 75, 23))
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_62.setGeometry(QtCore.QRect(0, 50, 75, 23))
        self.pushButton_62.setText("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_63 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_63.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_64.setGeometry(QtCore.QRect(0, 300, 75, 23))
        self.pushButton_64.setText("")
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_65 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_65.setGeometry(QtCore.QRect(240, 0, 75, 23))
        self.pushButton_65.setText("")
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_66.setGeometry(QtCore.QRect(360, 150, 75, 23))
        self.pushButton_66.setText("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_67.setGeometry(QtCore.QRect(480, 250, 75, 23))
        self.pushButton_67.setText("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_68.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.pushButton_68.setText("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_69.setGeometry(QtCore.QRect(120, 0, 75, 23))
        self.pushButton_69.setText("")
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_70.setGeometry(QtCore.QRect(240, 250, 75, 23))
        self.pushButton_70.setText("")
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_71.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.pushButton_71.setText("")
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_72.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 80, 561, 341))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_73 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_73.setGeometry(QtCore.QRect(0, 250, 75, 23))
        self.pushButton_73.setText("")
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_74 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_74.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.pushButton_74.setText("")
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_75.setGeometry(QtCore.QRect(120, 300, 75, 23))
        self.pushButton_75.setText("")
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_76.setGeometry(QtCore.QRect(0, 150, 75, 23))
        self.pushButton_76.setText("")
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_77.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.pushButton_77.setText("")
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_78.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_78.setText("")
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_79.setGeometry(QtCore.QRect(0, 100, 75, 23))
        self.pushButton_79.setText("")
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_80.setGeometry(QtCore.QRect(360, 50, 75, 23))
        self.pushButton_80.setText("")
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_81.setGeometry(QtCore.QRect(480, 150, 75, 23))
        self.pushButton_81.setText("")
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_82 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_82.setGeometry(QtCore.QRect(360, 300, 75, 23))
        self.pushButton_82.setText("")
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_83 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_83.setGeometry(QtCore.QRect(0, 200, 75, 23))
        self.pushButton_83.setText("")
        self.pushButton_83.setObjectName("pushButton_83")
        self.pushButton_84 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_84.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton_84.setText("")
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_85 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_85.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.pushButton_85.setText("")
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_86 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_86.setGeometry(QtCore.QRect(240, 100, 75, 23))
        self.pushButton_86.setText("")
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_87.setGeometry(QtCore.QRect(480, 100, 75, 23))
        self.pushButton_87.setText("")
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_88 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_88.setGeometry(QtCore.QRect(360, 250, 75, 23))
        self.pushButton_88.setText("")
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_89 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_89.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.pushButton_89.setText("")
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_90 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_90.setGeometry(QtCore.QRect(480, 0, 75, 23))
        self.pushButton_90.setText("")
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_91 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_91.setGeometry(QtCore.QRect(360, 0, 75, 23))
        self.pushButton_91.setText("")
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_92 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_92.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.pushButton_92.setText("")
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_93 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_93.setGeometry(QtCore.QRect(480, 200, 75, 23))
        self.pushButton_93.setText("")
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_94 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_94.setGeometry(QtCore.QRect(360, 100, 75, 23))
        self.pushButton_94.setText("")
        self.pushButton_94.setObjectName("pushButton_94")
        self.pushButton_95 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_95.setGeometry(QtCore.QRect(120, 250, 75, 23))
        self.pushButton_95.setText("")
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_96 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_96.setGeometry(QtCore.QRect(480, 300, 75, 23))
        self.pushButton_96.setText("")
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_97 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_97.setGeometry(QtCore.QRect(0, 50, 75, 23))
        self.pushButton_97.setText("")
        self.pushButton_97.setObjectName("pushButton_97")
        self.pushButton_98 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_98.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.pushButton_98.setText("")
        self.pushButton_98.setObjectName("pushButton_98")
        self.pushButton_99 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_99.setGeometry(QtCore.QRect(0, 300, 75, 23))
        self.pushButton_99.setText("")
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_100 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_100.setGeometry(QtCore.QRect(240, 0, 75, 23))
        self.pushButton_100.setText("")
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_101 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_101.setGeometry(QtCore.QRect(360, 150, 75, 23))
        self.pushButton_101.setText("")
        self.pushButton_101.setObjectName("pushButton_101")
        self.pushButton_102 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_102.setGeometry(QtCore.QRect(480, 250, 75, 23))
        self.pushButton_102.setText("")
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_103 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_103.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.pushButton_103.setText("")
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_104 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_104.setGeometry(QtCore.QRect(120, 0, 75, 23))
        self.pushButton_104.setText("")
        self.pushButton_104.setObjectName("pushButton_104")
        self.pushButton_105 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_105.setGeometry(QtCore.QRect(240, 250, 75, 23))
        self.pushButton_105.setText("")
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_106 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_106.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.pushButton_106.setText("")
        self.pushButton_106.setObjectName("pushButton_106")
        self.pushButton_107 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_107.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.pushButton_107.setText("")
        self.pushButton_107.setObjectName("pushButton_107")
        self.pushButton_108 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_108.setGeometry(QtCore.QRect(20, 410, 91, 31))
        self.pushButton_108.setObjectName("pushButton_108")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.search)
        self.pushButton_2.clicked.connect(MainWindow.search_youtube)



        
        self.pushButton_3.clicked.connect(MainWindow.clicked_Button0)
        self.pushButton_4.clicked.connect(MainWindow.clicked_Button1)
        self.pushButton_5.clicked.connect(MainWindow.clicked_Button2)
        self.pushButton_6.clicked.connect(MainWindow.clicked_Button3)
        self.pushButton_7.clicked.connect(MainWindow.clicked_Button4)
        self.pushButton_8.clicked.connect(MainWindow.clicked_Button5)
        self.pushButton_9.clicked.connect(MainWindow.clicked_Button6)
        self.pushButton_10.clicked.connect(MainWindow.clicked_Button7)
        self.pushButton_11.clicked.connect(MainWindow.clicked_Button8)
        self.pushButton_12.clicked.connect(MainWindow.clicked_Button9)
        self.pushButton_13.clicked.connect(MainWindow.clicked_Button10)
        self.pushButton_14.clicked.connect(MainWindow.clicked_Button11)
        self.pushButton_15.clicked.connect(MainWindow.clicked_Button12)
        self.pushButton_16.clicked.connect(MainWindow.clicked_Button13)
        self.pushButton_17.clicked.connect(MainWindow.clicked_Button14)
        self.pushButton_18.clicked.connect(MainWindow.clicked_Button15)
        self.pushButton_19.clicked.connect(MainWindow.clicked_Button16)
        self.pushButton_20.clicked.connect(MainWindow.clicked_Button17)
        self.pushButton_21.clicked.connect(MainWindow.clicked_Button18)
        self.pushButton_22.clicked.connect(MainWindow.clicked_Button19)
        self.pushButton_23.clicked.connect(MainWindow.clicked_Button20)
        self.pushButton_24.clicked.connect(MainWindow.clicked_Button21)
        self.pushButton_35.clicked.connect(MainWindow.clicked_Button22)
        self.pushButton_26.clicked.connect(MainWindow.clicked_Button23)
        self.pushButton_27.clicked.connect(MainWindow.clicked_Button24)
        self.pushButton_28.clicked.connect(MainWindow.clicked_Button25)
        self.pushButton_29.clicked.connect(MainWindow.clicked_Button26)
        self.pushButton_30.clicked.connect(MainWindow.clicked_Button27)
        self.pushButton_31.clicked.connect(MainWindow.clicked_Button28)
        self.pushButton_32.clicked.connect(MainWindow.clicked_Button29)
        self.pushButton_33.clicked.connect(MainWindow.clicked_Button30)
        self.pushButton_34.clicked.connect(MainWindow.clicked_Button31)
        self.pushButton_35.clicked.connect(MainWindow.clicked_Button32)
        self.pushButton_36.clicked.connect(MainWindow.clicked_Button33)
        self.pushButton_37.clicked.connect(MainWindow.clicked_Button34)



        self.pushButton_38.clicked.connect(MainWindow.clicked_Button35)
        self.pushButton_39.clicked.connect(MainWindow.clicked_Button36)
        self.pushButton_40.clicked.connect(MainWindow.clicked_Button37)
        self.pushButton_41.clicked.connect(MainWindow.clicked_Button38)
        self.pushButton_42.clicked.connect(MainWindow.clicked_Button39)
        self.pushButton_43.clicked.connect(MainWindow.clicked_Button40)
        self.pushButton_44.clicked.connect(MainWindow.clicked_Button41)
        self.pushButton_45.clicked.connect(MainWindow.clicked_Button42)
        self.pushButton_46.clicked.connect(MainWindow.clicked_Button43)
        self.pushButton_47.clicked.connect(MainWindow.clicked_Button44)
        self.pushButton_48.clicked.connect(MainWindow.clicked_Button45)
        self.pushButton_49.clicked.connect(MainWindow.clicked_Button46)
        self.pushButton_50.clicked.connect(MainWindow.clicked_Button47)
        self.pushButton_51.clicked.connect(MainWindow.clicked_Button48)
        self.pushButton_52.clicked.connect(MainWindow.clicked_Button49)
        self.pushButton_53.clicked.connect(MainWindow.clicked_Button50)
        self.pushButton_54.clicked.connect(MainWindow.clicked_Button51)
        self.pushButton_55.clicked.connect(MainWindow.clicked_Button52)
        self.pushButton_56.clicked.connect(MainWindow.clicked_Button53)
        self.pushButton_57.clicked.connect(MainWindow.clicked_Button54)
        self.pushButton_58.clicked.connect(MainWindow.clicked_Button55)
        self.pushButton_59.clicked.connect(MainWindow.clicked_Button56)
        self.pushButton_60.clicked.connect(MainWindow.clicked_Button57)
        self.pushButton_61.clicked.connect(MainWindow.clicked_Button58)
        self.pushButton_62.clicked.connect(MainWindow.clicked_Button59)
        self.pushButton_63.clicked.connect(MainWindow.clicked_Button60)
        self.pushButton_64.clicked.connect(MainWindow.clicked_Button61)
        self.pushButton_65.clicked.connect(MainWindow.clicked_Button62)
        self.pushButton_66.clicked.connect(MainWindow.clicked_Button63)
        self.pushButton_67.clicked.connect(MainWindow.clicked_Button64)
        self.pushButton_68.clicked.connect(MainWindow.clicked_Button65)
        self.pushButton_69.clicked.connect(MainWindow.clicked_Button66)
        self.pushButton_70.clicked.connect(MainWindow.clicked_Button67)
        self.pushButton_71.clicked.connect(MainWindow.clicked_Button68)
        self.pushButton_72.clicked.connect(MainWindow.clicked_Button69)
        self.pushButton_73.clicked.connect(MainWindow.clicked_Button70)


        self.pushButton_74.clicked.connect(MainWindow.clicked_Button71)
        self.pushButton_75.clicked.connect(MainWindow.clicked_Button72)
        self.pushButton_76.clicked.connect(MainWindow.clicked_Button73)
        self.pushButton_77.clicked.connect(MainWindow.clicked_Button74)
        self.pushButton_78.clicked.connect(MainWindow.clicked_Button75)
        self.pushButton_79.clicked.connect(MainWindow.clicked_Button76)
        self.pushButton_80.clicked.connect(MainWindow.clicked_Button77)
        self.pushButton_81.clicked.connect(MainWindow.clicked_Button78)
        self.pushButton_82.clicked.connect(MainWindow.clicked_Button79)
        self.pushButton_83.clicked.connect(MainWindow.clicked_Button80)
        self.pushButton_84.clicked.connect(MainWindow.clicked_Button81)
        self.pushButton_85.clicked.connect(MainWindow.clicked_Button82)
        self.pushButton_86.clicked.connect(MainWindow.clicked_Button83)
        self.pushButton_87.clicked.connect(MainWindow.clicked_Button84)
        self.pushButton_88.clicked.connect(MainWindow.clicked_Button85)
        self.pushButton_89.clicked.connect(MainWindow.clicked_Button86)
        self.pushButton_90.clicked.connect(MainWindow.clicked_Button87)
        self.pushButton_91.clicked.connect(MainWindow.clicked_Button88)
        self.pushButton_92.clicked.connect(MainWindow.clicked_Button89)
        self.pushButton_93.clicked.connect(MainWindow.clicked_Button90)
        self.pushButton_94.clicked.connect(MainWindow.clicked_Button91)
        self.pushButton_95.clicked.connect(MainWindow.clicked_Button92)
        self.pushButton_96.clicked.connect(MainWindow.clicked_Button93)
        self.pushButton_97.clicked.connect(MainWindow.clicked_Button94)
        self.pushButton_98.clicked.connect(MainWindow.clicked_Button95)
        self.pushButton_99.clicked.connect(MainWindow.clicked_Button96)
        self.pushButton_100.clicked.connect(MainWindow.clicked_Button97)
        self.pushButton_101.clicked.connect(MainWindow.clicked_Button98)
        self.pushButton_102.clicked.connect(MainWindow.clicked_Button99)
        self.pushButton_103.clicked.connect(MainWindow.clicked_Button100)
        self.pushButton_104.clicked.connect(MainWindow.clicked_Button101)
        self.pushButton_105.clicked.connect(MainWindow.clicked_Button102)
        self.pushButton_106.clicked.connect(MainWindow.clicked_Button103)
        self.pushButton_107.clicked.connect(MainWindow.clicked_Button104)
        self.pushButton_108.clicked.connect(MainWindow.clicked_Button105)


        self.remocon_btn.clicked.connect(MainWindow.remocon)
        self.corona_btn.clicked.connect(MainWindow.corona19)
        self.wether_btn.clicked.connect(MainWindow.wether)
        self.the_btn.clicked.connect(MainWindow.thre)
        self.next_btn.clicked.connect(MainWindow.next)
        self.back_btn.clicked.connect(MainWindow.back)
        self.pushButton_108.clicked.connect(MainWindow.dele)
        self.pushButton_108.clicked.connect(MainWindow.dele)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music List var.2"))
        self.label.setText(_translate("MainWindow", "??????"))
        self.label_2.setText(_translate("MainWindow", "?????????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????"))
        self.next_btn.setText(_translate("MainWindow", "??????->"))
        self.remocon_btn.setText(_translate("MainWindow", "?????????"))
        self.corona_btn.setText(_translate("MainWindow", "????????? ??????"))
        self.wether_btn.setText(_translate("MainWindow", "??????"))
        self.the_btn.setText(_translate("MainWindow", "?????????"))
        self.back_btn.setText(_translate("MainWindow", "<-??????"))
        self.radioButton.setText(_translate("MainWindow", "?????????"))
        self.radioButton_2.setText(_translate("MainWindow", "??????"))
        self.pushButton_108.setText(_translate("MainWindow", "??????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
