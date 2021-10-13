import logging
import sys
import os
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# модули созданные специально для Pupo
import SecondWindow
import Function as func
from DefaultVariable import *


class MainWindow(QMainWindow):

# Функция инициализации окна
    def __init__(self):
        super().__init__()
        logging.info("\n <============>")
        pixmapi = getattr(QStyle, 'SP_DialogResetButton')
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.File =  os.getcwd().replace('/', '\\')
        
        self.setWindowTitle(Title)
        self.setGeometry(window_X, window_Y, window_Width, window_Height)

        self.button_handle_function()
        self.handle_checkbox_function()
        self.handle_line_edit_function()
        self.show() # Функция отображения окна


#   Функция инициализации полей
    def handle_line_edit_function(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedSize(line_edit_wight,line_edit_height)
        self.lineEdit.setText(self.File)
        self.lineEdit.move(line_edit_xy,line_edit_xy)
        self.Text = QTextBrowser(self)
        self.Text.move(Text_X,Text_Y)
        self.Text.setFixedSize(Text_Wight,Text_Height)


    def create_check_box(self, name, y):
        checkbox = QCheckBox(name, self)
        checkbox.move(check_boxes_x, y)
        checkbox.setFixedSize(check_boxes_wight, check_boxes_height)
        return checkbox

#   Функция инициализации чекбоксов
    def handle_checkbox_function(self):
        
        self.checkbox_delete = self.create_check_box(delete_exe_str, check_box1_y)
        self.checkbox_rename = self.create_check_box(rename_Out_res, check_box2_y)
        self.checkbox_empty_dir = self.create_check_box(delete_empty_dir, check_box3_y)

    def create_button(self, name, function, x, y):
        btn = QPushButton(name, self)
        btn.move(x,y)
        btn.clicked.connect(function)
        btn.setFixedSize(btn_wight,btn_height)

        
#   Функция инициализации кнопок
    def button_handle_function(self):
        self.create_button(run, self.on_click, btn_run_x, btn_run_y)
        self.create_button(exit_, self.exit, btn_exit_x, btn_exit_y)
        self.create_button(review, self.select_main_directory, btn_review_x, btn_review_y)
        self.create_button(move_, self.open_new_window, btn_move_x, btn_move_y)


    def select_main_directory(self):
        self.File = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.lineEdit.setText(self.File)

    def open_new_window(self):
        self.w = SecondWindow.SecondWindowClass()
        self.w.log_update.connect(self.callback)
        self.w.show()


    def callback(self):
        func.Print(self, self.w.log_txt)
        QtGui.QGuiApplication.processEvents()


#   Главная функция удаления исполняемых файлов
    def delete_exe_files(self):
        path = ""
        Fsize = 0
        for root, _, files in os.walk(self.File):
                for file in files:
                    if file.endswith(exe):
                        path = os.path.join(root, file)
                        Fsize += os.stat(path).st_size 
                        os.remove(path)
                        func.Print(self,"Удалён: " + path)
        
        func.Print(self,f'Очищено: {str(round(Fsize,2))} {func.size_of_file(Fsize)}')

        if len(path) == 0:
            return False
        
        return True
        

#   Функция поиска dat-файлов
    def find_first_file(self,endswith, files):
        for file in files:
            if file.endswith(endswith):
                return file

#   Главная функция переименования выходных файлов
    def hangle_rename_txt_file(self):
        rename = ""
        for root, _, files in os.walk(self.File):
            dat_file = self.find_first_file(dat, files)
            txt_file = self.find_first_file(txt, files)
            if dat_file != None and txt_file != None:
                rename = f'{func.splitName(root)[-1]}_{func.splitDate(dat_file)}{txt}'
                func.Print(self,f'{root}/{txt_file} -> {root}/{rename}')        
            elif  dat_file == None and txt_file != None:
                rename = f'{func.splitName(root)[-1]}{txt}'
                func.Print(self, f'{root}/{txt_file} -> {root}/{func.splitName(root)[-1]}{txt}')
        
            os.rename(os.path.join(root, txt_file), os.path.join(root, rename))
        
        func.Print(self,"Done")

        if len(rename) == 0:
            return False
        
        return True


    def checked_some_box(self, check_box, function, text):
        if check_box.isChecked() and function:
            func.Print(self, text)

    @pyqtSlot()
    def on_click(self):
        self.checked_some_box(self.checkbox_delete, self.delete_exe_files, exe_files_not_found)
        self.checked_some_box(self.checkbox_rename, self.hangle_rename_txt_file, Out_res_not_found)
        self.checked_some_box(self.checkbox_empty_dir, func.del_empty_dirs, empty_dir_not_found)
                       

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()








