from PyQt5.QtWidgets import *
import os
import shutil

From    = ""
To      = ""

def splitName(str):
    return str.split('\\')[-1]





class CopyWindow(QMainWindow):
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
        self.LineEdit()
        self.Buttons()
        self.show()
    
    
    def LineEdit(self):
        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.setFixedSize(420,30)
        self.lineEdit_1.move(60,15)

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setFixedSize(420,30)
        self.lineEdit_2.move(60,70)


    def Buttons(self):
        button_1 = QPushButton("Обзор",self)
        button_1.move(490,14)
        button_1.setFixedSize(90,30)
        button_1.clicked.connect(self.selectDirectory_1)

        button_2 = QPushButton("Обзор",self)
        button_2.move(490,70)
        button_2.setFixedSize(90,30)
        button_2.clicked.connect(self.selectDirectory_2)
        
        button_3 = QPushButton("Копировать",self)
        button_3.move(490,140)
        button_3.clicked.connect(self.startCopy)

    def startCopy(self):
        if From == "":
            QMessageBox.critical(self, 'Ошибка', "Выберите откуда надо копировать файлы")
            return
        elif To == "":
            QMessageBox.critical(self, 'Ошибка', "Выберите куда надо копировать файлы")
            return

        for root, _, files in os.walk(From):
            for file in files:
                if file.endswith(".txt"):
                    shutil.copyfile(root + "\\" + file, To + "\\" + splitName(root) + ".txt")
                    self.close()
        
        QMessageBox.information(self, 'Успех', "Файлы скопированы")
        


    def selectDirectory_1(self):
        global From
        From = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit_1.setText(From)

    def selectDirectory_2(self):
        global To
        To = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit_2.setText(To)

