import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import timeit
from DefaultVariable import *

# пакеты созданные специально для Pupo
import CopyTxtFiles
import Function as func


class MainWindow(QMainWindow):

# Функция инициализации окна
    def __init__(self):
        super().__init__()
        # self.setWindowIcon(QIcon('Icon.png'))
        
        self.File =  os.getcwd().replace('/', '\\')
        
        

        self.setWindowTitle(Title)
        self.setGeometry(window_X, window_Y, window_Width, window_Height)

        self.ButtonUI()
        self.CheckBoxesUI()
        self.LineEditesUI()
        self.show() # Функция отображения окна


#   Функция инициализации полей
    def LineEditesUI(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedSize(line_edit_wight,line_edit_height)
        self.lineEdit.setText(self.File)
        self.lineEdit.move(line_edit_xy,line_edit_xy)
        self.Text = QTextBrowser(self)
        self.Text.move(Text_X,Text_Y)
        self.Text.setFixedSize(Text_Wight,Text_Height)

#   Функция инициализации чекбоксов
    def CheckBoxesUI(self):
        self.checkBox_Delete = QCheckBox(delete_exe_str, self)
        self.checkBox_Delete.move(check_boxes_x, check_box1_y)
        self.checkBox_Delete.setFixedSize(check_boxes_wight,check_boxes_height)

        self.checkBox_Rename = QCheckBox(rename_Out_res, self)
        self.checkBox_Rename.move(check_boxes_x, check_box2_y)
        self.checkBox_Rename.setFixedSize(check_boxes_wight,check_boxes_height)

        self.checkBox_EmptyDir = QCheckBox(delete_empty_dir, self)
        self.checkBox_EmptyDir.move(check_boxes_x, check_box3_y)
        self.checkBox_EmptyDir.setFixedSize(check_boxes_wight,check_boxes_height)


#   Функция инициализации кнопок
    def ButtonUI(self):
        btn_run = QPushButton(run, self)
        btn_exit = QPushButton(exit_, self)
        btn_review = QPushButton(review, self)
        btn_move = QPushButton(move_, self)
        
        
        btn_run.move(btn_run_x,btn_run_y)
        btn_run.clicked.connect(self.on_click)
        # btn_run.setIcon(QIcon('Icon_play.png'))
        # btn_run.setIconSize(QSize(30, 30))
        

        btn_exit.clicked.connect(self.exit)
        btn_exit.move(btn_exit_x,btn_exit_y)

        btn_review.clicked.connect(self.SelectMainDirectory)
        btn_review.move(btn_review_x,btn_review_y)
        btn_review.setFixedSize(btn_wight,btn_height)
        # btn_review.setIcon(QIcon('Icon_review.png'))
        # btn_review.setIconSize(QSize(20, 20))

        btn_move.clicked.connect(self.open_new_window)
        btn_move.move(btn_move_x,btn_move_y)
        btn_move.setFixedSize(btn_wight,btn_height)


    def SelectMainDirectory(self):
        self.File = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.lineEdit.setText(self.File)

    def open_new_window(self):
        self.w = CopyTxtFiles.CopyWindow()
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
                    if file.endswith(exe):
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
                if file.endswith(dat):
                    return func.splitDate(file)


#   Главная функция переименования выходных файлов
    def RenameTxtFiles(self):
        folder = ""
        for root, _ , files in os.walk(self.File):
            for file in files:
                if file.endswith(out_res):
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
                func.Print(self,exe_files_not_found)
            
            print(f"Time delete: {timeit.default_timer() - start}")
            
                

        if self.checkBox_Rename.isChecked() == True:
            start = timeit.default_timer()
            if self.RenameTxtFiles() == 0:
                func.Print(self,Out_res_not_found)
            # print(f"Time rename: {timeit.default_timer() - start}")


        if self.checkBox_EmptyDir.isChecked() == True:
            start = timeit.default_timer()
            if func.del_empty_dirs(self, self.File) == True:
                func.Print(self,empty_dir_not_found)
            # print(f"Time empty dir: {timeit.default_timer() - start}")


    def exit(self):
        sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()








