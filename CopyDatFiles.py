import os
import shutil
from PyQt5.QtWidgets import *


cwd = os.getcwd()
print(cwd)

From = ""
To = ""

files = []
files_list = []
for root, dirs, files in os.walk(cwd):  
    for file in files:
        if file.endswith(".dat") and file not in [f[1] for f in files_list]:
            files_list.append([root, file])


files = [os.path.join(f[0], f[1]) for f in files_list]
folders = set()
for i in range(len(files)):
    file = files_list[i][1]
    folders.add(files_list[i][0])
    shutil.move(f"{files[i]}", f"{cwd}\\{file}")

for i in folders:
    if i != cwd:
        print(f"Удалена папка {i}")
        shutil.rmtree(i,ignore_errors=True)



class CopyDatFiles(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Copy Files")
        label_1 = QLabel("From: ",self)
        label_1.setStyleSheet("font: bold 12px")
        label_1.move(10,15)

        label_2 = QLabel("To: ",self)
        label_2.setStyleSheet("font: bold 12px")
        label_2.move(10,70)

        ax = 400
        ay = 200        
        
        aw = 600
        ah = 180

        self.setGeometry(ax,ay,aw,ah)
        self.Line()
        self.Buttons()
        self.show()
    

    def Buttons(self):
        button_1 = QPushButton("Обзор",self)
        button_1.move(490,14)
        button_1.setFixedSize(90,30)
        button_1.clicked.connect(self.select_first_directory)

        button_2 = QPushButton("Обзор",self)
        button_2.move(490,70)
        button_2.setFixedSize(90,30)
        button_2.clicked.connect(self.select_second_directory)

        button_3 = QPushButton("Копировать",self)
        button_3.move(490,140)
        button_3.clicked.connect(self.startCopy)


    def Line(self):
        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.setFixedSize(420,30)
        self.lineEdit_1.move(60,15)

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setFixedSize(420,30)
        self.lineEdit_2.move(60,70)


    def select_first_directory(self):
        global From
        From = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit_1.setText(From)

    def select_second_directory(self):
        global To
        To = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit_2.setText(To)