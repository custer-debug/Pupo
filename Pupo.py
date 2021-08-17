import sys
import os
import CopyWindow 
import Function as func
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
        
        ax = 700
        ay = 300        
        
        aw = 620
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
        self.lineEdit.setFixedSize(480,28)
        self.lineEdit.setText(self.File)
        self.lineEdit.move(15,15)
        self.Text = QTextBrowser(self)
        self.Text.move(30,230)
        self.Text.setFixedSize(555,200)

#   Функция инициализации чекбоксов
    def CheckBoxesUI(self):
        self.checkBox_Delete = QCheckBox(CheckBox_1, self)
        self.checkBox_Delete.move(20, 60)
        self.checkBox_Delete.setFixedSize(400,20)

        self.checkBox_Rename = QCheckBox(CheckBox_2, self)
        self.checkBox_Rename.move(20, 80)
        self.checkBox_Rename.setFixedSize(400,20)

        #self.checkBox_Delete.stateChanged.connect(self.CheckedBox)
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


        button1.move(490,450)
        button1.clicked.connect(self.on_click)

        button2.clicked.connect(self.exit)
        button2.move(30,450)

        button3.clicked.connect(self.SelectMainDirectory)
        button3.move(500,14)
        button3.setFixedSize(90,30)

        button4.clicked.connect(self.open_new_window)
        button4.move(493,190)
        button4.setFixedSize(90,30)

        button5.clicked.connect(self.SelectForConvert)
        button5.move(400,190)
        button5.setFixedSize(90,30)


    def SelectForConvert(self):
        self.File = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit.setText(self.File)

    def SelectMainDirectory(self):
        self.File = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace('/', '\\')
        self.lineEdit.setText(self.File)

    def open_new_window(self):
        self.w = CopyWindow.CopyWindow()
        self.w.show()

        


#   Главная функция удаления исполняемых файлов
    def DeleteExeFiles(self):
        global Text
        path = str()
        for root, _, files in os.walk(self.File):
                for file in files:
                    if file.endswith(".exe"):
                        path = os.path.join(root, file)
                        os.remove(path)
                        self.Print(self,"Удалён: " + path)
        

        return len(path)


#   Функция поиска dat-файлов
    def findDatFiles(self):
        for _, _ , files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(".dat"):
                    return func.splitDate(file)



#   Главная функция переименования выходных файлов
    def RenameTxtFiles(self):
        folder = ""
        for root, _ , files in os.walk(self.File):
            for file in files:
                if file.endswith("Out_res.txt"):
                    folder = func.splitName(root)    #Директория поиска
                    data = self.findDatFiles()  #Дата первого dat-файла
                    func.Print(self,root + "\\" + file + " -> " + folder + "_" + data)
                    os.rename(os.path.join(root, file), os.path.join(root, folder) + "_" + data + ".txt")
        return len(folder)
            



    


    @pyqtSlot()
    def on_click(self):
        if self.checkBox_Delete.isChecked() == True:
            if self.DeleteExeFiles() == 0:
                func.Print(self,ExeError)

        if self.checkBox_Rename.isChecked() == True:
            if self.RenameTxtFiles() == 0:
                func.Print(self,TxtError)

        if self.checkBox_EmptyDir.isChecked() == True:
            if func.del_empty_dirs(self.File) == False:
                func.Print(self,EmptyError)
    

    


    def exit(self):
        sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()








