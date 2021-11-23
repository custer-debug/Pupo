# from sys import last_type
from typing import Sized
from PyQt5.QtWidgets import QLayout,QButtonGroup, QCheckBox, QHBoxLayout, QLineEdit, QRadioButton, QTextEdit, QWidget, QVBoxLayout, QTabWidget, QPushButton
from PyQt5 import QtCore
class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initTabs()
        self.init_first_tab()
        self.initButtons()
        # self.initLineEdit()
        # self.initTextEdit()
        self.initRadioButtons()
        # self.initCheckBoxes()



    def init_first_tab(self):
        layout = QHBoxLayout()
        # layout.setSizeConstraint()
        self.btn1 = QPushButton('Review', self.cleanUp_tab)
        self.btn1.setObjectName('btn1')
        # self.btn1.resize(65,30)
        self.line1 = QLineEdit(self.cleanUp_tab)
        layout.addWidget(self.line1, alignment= QtCore.Qt.AlignTop)
        layout.addWidget(self.btn1, alignment= QtCore.Qt.AlignTop)
        self.cleanUp_tab.setLayout(layout)


    def initButtons(self):
        # self.btn1 = QPushButton('Review', self.cleanUp_tab)
        # self.btn1.setGeometry(QtCore.QRect(380,10,65,30))

        self.btn2 = QPushButton('Execute', self.cleanUp_tab)
        self.btn2.setGeometry(QtCore.QRect(370,420,75,30))


    def initCheckBoxes(self):
        self.check_box1 = QCheckBox('Delete files', self.cleanUp_tab)
        self.check_box1.setGeometry(QtCore.QRect(20,50, 100, 30))

        self.check_box2 = QCheckBox('Rename files', self.cleanUp_tab)
        self.check_box2.setGeometry(QtCore.QRect(20,80, 100, 30))

        self.check_box2 = QCheckBox('Delete empty dir', self.cleanUp_tab)
        self.check_box2.setGeometry(QtCore.QRect(20,110, 100, 30))

    def initTextEdit(self):
        self.text = QTextEdit(self.cleanUp_tab)
        self.text.setGeometry(QtCore.QRect(10,150, 430, 250))
        self.text.setReadOnly(True)


    def initLineEdit(self):
        self.line1 = QLineEdit(self.cleanUp_tab)
        self.line1.setGeometry(QtCore.QRect(10,10, 360, 30))



    def initTabs(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.cleanUp_tab = QWidget()
        self.movefiles_tab = QWidget()
        self.txt_to_xlsx_tab = QWidget()
        self.config_tab = QWidget()

        self.tabs.resize(300,200)

        self.tabs.addTab(self.cleanUp_tab,"Clean up")
        self.tabs.addTab(self.movefiles_tab,"Move files")
        self.tabs.addTab(self.txt_to_xlsx_tab,"Txt to xlsx")
        self.tabs.addTab(self.config_tab,"Config file")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)
        self.setLayout(vbox)



    def initRadioButtons(self):
        l = QHBoxLayout()
        self.radio_button1 = QRadioButton('Collect txt', self.movefiles_tab)
        self.radio_button2 = QRadioButton('Split dat', self.movefiles_tab)
        self.radio_button3 = QRadioButton('Send out exe', self.movefiles_tab)
        l.addWidget(self.radio_button1, alignment=QtCore.Qt.AlignTop)
        l.addWidget(self.radio_button2,alignment=QtCore.Qt.AlignTop)
        l.addWidget(self.radio_button3, alignment=QtCore.Qt.AlignTop)
        self.movefiles_tab.setLayout(l)


        # y = 5
        # self.radio_button1.setGeometry(QtCore.QRect(10,y, 360, 20))
        # self.radio_button2.setGeometry(QtCore.QRect(180,y, 360, 20))
        # self.radio_button3.setGeometry(QtCore.QRect(350,y, 360, 20))


        group = QButtonGroup(self.movefiles_tab)
        group.addButton(self.radio_button1)
        group.addButton(self.radio_button2)
        group.addButton(self.radio_button3)
