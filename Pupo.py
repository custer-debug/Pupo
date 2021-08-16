import datetime
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

CheckBox_1 = "Удаление исполняемых файлов (.exe)"
CheckBox_2 = "Переименование выходных файлов (Out_res.txt)"

ExeError_1 = "Ни одного exe-файла не найдено"
TxtError_1 = "Ни одного txt-файла не найдено"


def splitName(str):
    return str.split('\\')[-1]


def splitDate(str):
    s = str.split('_')
    s.pop(0)
    a = s[-1].split('.')
    s.pop(-1)
    s.append(a[0])
    res = '_'.join(s)
    return res



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Cleaning program'
        self.setWindowIcon(QIcon('icon.png'))
        self.File =  os.getcwd().replace('/', '\\')
        self.left = 700
        self.top = 300        
        self.checkBox_Delete = QCheckBox(CheckBox_1, self)
        self.checkBox_Delete.move(20, 50)
        self.checkBox_Delete.setFixedSize(400,20)

        self.checkBox_Rename = QCheckBox(CheckBox_2, self)
        self.checkBox_Rename.move(20, 70)
        self.checkBox_Rename.setFixedSize(400,20)


        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedSize(480,28)
        #self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(self.File)

        flo = QFormLayout()
        flo.addRow(self.lineEdit)
        self.setLayout(flo)


        self.width = 620
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button1 = QPushButton('Run', self)
        button1.move(500,450)
        button1.clicked.connect(self.on_click)

        button2 = QPushButton('Exit', self)
        button2.clicked.connect(self.exit)
        button2.move(30,450)

        button3 = QPushButton('Review', self)
        button3.clicked.connect(self.selectDirectory)
        button3.move(500,10)
        self.show()


    def DeleteExeFiles(self):
        path = str()
        for root, _, files in os.walk(self.File):
                for file in files:
                    if file.endswith(".exe"):
                        path = os.path.join(root, file)
                        os.remove(path)
                        print(path)
        return len(path)





    def findDatFiles(self):
        for _, _ , files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(".dat"):
                    return splitDate(file)


    def RenameTxtFiles(self):
        folder = ""
        for root, _ , files in os.walk(self.File):
            for file in files:
                if file.endswith("Out_res.txt"):
                    folder = splitName(root)    #Директория поиска
                    data = self.findDatFiles()  #Дата первого dat-файла
                    print(root + "\\" + file, " -> ", folder + "_" + data)
                    os.rename(os.path.join(root, file), os.path.join(root, folder) + "_" + data + ".txt")
        return len(folder)
            
        

    @pyqtSlot()
    def on_click(self):
        if self.checkBox_Delete.isChecked() == True:
            if self.DeleteExeFiles() == 0:
                print(ExeError_1)
        if self.checkBox_Rename.isChecked() == True:
            if self.RenameTxtFiles() == 0:
                print(TxtError_1) 
                
        
    

    def selectDirectory(self):
        self.File = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit.setText(self.File)




    def exit(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()








