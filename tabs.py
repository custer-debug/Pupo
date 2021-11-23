# from sys import last_type
from typing import Sized
from PyQt5.QtWidgets import QGridLayout, QLayout,QButtonGroup, QCheckBox, QHBoxLayout, QLineEdit, QRadioButton, QTextEdit, QWidget, QVBoxLayout, QTabWidget, QPushButton
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initTabs()
        self.init_first_tab()
        self.initRadioButtons()



    def init_first_tab(self):
        grid = QGridLayout()
        self.btn1 = QPushButton('Review', self.cleanUp_tab)
        self.btn1.setObjectName('btn1')
        self.btn2 = QPushButton('Execute', self.cleanUp_tab)

        self.line1 = QLineEdit(self.cleanUp_tab)
        self.line1.setObjectName('line1')

        self.check_box1 = QCheckBox('Delete files', self.cleanUp_tab)
        self.check_box2 = QCheckBox('Rename files', self.cleanUp_tab)
        self.check_box3 = QCheckBox('Delete empty dir', self.cleanUp_tab)
        self.text = QTextEdit(self.cleanUp_tab)


        grid.addWidget(self.line1, 0, 0)
        grid.addWidget(self.btn1, 0, 1)
        grid.addWidget(self.check_box1, 1,0)
        grid.addWidget(self.check_box2, 2,0)
        grid.addWidget(self.check_box3, 3,0)
        grid.addWidget(self.text, 4,0,5,2)
        grid.addWidget(self.btn2, 10, 1)


        self.cleanUp_tab.setLayout(grid)


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

        group = QButtonGroup(self.movefiles_tab)
        group.addButton(self.radio_button1)
        group.addButton(self.radio_button2)
        group.addButton(self.radio_button3)
