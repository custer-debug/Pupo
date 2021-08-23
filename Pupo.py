import sys
import os

from PyQt5 import QtGui
import CopyWindow 
import Function as func
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import timeit


CheckBox_1 = "Удаление исполняемых файлов (.exe)"
CheckBox_2 = "Переименование выходных файлов (Out_res.txt)"
CheckBox_3 = "Удаление пустых папок"

EmptyError = "Пустых директорий не найдено"
ExeError = "Исполняемых файлов не найдено"
TxtError = "Out_res-файлов не найдено"

Warning = "Внимание!"
Message = "Сообщение "



class MainWindow(QMainWindow):

# Функция инициализации окна
    def __init__(self):
        super().__init__()
        Title = 'Cleaning program'
        self.setWindowIcon(QIcon('icon.png'))
        
        self.File =  os.getcwd().replace('/', '\\')
        
        ax = 600
        ay = 300        
        
        aw = 700
        ah = 500

        self.setWindowTitle(Title)
        self.setGeometry(ax, ay, aw, ah)

        self.ButtonUI()
        self.CheckBoxesUI()
        self.LineEditesUI()
        self.show() # Функция отображения окна


#   Функция инициализации полей
    def LineEditesUI(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedSize(580,28)
        self.lineEdit.setText(self.File)
        self.lineEdit.move(15,15)
        self.Text = QTextBrowser(self)
        self.Text.move(30,190)
        self.Text.setFixedSize(640,250)

#   Функция инициализации чекбоксов
    def CheckBoxesUI(self):
        self.checkBox_Delete = QCheckBox(CheckBox_1, self)
        self.checkBox_Delete.move(20, 60)
        self.checkBox_Delete.setFixedSize(400,20)

        self.checkBox_Rename = QCheckBox(CheckBox_2, self)
        self.checkBox_Rename.move(20, 80)
        self.checkBox_Rename.setFixedSize(400,20)

        self.checkBox_EmptyDir = QCheckBox(CheckBox_3, self)
        self.checkBox_EmptyDir.move(20, 100)
        self.checkBox_EmptyDir.setFixedSize(400,20)


#   Функция инициализации кнопок
    def ButtonUI(self):
        button1 = QPushButton('Run', self)
        button2 = QPushButton('Exit', self)
        button3 = QPushButton('Review', self)
        button4 = QPushButton('Copy Files', self)
        button5 = QPushButton('Txt to xlsx', self)


        button1.move(570,450)
        button1.clicked.connect(self.on_click)

        button2.clicked.connect(self.exit)
        button2.move(30,450)

        button3.clicked.connect(self.SelectMainDirectory)
        button3.move(600,14)
        button3.setFixedSize(90,30)

        button4.clicked.connect(self.open_new_window)
        button4.move(580,150)
        button4.setFixedSize(90,30)

        button5.clicked.connect(self.SelectForConvert)
        button5.move(480,150)
        button5.setFixedSize(90,30)


    def SelectForConvert(self):
        self.File = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit.setText(self.File)

    def SelectMainDirectory(self):
        self.File = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit.setText(self.File)

    def open_new_window(self):
        self.w = CopyWindow.CopyWindow()
        self.w.log_update.connect(self.callback)
        self.w.show()

    def callback(self):
        func.Print(self, self.w.log_txt)
        QtGui.QGuiApplication.processEvents()
        




#   Главная функция удаления исполняемых файлов
    def DeleteExeFiles(self):
        global Text
        path = ""
        res = ""

        Fsize = 0
        for root, _, files in os.walk(self.File):
                for file in files:
                    if file.endswith(".exe"):
                        path = os.path.join(root, file)
                        Fsize += os.stat(path).st_size 
                        os.remove(path)
                        func.Print(self,"Удалён: " + path)
        
        if Fsize >= 1024: #byte -> kilobyte
            Fsize /= 1024
            res = "Kb"

        if Fsize >= 1024: #kilobyte -> megabyte
            Fsize /= 1024
            res = "Mb"
    
        if Fsize >= 1024: #megabyte -> gigabyte 
            Fsize /= 1024
            res = "Gb"


        func.Print(self,"Очищено: " + str(round(Fsize, 2)) + " " + res)
        return len(path)


#   Функция поиска dat-файлов
    def findDatFiles(self):
        for _, _ , files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith('.dat'):
                    return func.splitDate(file)


#   Главная функция переименования выходных файлов
    def RenameTxtFiles(self):
        folder = ""
        for root, _ , files in os.walk(self.File):
            for file in files:
                if file.endswith(".txt"):
                    folder = func.splitName(root)    #Директория поиска
                    data = self.findDatFiles()
                    if data == None:
                        func.Print(self,"В папке " + root + " Dat-файлов не найдено")
                        os.rename(os.path.join(root, file), os.path.join(root, folder) + ".txt")
                    else:
                        func.Print(self,root + "\\" + file + " -> " + folder + "_" + data)
                        os.rename(os.path.join(root, file), os.path.join(root, folder) + "_" + data + ".txt")
        func.Print(self,"Done")
        return len(folder)


    @pyqtSlot()
    def on_click(self):
        if self.checkBox_Delete.isChecked() == True:
            start = timeit.default_timer()
            if self.DeleteExeFiles() == 0:
                func.Print(self,ExeError)
            
            print(f"Time delete: {timeit.default_timer() - start}")
            
                

        if self.checkBox_Rename.isChecked() == True:
            start = timeit.default_timer()
            if self.RenameTxtFiles() == 0:
                func.Print(self,TxtError)
            print(f"Time rename: {timeit.default_timer() - start}")


        if self.checkBox_EmptyDir.isChecked() == True:
            start = timeit.default_timer()
            if func.del_empty_dirs(self, self.File) == True:
                func.Print(self,EmptyError)
            print(f"Time empty dir: {timeit.default_timer() - start}")


    def exit(self):
        sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()








