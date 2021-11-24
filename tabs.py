from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initTabsWidget()
        self.init_tab1()
        self.init_tab2()
        self.init_tab3()
        self.init_tab4()


    def init_tab1(self):
        # Create elements
        self.btn1 = QPushButton('Review', self.tab1)
        self.btn1.setObjectName('btn1')
        self.btn2 = QPushButton('Run', self.tab1)

        self.line1 = QLineEdit(self.tab1)
        self.line1.setObjectName('line1')

        self.check_box1 = QCheckBox('Delete files', self.tab1)
        self.check_box2 = QCheckBox('Rename files', self.tab1)
        self.check_box3 = QCheckBox('Delete empty dir', self.tab1)

        self.text = QTextEdit(self.tab1)
        self.text.setReadOnly(True)

        # Create grid
        grid = QGridLayout()
        grid.addWidget(self.line1, 0, 0)
        grid.addWidget(self.btn1, 0, 1)
        grid.addWidget(self.check_box1, 1,0)
        grid.addWidget(self.check_box2, 2,0)
        grid.addWidget(self.check_box3, 3,0)
        grid.addWidget(self.text, 4,0,5,2)
        grid.addWidget(self.btn2, 10, 1)

        self.tab1.setLayout(grid)

    def init_tab2(self):
        # Create elements
        self.radio_button1 = QRadioButton('Collect txt', self.tab2)
        self.radio_button2 = QRadioButton('Split dat', self.tab2)
        self.radio_button3 = QRadioButton('Send out exe', self.tab2)

        group = QButtonGroup(self.tab2)
        group.addButton(self.radio_button1)
        group.addButton(self.radio_button2)
        group.addButton(self.radio_button3)

        self.label_1 = QLabel('Path', self.tab2)
        self.label_2 = QLabel('Path', self.tab2)
        self.label_3 = QLabel('Path', self.tab2)

        self.path1 = QLineEdit(self.tab2)
        self.path2 = QLineEdit(self.tab2)
        self.path3 = QLineEdit(self.tab2)

        self.probar = QProgressBar(self.tab2)
        self.probar.setValue(20)
        self.probar.setAlignment(Qt.AlignCenter)

        self.btn1 = QPushButton('Review',self.tab2)
        self.btn2 = QPushButton('Review',self.tab2)
        self.btn3 = QPushButton('Review',self.tab2)
        self.btn4 = QPushButton('Run',self.tab2)

        # Create grid for paint elements
        grid = QGridLayout()
        grid.setVerticalSpacing(30)
        grid.setRowStretch(6,2)
        grid.setColumnStretch(0,1)
        grid.setColumnStretch(1,5)
        grid.setColumnStretch(2,5)
        grid.setColumnStretch(3,5)


        grid.addWidget(self.radio_button1, 0,1, alignment=Qt.AlignLeft)
        grid.addWidget(self.radio_button2, 0,2, alignment=Qt.AlignCenter)
        grid.addWidget(self.radio_button3, 0,3, alignment=Qt.AlignRight)

        grid.addWidget(self.label_1, 1,0)
        grid.addWidget(self.label_2, 2,0)
        grid.addWidget(self.label_3, 3,0)

        grid.addWidget(self.path1, 1,1,1,3)
        grid.addWidget(self.path2, 2,1,1,3)
        grid.addWidget(self.path3, 3,1,1,3)

        grid.addWidget(self.btn1, 1, 4, 1,1)
        grid.addWidget(self.btn2, 2, 4, 1,1)
        grid.addWidget(self.btn3, 3, 4, 1,1)
        grid.addWidget(self.btn4, 5, 4, 1,1)
        grid.addWidget(self.probar, 4, 1, 1, 4)

        self.tab2.setLayout(grid)

    def init_tab4(self):
        # Create elements
        self.radio_config1 = QRadioButton('1200', self.tab4)
        self.radio_config2 = QRadioButton('2500', self.tab4)
        self.radio_config3 = QRadioButton('Local', self.tab4)
        self.radio_config4 = QRadioButton('Reson', self.tab4)
        self.radio_config5 = QRadioButton('2', self.tab4)
        self.radio_config6 = QRadioButton('4', self.tab4)

        group1 = QButtonGroup(self.tab4)
        group1.addButton(self.radio_config1)
        group1.addButton(self.radio_config2)

        group2 = QButtonGroup(self.tab4)
        group2.addButton(self.radio_config3)
        group2.addButton(self.radio_config4)

        group3 = QButtonGroup(self.tab4)
        group3.addButton(self.radio_config5)
        group3.addButton(self.radio_config6)



        grid = QGridLayout()
        grid.addWidget(QLabel('Radar'), 0,0)
        grid.addWidget(self.radio_config1, 0,1)
        grid.addWidget(self.radio_config2, 0,2)
        grid.addWidget(QLabel('Mode'), 1,0)
        grid.addWidget(self.radio_config3, 1,1)
        grid.addWidget(self.radio_config4, 1,2)
        grid.addWidget(QLabel('Channel'), 2,0)
        grid.addWidget(self.radio_config5, 2,1)
        grid.addWidget(self.radio_config6, 2,2)
        grid.setRowStretch(4,2)
        grid.setVerticalSpacing(20)

        self.tab4.setLayout(grid)

    def init_tab3(self):
        self.line_found = QLineEdit(self.tab3)
        self.line_save1 = QLineEdit(self.tab3)
        self.line_save2 = QLineEdit(self.tab3)

        self.btn_review = QPushButton('Review',self.tab3)
        self.btn_found = QPushButton('Found',self.tab3)
        self.btn_save = QPushButton('Save',self.tab3)
        self.btn_select_all = QPushButton('Select/Remove all', self.tab3)
        self.label_select = QLabel(self.tab3)
        self.label_select.setText('Selected: ')
        self.list = QListWidget(self.tab3)
        self.list.setSelectionMode(QAbstractItemView.MultiSelection)
        # l = ['asd','sdf','sdf']
        # self.list.addItems(l)
        self.list.itemSelectionChanged.connect(self.select)
        self.checkbox_xlsx1 = QCheckBox('One file = one sheet',self.tab3)
        self.checkbox_xlsx2 = QCheckBox('Many files = one sheet',self.tab3)

        grid = QGridLayout()
        grid.addWidget(self.line_found, 0,0,1,2)
        grid.addWidget(self.btn_review, 0,2)
        grid.addWidget(self.btn_found, 0,3)
        grid.addWidget(self.checkbox_xlsx1, 1,0)
        grid.addWidget(self.line_save1, 1,1)
        grid.addWidget(self.checkbox_xlsx2, 2,0)
        grid.addWidget(self.line_save2, 2,1)
        grid.addWidget(self.btn_select_all,4,0, alignment=Qt.AlignLeft)
        grid.addWidget(self.label_select, 4,1)

        grid.addWidget(self.list, 3,0,1,4)
        grid.addWidget(self.btn_save, 4,3)
        # grid.setColumnStretch(4,1)
        # grid.setRowStretch(4,1)
        self.tab3.setLayout(grid)


    def select(self):
        print("start")
        print([item.text() for item in self.list.selectedItems()])

    def initTabsWidget(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300,200)

        self.tabs.addTab(self.tab1,"Clean up")
        self.tabs.addTab(self.tab2,"Move files")
        self.tabs.addTab(self.tab3,"Txt to xlsx")
        self.tabs.addTab(self.tab4,"Config file")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)
        self.setLayout(vbox)
